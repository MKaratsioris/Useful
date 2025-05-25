import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import logging
import time

# --- CONFIG ---

EMAIL = "your-email@example.com"
PASSWORD = "your-udemy-password"

BASE_URL = "https://www.udemy.com"
LOGIN_URL = "https://www.udemy.com/join/login-popup/"
COURSES_URL = "https://www.udemy.com/api-2.0/users/me/subscribed-courses/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(SCRIPT_DIR, "udemy-videos")
LOG_FILE = os.path.join(SCRIPT_DIR, "udemy-download.log")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger()

# --- SESSION SETUP ---
session = requests.Session()
session.headers.update(HEADERS)

def login_udemy(email, password):
    logger.info("Logging in to Udemy...")
    resp = session.get(LOGIN_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
    
    login_data = {
        "email": email,
        "password": password,
        "csrfmiddlewaretoken": csrf_token,
        "locale": "en_US",
        "displayName": "",
        "isSubmitted": "true",
        "credentialType": "email",
    }

    # Need to send cookies and headers to simulate browser
    headers = HEADERS.copy()
    headers["Referer"] = LOGIN_URL

    # Send login POST
    login_resp = session.post(LOGIN_URL, data=login_data, headers=headers)
    
    if login_resp.url != BASE_URL + "/":
        logger.error("Login failed. Check your credentials.")
        return False
    
    logger.info("Logged in successfully.")
    return True

def get_courses():
    logger.info("Fetching enrolled courses...")
    # Udemy provides a JSON API for courses
    resp = session.get(COURSES_URL)
    if resp.status_code != 200:
        logger.error(f"Failed to fetch courses. Status: {resp.status_code}")
        return []
    data = resp.json()
    courses = data.get("results", [])
    logger.info(f"Found {len(courses)} course(s).")
    return courses

def get_lectures(course_id):
    logger.info(f"Fetching lectures for course {course_id}...")
    lectures_url = f"https://www.udemy.com/api-2.0/courses/{course_id}/cached-subscriber-curriculum-items?page_size=1000"
    resp = session.get(lectures_url)
    if resp.status_code != 200:
        logger.error(f"Failed to fetch lectures for course {course_id}. Status: {resp.status_code}")
        return []
    items = resp.json().get("results", [])
    lectures = [item for item in items if item["_class"] == "lecture"]
    logger.info(f"Found {len(lectures)} lectures.")
    return lectures

def download_video_from_url(url, output_path, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            with session.get(url, stream=True) as r:
                r.raise_for_status()
                total = int(r.headers.get('content-length', 0))
                with open(output_path, 'wb') as f, tqdm(
                    total=total, unit='B', unit_scale=True, desc=os.path.basename(output_path)
                ) as bar:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            bar.update(len(chunk))
            return True
        except Exception as e:
            attempt += 1
            logger.warning(f"Retry {attempt}/{retries} failed for {output_path}: {e}")
            time.sleep(3)
    logger.error(f"Failed to download video after {retries} attempts: {output_path}")
    return False

def get_video_url_from_lecture(lecture):
    # The 'lecture' JSON includes 'asset' dict with video info if available
    asset = lecture.get("asset", {})
    if asset.get("_class") == "video":
        # The URLs to actual video files can be complex.
        # We look for 'streams' > 'http' or 'progressive' urls:
        streams = asset.get("streams", [])
        # Find highest quality progressive stream URL
        progressive_streams = [s for s in streams if s.get("format") == "mp4" and s.get("quality")]
        if progressive_streams:
            # Pick the highest quality by sorting
            progressive_streams.sort(key=lambda x: x["quality"], reverse=True)
            return progressive_streams[0].get("url")
        # Alternatively try 'download_urls'
        download_urls = asset.get("download_urls", {})
        if "Video" in download_urls:
            video_urls = download_urls["Video"].get("Standard", [])
            if video_urls:
                return video_urls[0].get("file")
    return None

def sanitize_filename(name):
    return "".join(c for c in name if c.isalnum() or c in " .-_()[]").rstrip()

def main():
    if not login_udemy(EMAIL, PASSWORD):
        return

    courses = get_courses()

    for course in courses:
        course_id = course["id"]
        course_title = sanitize_filename(course["title"])
        course_dir = os.path.join(DOWNLOAD_DIR, course_title)
        os.makedirs(course_dir, exist_ok=True)

        lectures = get_lectures(course_id)

        for lecture in lectures:
            lecture_title = sanitize_filename(lecture.get("title", "untitled"))
            video_url = get_video_url_from_lecture(lecture)
            if not video_url:
                logger.info(f"No downloadable video found for lecture '{lecture_title}', skipping.")
                continue

            video_path = os.path.join(course_dir, f"{lecture_title}.mp4")
            if os.path.exists(video_path):
                logger.info(f"Video already exists, skipping: {video_path}")
                continue

            logger.info(f"Downloading lecture: {lecture_title}")
            download_video_from_url(video_url, video_path)

    logger.info("All downloads finished.")

if __name__ == "__main__":
    main()

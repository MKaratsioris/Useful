# Docker Image Vulnerabilities

## Use trivy and jq
```bash
$ sudo apt-get install trivy -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  trivy
0 to upgrade, 1 to newly install, 0 to remove and 2 not to upgrade.
Need to get 45,4 MB of archives.
After this operation, 153 MB of additional disk space will be used.
Get:1 https://aquasecurity.github.io/trivy-repo/deb jammy/main amd64 trivy amd64 0.62.1 [45,4 MB]
Fetched 45,4 MB in 7s (6.287 kB/s)                                                                                                                           
Selecting previously unselected package trivy.
dpkg: warning: files list file for package 'omnissa-horizon-client' missing; assuming package has no files currently installed
(Reading database ... 263371 files and directories currently installed.)
Preparing to unpack .../trivy_0.62.1_amd64.deb ...
Unpacking trivy (0.62.1) ...
Setting up trivy (0.62.1) ...
```
```bash
$ trivy image --no-progress --ignore-unfixed --severity CRITICAL,HIGH,MEDIUM,LOW --timeout 15m -f json -o report.json <image-name>:<image-version>
2025-05-09T17:01:08+02:00	INFO	[vulndb] Need to update DB
2025-05-09T17:01:08+02:00	INFO	[vulndb] Downloading vulnerability DB...
2025-05-09T17:01:08+02:00	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
2025-05-09T17:01:18+02:00	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2025-05-09T17:01:18+02:00	INFO	[vuln] Vulnerability scanning is enabled
2025-05-09T17:01:18+02:00	INFO	[secret] Secret scanning is enabled
2025-05-09T17:01:18+02:00	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-05-09T17:01:18+02:00	INFO	[secret] Please see also https://trivy.dev/v0.62/docs/scanner/secret#recommendation for faster secret detection
2025-05-09T17:01:48+02:00	INFO	[python] Licenses acquired from one or more METADATA files may be subject to additional terms. Use `--debug` flag to see all affected packages.
2025-05-09T17:01:48+02:00	INFO	Detected OS	family="debian" version="12.10"
2025-05-09T17:01:48+02:00	INFO	[debian] Detecting vulnerabilities...	os_version="12" pkg_num=429
2025-05-09T17:01:48+02:00	INFO	Number of language-specific files	num=1
2025-05-09T17:01:48+02:00	INFO	[python-pkg] Detecting vulnerabilities...
2025-05-09T17:01:48+02:00	WARN	Using severities from other vendors for some vulnerabilities. Read https://trivy.dev/v0.62/docs/scanner/vulnerability#severity-selection for details.
```
```bash
$ jq . report.json

.Results[*].Vulnerabilities
{
  ...
  "Results": [
    {},
    {
      "Vulnerabilities": [
        {
          "VulnerabilityID": "CVE-2024-6345",
          "PkgName": "setuptools",
          "PkgPath": "usr/local/lib/python3.11/site-packages/setuptools-65.5.1.dist-info/METADATA",
          "PkgIdentifier": {
            "PURL": "pkg:pypi/setuptools@65.5.1",
            "UID": "d283ebd8a092b80b"
          },
          "InstalledVersion": "65.5.1",
          "FixedVersion": "70.0.0",
          "Status": "fixed",
          "Layer": {
            "DiffID": "sha256:0ea78469ed45093f6cebf97139db2fff92fb301ddf6feb34eab48279a7770c18"
          },
          "SeveritySource": "ghsa",
          "PrimaryURL": "https://avd.aquasec.com/nvd/cve-2024-6345",
          "DataSource": {
            "ID": "ghsa",
            "Name": "GitHub Security Advisory pip",
            "URL": "https://github.com/advisories?query=type%3Areviewed+ecosystem%3Apip"
          },
          "Title": "pypa/setuptools: Remote code execution via download functions in the package_index module in pypa/setuptools",
          "Description": "A vulnerability in the package_index module of pypa/setuptools versions up to 69.1.1 allows for remote code execution via its download functions. These functions, which are used to download packages from URLs provided by users or retrieved from package index servers, are susceptible to code injection. If these functions are exposed to user-controlled inputs, such as package URLs, they can execute arbitrary commands on the system. The issue is fixed in version 70.0.",
          "Severity": "HIGH",
          "CweIDs": [
            "CWE-94"
          ],
          "VendorSeverity": {
            "alma": 3,
            "amazon": 3,
            "azure": 3,
            "bitnami": 3,
            "cbl-mariner": 3,
            "ghsa": 3,
            "oracle-oval": 3,
            "photon": 3,
            "redhat": 3,
            "rocky": 3,
            "ubuntu": 2
          },
          "CVSS": {
            "bitnami": {
              "V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
              "V3Score": 8.8
            },
            "ghsa": {
              "V3Vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
              "V3Score": 8.8
            },
            "redhat": {
              "V3Vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
              "V3Score": 8.8
            }
          },
          "References": [
            "https://access.redhat.com/errata/RHSA-2024:6726",
            "https://access.redhat.com/security/cve/CVE-2024-6345",
            "https://bugzilla.redhat.com/2297771",
            "https://bugzilla.redhat.com/show_bug.cgi?id=2297771",
            "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6345",
            "https://errata.almalinux.org/9/ALSA-2024-6726.html",
            "https://errata.rockylinux.org/RLSA-2024:6726",
            "https://github.com/pypa/setuptools",
            "https://github.com/pypa/setuptools/commit/88807c7062788254f654ea8c03427adc859321f0",
            "https://github.com/pypa/setuptools/pull/4332",
            "https://huntr.com/bounties/d6362117-ad57-4e83-951f-b8141c6e7ca5",
            "https://linux.oracle.com/cve/CVE-2024-6345.html",
            "https://linux.oracle.com/errata/ELSA-2024-6726.html",
            "https://nvd.nist.gov/vuln/detail/CVE-2024-6345",
            "https://ubuntu.com/security/notices/USN-7002-1",
            "https://www.cve.org/CVERecord?id=CVE-2024-6345"
          ]
        }
      ]
    }
  ]
}
```

## python:3.11

### 🔒 Vulnerability Detected: CVE-2024-6345
- Affected Package: setuptools
- Installed Version: 65.5.1
- Fixed Version: 70.0.0
- Severity: Likely high (based on the use of GitHub Security Advisories and needing a patch)
- Path: usr/local/lib/python3.11/site-packages/setuptools-65.5.1.dist-info/METADATA
- Reference: AVD: CVE-2024-6345
- Status: Fixed (upgrade available)

### ✅ Fix Recommendation
You should upgrade setuptools to version 70.0.0 or higher. 

#### Building a custome image
Update your Dockerfile to include:
```bash
RUN pip install --no-cache-dir --upgrade setuptools
```
or explicitly
```bash
RUN pip install --no-cache-dir setuptools==70.0.0
```

#### Using python:3.11 directly:
You'll need to override the vulnerable version after the container starts or in your derived Dockerfile.
In your Dockerfile (or wherever setuptools is installed), change the version install line from:
```bash
pip install 'setuptools==65.5.1'
```
to
```bash
pip install 'setuptools>=70.0.0'
```
Example Dockerfile:
```bash
FROM python:3.11

# Upgrade pip and setuptools to safe versions
RUN pip install --upgrade pip setuptools>=70.0.0

# (Optional) Install your other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Your existing steps (copy app code, set workdir, etc.)
COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
```

Then rebuild your image:
```bash
docker build -t your-image-name .
```
After rebuilding, re-run Trivy to verify the vulnerability is gone.

## node:18

### 🔒 Vulnerability Found
- Package: cross-spawn
- Installed Version: 7.0.3
- Vulnerability ID: CVE-2024-21538
- Severity: Likely High (source: ghsa)
- Fixed Versions:
  - 7.0.5 (preferred)
  - 6.0.6 (older major)

#### Using node:18 directly:
```bash
# Start from the official Node.js 18 image
FROM node:18

# Update npm to the latest stable version to get patched dependencies
RUN npm install -g npm@latest

# Optional: Ensure vulnerable package is not cached in global or local dirs
RUN npm cache clean --force

# Copy app code
COPY . /app
WORKDIR /app

# Install dependencies
RUN npm install

# Build or run the app
CMD ["npm", "start"]  # Or ["npm", "run", "build"] for Angular
```
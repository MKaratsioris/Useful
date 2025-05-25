import difflib
from pathlib import Path, PosixPath


folder: PosixPath = Path(__file__).parent

old_file_name: str = 'relationship_old'
old_file_path: PosixPath = folder.joinpath(f"{old_file_name}.py")

new_file_name: str = 'relationship_new'
new_file_path: PosixPath = folder.joinpath(f"{new_file_name}.py")

with open(old_file_path) as old_file:
    old_file_text = old_file.readlines()

with open(new_file_path) as new_file:
    new_file_text = new_file.readlines()

for line in difflib.unified_diff(
    old_file_text, new_file_text, fromfile=f"{old_file_path}", 
    tofile=f"{new_file_path}", lineterm=''):
    print(line)
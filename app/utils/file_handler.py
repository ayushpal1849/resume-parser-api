import os
import shutil
from app.config import UPLOAD_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(upload_file):
    file_path = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)

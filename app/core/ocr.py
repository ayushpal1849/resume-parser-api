import pytesseract
import cv2
from pypdf import PdfReader

def extract_text(path: str) -> str:
    if path.lower().endswith('.pdf'):
        try:
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except Exception as e:
            raise ValueError(f"Failed to extract text from PDF: {e}")

    image = cv2.imread(path)
    if image is None:
        raise ValueError("Could not read the file. Please ensure it is a valid image (PNG, JPG) or PDF.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)

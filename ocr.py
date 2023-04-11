import sys
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Apps\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path, output_file=None, lang='chi_sim'):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(text)

    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr.py IMAGE_PATH [OUTPUT_FILE]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    text = ocr_image(image_path, output_file)
    print(text)

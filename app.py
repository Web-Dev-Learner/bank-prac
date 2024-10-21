
import os
from PIL import Image
import fitz  
# PyMuPDF

# Step 1: Read the PDF
def read_pdf(file_path):
    try:
        pdf_document = fitz.open(file_path)
        print(f"Successfully loaded PDF: {file_path}")
        return pdf_document
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

# Step 2: Parse the PDF (optional - get metadata)
def parse_pdf(pdf_document):
    try:
        metadata = pdf_document.metadata
        print(f"PDF Metadata: {metadata}")
        return metadata
    except Exception as e:
        print(f"Error parsing PDF metadata: {e}")
        return None

# Step 3: Split the PDF into pages (optional function if you need individual page objects)
def extract_pages(pdf_document):
    pages = []
    try:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pages.append(page)
        print(f"Extracted {len(pages)} pages from PDF")
    except Exception as e:
        print(f"Error extracting pages: {e}")
    return pages

# Step 4: Convert each page into images
def convert_pages_to_images(pdf_document):
    images = []
    try:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()  # Get pixmap of the page
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Create an image from the pixmap
            images.append(img)
        print(f"Converted {len(images)} pages into images.")
    except Exception as e:
        print(f"Error converting pages to images: {e}")
        return []
    return images

# Step 5: Save the images to the specified folder
def save_images(images, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")  # Construct the file path
        image.save(image_path, 'JPEG')  # Save the image as a JPEG file
        print(f"Saved image: {image_path}")

# Main function to run the whole process
def main():
    # File paths and folders
    pdf_path = 'pdfs/sample.pdf'  # Path to your actual PDF file
    output_folder = 'img'               # Folder where images will be saved

    # Step 1: Read the PDF
    pdf_document = read_pdf(pdf_path)
    if not pdf_document:
        return

    # Step 2 (Optional): Parse metadata from PDF
    parse_pdf(pdf_document)

    # Step 3: Extract pages (if you need individual page objects)
    pages = extract_pages(pdf_document)

    # Step 4: Convert pages to images
    images = convert_pages_to_images(pdf_document)
    if images:
        # Step 5: Save the images to the output folder
        save_images(images, output_folder)

if __name__ == "__main__":
    main()

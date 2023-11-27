from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tqdm import tqdm
import os
import time

def convert_images_to_pdf(input_folder, output_pdf):
    images = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.jpeg')]
    images.sort()  # Ensure images are in the correct order

    if not images:
        print("No JPEG images found in the input folder.")
        return

    total_images = len(images)
    start_time = time.time()

    with open(output_pdf, 'wb') as pdf_file:
        pdf_canvas = canvas.Canvas(pdf_file, pagesize=letter)

        for i, image_file in enumerate(tqdm(images, desc="Converting to PDF", unit="image")):
            image_path = os.path.join(input_folder, image_file)
            img = Image.open(image_path)
            width, height = letter
            pdf_canvas.setPageSize((width, height))
            pdf_canvas.drawInlineImage(img, 0, 0, width, height)

            # Add a new page for the next image
            pdf_canvas.showPage()

            # Calculate and display percentage
            percent_complete = (i + 1) / total_images * 100
            tqdm.write(f"Progress: {percent_complete:.2f}%")

        pdf_canvas.save()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"PDF created successfully: {output_pdf}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

# Example usage
input_folder_path = 'images'
output_pdf_path = 'output.pdf'

convert_images_to_pdf(input_folder_path, output_pdf_path)

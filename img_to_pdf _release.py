import os
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import webbrowser
from PIL import Image
from PyPDF2 import PdfMerger

# Create the Tkinter GUI window
root = ctk.CTk()
root.title("Image to PDF Converter")
root.geometry("300x140")
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Define a function to convert the selected images to PDF
# Define a function to convert the selected images to PDF
def convert_to_pdf():
    # Ask the user to select the input images
    label.configure(text="Select images to convert")
    filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"))
    input_images = filedialog.askopenfilenames(filetypes=filetypes)
    if not input_images:
        return

    # Ask the user to select the output PDF file
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf")
    if not output_pdf:
        return

    # Create a PDF merger object
    pdf_merger = PdfMerger()

    # Loop through each input image and convert it to a PDF page
    for input_image in input_images:
        # Open the input image using Pillow
        image = Image.open(input_image)

        # Convert the image to RGB mode if necessary
        if image.mode == "RGBA":
            image = image.convert("RGB")
        
        label.configure(text="Configuring Images")
        global temp_pdf
        # Create a temporary PDF file for the current image
        temp_pdf = os.path.splitext(input_image)[0] + ".pdf"
        # Save the image to disk
        with open(temp_pdf, "wb") as f:
            image.save(f, "PDF", resolution=100.0)

        # Add the temporary PDF file to the PDF merger
        pdf_merger.append(temp_pdf)

    # Write the merged PDF file to disk
    with open(output_pdf, "wb") as f:
        pdf_merger.write(f)
    # Close the PDF merger object
    pdf_merger.close()
    for input_image in input_images:
        os.remove(os.path.splitext(input_image)[0]+'.pdf')
        print(os.path.splitext(input_image)[0]+ '   ---removed---')
    # Delete the temporary PDF file
    #os.remove(temp_pdf)
    label.configure(text="Pdf file saved")

def callback():
    webbrowser.open("https://github.com/entpnrusman/")
# Add a button to trigger the conversion
convert_button = ctk.CTkButton(root, text="Select images to convert", command=convert_to_pdf)
convert_button.pack(pady=10)

label = ctk.CTkLabel(root, text="Select images to convert")
label.pack(pady=10)

github_link = ctk.CTkButton(root, text="github.com/entpnrusman", command=callback)
github_link.pack(pady=10)
# Start the Tkinter main event loop
root.mainloop()

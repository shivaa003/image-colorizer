import matplotlib.pyplot as plt
import torch
import tkinter as tk
from tkinter import filedialog
from colorizers import *
from PIL import Image

# Function to select an image
def select_image():
    global img_path
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg;*.webp")])
    if img_path:
        process_image(img_path)

def process_image(img_path):
    # Load colorizers
    colorizer_eccv16 = eccv16(pretrained=True).eval()
    colorizer_siggraph17 = siggraph17(pretrained=True).eval()
    
    # Process Image
    img = load_img(img_path)
    (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
    
    # Colorize
    out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
    out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())
    
    # Display Results
    plt.figure(figsize=(12, 8))
    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title('Original')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(out_img_eccv16)
    plt.title('Output (ECCV 16)')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(out_img_siggraph17)
    plt.title('Output (SIGGRAPH 17)')
    plt.axis('off')
    
    plt.show()

# Call the image selection function
select_image()

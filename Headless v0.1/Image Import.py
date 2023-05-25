import tkinter as tk
from tkinter import filedialog
import cv2
import os

def open_image():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if file_path:

        image = cv2.imread(file_path)

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        file_dir, file_name = os.path.split(file_path)
        new_file_name = f"{first_name}_{last_name}{os.path.splitext(file_name)[1]}"
        
        images_folder = os.path.join(os.path.dirname(__file__), "Images")
        os.makedirs(images_folder, exist_ok=True)
 
        new_file_path = os.path.join(images_folder, new_file_name)
        cv2.imwrite(new_file_path, image)
        
        print(f"Image saved as: {new_file_name}")

window = tk.Tk()

button = tk.Button(window, text="Open Image", command=open_image)
button.pack()

window.mainloop()


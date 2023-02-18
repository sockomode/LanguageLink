import tkinter as tk
from tkinter import filedialog
from PIL import Image


def get_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    return img


class Profile:
    name = ''
    spokenLanguage = ''
    learningLanguage = ''
    country = ''
    email = ''
    password = ''
    image = get_image()
    age = 0
    phoneNumber = 0
    netCode = 0
    matches = []

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
    spokenLanguages = []
    learningLanguage = ''
    country = ''
    email = ''
    password = ''
    image = get_image()
    age = 0
    phoneNumber = 0
    netCode = 0
    matches = []
    likes = []

    def __init__(self, name, spoke, learn, count, age, phone, net):
        self.name = name
        self.spokenLanguage = spoke
        self.learningLanguage = learn
        self.country = count
        self.age = age
        self.phoneNumber = phone
        self.netCode = net
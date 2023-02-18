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

    def __init__(self, name, spokenLanguages, learningLanguage, country, email, password, age, phoneNumber, netCode, matches):
        self.name = name
        self.spokenLanguages = spokenLanguages
        self.learningLanguage = learningLanguage
        self.country = country
        self.email = email
        self.password = password
        self.age = age
        self.phoneNumber = phoneNumber
        self.netCode = netCode
        self.matches = matches


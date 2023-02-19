import tkinter as tk
from tkinter import filedialog
from PIL import Image
import socket

def get_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    return img

class Account:
    email = ''
    password = ''
    netCode = ''
    ipaddress = ''

class Profile(Account):
    name = ''
    spokenLanguages = []
    learningLanguage = ''
    country = ''
    #image = get_image()
    age = 0
    phoneNumber = 0
    matches = []
    likes = []

    def __init__(self, name, spokenLanguages, learningLanguage, country, email, password, age, phoneNumber, netCode):
        self.name = name
        self.spokenLanguages = spokenLanguages
        self.learningLanguage = learningLanguage
        self.country = country
        self.email = email
        self.password = password
        self.age = age
        self.phoneNumber = phoneNumber
        self.netCode = netCode
        self.ipaddress = socket.gethostbyname(socket.gethostname())

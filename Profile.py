import tkinter as tk
from tkinter import filedialog
from PIL import Image
import base64
import random
from io import BytesIO
import socket


def get_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    with open(file_path, 'rb') as image_file:
        image_content = image_file.read()
        encoded_image = base64.b64encode(image_content)
        image_str = encoded_image.decode('utf-8')

    return image_str

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
    image = get_image()
    age = 0
    phoneNumber = 0
    netCode = 0
    matches = []
    likes = []
    dislikes = []



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

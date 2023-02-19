import tkinter as tk
from tkinter import filedialog
import base64
import socket
import Messenger
import functions
import sqlite3
import threading
import time
import queue

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
    age = 0
    phoneNumber = 0
    matches = []
    likes = []
    dislikes = []
    conversations = []
    conn = sqlite3.connect('convos.db')
    c = conn.cursor()
    itr = 0

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

    def get_image(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()

        with open(file_path, 'rb') as image_file:
            image_content = image_file.read()
            encoded_image = base64.b64encode(image_content)
            image_str = encoded_image.decode('utf-8')

        self.image = image_str

    def storeConvos(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS match
                    id INTEGER PRIMARY KEY,
                    member TEXT,
                    port INTEGER
                    ''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS convo
                    id INTEGER PRIMARY KEY,
                    message TEXT,
                    time TEXT,
                    sender TEXT
                    FOREIGN KEY(match_id) REFERENCES match(id)
                    ''')
        self.conn.commit()
        self.conn.close()
        for conv in self.conversations:
            self.c.execute("INSERT INTO match (member, port) VALUES (?, ?)", (conv.member.netCode, conv.port))
            for mess in conv.messages:
                me = ''
                if mess.sent == True:
                    me = 'me'
                else:
                    me = 'them'
                self.c.execute("INSERT INTO match (message, time, sender) VALUES (?, ?, ?)", (mess.text, mess.time, me))

    def getConvos(self):
        self.c.execute('''SELECT match.member, match.port, convo.message, convo.time, convo.sender FROM match INNER JOIN convo ON match.id = convo.match_id''')
        rows = self.c.fetchall
        messInst = {}
        for row in rows:
            hold = True
            if (row[4] == 'me'):
                hold = True
            else:
                hold = False
            mess = Messenger.Message(row[2], row[3], hold)
            indexId = row[0]
            if indexId in messInst:
                messInst[indexId].append(mess)
            else:
                messInst[indexId] = [mess]
        for row in row:
            indexId = row[0]
            if indexId in messInst:
                messInst2 = messInst[indexId]
            else:
                messInst2 = []
            convo = Messenger.Conversation(row[0], row[1], messInst2)
            self.conversations.append(convo)

    profQueue = queue.Queue()
    cQueue = queue.Queue()
    def getProf(self, lang):
        if (self.itr >= len(functions.pullJsons(lang))):
            return 'Empty'
        for like in self.likes:
            if functions.pullJsons(lang)[self.itr].netCode == like.netCode:
                self.itr+=1
                self.getProf(lang)
            else:
                self.itr+=1
                return functions.pullJsons(lang)[(self.itr)-1]


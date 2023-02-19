import tkinter as tk
from tkinter import filedialog
import base64
import socket
import Messenger
import functions
import sqlite3
import json
import queue
import requests
import random
import threading
import time
import string

class Account:
    email = ''
    password = ''
    netCode = ''
    ipaddress = ''

class Profile(Account):
    name = ''
    image = ''
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
    index = 0
    itr = 0

    def __init__(self, name, spokenLanguages, learningLanguage, country, email, password, age, phoneNumber):
        self.name = name
        self.spokenLanguages = spokenLanguages
        self.learningLanguage = learningLanguage
        self.country = country
        self.email = email
        self.password = password
        self.age = age
        self.phoneNumber = phoneNumber
        self.ipaddress = socket.gethostbyname(socket.gethostname())
        self.generateNetCode()
        index = functions.giveLen(spokenLanguages[0])
        functions.sortProf(functions.profToList(self))
        #thread = threading.Thread(target=self.findMatch())
        #thread.daemon = True
        #thread.start()

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
            convo = Messenger.Conversation(row[0], row[1], messInst2, self.learningLanguage)
            self.conversations.append(convo)

    profQueue = queue.Queue()
    cQueue = queue.Queue()
    def getProf(self):
        if (self.itr >= len(functions.pullJsons(self.learningLanguage))):
            return 'Empty'
        for like in self.likes:
            if functions.pullJsons(self.learningLanguage)[self.itr].netCode == like.netCode:
                self.itr+=1
                self.getProf(self.learningLanguage)
            for dislike in self.dislikes:
                if functions.pullJsons(self.learningLanguage)[self.itr].netCode == dislike.netCode:
                    self.itr += 1
                    self.getProf(self.learningLanguage)
            if functions.pullJsons(self.learningLanguage)[self.itr].netCode == self.netCode:
                self.itr += 1
                self.getProf(self.learningLanguage)
            else:
                self.itr+=1
                return functions.pullJsons(self.learningLanguage)[(self.itr)-1]

    def createAccount(self):
        url = 'https://api.jsonbin.io/v3/b/63f1e90eebd26539d0811cb8/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        accList = json.loads(data)
        if accList == 'Hello World':
            accList = []
            nAcc = [self.netCode, self.email, self.password, self.ipaddress]
            accList.append(nAcc)
            url = 'https://api.jsonbin.io/v3/b/63f1e90eebd26539d0811cb8'
            headers = {
                'Content-Type': 'application/json',
                'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
            }
            data = json.dumps(accList)
            requests.put(url, json=data, headers=headers)
        else:
            nAcc = [self.netCode, self.email, self.password, self.ipaddress]
            accList.append(nAcc)
            url = 'https://api.jsonbin.io/v3/b/63f1e90eebd26539d0811cb8'
            headers = {
                'Content-Type': 'application/json',
                'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
            }
            data = json.dumps(accList)
            requests.put(url, json=data, headers=headers)
        functions.sortProf(self.spokenLanguages[0])
        functions.toJson(self.spokenLanguages[0])

    def generateNetCode(self):
        url = 'https://api.jsonbin.io/v3/b/63f1e90eebd26539d0811cb8/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        print(data)
        accList = data.json()
        taken = False
        characters = string.ascii_letters + string.digits
        self.netCode = ''.join(random.choice(characters) for i in range(10))
        for acc in accList:
            if acc == self.netCode:
                taken = True
                break
        while taken == True:
            self.netCode = ''.join(random.choice(characters) for i in range(10))
            for acc in accList:
                if acc == self.netCode:
                    taken = True
                    break
            taken = False

    def likeProfile(self, prof):
        self.likes.append(prof)
        for like in prof[7]:
            if (self.netCode == like[6]):
                self.matchProf(like)

    def dislikeProfile(self, prof):
        self.dislikes.append(prof)

    #THIS IS WRONG MAN
    def matchProf(self, mem):
        self.matches.append(mem)
        hold = functions.pullJsons(self.spokenLanguages[0])
        hold[self.index] = functions.profToList(self)
        functions.toJson(self.spokenLanguages[0])

    #thread this bad boy
    #def findMatch(self):
    #    while True:
    #        time.sleep(2)
    #        for match in self.matches:
    #            if match[9] != functions.pullJsons(self.spokenLanguages[0])[9]:
    #                curLen = len(self.matches)
    #                port = random.randint(1024, 65000)
    #                if (functions.pullJsons(self.spokenLanguages[0])[0] != 'Hello World'):
    #                    self.matches.append(functions.pullJsons(self.spokenLanguages[0])[9][curLen-1][6])
    #                    convo = Messenger.Conversation(self.ipaddress, port, functions.pullJsons(self.spokenLanguages[0])[9][curLen])
    #                    self.conversations.append(convo)
    #                else:
    #                    pass

    def changeName(self, name):
        self.name = name

    def changeAge(self, age):
        self.age = age

    def changeCountry(self, country):
        self.country = country
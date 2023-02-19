import socket
import threading
import datetime
import functions

class Message():
    text = ''
    time = ''
    sent = True

    def __init__(self, mess, sent):
        self.text = mess
        self.sent = sent
        curTime = datetime.datetime.now().time()
        half = ''
        hour = ''
        min = ''
        if curTime.hour > 12:
            hour = str(curTime - 12)
        else:
            hour = str(curTime)
        if curTime.hour > 11 and curTime < 24:
            half = 'pm'
        else:
            half = 'am'
        min = str(curTime.minute)
        self.time = str(hour + ":" + min + " " + half)

class Conversation():
    messages = []
    member = []
    ip = 0
    portNum = 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, portNum))

    def __init__(self, mem, port):
        self.member = functions.profToList(mem)
        self.portNum = port
        message_thread = threading.Thread(target=self.receiveMessage())
        message_thread.start()

    def __init__ (self, code, port, messlist, llang):
        for mem in functions.pullJsons(llang):
            if mem[6] == code:
                self.member = mem
        self.portNum = port
        self.messages = messlist
        message_thread = threading.Thread(target=self.receiveMessage())
        message_thread.start()

    def __init__ (self, ip, port, mem):
        self.ip = ip
        self.portNum = port
        self.member = mem
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, self.portNum))


    #gotta fix the ip thing this dont work
    def sendMessage(self, mess):
        self.sock.sendall(mess.encode())
        sentMess = Message(mess, True)
        self.messages.append(sentMess)

    def receiveMessage(self):
        while True:
            data = self.sock.recv(self.portNum)
            if not data:
                break
            message = data.decode()
            recMess = Message(message, False)
            self.messages.append(recMess)
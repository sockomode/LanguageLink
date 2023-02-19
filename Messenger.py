import socket
import Profile
import threading
import datetime

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
            time = 'pm'
        else:
            time = 'am'
        min = str(curTime.minute)
        self.time = str(hour + ":" + min + " " + half)

class Conversation():
    messages = []
    member = Profile
    portNum = 80
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((member.ipaddress, portNum))

    def __init__(self, mem, port):
        self.member = mem
        self.portNum = port
        message_thread = threading.Thread(target=self.receiveMessage())
        message_thread.start()

    def sendMessage(self, mess):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        receiver_address = (self.member.ipaddress, self.portNum)
        sock.connect(receiver_address)
        sock.sendall(mess.encode())
        sock.close()
        sentMess = Message(mess, True)
        self.messages.append(sentMess)

    def receiveMessage(self):
        while True:
            data = self.client_socket.recv(self.portNum)
            if not data:
                break
            message = data.decode()
            recMess = Message(message, False)
            self.messages.append(recMess)

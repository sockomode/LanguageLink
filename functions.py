import Profile
import json
import requests
import random


engSpeak = []
chiSpeak = []
japanSpeak = []
gerSpeak = []
frenSpeak = []
spanSpeak = []
italSpeak = []
def sortProf(sortMe):
    for lang in sortMe[1]:
        if lang == 'English':
            engSpeak.append(sortMe)
        if lang == 'Chinese':
            chiSpeak.append(sortMe)
        if lang == 'Japanese':
            japanSpeak.append(sortMe)
        if lang == 'German':
            gerSpeak.append(sortMe)
        if lang == 'French':
            frenSpeak.append(sortMe)
        if lang == 'Spanish':
            spanSpeak.append(sortMe)
        if lang == 'Italian':
            italSpeak.append(sortMe)

def profToList(prof):
    rList = []
    rList.append(prof.name)
    rList.append(prof.spokenLanguages)
    rList.append(prof.learningLanguage)
    rList.append(prof.country)
    rList.append(prof.age)
    rList.append(prof.phoneNumber)
    rList.append(prof.netCode)
    rList.append(prof.likes)
    rList.append(prof.dislikes)
    rList.append(prof.matches)
    return rList
def toJson(type):
    if (type == 'Japanese'):
        url = 'https://api.jsonbin.io/v3/b/63f18a85ace6f33a22e12bce'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = japanSpeak
        requests.put(url, json=data, headers=headers)
    if (type == 'Chinese'):
        url = 'https://api.jsonbin.io/v3/b/63f18aa1ebd26539d080fdb3'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = chiSpeak
        requests.put(url, json=data, headers=headers)
    elif (type == 'German'):
        url = 'https://api.jsonbin.io/v3/b/63f18a90c0e7653a057a3d8d'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = gerSpeak
        requests.put(url, json=data, headers=headers)
    elif (type == 'French'):
        url = 'https://api.jsonbin.io/v3/b/63f18aabace6f33a22e12bdc'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = frenSpeak
        requests.put(url, json=data, headers=headers)
    elif (type == 'Spanish'):
        url = 'https://api.jsonbin.io/v3/b/63f18ab3c0e7653a057a3d9c'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = spanSpeak
        requests.put(url, json=data, headers=headers)
    elif (type == 'Italian'):
        url = 'https://api.jsonbin.io/v3/b/63f18abac0e7653a057a3da0'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = italSpeak
        requests.put(url, json=data, headers=headers)
    elif (type == 'English'):
        url = 'https://api.jsonbin.io/v3/b/63f18a99ace6f33a22e12bd5'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = engSpeak
        requests.put(url, json=data, headers=headers)

def pullJsons(lang):
    if (lang == 'English'):
        url = 'https://api.jsonbin.io/v3/b/63f18a99ace6f33a22e12bd5/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'Spanish'):
        url = 'https://api.jsonbin.io/v3/b/63f18ab3c0e7653a057a3d9c/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'French'):
        url = 'https://api.jsonbin.io/v3/b/63f18aabace6f33a22e12bdc/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'Japanese'):
        url = 'https://api.jsonbin.io/v3/b/63f18a85ace6f33a22e12bce/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'Chinese'):
        url = 'https://api.jsonbin.io/v3/b/63f18aa1ebd26539d080fdb3/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'Italian'):
        url = 'https://api.jsonbin.io/v3/b/63f18abac0e7653a057a3da0/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)
    elif (lang == 'German'):
        url = 'https://api.jsonbin.io/v3/b/63f18a90c0e7653a057a3d8d/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data)

def match_profiles(profile1, profile2):
    if profile1 in profile2.likes and profile2 in profile1.likes:
        port = random.randint(1024, 65000)
        profile1.matches.append(profile2)
        profile2.matches.append(profile1)
    

spoken = ['German', 'English']
test = Profile.Profile('Alec', spoken, 'Japanese', 'USA', 'alecjsommerhauser@gmail.com', 'Password',  22, 8057967740, 'A43DKF32KS')
test1 = Profile.Profile('Elijah', spoken, 'Chinese', 'USA', 'eli123013@gmail.com', 'Password',  19 , 1234567890, 'XD4LDR15FF')
sortProf(profToList(test))

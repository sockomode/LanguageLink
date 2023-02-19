import json
import requests

engSpeak = []
chiSpeak = []
japanSpeak = []
gerSpeak = []
frenSpeak = []
spanSpeak = []
italSpeak = []

def fill():
    if pullJsons('English')[0] == 'Hello World':
        engSpeak = []
    else:
        engSpeak = pullJsons('English')
    if pullJsons('Chinese') == 'Hello World':
        chiSpeak = []
    else:
        chiSpeak = pullJsons('Chinese')
    if pullJsons('Japanese') == 'Hello World':
        japanSpeak = []
    else:
        japanSpeak = pullJsons('Japanese')
    if pullJsons('German') == 'Hello World':
        gerSpeak = []
    else:
        gerSpeak = pullJsons('German')
    if pullJsons('French') == 'Hello World':
        frenSpeak = []
    else:
        frenSpeak = pullJsons('French')
    if pullJsons('Spanish') == 'Hello World':
        spanSpeak = []
    else:
        spanSpeak = pullJsons('Spanish')
    if pullJsons('Italian') == 'Hello World':
        italSpeak = []
    else:
        italSpeak = pullJsons('Italian')
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
    rList.append(prof.image)
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

def giveLen(lang):
    if lang == 'English':
        return len(engSpeak)
    if lang == 'Chinese':
        return len(chiSpeak)
    if lang == 'Japanese':
        return len(japanSpeak)
    if lang == 'German':
        return len(gerSpeak)
    if lang == 'French':
        return len(frenSpeak)
    if lang == 'Spanish':
        return len(spanSpeak)
    if lang == 'Italian':
        return len(italSpeak)

def pullJsons(lang):
    if (lang == 'English'):
        url = 'https://api.jsonbin.io/v3/b/63f18a99ace6f33a22e12bd5/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'Spanish'):
        url = 'https://api.jsonbin.io/v3/b/63f18ab3c0e7653a057a3d9c/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'French'):
        url = 'https://api.jsonbin.io/v3/b/63f18aabace6f33a22e12bdc/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'Japanese'):
        url = 'https://api.jsonbin.io/v3/b/63f18a85ace6f33a22e12bce/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'Chinese'):
        url = 'https://api.jsonbin.io/v3/b/63f18aa1ebd26539d080fdb3/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'Italian'):
        url = 'https://api.jsonbin.io/v3/b/63f18abac0e7653a057a3da0/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
    elif (lang == 'German'):
        url = 'https://api.jsonbin.io/v3/b/63f18a90c0e7653a057a3d8d/latest'
        headers = {
            'X-Master-Key': '$2b$10$IJVhxdyA.TMihLxk.V.vBu/1kMCV2y.xDxMrrlbTwatPnQ105RTxm'
        }
        data = requests.get(url, json=None, headers=headers)
        return json.dumps(data.json())
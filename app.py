
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import Profile
import json
import requests


engSpeak = []
chiSpeak = []
japanSpeak = []
gerSpeak= []
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
    return rList
def toJson(type):
    if (type == 'All'):
        english = json.dumps(engSpeak)
        chinese = json.dumps(chiSpeak)
        japanese = json.dumps(japanSpeak)
        german = json.dumps(gerSpeak)
        french = json.dumps(frenSpeak)
        spanish = json.dumps(spanSpeak)
        italian = json.dumps(italSpeak)
        rList = [english, chinese, japanese, german, french, spanish, italian]
        return rList
    elif (type == 'English'):
        english = json.dumps(engSpeak)
        return english
    elif (type == 'Chinese'):
        chinese = json.dumps(chiSpeak)
        return chinese
    elif (type == 'Japanese'):
        japanese = json.dumps(japanSpeak)
        return japanese
    elif (type == 'German'):
        german = json.dumps(gerSpeak)
        return german
    elif (type == 'French'):
        french = json.dumps(frenSpeak)
        return french
    elif (type == 'Spanish'):
        spanish = json.dumps(spanSpeak)
        return spanish
    elif (type == 'Italian'):
        italian = json.dumps(italSpeak)
        return italian

spoken = ['German', 'English']
test = Profile.Profile('Alec', spoken, 'Japanese', 'USA', 'alecjsommerhauser@gmail.com', 'Password',  22, 8057967740, 'A43DKF32KS')
sortProf(profToList(test))

app = Flask(__name__)

@app.route('/german')
def german():
    return toJson('German')

@app.route('/english')
def english():
    return toJson('English')

@app.route('/chinese')
def chinese():
    return toJson('Chinese')

@app.route('/japanese')
def japanese():
    return toJson('Japanese')

@app.route('/french')
def french():
    return toJson('French')

@app.route('/spanish')
def spanish():
    return toJson('Spanish')

@app.route('/italian')
def italian():
    return toJson('Italian')

@app.route('/test', methods=['POST'])
def myscript():
    json_data = requests.get_data()
    data = json.loads(json_data)
    return "OK"

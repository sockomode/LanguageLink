import Profile
import json

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
            print('AYO')
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
print(toJson('German'))
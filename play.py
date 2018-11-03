import os

file = 'sounds/punch.wav'

def play(file):
    os.system('omxplayer -o local ' + file + '')

def sendSignal(code):
    os.system('../433Utils/RPi_utils/codesend '+code+' 5 500')

def turnOffLights():
    print "Turning off lights"
    sendSignal('0')

def turnOnLights():
    sendSignal('1')


def scareMe():
    print "Now scare me!"
    play(file)
    turnOffLights()
    #play(file)
    turnOnLights()

scareMe()


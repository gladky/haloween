import os
import pygame
import time
from sensor import read

punchSound = 'sounds/punch.wav'
attractSound = 'sounds/attract2.ogg'
pygame.init()
pygame.mixer.music.load(punchSound)
os.system('amixer cset numid=3 1')


def sendSignal(code):
    os.system('../433Utils/RPi_utils/codesend '+code+' 5 500')

def turnOffLights():
    print "Turning off lights"
    sendSignal('0')

def turnOnLights():
    sendSignal('1')


def scareMe():
    print "Now scare me!"
    pygame.mixer.music.play()
    turnOffLights()
    #play(file)

    time.sleep(5)
    turnOnLights()

def attractAndScare():
    pygame.mixer.music.load(attractSound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    pygame.mixer.music.load(punchSound)

    print "Wait for signal"
    for x in range(600):
        result = read()
        time.sleep(0.1)
        if result:
            print "Signal detected"
            scareMe()
            break
        else:
            print "Nobody here"

attractAndScare()


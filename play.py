import os
import pygame
import time

punchSound = 'sounds/punch.wav'
attractSound = 'sounds/punch.wav'
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
    turnOnLights()

def attractAndScare():
    pygame.mixer.music.load(attractSound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    pygame.mixer.music.load(punchSound)

    print "Wait for signal"
    time.sleep(2)
    print "Signal detected"
    scareMe()

attractAndScare()


import time
import pygame
import datetime

freq = 1000    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.set_volume(10)
def playsound(music):
    pygame.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(5)

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        # print "Playing..."
        pygame.mixer.music.play(5)
        # print("playing...........")
        pygame.mixer.music.rewind()
        clock.tick(1000)

watertime=0
eyestime=0
physicletime=0
while True:
    with open("healthyprogram.txt",'a') as f:
        time.sleep(1)
        watertime+=1
        eyestime+=1
        physicletime+=1
        if(watertime==20*60):
            playsound("water.mp3")
            if input("Are you drinking water :")=='done':
                f.write(datetime.datetime.now(),"you drank water at \n")
                pygame.mixer.music.stop()
            watertime=0
        elif(eyestime==30*60):
            playsound('eyes.mp3')
            if input("Are you drinking water :")=='done':
                f.write(datetime.datetime.now(),"eyes excersice \n")

                pygame.mixer.music.stop()

            eyestime=0
        elif physicletime==45*60:
            playsound("physical.mp3")
            if input("Are you drinking water :")=='done':
                f.write(datetime.datetime.now(),"physical excersice \n")

                pygame.mixer.music.stop()
            physicletime=0
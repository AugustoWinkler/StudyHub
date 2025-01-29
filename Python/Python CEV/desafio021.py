#Objetivo faça um programa que reproduza um Arquivo Mp3

import pygame

pygame.init()
pygame.mixer_music.load('ragnaroktheme.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()





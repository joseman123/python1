# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:41:54 2023
@author: z120
"""
import sys
import pygame
from Boton import Button
from juego_oficial import *

pygame.init()

pygame.display.set_caption("PRINCESAS DEL CAOS ELEMENTAL")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BKGN = pygame.image.load("fondo_no mute.jpg")
BKGN4 = pygame.image.load("ganaste.jpg")
BKGN5 = pygame.image.load("perdiste.jpg")
BKGN6 = pygame.image.load("fondo_si mute.jpg")
BKGNTIERRA = pygame.image.load("tierracaravana.jpg")
BKGNFUEGO = pygame.image.load("fuegocaravana.jpg")
BKGNAIRE = pygame.image.load("airecaravana.jpg")
BKGNAGUA = pygame.image.load("aguacaravana.jpg")

size = (1280, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

jugador_puntos = 0
intentos_restantes = 3

def get_font(size):
    return pygame.font.Font(None, size)

def dibujar_boton_continuar():
    font = get_font(30)
    texto = font.render("CONTINUAR", True, WHITE)
    boton_rect = texto.get_rect()
    boton_rect.center = (size[0] // 2, size[1] - 50)
    screen.blit(texto, boton_rect)
    return boton_rect

def mostrar_resultado(ganador):
    if ganador:
        img_resultado = pygame.image.load("ganaste.jpg")
    else:
        img_resultado = pygame.image.load("perdiste.jpg")
    screen.blit(img_resultado, (0, 0))
    pygame.display.flip()
    pygame.time.wait(2000)

def play_music():
    pygame.mixer.music.load("the-princess-and-her-jewels-120679.mp3")
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def win():
    play_music()
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill(BLACK)
        screen.blit(BKGN4, (100, 0))

        OPTIONS_TEXT = get_font(75).render("¡Ganaste!", True, BLUE)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(690, 180))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(695, 670), 
        text_input="Menu", font=get_font(45), base_color=WHITE, hovering_color=BLUE)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def lose():
    play_music()
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill(BLACK)
        screen.blit(BKGN5, (100, 0))

        OPTIONS_TEXT = get_font(75).render("Perdiste!", True, WHITE)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(690, 180))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(695, 670), 
        text_input="Menu", font=get_font(45), base_color=WHITE, hovering_color=BLUE)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    play_music()

    is_music_playing = True
    is_BKGN6_displayed = False

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        if is_BKGN6_displayed:
            screen.blit(BKGN6, (0, 0))
        else:
            screen.blit(BKGN, (0, 0))

        button_position = (1100, 700)
        button = Button(image=pygame.image.load("Play Rect.png"), pos=button_position, 
                            text_input="", font=get_font(30), base_color=WHITE, hovering_color=GREEN)

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(680, 480), 
                            text_input="", font=get_font(60), base_color=WHITE, hovering_color=RED)
        
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(685, 580), 
                            text_input="", font=get_font(60), base_color=WHITE, hovering_color=RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.checkForInput(MENU_MOUSE_POS):
                    if is_BKGN6_displayed:
                        screen.blit(BKGN, (0, 0))
                        play_music()
                        is_music_playing = True
                        is_BKGN6_displayed = False
                    else:
                        screen.blit(BKGN6, (0, 0))
                        stop_music()
                        is_music_playing = False
                        is_BKGN6_displayed = True
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    win()
                if event.key == pygame.K_l:
                    lose()

        pygame.display.update()

main_menu()

pygame.display.flip()
clock.tick(60)

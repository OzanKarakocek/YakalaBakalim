import turtle
import pygame
import random


def arka_plan_muzigi(volume=0.1):
    pygame.mixer.init()
    pygame.mixer.music.load("Dynamic Music.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops=-1)


drawing_board = turtle.Screen()
drawing_board.bgcolor("#43523d")
drawing_board.title("Yakala Bakalım")


drawing_board._root.iconbitmap("simge.ico")


arka_plan_muzigi(volume=0.1)


kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("white")
kaplumbaga.speed(5)
kaplumbaga.penup()


skor = 0
sure = 30
oyun_devam_ediyor = True


yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.goto(0, 500)
yazi.color("white")


def skoru_guncelle():
    yazi.clear()
    yazi.write(f"Skor: {skor}  Süre: {sure}", align="center", font=("Arial", 18, "normal"))


def sure_azalt():
    global sure, oyun_devam_ediyor
    if sure > 0:
        sure -= 1
        skoru_guncelle()
        drawing_board.ontimer(sure_azalt, 1000)
    else:
        oyun_devam_ediyor = False
        yazi.clear()
        yazi.goto(0, 0)
        yazi.write(f"Oyun Bitti! Skorun: {skor}", align="center", font=("Arial", 24, "bold"))
        kaplumbaga.hideturtle()

def otomatik_yer_degistir():
    if oyun_devam_ediyor:
        yeni_x = random.randint(-200, 200)
        yeni_y = random.randint(-200, 200)
        kaplumbaga.goto(yeni_x, yeni_y)
        drawing_board.ontimer(otomatik_yer_degistir, 3000)


def kaplumbagaya_tiklandi(x, y):
    global skor
    if oyun_devam_ediyor and kaplumbaga.distance(x, y) < 20:
        skor += 1
        yeni_x = random.randint(-200, 200)
        yeni_y = random.randint(-200, 200)
        kaplumbaga.goto(yeni_x, yeni_y)
        skoru_guncelle()


kaplumbaga.onclick(kaplumbagaya_tiklandi)


skoru_guncelle()
sure_azalt()
otomatik_yer_degistir()


turtle.done()

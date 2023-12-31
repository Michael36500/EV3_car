from time import sleep
import pygame
import websocket

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 100)

window = pygame.display.set_mode((600, 300))

keys = {"left":False, "right":False, "up":False, "down":False}

ws = websocket.create_connection("ws://192.168.10.29:8000")
send = [0, 0]

while True:
    window.fill((255, 255, 255))
    # pygame.draw.rect(window, (255, 0, 0), (0, 0, 100, 100))

    for eve in pygame.event.get():
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_LEFT:
                keys["left"] = True
            if eve.key == pygame.K_RIGHT:
                keys["right"] = True
            if eve.key == pygame.K_DOWN:
                keys["down"] = True
            if eve.key == pygame.K_UP:
                keys["up"] = True

        if eve.type == pygame.KEYUP:
            if eve.key == pygame.K_LEFT:
                keys["left"] = False
            if eve.key == pygame.K_RIGHT:
                keys["right"] = False
            if eve.key == pygame.K_DOWN:
                keys["down"] = False
            if eve.key == pygame.K_UP:
                keys["up"] = False

    text = ""
    for x in keys:
        if keys[x]:
            text += x + " "
    
    window.blit(my_font.render(text, True, (0,0,0)), (50, 50))

    text = ""
    if keys["left"]: text += "-1;"
    elif keys["right"]: text += "1;"
    else: text += "0;"

    if keys["up"]: text += "0.5"
    elif keys["down"]: text += "-0.25"
    else: text += "0"

    ws.send(text)


    sleep(0.1)
    pygame.display.update() 
"""
Freeze_tag

Description:
"""
# import tsk
import random
import pygame

pygame.init()

# create the window
w = pygame.display.set_mode([1000, 500])

# Create the players
p1 = pygame.Rect(400, 250, 20, 20)
p2 = pygame.Rect(500, 250, 20, 20)
p3 = pygame.Rect(600, 250, 20, 20)

# Create the variables
run = True
it = 0
timer = 0
p1color = (255, 255, 255)
p2color = (255, 255, 255)
p3color = (255, 255, 255)
itcolor = (255, 0, 0)
frozencolor = (170, 0, 255)
frozen = 0
p1m = True
p2m = True
p3m = True
p2alive = True
p3alive = True
p1alive = True

# Set the IT
who = random.randint(1, 3)
if who == 1:
    it = p1
    p1color = itcolor
if who == 2:
    it = p2
    p2color = itcolor
if who == 3:
    it = p3
    p3color = itcolor


# def p1_move():
#     global p1
#     global p1m
#     if p1m == True:
#         if tsk.get_key_pressed(pygame.K_w):
#             p1.y -= 3
#         if tsk.get_key_pressed(pygame.K_s):
#             p1.y += 3
#         if tsk.get_key_pressed(pygame.K_a):
#             p1.x -= 3
#         if tsk.get_key_pressed(pygame.K_d):
#             p1.x += 3
#
#
# def p2_move():
#     global p2
#     global p2m
#     if p2m == True:
#         if tsk.get_key_pressed(pygame.K_i):
#             p2.y -= 3
#         if tsk.get_key_pressed(pygame.K_k):
#             p2.y += 3
#         if tsk.get_key_pressed(pygame.K_j):
#             p2.x -= 3
#         if tsk.get_key_pressed(pygame.K_l):
#             p2.x += 3
#
#
# def p3_move():
#     global p3
#     global p3m
#     if p3m == True:
#         if tsk.get_key_pressed(pygame.K_UP):
#             p3.y -= 3
#         if tsk.get_key_pressed(pygame.K_DOWN):
#             p3.y += 3
#         if tsk.get_key_pressed(pygame.K_LEFT):
#             p3.x -= 3
#         if tsk.get_key_pressed(pygame.K_RIGHT):
#             p3.x += 3


# Game Intro
print(
    'Welcome to freeze tag! A random player gets to be the "IT" and tag everyone! Good luck running away from the "IT" :)')

# Game loop
while run:
    w.fill((81, 214, 201))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if p1m == True:
        if keys[pygame.K_UP]:
            p3.y -= 1
        if keys[pygame.K_DOWN]:
            p3.y += 1
        if keys[pygame.K_LEFT]:
            p3.x -= 1
        if keys[pygame.K_RIGHT]:
            p3.x += 1

    if p2m == True:
        if keys[pygame.K_w]:
            p1.y -= 1
        if keys[pygame.K_s]:
            p1.y += 1
        if keys[pygame.K_a]:
            p1.x -= 1
        if keys[pygame.K_d]:
            p1.x += 1

    if p3m == True:
        if keys[pygame.K_i]:
            p2.y -= 1
        if keys[pygame.K_k]:
            p2.y += 1
        if keys[pygame.K_j]:
            p2.x -= 1
        if keys[pygame.K_l]:
            p2.x += 1

    # Draw the players
    pygame.draw.rect(w, p1color, p1)
    pygame.draw.rect(w, p2color, p2)
    pygame.draw.rect(w, p3color, p3)

    # it p1 collision between players
    # Frozen and helping the frozen
    if it == p1:

        if p1.x + 25 > p2.x and p1.x - 25 < p2.x:
            if p1.y + 25 > p2.y and p1.y - 25 < p2.y:
                frozen = p2
                p2color = frozencolor
                p2m = False
                p2alive = False
        if p3.x + 25 > p2.x and p3.x - 25 < p2.x:
            if p3.y + 25 > p2.y and p3.y - 25 < p2.y:
                p2m = True
                p2color = (255, 255, 255)
                p2alive = True

        if p1.x + 25 > p3.x and p1.x - 25 < p3.x:
            if p1.y + 25 > p3.y and p1.y - 25 < p3.y:
                frozen = p3
                p3color = frozencolor
                p3m = False
                p3alive = False

        if p2.x + 25 > p3.x and p2.x - 25 < p3.x:
            if p2.y + 25 > p3.y and p2.y - 25 < p3.y:
                frozen = p3
                p3color = (255, 255, 255)
                p3m = True
                p3alive = True

        if p2alive == False and p3alive == False:
            print("Player 1 won!")
            run = False

    # It p2 collision between players
    # frozen and gelping the frozen
    if it == p2:

        if p2.x + 25 > p1.x and p2.x - 25 < p1.x:
            if p2.y + 25 > p1.y and p2.y - 25 < p1.y:
                frozen = p1
                p1color = frozencolor
                p1m = False
                p1alive = False

        if p3.x + 25 > p1.x and p3.x - 25 < p1.x:
            if p3.y + 25 > p1.y and p3.y - 25 < p1.y:
                frozen = p1
                p1color = (255, 255, 255)
                p1m = True
                p1alive = True

        if p2.x + 25 > p3.x and p2.x - 25 < p3.x:
            if p2.y + 25 > p3.y and p2.y - 25 < p3.y:
                frozen = p3
                p3color = frozencolor
                p3m = False
                p3alive = False

        if p1.x + 25 > p3.x and p1.x - 25 < p3.x:
            if p1.y + 25 > p3.y and p1.y - 25 < p3.y:
                frozen = p3
                p3color = (255, 255, 255)
                p3m = True
                p3alive = True

        if p3alive == False and p1alive == False:
            print("Player 2 won!")
            run = False

    # It p3 collision between players
    # frozen and helping the frozen
    if it == p3:

        if p3.x + 25 > p1.x and p3.x - 25 < p1.x:
            if p3.y + 25 > p1.y and p3.y - 25 < p1.y:
                frozen = p1
                p1color = frozencolor
                p1m = False
                p1alive = False

        if p2.x + 25 > p1.x and p2.x - 25 < p1.x:
            if p2.y + 25 > p1.y and p2.y - 25 < p1.y:
                frozen = p1
                p1color = (255, 255, 255)
                p1m = True
                p1alive = True

        if p3.x + 25 > p2.x and p3.x - 25 < p2.x:
            if p3.y + 25 > p2.y and p3.y - 25 < p2.y:
                frozen = p2
                p2color = frozencolor
                p2m = False
                p2alive = False

        if p1.x + 25 > p2.x and p1.x - 25 < p2.x:
            if p1.y + 25 > p2.y and p1.y - 25 < p2.y:
                frozen = p2
                p2color = (255, 255, 255)
                p2m = True
                p2alive = True

        if p2alive == False and p1alive == False:
            print("Player 3 won!")
            run = False

    # flip the display
    pygame.display.flip()

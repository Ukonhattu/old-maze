import pygame, sys
from pygame.locals import *
t0="images/passable.png"
t1="images/wall.png"
t2="images/pit.png"
t3="images/stone.png"
t4="images/start.png"
t5="images/goal.png"
t6="images/crack.png"
t7="images/bomb.png"
grid=0
cx=0
cy=0
cordinate=[]
maze=[]
loop=0
mazeid=1
move_event=1
load_event=1

pygame.init()

screen=pygame.display.set_mode((480,480),0,32)

i0=pygame.image.load(t0).convert_alpha()
i1=pygame.image.load(t1).convert_alpha()
ix=pygame.image.load(t2).convert_alpha()
ir=pygame.image.load(t3).convert_alpha()
iz=pygame.image.load(t4).convert()
ig=pygame.image.load(t5).convert_alpha()
ic=pygame.image.load(t6).convert_alpha()
ib=pygame.image.load(t7).convert_alpha()

colorkey = iz.get_at((0,0))
iz.set_colorkey(colorkey, RLEACCEL)


while cy < 480:
    cordinate.append((cx,cy))
    cx += 32
    if cx >= 480:
        cy += 32
        cx = 0

while True:

    if load_event == 1:
        if mazeid > 6:
            pygame.quit()
            sys.exit()
        f=open("Mazes/Maze%s.txt" % mazeid,"r") 
        while grid <= 224:
            nl = f.read(1)
            if nl == "0":
                maze += [i0]
                grid += 1
            if nl == "1":
                maze += [i1]
                grid += 1
            if nl == "x":
                maze += [ix]
                grid += 1
            if nl == "r":
                maze += [ir]
                grid += 1
            if nl == "s":
                maze += [i0]
                cx,cy = cordinate[grid]
                grid += 1
            if nl == "g":
                maze += [ig]
                grid += 1
            if nl == "#":
                maze += [ic]
                grid += 1
            if nl == "b":
                maze += [ib]
                grid += 1
        f.close()
        grid = 0
        load_event = 0
        mazeid += 1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if move_event == 1:
                    if cy > 0:
                        testdir = ( cy // 32 * 15 + cx // 32 ) - 15
                        if maze[testdir] == i0:
                            cy -= 32
                        if maze[testdir] == ig:
                            load_event = 1
                        if maze[testdir] == ir:
                            testdir2 = testdir - 15
                            if cy - 32 > 0:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cy -= 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cy -= 32
                                if maze[testdir2] == ic:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cy -= 32
                        if maze[testdir] == ic:
                            maze[testdir] = ix
                            cy -= 32
                        if maze[testdir] == ib:
                            testdir2 = testdir - 15
                            if cy - 32 > 0:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ib
                                    cy -= 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cy -= 32
                                if maze[testdir2] == ir:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cy -= 32
                                if maze[testdir2] == i1:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cy -= 32
                    move_event = 0
            if event.key == K_DOWN:
                if move_event == 1:
                    if cy < 448:
                        testdir = ( cy // 32 * 15 + cx // 32 ) + 15
                        if maze[testdir] == i0:
                            cy += 32
                        if maze[testdir] == ig:
                            load_event = 1
                        if maze[testdir] == ir:
                            testdir2 = testdir + 15
                            if cy + 32 < 448:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cy += 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cy += 32
                                if maze[testdir2] == ic:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cy += 32
                        if maze[testdir] == ic:
                            maze[testdir] = ix
                            cy += 32
                        if maze[testdir] == ib:
                            testdir2 = testdir + 15
                            if cy + 32 < 448:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ib
                                    cy += 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cy += 32
                                if maze[testdir2] == ir:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cy += 32
                                if maze[testdir2] == i1:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cy += 32
                    move_event = 0
            if event.key == K_LEFT:
                if move_event == 1:
                    if cx > 0:
                        testdir = ( cy // 32 * 15 + cx // 32 ) - 1
                        if maze[testdir] == i0:
                            cx -= 32
                        if maze[testdir] == ig:
                            load_event = 1
                        if maze[testdir] == ir:
                            testdir2 = testdir - 1
                            if cx - 32 > 0:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cx -= 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cx -= 32
                                if maze[testdir2] == ic:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cx -= 32
                        if maze[testdir] == ic:
                            maze[testdir] = ix
                            cx -= 32
                        if maze[testdir] == ib:
                            testdir2 = testdir - 1
                            if cx - 32 > 0:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ib
                                    cx -= 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cx -= 32
                                if maze[testdir2] == ir:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cx -= 32
                                if maze[testdir2] == i1:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cx -= 32
                    move_event = 0
            if event.key == K_RIGHT:
                if move_event == 1:
                    if cx < 448:
                        testdir = ( cy // 32 * 15 + cx // 32 ) + 1
                        if maze[testdir] == i0:
                            cx += 32
                        if maze[testdir] == ig:
                            load_event = 1
                        if maze[testdir] == ir:
                            testdir2 = testdir + 1
                            if cx + 32 < 448:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cx += 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cx += 32
                                if maze[testdir2] == ic:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cx += 32
                        if maze[testdir] == ic:
                            maze[testdir] = ix
                            cx += 32
                        if maze[testdir] == ib:
                            testdir2 = testdir + 1
                            if cx + 32 < 448:
                                if maze[testdir2] == i0:
                                    maze[testdir] = i0
                                    maze[testdir2] = ib
                                    cx += 32
                                if maze[testdir2] == ix:
                                    maze[testdir] = i0
                                    maze[testdir2] = ix
                                    cx += 32
                                if maze[testdir2] == ir:
                                    maze[testdir] = i0
                                    maze[testdir2] = i0
                                    cx += 32
                                if maze[testdir2] == i1:
                                    maze[testdir] = i0
                                    maze[testdir2] = ir
                                    cx += 32
                    move_event = 0
            if event.key == K_r:
                mazeid -= 1
                load_event = 1
                move_event = 0
    move_event=1

    screen.blit(maze[loop], cordinate[loop])

    loop += 1
    if loop > 224: loop = 0

    screen.blit(iz, (cx,cy))

    if load_event == 1: maze=[]

    pygame.display.update()

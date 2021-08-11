import pygame
import sys
import math
import time
import random
import tkinter as tk
import numpy as np

start = time.time()
pygame.init()
innerloop = True
RADIUS = 35
WIDTH = 640
HEIGHT = 640
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 191, 255)
KINGRED = (139, 0, 0)
KINGBLACK = (180, 180, 180)
BLOCK_SIZE = 80
BOARD_DIM = 8
game_board = [[None] * 8 for _ in range(8)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
r, c = (8, 8)
checkers_pos = [[0 for i in range(c)] for j in range(r)]


def draw_board():
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            x = BLOCK_SIZE * column
            y = BLOCK_SIZE * row
            block_color = WHITE if (row + column) % 2 == 0 else BLACK
            pygame.draw.rect(screen, block_color, [x, y, BLOCK_SIZE, BLOCK_SIZE])
    create_initial_pos()


def create_initial_pos():
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            circle_x = (BLOCK_SIZE * column) + 40
            circle_y = (BLOCK_SIZE * row) + 40
            if ((row + column) % 2 != 0) and row < 3:
                checkers_pos[column][row] = 1
            if ((row + column) % 2 != 0) and row > 4:
                checkers_pos[column][row] = 2


def draw_checkers():
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            block_color = WHITE if (row + column) % 2 == 0 else BLACK
    for row in range(BOARD_DIM):
        for column in range(BOARD_DIM):
            if checkers_pos[column][row] == 1:
                circle_x = (BLOCK_SIZE * column) + 40
                circle_y = (BLOCK_SIZE * row) + 40
                pygame.draw.circle(screen, RED, (circle_x, circle_y), RADIUS, 35)
            if checkers_pos[column][row] == 2:
                circle_x = (BLOCK_SIZE * column) + 40
                circle_y = (BLOCK_SIZE * row) + 40
                pygame.draw.circle(screen, WHITE, (circle_x, circle_y), RADIUS, 2)
            if checkers_pos[column][row] == 3:
                circle_x = (BLOCK_SIZE * column) + 40
                circle_y = (BLOCK_SIZE * row) + 40
                pygame.draw.circle(screen, KINGRED, (circle_x, circle_y), RADIUS, 35)
            if checkers_pos[column][row] == 4:
                circle_x = (BLOCK_SIZE * column) + 40
                circle_y = (BLOCK_SIZE * row) + 40
                pygame.draw.circle(screen, KINGBLACK, (circle_x, circle_y), RADIUS, 6)


def check_possible(mosX, mosY, arr):
    itr = 0
    temp = checkers_pos[mosX][mosY]

    DL = (mosX - 1, mosY + 1)
    DR = (mosX + 1, mosY + 1)
    UL = (mosX - 1, mosY - 1)
    UR = (mosX + 1, mosY - 1)
    DDL = (mosX - 2, mosY + 2)
    DDR = (mosX + 2, mosY + 2)
    UUL = (mosX - 2, mosY - 2)
    UUR = (mosX + 2, mosY - 2)

    if temp == 1:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            arr.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            arr.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 3 and checkers_pos[xl][yl] != 1 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            arr.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 3 and checkers_pos[xr][yr] != 1 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            arr.insert(itr, DDR)
            itr += 1
    if temp == 2:
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            arr.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            arr.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 4 and checkers_pos[xul][
            yul] != 2 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            arr.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 4 and checkers_pos[xur][
            yur] != 2 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            arr.insert(itr, UUR)
            itr += 1

    if temp == 3:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            arr.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            arr.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 3 and checkers_pos[xl][yl] != 1 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            arr.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 3 and checkers_pos[xr][yr] != 1 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            arr.insert(itr, DDR)
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            arr.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            arr.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 1 and checkers_pos[xul][
            yul] != 3 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            arr.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 1 and checkers_pos[xur][
            yur] != 3 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            arr.insert(itr, UUR)
            itr += 1
    if temp == 4:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            arr.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            arr.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 4 and checkers_pos[xl][yl] != 2 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            arr.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 4 and checkers_pos[xr][yr] != 2 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            arr.insert(itr, DDR)
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            arr.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            arr.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 4 and checkers_pos[xul][
            yul] != 2 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            arr.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 4 and checkers_pos[xur][
            yur] != 2 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            arr.insert(itr, UUR)
            itr += 1
    return arr


def check_valid_move(mosX, mosY):
    itr = 0
    temp = checkers_pos[mosX][mosY]

    DL = (mosX - 1, mosY + 1)
    DR = (mosX + 1, mosY + 1)
    UL = (mosX - 1, mosY - 1)
    UR = (mosX + 1, mosY - 1)
    DDL = (mosX - 2, mosY + 2)
    DDR = (mosX + 2, mosY + 2)
    UUL = (mosX - 2, mosY - 2)
    UUR = (mosX + 2, mosY - 2)

    if temp == 1:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            possibleMoves.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            possibleMoves.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 3 and checkers_pos[xl][yl] != 1 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            possibleMoves.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 3 and checkers_pos[xr][yr] != 1 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            possibleMoves.insert(itr, DDR)
            itr += 1
    if temp == 2:
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            possibleMoves.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            possibleMoves.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 4 and checkers_pos[xul][
            yul] != 2 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            possibleMoves.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 4 and checkers_pos[xur][
            yur] != 2 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            possibleMoves.insert(itr, UUR)
            itr += 1

    if temp == 3:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            possibleMoves.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            possibleMoves.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 3 and checkers_pos[xl][yl] != 1 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            possibleMoves.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 3 and checkers_pos[xr][yr] != 1 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            possibleMoves.insert(itr, DDR)
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            possibleMoves.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            possibleMoves.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 1 and checkers_pos[xul][
            yul] != 3 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            possibleMoves.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 1 and checkers_pos[xur][
            yur] != 3 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            possibleMoves.insert(itr, UUR)
            itr += 1
    if temp == 4:
        xl, yl = DL
        xr, yr = DR
        xll, yll = DDL
        xrr, yrr = DDR
        xul, yul = UL
        xur, yur = UR
        xull, yull = UUL
        xurr, yurr = UUR
        if xl > -1 and yl < 8 and checkers_pos[xl][yl] == 0:
            possibleMoves.insert(itr, DL)
            itr += 1
        if xr < 8 and yr < 8 and checkers_pos[xr][yr] == 0:
            possibleMoves.insert(itr, DR)
            itr += 1
        if xl > -1 and xll > -1 and yl < 8 and yll < 8 and checkers_pos[xl][yl] != 4 and checkers_pos[xl][yl] != 2 and \
                checkers_pos[xl][yl] != 0 and checkers_pos[xll][yll] == 0:
            possibleMoves.insert(itr, DDL)
            itr += 1
        if xr < 8 and xrr < 8 and yr < 8 and yrr < 8 and checkers_pos[xr][yr] != 4 and checkers_pos[xr][yr] != 2 and \
                checkers_pos[xr][yr] != 0 and checkers_pos[xrr][yrr] == 0:
            possibleMoves.insert(itr, DDR)
        if xul > -1 and yul > -1 and checkers_pos[xul][yul] == 0:
            possibleMoves.insert(itr, UL)
            itr += 1
        if xur < 8 and yur > -1 and checkers_pos[xur][yur] == 0:
            possibleMoves.insert(itr, UR)
            itr += 1
        if xul > -1 and yul > -1 and xull > -1 and yull > -1 and checkers_pos[xul][yul] != 4 and checkers_pos[xul][
            yul] != 2 and checkers_pos[xul][yul] != 0 and checkers_pos[xull][yull] == 0:
            possibleMoves.insert(itr, UUL)
            itr += 1
        if xur < 8 and yur > -1 and xurr < 8 and yurr > -1 and checkers_pos[xur][yur] != 4 and checkers_pos[xur][
            yur] != 2 and checkers_pos[xur][yur] != 0 and checkers_pos[xurr][yurr] == 0:
            possibleMoves.insert(itr, UUR)
            itr += 1


def check_extra_jump(xcord, ycord, type, count):
    jump = False
    xdl = xcord - 2
    ydl = ycord + 2
    xdr = xcord + 2
    ydr = ycord + 2
    xul = xcord - 2
    yul = ycord - 2
    xur = xcord + 2
    yur = ycord - 2
    if type == 1:
        if ((xcord - 1 > -1 and ycord + 1 < 8) and (checkers_pos[xcord - 1][ycord + 1] == 2 or checkers_pos[xcord - 1][ycord + 1] == 4)) and ((xdl > -1 and ydl < 8) and (checkers_pos[xdl][ydl] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord + 1] = 0
            checkers_pos[xdl][ydl] = type
            xcordnew = xul
            ycordnew = yul
            rectx = xcord - 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord + 1 < 8) and (checkers_pos[xcord + 1][ycord + 1] == 2 or checkers_pos[xcord + 1][ycord + 1] == 4)) and ((xdr < 8 and ydr < 8) and (checkers_pos[xdr][ydr] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord + 1] = 0
            checkers_pos[xdr][ydr] = type
            xcordnew = xdr
            ycordnew = ydr
            rectx = xcord + 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
    if type == 2:
        if ((xcord - 1 > -1 and ycord - 1 > -1) and (checkers_pos[xcord - 1][ycord - 1] == 1 or checkers_pos[xcord - 1][ycord - 1] == 3)) and ((xul > -1 and yul > -1) and (checkers_pos[xul][yul] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord - 1] = 0
            checkers_pos[xul][yul] = type
            xcordnew = xul
            ycordnew = yul
            rectx = xcord - 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord - 1 > -1) and (checkers_pos[xcord + 1][ycord - 1] == 1 or checkers_pos[xcord + 1][ycord - 1] == 3)) and ((xur < 8 and yur > -1) and (checkers_pos[xur][yur] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord - 1] = 0
            checkers_pos[xur][yur] = type
            xcordnew = xur
            ycordnew = yur
            rectx = xcord + 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True

    if type == 3:
        if ((xcord - 1 > -1 and ycord + 1 < 8) and (checkers_pos[xcord - 1][ycord + 1] == 2 or checkers_pos[xcord - 1][ycord + 1] == 4)) and ((xdl > -1 and ydl < 8) and (checkers_pos[xdl][ydl] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord + 1] = 0
            checkers_pos[xdl][ydl] = type
            xcordnew = xdl
            ycordnew = ydl
            rectx = xcord - 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord + 1 < 8) and (checkers_pos[xcord + 1][ycord + 1] == 2 or checkers_pos[xcord + 1][ycord + 1] == 4)) and ((xdr < 8 and ydr < 8) and (checkers_pos[xdr][ydr] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord + 1] = 0
            checkers_pos[xdr][ydr] = type
            xcordnew = xdr
            ycordnew = ydr
            rectx = xcord + 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord - 1 > -1 and ycord - 1 > -1) and (checkers_pos[xcord - 1][ycord - 1] == 2 or checkers_pos[xcord - 1][ycord - 1] == 4)) and ((xul > -1 and yul > -1) and (checkers_pos[xul][yul] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord - 1] = 0
            checkers_pos[xul][yul] = type
            xcordnew = xul
            ycordnew = yul
            rectx = xcord - 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord - 1 > -1) and (checkers_pos[xcord + 1][ycord - 1] == 2 or checkers_pos[xcord + 1][ycord - 1] == 4)) and ((xur < 8 and yur > -1) and (checkers_pos[xur][yur] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord - 1] = 0
            checkers_pos[xur][yur] = type
            xcordnew = xur
            ycordnew = yur
            rectx = xcord + 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True

    if type == 4:
        if ((xcord - 1 > -1 and ycord + 1 < 8) and (checkers_pos[xcord - 1][ycord + 1] == 1 or checkers_pos[xcord - 1][ycord + 1] == 3)) and ((xdl > -1 and ydl < 8) and (checkers_pos[xdl][ydl] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord + 1] = 0
            checkers_pos[xdl][ydl] = type
            xcordnew = xdl
            ycordnew = ydl
            rectx = xcord - 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord + 1 < 8) and (checkers_pos[xcord + 1][ycord + 1] == 1 or checkers_pos[xcord + 1][ycord + 1] == 3)) and ((xdr < 8 and ydr < 8) and (checkers_pos[xdr][ydr] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord + 1] = 0
            checkers_pos[xdr][ydr] = type
            xcordnew = xdr
            ycordnew = ydr
            rectx = xcord + 1
            recty = ycord + 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord - 1 > -1 and ycord - 1 > -1) and (checkers_pos[xcord - 1][ycord - 1] == 1 or checkers_pos[xcord - 1][ycord - 1] == 3)) and ((xul > -1 and yul > -1) and (checkers_pos[xul][yul] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord - 1][ycord - 1] = 0
            checkers_pos[xul][yul] = type
            xcordnew = xul
            ycordnew = yul
            rectx = xcord - 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True
        elif ((xcord + 1 < 8 and ycord - 1 > -1) and (checkers_pos[xcord + 1][ycord - 1] == 1 or checkers_pos[xcord + 1][ycord - 1] == 3)) and ((xur < 8 and yur > -1) and (checkers_pos[xur][yur] == 0)):
            checkers_pos[xcord][ycord] = 0
            checkers_pos[xcord + 1][ycord - 1] = 0
            checkers_pos[xur][yur] = type
            xcordnew = xur
            ycordnew = yur
            rectx = xcord + 1
            recty = ycord - 1
            pygame.draw.rect(screen, BLACK, [rectx * 80, recty * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = True

        pygame.display.update()
        if jump == False:
            count += 1
        if count == 4:
            return
        if jump == True:
            check_extra_jump(xcordnew, ycordnew, type, count)


def update_array(mos_1_X, mos_1_Y, mos_2_X, mos_2_Y):
    jump = 0
    checkertype = checkers_pos[mos_1_X][mos_1_Y]
    checkers_pos[mos_1_X][mos_1_Y] = 0
    drawx = mos_1_X * 80
    drawy = mos_1_Y * 80
    absolute = abs(mos_1_X - mos_2_X)
    if absolute > 1:
        if (mos_2_X < mos_1_X and mos_2_Y < mos_1_Y):
            tmpx = mos_1_X - 1
            tmpy = mos_1_Y - 1
            checkers_pos[tmpx][tmpy] = 0
            pygame.draw.rect(screen, BLACK, [tmpx * 80, tmpy * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = 1
        if (mos_2_X < mos_1_X and mos_2_Y > mos_1_Y):
            tmpx = mos_1_X - 1
            tmpy = mos_1_Y + 1
            checkers_pos[tmpx][tmpy] = 0
            pygame.draw.rect(screen, BLACK, [tmpx * 80, tmpy * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = 1
        if (mos_2_X > mos_1_X and mos_2_Y < mos_1_Y):
            tmpx = mos_1_X + 1
            tmpy = mos_1_Y - 1
            checkers_pos[tmpx][tmpy] = 0
            pygame.draw.rect(screen, BLACK, [tmpx * 80, tmpy * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = 1
        if (mos_2_X > mos_1_X and mos_2_Y > mos_1_Y):
            tmpx = mos_1_X + 1
            tmpy = mos_1_Y + 1
            checkers_pos[tmpx][tmpy] = 0
            pygame.draw.rect(screen, BLACK, [tmpx * 80, tmpy * 80, BLOCK_SIZE, BLOCK_SIZE])
            jump = 1

    pygame.draw.rect(screen, BLACK, [drawx, drawy, BLOCK_SIZE, BLOCK_SIZE])
    if checkertype == 1:
        checkers_pos[mos_2_X][mos_2_Y] = 1
    if checkertype == 2:
        checkers_pos[mos_2_X][mos_2_Y] = 2
    if checkertype == 3:
        checkers_pos[mos_2_X][mos_2_Y] = 3
    if checkertype == 4:
        checkers_pos[mos_2_X][mos_2_Y] = 4
    return jump


def draw_options(color, possible):
    length = len(possible)
    for i in range(length):
        tempx, tempy = possible[i]
        tempx = tempx * 80
        tempy = tempy * 80
        pygame.draw.rect(screen, color, [tempx, tempy, BLOCK_SIZE, BLOCK_SIZE])


def check_red_movement_loss():
    arr = []
    for i in range(8):
        for j in range(8):
            if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                check_possible(j, i, arr)
                if len(arr) != 0:
                    return False
    return True


def check_black_movement_loss():
    arr = []
    for i in range(8):
        for j in range(8):
            if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                check_possible(j, i, arr)
                if len(arr) != 0:
                    return False
    return True


def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()


def message(text):
    textType = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, textType)
    TextRect.center = (320, 320)
    screen.blit(TextSurf, TextRect)


def check_surrounding(x, y, weight):
    type = checkers_pos[x][y]

    if type == 1 or type == 3:
        # check left
        if x - 1 > -1 and y + 1 < 8:
            if checkers_pos[x - 1][y + 1] == 2 or checkers_pos[x - 1][y + 1] == 4:
                weight += 1
        if x - 1 > -1 and y - 1 > -1:
            if checkers_pos[x - 1][y - 1] == 4:
                weight += 1

        # check right
        if x + 1 < 8 and y + 1 < 8:
            if checkers_pos[x + 1][y + 1] == 2 or checkers_pos[x + 1][y + 1] == 4:
                weight += 1
        if x + 1 < 8 and y - 1 > -1:
            if checkers_pos[x + 1][y - 1] == 4:
                weight += 1
        return weight
    if type == 2 or type == 4:
        # check left
        if x - 1 > -1 and y - 1 > -1:
            if checkers_pos[x - 1][y - 1] == 1 or checkers_pos[x - 1][y - 1] == 3:
                weight += 1
        if x - 1 > -1 and y + 1 < 8:
            if checkers_pos[x - 1][y + 1] == 3:
                weight += 1

        # check right
        if x + 1 < 8 and y - 1 > -1:
            if checkers_pos[x + 1][y - 1] == 1 or checkers_pos[x + 1][y - 1] == 3:
                weight += 1
        if x + 1 < 8 and y + 1 < 8:
            if checkers_pos[x + 1][y + 1] == 3:
                weight += 1
        return weight


def red_artificial_player(color):
    count = 0
    arr = []
    redmoveslist = []
    for i in range(8):
        for j in range(8):
            arr = []
            if color == "RED" and turn % 2 != 0 and (checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3):
                check_possible(j, i, arr)
                for b in range(len(arr)):
                    weight = 0
                    weight = check_surrounding(j, i, weight)
                    if len(arr) > 0:
                        tmpx, tmpy = arr[b]
                        if abs(j - tmpx) > 1:
                            weight -= 4
                        if weight == 0:
                            weight = random.randint(0,3)
                        movepossibility = (j, i, tmpx, tmpy, weight)
                        redmoveslist.insert(count, movepossibility)
    endmove = sorted(redmoveslist, key=lambda q: q[4])
    posx, posy, movex, movey, tmpweight = endmove[0]
    thetype = checkers_pos[posx][posy]
    madejump = update_array(posx, posy, movex, movey)
    if madejump == 1:
        check_extra_jump(movex, movey, thetype, 0)
        madejump = 0
    draw_checkers()
    pygame.display.update()
    redmoveslist.clear()
    arr.clear()

def artificial_player(color):
    count = 0
    arr = []
    moveslist = []
    for i in range(8):
        for j in range(8):
            arr = []
            if color == "BLACK" and turn % 2 == 0 and checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                check_possible(j, i, arr)
                for b in range(len(arr)):
                    weight = 0
                    weight = check_surrounding(j, i, weight)
                    if len(arr) > 0:
                        tmpx,tmpy = arr[b]
                        if abs(j-tmpx) > 1:
                            weight-=4
                        if weight == 0:
                            weight = random.randint(0,3)
                        movepossibility = (j, i, tmpx, tmpy, weight)
                        moveslist.insert(count, movepossibility)
    endmove = sorted(moveslist, key = lambda q: q[4])
    posx,posy,movex,movey,tmpweight = endmove[0]
    thetype = checkers_pos[posx][posy]
    madejump = update_array(posx, posy, movex, movey)
    if madejump == 1:
        check_extra_jump(movex, movey, thetype, 0)
        madejump = 0
    draw_checkers()
    pygame.display.update()
    moveslist.clear()
    arr.clear()


win = tk.Tk()

win.title("Checkers")
win.geometry("700x700")
win.resizable(False, False)

# Frames-----------------------------------------------------------------------------

TitleFrame = tk.Frame(win)
TitleFrame.pack()

OptionsFrame = tk.Frame(win)
OptionsFrame.pack(pady=100)

PlayerOptionsFrame = tk.LabelFrame(OptionsFrame, text="Player Options", padx=50)
PlayerOptionsFrame.pack(anchor=tk.W, padx=10, side=tk.LEFT)

TimeOptionsFrame = tk.LabelFrame(OptionsFrame, text="Time Options", padx=50)
TimeOptionsFrame.pack(anchor=tk.CENTER, padx=50, side=tk.LEFT)

DebugOptionsFrame = tk.LabelFrame(OptionsFrame, text="Debug Options", padx=50)
DebugOptionsFrame.pack(anchor=tk.E, padx=10, side=tk.LEFT)

StartButtonFrame = tk.Frame(win)
StartButtonFrame.pack()
# ------------------------------------------------------------------------------------

# Labels-----------------------------------------------------------------------------
tk.Label(TitleFrame, text="Checkers", font=50).pack()
# ------------------------------------------------------------------------------------

# RadioButton Options---------------------------------------------------------------------

p = tk.IntVar()
t = tk.IntVar()
d = tk.IntVar()

#default settings
p.set(1)
t.set(900)
d.set(1)

tk.Radiobutton(PlayerOptionsFrame, text="2 Players", variable=p, value=1).pack(anchor=tk.W)
tk.Radiobutton(PlayerOptionsFrame, text="1 Player, 1 AI", variable=p, value=2).pack(anchor=tk.W)
tk.Radiobutton(PlayerOptionsFrame, text="2 AIs", variable=p, value=3).pack(anchor=tk.W)

tk.Radiobutton(TimeOptionsFrame, text="15 minutes", variable=t, value=900).pack(anchor=tk.W)
tk.Radiobutton(TimeOptionsFrame, text="20 minutes", variable=t, value=1200).pack(anchor=tk.W)
tk.Radiobutton(TimeOptionsFrame, text="30 minutes", variable=t, value=1800).pack(anchor=tk.W)

tk.Radiobutton(DebugOptionsFrame, text="Yes", variable=d, value=1).pack(anchor=tk.W)
tk.Radiobutton(DebugOptionsFrame, text="No", variable=d, value=2).pack(anchor=tk.W)

#-------------------------------------------------------------------------------------------


# Start Button-----------------------------------------
def startclicked():
    win.destroy()

startbutton = tk.Button(StartButtonFrame, text="Start Game", command=startclicked).pack()

# -----------------------------------------------------

win.mainloop()


made_jump = 0
game_over = False
turn = 1
draw_board()
pygame.display.set_caption("CHECKERS")
while not game_over:
    if time.time() - start > t.get():
        break
    draw_checkers()
    pygame.display.update()
    if p.get() == 3:
        time.sleep(.3)
        if turn % 2 != 0:
            if d.get() == 1:
                for i in range(8):
                    print(checkers_pos[i])
                print("Turn number: ", turn)
                print("\n")
            red_artificial_player("RED")
            pygame.display.update()
            turn += 1
            for i in range(8):
                if checkers_pos[i][0] == 2:
                    checkers_pos[i][0] = 4

                if checkers_pos[i][7] == 1:
                    checkers_pos[i][7] = 3
            redcount = 0
            blackcount = 0
            for i in range(8):
                for j in range(8):
                    if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                        redcount += 1
                    if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                        blackcount += 1
            if redcount == 0:
                message("BLACK WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if blackcount == 0:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_red_movement_loss() == True:
                message("BLACK WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_black_movement_loss() == True:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
        elif turn % 2 == 0:
            if d.get() == 1:
                for i in range(8):
                    print(checkers_pos[i])
                print("Turn number: ", turn)
                print("\n")
            artificial_player("BLACK")
            turn += 1
            for i in range(8):
                if checkers_pos[i][0] == 2:
                    checkers_pos[i][0] = 4

                if checkers_pos[i][7] == 1:
                    checkers_pos[i][7] = 3
            redcount = 0
            blackcount = 0
            for i in range(8):
                for j in range(8):
                    if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                        redcount += 1
                    if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                        blackcount += 1
            if redcount == 0:
                message("BLACK WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if blackcount == 0:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_red_movement_loss() == True:
                message("BLACK WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_black_movement_loss() == True:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and p.get() == 1:
            possibleMoves = []

            x, y = pygame.mouse.get_pos()
            x = int(math.floor(x / 80))
            y = int(math.floor(y / 80))
            check_type = checkers_pos[x][y]

            if turn % 2 != 0 and (check_type == 1 or check_type == 3):
                check_valid_move(x, y)
                draw_options(BLUE, possibleMoves)
                event_happened = False
                pygame.display.update()
                if len(possibleMoves) == 0:
                    break
            elif turn % 2 == 0 and (check_type == 2 or check_type == 4):
                check_valid_move(x, y)
                draw_options(BLUE, possibleMoves)
                event_happened = False
                pygame.display.update()
                if len(possibleMoves) == 0:
                    break
            else:
                event = pygame.event.wait()
                break
            loop = True
            while loop == True:
                event = pygame.event.wait()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    xmove, ymove = pygame.mouse.get_pos()
                    x2 = math.floor(xmove/80)
                    y2 = math.floor(ymove/80)
                    combined = (x2, y2)
                    length = len(possibleMoves)
                    for l in range(length):
                        if turn % 2 != 0 and combined == possibleMoves[l]:
                            draw_options(BLACK, possibleMoves)
                            pygame.display.update()
                            loop = False
                            made_jump = update_array(x, y, x2, y2)
                            if made_jump == 1:
                                check_extra_jump(x2, y2, check_type, 0)
                                made_jump = 0
                            continue
                        elif turn % 2 == 0 and combined == possibleMoves[l]:
                            draw_options(BLACK, possibleMoves)
                            pygame.display.update()
                            loop = False
                            made_jump = update_array(x, y, x2, y2)
                            if made_jump == 1:
                                check_extra_jump(x2, y2, check_type, 0)
                                made_jump = 0
                            continue
            turn += 1
            for i in range(8):
                if checkers_pos[i][0] == 2:
                    checkers_pos[i][0] = 4

                if checkers_pos[i][7] == 1:
                    checkers_pos[i][7] = 3
            redcount = 0
            blackcount = 0
            for i in range(8):
                for j in range(8):
                    if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                        redcount += 1
                    if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                        blackcount += 1
            if redcount == 0:
                message("BLACK WINS")
                pygame.display.update()

                time.sleep(5)
                sys.exit()
            if blackcount == 0:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_red_movement_loss() == True:
                message("BLACK WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if check_black_movement_loss() == True:
                message("RED WINS")
                pygame.display.update()
                time.sleep(5)
                sys.exit()
            if d.get() == 1:
                for i in range(8):
                    print(checkers_pos[i])
                print("Turn number: ", turn)
                print("\n")
            break


        elif p.get() == 2:
            if turn % 2 != 0:
                Toploop = True
                while Toploop == True:
                    event = pygame.event.wait()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        possibleMoves = []

                        x, y = pygame.mouse.get_pos()
                        x = int(math.floor(x / 80))
                        y = int(math.floor(y / 80))
                        check_type = checkers_pos[x][y]

                        if turn % 2 != 0 and (check_type == 1 or check_type == 3):
                            check_valid_move(x, y)
                            draw_options(BLUE, possibleMoves)
                            event_happened = False
                            pygame.display.update()
                            Toploop = False
                            if len(possibleMoves) == 0:
                                break
                        else:
                            event = pygame.event.wait()
                            for i in range(8):
                                if checkers_pos[i][0] == 2:
                                    checkers_pos[i][0] = 4

                                if checkers_pos[i][7] == 1:
                                    checkers_pos[i][7] = 3
                            redcount = 0
                            blackcount = 0
                            for i in range(8):
                                for j in range(8):
                                    if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                                        redcount += 1
                                    if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                                        blackcount += 1
                            if redcount == 0:
                                message("BLACK WINS")
                                pygame.display.update()
                                time.sleep(5)
                                sys.exit()
                            if blackcount == 0:
                                message("RED WINS")
                                pygame.display.update()
                                time.sleep(5)
                                sys.exit()
                            if check_red_movement_loss() == True:
                                message("BLACK WINS")
                                pygame.display.update()
                                time.sleep(5)
                            if check_black_movement_loss() == True:
                                message("RED WINS")
                                pygame.display.update()
                                time.sleep(5)
                                sys.exit()
                            break
                        loop = True
                        while loop == True:
                            event = pygame.event.wait()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                xmove, ymove = pygame.mouse.get_pos()
                                x2 = math.floor(xmove/80)
                                y2 = math.floor(ymove/80)
                                combined = (x2, y2)
                                length = len(possibleMoves)
                                for l in range(length):
                                    if turn % 2 != 0 and combined == possibleMoves[l]:
                                        draw_options(BLACK, possibleMoves)
                                        pygame.display.update()
                                        loop = False
                                        made_jump = update_array(x, y, x2, y2)
                                        if made_jump == 1:
                                            check_extra_jump(x2, y2, check_type, 0)
                                            made_jump = 0
                                        continue

                        turn += 1
                        for i in range(8):
                            if checkers_pos[i][0] == 2:
                                checkers_pos[i][0] = 4

                            if checkers_pos[i][7] == 1:
                                checkers_pos[i][7] = 3
                        redcount = 0
                        blackcount = 0
                        for i in range(8):
                            for j in range(8):
                                if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                                    redcount += 1
                                if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                                    blackcount += 1
                        if redcount == 0:
                            message("BLACK WINS")
                            pygame.display.update()
                            time.sleep(5)
                            sys.exit()
                        if blackcount == 0:
                            message("RED WINS")
                            pygame.display.update()
                            time.sleep(5)
                            sys.exit()
                        if check_red_movement_loss() == True:
                            message("BLACK WINS")
                            pygame.display.update()
                            time.sleep(5)
                            sys.exit()
                        if check_black_movement_loss() == True:
                            message("RED WINS")
                            pygame.display.update()
                            time.sleep(5)
                            sys.exit()
                        if d.get() == 1:
                            for i in range(8):
                                print(checkers_pos[i])
                            print("Turn number: ", turn)
                            print("\n")
            elif turn % 2 == 0:
                artificial_player("BLACK")
                turn += 1
                for i in range(8):
                    if checkers_pos[i][0] == 2:
                        checkers_pos[i][0] = 4

                    if checkers_pos[i][7] == 1:
                        checkers_pos[i][7] = 3
                redcount = 0
                blackcount = 0
                for i in range(8):
                    for j in range(8):
                        if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
                            redcount += 1
                        if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
                            blackcount += 1
                if redcount == 0:
                    message("BLACK WINS")
                    time.sleep(5)
                    pygame.display.update()
                    sys.exit()
                if blackcount == 0:
                    message("RED WINS")
                    pygame.display.update()
                    time.sleep(5)
                    sys.exit()
                if check_red_movement_loss() == True:
                    message("BLACK WINS")
                    pygame.display.update()
                    time.sleep(5)
                    sys.exit()
                if check_black_movement_loss() == True:
                    message("RED WINS")
                    pygame.display.update()
                    time.sleep(5)
                    sys.exit()
                if d.get() == 1:
                    for i in range(8):
                        print(checkers_pos[i])
                    print("Turn number: ", turn)
                    print("\n")
    pygame.display.update()

for i in range(8):
    for j in range(8):
        if checkers_pos[j][i] == 1 or checkers_pos[j][i] == 3:
            redcount += 1
        if checkers_pos[j][i] == 2 or checkers_pos[j][i] == 4:
            blackcount += 1
if redcount > blackcount:
    message("RED WINS")
elif blackcount > redcount:
    message("BLACK WINS")
else:
    message("TIE")
pygame.display.update()
time.sleep(5)
sys.exit()

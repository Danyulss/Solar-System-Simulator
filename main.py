import pygame as pg
from OpenGL.GL import *

class sim:

    def __init__(self):
        pg.init()
        pg.display.set_mode((1280, 720), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)
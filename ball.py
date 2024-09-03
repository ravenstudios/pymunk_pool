import pygame
from constants import *
import random
import pymunk

class Ball:
    def __init__(self, x, y, color, space, static_body):
        self.x = x
        self.y = y
        self.radius = 16

        self.body = pymunk.Body(10, 1, pymunk.Body.DYNAMIC)
        self.body.position = (x, y)

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.mass = 5
        self.shape.elasticity = 0.8

        self.center = (int(self.body.position.x), int(self.body.position.y))
        self.color = color
        print(f'self.body:{self.shape}')

        # Friction
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 100

        space.add(self.body, self.shape, self.pivot)


    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.body.position += (-2, 0)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.body.position += (2, 0)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.body.position += (0, -2)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.body.position += (0, 2)



    def draw(self, surface):
        self.center = (int(self.body.position.x - self.radius), int(self.body.position.y - self.radius))
        pygame.draw.circle(surface, self.color, self.center, self.radius, width=0)

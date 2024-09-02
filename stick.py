import pygame
from constants import *
import random
import pymunk
import math

class Stick:
    def __init__(self, x, y, color, space, static_body, cue_ball):
        self.color = color

        # Stick properties
        self.length = 200
        self.width = 5
        self.mass = 10

        # Create the stick body and shape
        self.body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, (self.width, self.length)))
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.length))
        self.shape.friction = 0.9

        # Add the body and shape to the space
        space.add(self.body, self.shape)

        # Store a reference to the cue ball
        self.cue_ball = cue_ball

        self.fixed_distance = 200



    def update(self, cue_ball_position):
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the direction vector from the cue ball to the mouse position
        direction = pygame.Vector2(mouse_pos) - pygame.Vector2(self.cue_ball.body.position)

        # Normalize the direction and scale it by the fixed distance
        direction = direction.normalize() * self.fixed_distance

        # Calculate the angle between the stick and the cue ball
        angle = math.atan2(direction.y, direction.x)

        # Set the stick's angle to point toward the mouse
        self.body.angle = angle + math.pi / 2

        # Position the stick's body so that the front of the stick is at the fixed distance
        # from the cue ball. The stick is positioned so that its front is at the fixed distance,
        # and the rest of the stick extends behind the cue ball.
        self.body.position = self.cue_ball.body.position + direction



    def draw(self, surface):
        # x = int(self.body.position.x) - (self.width // 2)
        # y = int(self.body.position.y) - (self.length // 2)

        stick_start_pos = stick_body.position
        stick_end_pos = stick_body.position + pymunk.Vec2d(stick_length, 0).rotated(stick_body.angle)


        pygame.draw.rect(surface, self.color, (stick_start_pos.x , stick_start_pos.y, stick_end_pos.x, stick_end_pos.y), width=0)

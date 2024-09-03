from constants import *
import pymunk
import pymunk.pygame_util
import pygame

import ball
import solid
import wall
import stick

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
clock = pygame.time.Clock()


space = pymunk.Space()
# space.gravity = (0, 981)  # Example for Earth-like gravity, adjust as needed

static_body = space.static_body

options = pymunk.pygame_util.DrawOptions(surface)


cue_ball = ball.Ball(GAME_WIDTH // 2, GAME_HEIGHT // 2, WHITE, space, static_body)
stick = stick.Stick(320, 400, BROWN, space, static_body, cue_ball)

wall1 = wall.Wall((0, 0, GAME_WIDTH, 40), GREEN, space)
wall2 = wall.Wall((GAME_WIDTH - 40, 0, 40, GAME_HEIGHT), GREEN, space)
wall3 = wall.Wall((0, GAME_HEIGHT - 40, GAME_WIDTH, 40), GREEN, space)
wall4 = wall.Wall((0, 0, 40, GAME_HEIGHT), GREEN, space)

def main():
    running = True
    global stick
    while running:

        clock.tick(TICK_RATE)
        space.step(1 / TICK_RATE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    pendulum.reset()
                if event.key == pygame.K_q:
                    running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # stick.body.apply_impulse_at_local_point((0, -2000), (0, 0))
            stick.hit_ball()


        draw()
        update(events)
        pygame.display.update()

    pygame.quit()




def draw():
    surface.fill((75, 75, 75))#background

    # pendulum.draw(surface)
    space.debug_draw(options)
    # pygame.display.update()



def update(events):
    cue_ball.update()
    stick.update(cue_ball.body.position)



if __name__ == "__main__":
    main()

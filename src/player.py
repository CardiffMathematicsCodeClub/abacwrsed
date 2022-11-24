import math
import numpy as np
import pygame

SQUARE_ROOT_OF_TWO = math.sqrt(2)

class Player(pygame.sprite.Sprite):
    def __init__(self, startx, starty, group, boxes):
        super().__init__(group)

        self.stand_image = pygame.image.load("Graphics/players/p1_front.png").convert_alpha()
        self.cry_image = pygame.image.load("Graphics/players/p1_front_cry.png").convert_alpha()
        self.jump_image = pygame.image.load("Graphics/players/p1_jump.png").convert_alpha()
        self.walk_cycle = [
            pygame.image.load(f"Graphics/players/p1_walk{i:0>2}.png") for i in range(1, 12)
        ]
        
        self.image = self.stand_image
        self.rect = self.image.get_rect(center=(startx, starty))

        self.boxes = boxes

        self.animation_index = 0
        self.facing_left = False

        self.speed = 8
        self.jumpspeed = 20
        self.vsp = 0
        self.gravity = 0
        self.min_jumpspeed = 4
        self.prev_key = pygame.key.get_pressed()

    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle) - 1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        """
        TODO Document this method.
        """
        hsp = 0
        vsp = 0
        onground = self.check_collision(0, 1, grounds=self.boxes)
        # check keys
        keys = pygame.key.get_pressed()

        hsp = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * self.speed
        vsp = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * self.speed

        # MOVEMENT ANIMATION DISABLED FOR SIMPLIFIED TESTING [1]

        # if hsp < 0:
        #    self.facing_left = True
        #    self.walk_animation()

        # else:
        #    self.facing_left = False
        #    self.walk_animation()

        # END OF DISABLE [1]

        if hsp * vsp != 0:
            hsp /= SQUARE_ROOT_OF_TWO
            vsp /= SQUARE_ROOT_OF_TWO
        if hsp == vsp == 0:
            self.image = self.image

        # TODO This is a relic, should be removed if we do not use jumping.
        if self.prev_key[pygame.K_UP] and not keys[pygame.K_UP]:
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed

        self.prev_key = keys

        # movement
        self.move(hsp, vsp)

    def move(self, x, y):
        dx = x
        dy = y

        while self.check_collision(0, dy, self.boxes):
            dy -= np.sign(dy)

        while self.check_collision(dx, dy, self.boxes):
            dx -= np.sign(dx)

        self.rect.move_ip([dx, dy])

    def check_collision(self, x, y, grounds):
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, grounds)
        if collide:
            collide.event(player=self)

        self.rect.move_ip([-x, -y])
        return collide

import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty, group):
        super().__init__(group)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(startx, starty))

    def update(self):
        pass

    def event(self, **kwargs):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Wall_H(Sprite):
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_H.png", startx, starty, group)


class Wall_V(Sprite):
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_V.png", startx, starty, group)


class Wall_H_JD(Sprite):
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_H_JD.png", startx, starty, group)


class Wall_VE_JU(Sprite):
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_VE_JU.png", startx, starty, group)


class Barrier(Sprite):
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/Barrier.png", startx, starty, group)


class SadBarrier(Barrier):
    def event(self, player):
        player.image = player.cry_image


class HappyBarrier(Barrier):
    def event(self, player):
        player.image = player.stand_image

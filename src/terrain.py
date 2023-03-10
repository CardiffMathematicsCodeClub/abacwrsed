import pygame

import inventory

class Sprite(pygame.sprite.Sprite):
    """
    Generic Sprite class to be inherited by other sprites classes.
    """

    def __init__(self, image, startx, starty, group):
        super().__init__(group)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(startx, starty))

    def event(self, **kwargs):
        """
        This method is called when an event is triggered.
        """
        pass

    def draw(self, screen):
        """
        Draw the sprite on the screen.
        """
        screen.blit(self.image, self.rect)


class Wall_H(Sprite):
    """
    Horizontal wall sprite.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_H.png", startx, starty, group)


class Wall_V(Sprite):
    """
    Vertical wall sprite.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_V.png", startx, starty, group)


class Wall_H_JD(Sprite):
    """
    Horizontal wall sprite with a down junction.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_H_JD.png", startx, starty, group)


class Wall_VE_JU(Sprite):
    """
    Vertical wall sprite that is the end of the wall.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/TempWall_VE_JU.png", startx, starty, group)


class Barrier(Sprite):
    """
    Barrier sprite.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/Barrier.png", startx, starty, group)


class SadBarrier(Barrier):
    """
    Sad barrier sprite. This barrier makes the player cry.
    """
    def event(self, player):
        player.image = player.cry_image


class HappyBarrier(Barrier):
    """
    Happy barrier sprite. This barrier stops the player from crying.
    """
    def event(self, player):
        player.image = player.stand_image


class Collectible(Sprite):
    """
    Collectible sprite.
    """
    def __init__(self, startx, starty, group):
        super().__init__("Graphics/terrain/boxAlt.png", startx, starty, group)
        self.item = inventory.Box()

    def event(self, player):
        player.bag.put(self.item)
        self.kill()


class SecondBox(Collectible):
    def __init__(self, startx, starty, group):
        super().__init__(startx, starty, group)
        self.item = inventory.SecondBox()

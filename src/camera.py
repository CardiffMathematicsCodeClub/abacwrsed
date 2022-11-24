import pygame


class CameraGroup(pygame.sprite.Group):
    """
    The CameraGroup class is a subclass of pygame.sprite.Group that
    automatically adjusts the position of all sprites in the group
    based on the position of the player. In other words, it works in
    such a way that when the player "moves", the player doesn't really
    move. Instead everything else moves around the player to give the
    illusion of the player navigating the environment, while also keeping
    the player at the center of the screen.
    """

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2

        # Box setup
        # These are the parameters that define the box that the player can move
        # around in when using the box_center_camera method.
        self.camera_borders = {"left": 600, "right": 600, "top": 350, "bottom": 350}
        left = self.camera_borders["left"]
        top = self.camera_borders["top"]
        width = self.display_surface.get_size()[0] - (
            self.camera_borders["left"] + self.camera_borders["right"]
        )
        height = self.display_surface.get_size()[1] - (
            self.camera_borders["top"] + self.camera_borders["bottom"]
        )
        self.camera_rect = pygame.Rect(left, top, width, height)

        # Keyboard camera speed
        self.keyboard_camera_speed = 8

    def center_target_camera(self, target):
        """
        Readjusts the offset parameter base on the target's location.
        This camera option will keep the target at the center of the
        screen.
        """
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def box_target_camera(self, target):
        """
        Readjusts the offset parameter base on the target's location.
        This camera option will keep the target within a "camera box"
        that is centered on the screen.
        """
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders["left"]
        self.offset.y = self.camera_rect.top - self.camera_borders["top"]

    def keyboard_control_camera(self, target):
        """
        Readjusts the offset parameter based on the keyboard input.
        This camera option will allow the user to move the camera
        around the screen using WASD.
        """
        if target.prev_key[pygame.K_a]:
            self.camera_rect.x -= self.keyboard_camera_speed
        if target.prev_key[pygame.K_d]:
            self.camera_rect.x += self.keyboard_camera_speed
        if target.prev_key[pygame.K_w]:
            self.camera_rect.y -= self.keyboard_camera_speed
        if target.prev_key[pygame.K_s]:
            self.camera_rect.y += self.keyboard_camera_speed

        self.offset.x = self.camera_rect.left - self.camera_borders["left"]
        self.offset.y = self.camera_rect.top - self.camera_borders["top"]

    def custom_draw(self, player):
        """
        Draws all sprites in the group, but first adjusts the position
        of each sprite based on the offset parameter.
        """
        # Use the camera where the player is exactly in the middle of the screen
        self.center_target_camera(player)

        # Use the box camera where the player is in the middle of the screen
        self.box_target_camera(player)

        # Use the keyboard camera where the player can move the camera with WASD
        self.keyboard_control_camera(player)

        # active elements
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

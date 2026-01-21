import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

class Swingcopter(pygame.sprite.Sprite):
    def __init__(self):
        """The player"""
        super().__init__()

        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect()

        self.acceleration = 0.5

        self.vel_y = 0

    def switchgravity(self):
        self.acceleration = self.acceleration * -1

    def update(self):
        keys_pressed = pygame.key.get_pressed()

        # calculate the grav
        self.vel_y += self.acceleration
        # move the swingcopter
        self.rect.y += self.vel_y
        # max speed
        if self.vel_y >= 7.5:
            self.vel_y = 7.5

        if self.vel_y <= -7.5:
            self.vel_y = -7.5

        print(self.vel_y, self.acceleration, self.rect.y)

class Spikewall(pygame.sprite.Sprite):
    def __init__(self):
        """The Spikewall"""
        super().__init__()

        # create the spike wall

        self.image = pygame.Surface((5, 600))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

class Visiblemusicline(pygame.sprite.Sprite):
    def __init__(self):
        """visible music line"""
        super().__init__()

        self.image = pygame.Surface((1000, 2))
        self.rect = self.image.get_rect()

class Musicline(pygame.sprite.Sprite):
    def __init__(self):
        """music line hitbox"""
        super().__init__()

        self.image = pygame.Surface((1000, 75))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()


def game():
    pygame.init()


    # CONSTANTS
    WIDTH = 1000
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Game borders


    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Your Title Here")

    # Variables
    done = False
    clock = pygame.time.Clock()


    all_sprites_group = pygame.sprite.Group()
    spike_wall_group = pygame.sprite.Group()
    music_line_group = pygame.sprite.Group()
    swingcopter = Swingcopter()
    swingcopter.rect.centery = HEIGHT / 2
    swingcopter.rect.centerx = (WIDTH / 2) - 125
    spikewall = Spikewall()
    spikewall.rect.centery = HEIGHT / 2
    spikewall.rect.centerx = (WIDTH - 50)
    vmusicline = Visiblemusicline()
    vmusicline.rect.centery = HEIGHT / 2
    vmusicline.rect.centerx = WIDTH / 2
    musicline = Musicline()
    musicline.rect.centery = HEIGHT / 2
    musicline.rect.centerx = WIDTH / 2
    all_sprites_group.add(musicline)
    all_sprites_group.add(vmusicline)
    all_sprites_group.add(spikewall)
    all_sprites_group.add(swingcopter)
    spike_wall_group.add(spikewall)
    music_line_group.add(musicline)
    music_line_group.add(vmusicline)



    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    swingcopter.switchgravity()

        # ------ GAME LOGIC
        all_sprites_group.update()

        # TODO: if swingcopter top is less than or equal to 10
        # keep top at 10
        if swingcopter.rect.centery <= 10:
            swingcopter.rect.centery = 10
        # TODO: if swingcopter bottom is greater than or equal to HEIGHT - 10
        if swingcopter.rect.bottom >= HEIGHT:
            swingcopter.rect.bottom = HEIGHT

        # game over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # collision

        wall_collided = pygame.sprite.spritecollide(swingcopter, spike_wall_group, False)

        # if player collides with spikewall, game = over
        if wall_collided:
            done = True

        # make the spikewall move away and towards the player

        line_collided = pygame.sprite.spritecollide(swingcopter, music_line_group, False)

        if line_collided:
            spikewall.rect.centerx = spikewall.rect.centerx + 1

        else:
            spikewall.rect.centerx = spikewall.rect.centerx - 2

        # cap the spikewall to a certain distance

        if spikewall.rect.centerx >= 950:
            spikewall.rect.centerx = 950
        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()

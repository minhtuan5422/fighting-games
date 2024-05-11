import pygame
from fighter import Fighter

pygame.init()

# Create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting games")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250 
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]


# Load background image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

# Load sprite sheet
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

# Define number of step in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3 , 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3 , 7]

# Function for drawing background
def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))

# Function for drawing fighter health bars
def draw_health_bars(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Create two instances of fighters
fighter_1 = Fighter(200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310, True,  WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)

# Game loop 
run = True
while run:
    
    clock.tick(FPS)
    
    # Draw background
    draw_bg()
    
    # Show player stats
    draw_health_bars(fighter_1.health, 20, 20)
    draw_health_bars(fighter_2.health, 580, 20)
    
    # Move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    ''' fighter_2.move() '''
    
    # Draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
        
    
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # Update display
    pygame.display.update()
            
# Exit pygame
pygame.quit()
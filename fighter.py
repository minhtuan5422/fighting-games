import pygame

class Fighter():
    def __init__(self, x, y, flip,  data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        
    def load_images(self, sprite_sheet, animation_steps):
        # Extract images from sprite sheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for j in range(animation):
                temp_img = sprite_sheet.subsurface(j * self.size, 0, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        print(animation_list)
        return animation_list
    
    
    def move(self, screen_width, screen_height, surface, target):
        SPEED  = 10 
        GRAVITY = 2
        dx = 0
        dy = 0
        
        # Get key presses
        key = pygame.key.get_pressed()
        
        # Can only perform other actions if not currently attacking 
        if self.attacking == False:
            # Movement 
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            # Jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            # Attack
            if key[pygame.K_j] or key[pygame.K_k]:
                self.attack(surface, target)
                if key[pygame.K_j]:
                    self.attack_type = 1
                else:
                    self.attack_type = 2
            
        #Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y   
            
        # Ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0 
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom
            
        # Ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True
            
        # Update player position
        self.rect.x += dx
        self.rect.y += dy
        
    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
        
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
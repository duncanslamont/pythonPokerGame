import pygame
import os

# Initialize Pygame and its sound mixer
pygame.init()
pygame.mixer.init()

# Set up display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Gun Click Game")

# Load gun image
gun_image = pygame.image.load("resources/gun.png")
# Scale the image if needed (adjust numbers as needed for your image)
gun_image = pygame.transform.scale(gun_image, (200, 200))
gun_rect = gun_image.get_rect()

# Center the gun on screen
gun_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Load sound (you can use any sound file - .wav works best with Pygame)
try:
    gun_sound = pygame.mixer.Sound("resources/gunshot.wav")
except:
    # If no sound file, we'll use a simple beep
    gun_sound = pygame.mixer.Sound.play(pygame.mixer.Sound(pygame.mixer.Sound.tone(440, 100)))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if click was on the gun
            if gun_rect.collidepoint(event.pos):
                gun_sound.play()

    # Fill screen with white
    screen.fill((255, 255, 255))
    
    # Draw the gun
    screen.blit(gun_image, gun_rect)
    
    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()

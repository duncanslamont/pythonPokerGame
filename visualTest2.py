import pygame
import math
from deck import *
import random 


# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600)) 

card_font = pygame.font.Font(None, 12)

deck = getNewDeck()
hand_pos = [[300,500],[500,500]]
# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Text Animation Examples")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font setup
font_size = 48
font = pygame.font.Font(None, font_size)

# Animation variables
time = 0
running = True
clock = pygame.time.Clock()

def draw_wave_text(text, y_pos, amplitude=20, frequency=0.1):
    """Draw text where each letter waves independently"""
    x_pos = WIDTH/2 - (len(text) * font_size/4)
    for i, letter in enumerate(text):
        letter_surface = font.render(letter, True, WHITE)
        offset = math.sin(time * frequency * 5 + i * 0.5) * amplitude
        pos = (x_pos + i * font_size/2, y_pos + offset)
        screen.blit(letter_surface, pos)

def draw_card(text, x_pos, y_pos, frequency=2):
    """Draw text on a white card background"""
    card_width = 100  # Adjust size as needed
    card_height = 150
    card_surface = pygame.Surface((card_width, card_height))
    card_surface.fill(WHITE)
    text_surface = card_font.render(text, True, BLACK)  # Changed text to black for contrast
    text_rect = text_surface.get_rect(center=(card_width/2, card_height/2))
    # Draw text onto the card surface
    card_surface.blit(text_surface, text_rect)
    # Create a rect for the final card position on screen
    card_rect = card_surface.get_rect(center=(x_pos, y_pos))
    
    # Draw the complete card onto the screen
    screen.blit(card_surface, card_rect)

# Main game loop

selected_card_one = random.choice(deck)
selected_card_two = random.choice(deck)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw different text animations
    draw_wave_text("Crazy Casino!", 250)
    draw_card(selected_card_one,hand_pos[0][0],hand_pos[0][1])
    draw_card(selected_card_two,hand_pos[1][0],hand_pos[1][1])
    
    # Update display
    pygame.display.flip()
    
    # Update time and control frame rate
    time += 0.05
    clock.tick(60)

pygame.quit()

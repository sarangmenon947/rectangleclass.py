import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill("green")
pygame.display.update()

class Rectangle():
    def __init__(self, colour, dimensions):
        self.screen = screen
        self.colour = colour
        self.dimensions = dimensions

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.dimensions)

# Create rectangle objects once before the loop
red_rectangle = Rectangle("red", (50, 20, 150, 70))
blue_rectangle = Rectangle("blue", (200, 100, 150, 70))
orange_rectangle = Rectangle("orange", (400, 200, 150, 70))
pink_rectangle = Rectangle("pink", (300, 300, 150, 70))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()  # Properly exit the program

    # Draw the rectangles
    red_rectangle.draw()
    blue_rectangle.draw()
    orange_rectangle.draw()
    pink_rectangle.draw()

    pygame.display.update()
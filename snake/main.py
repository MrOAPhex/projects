import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 704))
clock = pygame.time.Clock()
running = True
lng = 2
eaten = False
ax, ay = 10*32, 5*32 
apple = pygame.image.load("apple.png").convert_alpha()
apple = pygame.transform.scale(apple, (32, 32))
snake = [{"type": "cell", "loc": (5, 8), "point": (5, 9)}, {"type": "head", "loc": (5, 4), "point": (5, 5)}, {"type": "cell", "loc": (5, 7), "point": (5, 8)}, {"type": "cell", "loc": (5, 6), "point": (5, 7)}, {"type": "cell", "loc": (5, 5), "point": (5, 6)}]

moving = "right"

def movement(movin, loc):

    if movin == "up":
        new_loc = (loc[0], loc[1]-1) 
    if movin == "down":
        new_loc = (loc[0], loc[1]+1) 
    if movin == "left":
        new_loc = (loc[0]-1, loc[1]) 
    if movin == "right":
        new_loc = (loc[0]+1, loc[1]) 
    return new_loc, loc

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    
    # perus näppäin setup

    old_movin = moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moving = "up"
    if keys[pygame.K_s]:
        moving = "down"
    if keys[pygame.K_a]:
        moving = "left"
    if keys[pygame.K_d]:
        moving = "right"
    if old_movin == "up" and moving == "down" or old_movin == "down" and moving == "up" or old_movin == "left" and moving == "right" or old_movin == "right" and moving == "left":
        moving = old_movin
        print("moving block")

    for cell_eaten in snake:
        if cell_eaten["loc"] == (ax/32, ay/32):
            ax, ay = random.randint(0, 32)*32, random.randint(0, 21)*32
            lng = 1
    screen.blit(apple, (ax, ay))

    # tuff shit main for-looppi
    for cell in snake:
        # uusi pää
        if cell["type"] == "head":
            cell["type"] = "cell"
            print(f"lisätään {cell["loc"]}")
            nh_loc, nh_poi = movement(moving, cell["loc"]) 
            snake.append({"type": "head", "loc": nh_loc, "point": nh_poi})          
            if nh_loc[1] > 21 or nh_loc[1] < 0 or  nh_loc[0] > 39 or nh_loc[0] < 0:
                running = False
            break

    for collision in snake:
        if collision["loc"] == nh_loc and collision["type"] == "cell":
            print(nh_loc, collision["loc"], collision["type"])
            running = False

    for dl_tail in snake:
        # räjäytä häntä
        if dl_tail["type"] == "cell":
            pointing_to = dl_tail["point"]
            pointing_bool = False
            for x in range(0, len(snake)):
                old_cell = snake[x]
                if pointing_to == old_cell["loc"] and old_cell["type"] == "cell":
                    # poista celli jos ei osu
                    pointing_bool = True
            if pointing_bool == False and lng <= 0:
                print(f"poistetaan {dl_tail["loc"]}")
                snake.remove(dl_tail)
                break
                
    lng -= 1
    # printataa se ny
    for printattava in snake:
        cords = printattava["loc"]
        xykoko = (cords[0]*32, cords[1]*32, 32, 32)
        pygame.draw.rect(screen, (255, 255, 255), (xykoko))

    pygame.display.flip()

    clock.tick(8)
pygame.quit()


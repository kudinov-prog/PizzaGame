from livewires import games
import time
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = - self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = - self.dy

class Pan(games.Sprite):
    """ Сковорода """
    def update(self):
        """ Перемещение в позицию курсора"""
        self.x = games.mouse.x
        self.y = games.mouse.y


def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image("pizza.bmp")
    the_pizza = Pizza(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx =2,
                         dy =2)
    games.screen.add(the_pizza)

    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.event_grab = False

    
    games.screen.mainloop()
main()
"""won_message = games.Message(value = "Victory!", 
                            size = 100, 
                            color = color.red, 
                            x = games.screen.width/2, 
                            y = games.screen.height/2, 
                            lifetime = 250, 
                            after_death = games.screen.quit)
games.screen.add(won_message)"""

"""pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
games.screen.add(pizza)

the_pizza = games.Sprite(image = pizza_image,
                         x = games.screen.width/2,
                         y = games.screen.height/2,
                         dx =1,
                         dy =1)
games.screen.add(the_pizza)"""

"""score = games.Text(value = 1756521, size = 60, color = color.black, x = 550, y = 30)
games.screen.add(score)
"""

"""class New():
    def create_pizza():
        pizza_image = games.load_image("pizza.bmp")
        the_pizza = Pizza(image = pizza_image,
                            x = random.randint(50, 450),
                            y = random.randint(50, 600),
                            dx =2,
                            dy =2)
        games.screen.add(the_pizza)"""

"""for piz in range(5):
        New.create_pizza()"""
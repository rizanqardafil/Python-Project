import random
import math
import arcade

Width = 800
Height = 600
Title = "SnowFall"

class snow_fall:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_snow(self):
        self.y = random.randrange(Height, Height + 100)
        self.x = random.randrange(Width)

class snowfall(arcade.Window):
    def  __init__(self, width, height, title):
        super().__init__(width, height, title)

    def start_snowfall(self):
        self.snowfall_list =  [ ]

        for i in range(50):
            snowfall = snow_fall()
            snowfall.x = random.randrange(Width)
            snowfall.y = random.randrange(Height + 200)

            snowfall.size = random.randrange(8)
            snowfall.speed = random.randrange(20, 40)
            snowfall.angle = random.uniform(math.pi, math.pi * 2)

            self.snowfall_list.append(snowfall)

arcade.set_backround_color(arcade.color.BLUE)

def on_draw(self):
    arcade.start_render()
    for snowfall in self.snowfall_list:
        arcade.draw_circle_filled(snowfall.x, snowfall.y, 
                                                    snowfall.size, arcade.color.WHITE)

    def on_update(self, delta_time):
        for snowfall in self.snowfall_list:
            snowfall.y -= snowfall.speed * delta_time

            if snowfall.y < 0:
                snowfall.reset_snow()
            
            snowfall.x += snowfall.speed * \
                math.cos(snowfall.angle) * delta_time
            snowfall.angle += 1 * delta_time

screen = snowfall(800, 600, "Snow")
screen.start_snowfall()
arcade.run()
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise


class Block(Button):

    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            orgin_y=0.5,
            texture="white_cube",
            color=color.green,
            highlight_color=color.white,
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                block = Block(position=self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)


app = Ursina()
scale = 24
noise = PerlinNoise(octaves=3, seed=2023)

for z in range(30):
    for x in range(30):
        block = Block(position=(x, 0, z))
        block.y = floor(noise([x / scale, z / scale]) * 8)

scene.fog_color = color.white
scene.fog_density = 0.04


def input(key):
    if key == "q" or key == "escape":
        quit()
        application.quit()


player = FirstPersonController()

app.run()

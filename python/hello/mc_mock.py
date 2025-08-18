from ursina import *

app = Ursina()

class test_cube(Entity):
    def __init__(self,):
        super().__init__(
            model='cube',
            texture='a.png',
            color=color.white,
            rotation = Vec3(45,45,45)
        )

class Jason_button(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='brick',
            color=color.white,
            highlight_color=color.red,
            pressed_color=color.orange,
        )


def update():
    if held_keys['a']:
        test.x = test.x - 1*time.dt

test = Entity(model='cube',color=color.orange, scale=1, position=(5,0))
test2 = Text(text='codinghou',scale=2)
# test3 = Entity(model='cube',texture='a.png')
test4 = test_cube()
test5 = Jason_button()

app.run()


























app.run()
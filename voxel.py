from ursina import *


class Voxel(Button):
    def __init__(self, player, position=(0, 0, 0), texture=None):
        super().__init__(
            parent=scene, model='model/grass.obj',
            scale=0.5, texture=texture, position=position,
            origin_y=0.0015, color=color.color(0, 0, random.uniform(0.9, 1))
        )
        self.player = player

    def input(self, key):
        shift_clicks = 0
        if self.hovered:
            if key == 'right mouse down':
                pass

            if key == 'left mouse down':
                destroy(self)

            if key == 'space':
                self.player.gravity = -0.02

                self.gravity = 0.5
            if key == 'escape':  # кнопка выхода из игры
                quit()

            if key == 'shift':  # кнопка быстрого бега

                self.player.speed +=  3  # увеличиваем скорость при нажатии
                shift_clicks += 1

            if key == 'control':
                self.player.speed -= 3
                shift_clicks -= 1

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

grass_texture = load_texture('textures/Grass_Block_TEX.png')


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene, model='model/grass.obj',
            scale=0.5, texture=texture, position=position,
            origin_y=0.0015, color=color.color(0, 0, random.uniform(0.9, 1))
        )

    def input(self, key):
        shift_clicks = 0
        if self.hovered:
            if key == 'right mouse down':
                pass

            if key == 'left mouse down':
                destroy(self)

            if key == 'space':
                player.gravity = -0.02

                player.gravity = 0.5
            if key == 'escape':  # кнопка выхода из игры
                quit()

            if key == 'shift':  # кнопка быстрого бега

                player.speed = normal_speed + 3  # увеличиваем скорость при нажатии
                shift_clicks += 1

            if key == 'control':
                player.speed = normal_speed - 3
                shift_clicks -= 1


# генерация платформы из блоков Voxel
for x_dynamic in range(60):
    for z_dynamic in range(60):
        Voxel(position=(x_dynamic, 0, z_dynamic))

hand = Entity(parent=camera.ui, model='model/hand.obj',
              rotation=Vec3(150, -10, 0), position=Vec2(0.6, -0.6))

sky = Entity(
    model='sphere', texture=load_texture('textures/skybox.jpg'),
    scale=1000, double_sided=True
)
player = FirstPersonController()
normal_speed = player.speed = 5

player.gravity = 0.0
app.run()

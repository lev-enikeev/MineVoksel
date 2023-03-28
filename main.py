from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from inventory import Inventory
from voxel import Voxel

app = Ursina()

inventory = None

def input(key):
    global inventory
    if key == 'e':
        if not inventory:
            inventory = Inventory()

        player.enabled = False


    if key == 'r':
        destroy(inventory)
        player.enabled = True


player = FirstPersonController()
player.speed = 5

player.gravity = 0.0
grass_texture = load_texture('textures/Grass_Block_TEX.png')
# генерация платформы из блоков Voxel
for x_dynamic in range(60):
    for z_dynamic in range(60):
        Voxel(player, position=(x_dynamic, 0, z_dynamic), texture=grass_texture)

hand = Entity(parent=camera.ui, model='model/hand.obj',
              rotation=Vec3(150, -10, 0), position=Vec2(0.6, -0.6))


sky = Entity(
    model='sphere', texture=load_texture('textures/skybox.jpg'),
    scale=1000, double_sided=True
)

app.run()

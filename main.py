from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from inventory.inventory import Inventory
from inventory.quick_menu import QuickInventory
from voxel import Voxel
app = Ursina()

inventory = None
quickInventory = None
quickInventory = QuickInventory()


def input(key):
    global inventory
    if key == 'e':
        if not inventory:
            inventory = Inventory()

        player.enabled = False
    if key == 'left mouse down':
        hand.rotation_x = 160
        hand.frame = 5

    if key == 'r':
        destroy(inventory)
        player.enabled = True


def update():
    if hand.frame > 0:
        hand.frame -= 1
    if hand.frame == 0 and hand.rotation_x != 150:
        hand.rotation_x = 150


player = FirstPersonController()
player.speed = 5

player.gravity = 0.0
grass_texture = load_texture('textures/Grass_Block_TEX.png')
# генерация платформы из блоков Voxel
for x_dynamic in range(60):
    for z_dynamic in range(60):
        Voxel(player, position=(x_dynamic, 0, z_dynamic), texture=grass_texture)

hand = Entity(parent=camera.ui, model='model/hand_000',
              rotation=Vec3(150, -10, 0), position=Vec2(0.6, -0.6))
hand.frame = 0

sky = Entity(
    model='sphere', texture=load_texture('textures/skybox.jpg'),
    scale=1000, double_sided=True
)

app.run()

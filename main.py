from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from inventory import Inventory
from quick_menu import QuickInventory
from voxel import Voxel
import time
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
        hand.model ="model\hand_005"


    if key == 'r':
        destroy(inventory)
        player.enabled = True


def update():
    print(hand.model)
    if "hand_005.obj" in hand.model:
        print("tut")
        hand.model ="model\hand_000"

player = FirstPersonController()
player.speed = 5

player.gravity = 0.0
grass_texture = load_texture('textures/Grass_Block_TEX.png')
# генерация платформы из блоков Voxel
for x_dynamic in range(60):
    for z_dynamic in range(60):
        Voxel(player, position=(x_dynamic, 0, z_dynamic), texture=grass_texture)

hand = Entity(parent=camera.ui, model='model/hand_000.obj',
              rotation=Vec3(150, -10, 0), position=Vec2(0.6, -0.6))


sky = Entity(
    model='sphere', texture=load_texture('textures/skybox.jpg'),
    scale=1000, double_sided=True
)

app.run()

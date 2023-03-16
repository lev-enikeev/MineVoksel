from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 
import time
from ursina.shaders import lit_with_shadows_shader 

app = Ursina() 


grass_texture = load_texture('textures/Grass_Block_TEX.png')


class Voxel(Button):
   def __init__(self, position=(0, 0, 0), texture=grass_texture):
       super().__init__(
           parent=scene, model='Grass_Block.obj', 
           scale=0.5, texture=texture, position=position,
           origin_y=0.0015, color = color.color(0,0,random.uniform(0.9,1))
       )
       
   
   #  добавляем input — встроенную функцию взаимодействия с блоком Voxel:
   #     		если нажали на ПКМ — появится блок
   #     		если нажали на ЛКМ — удалится 
   def input(self, key):
       shift_clicks = 0
       if self.hovered:
           if key == 'right mouse down':
               Voxel(position=self.position + mouse.normal, texture="textures/Grass_Block_TEX.png")
           if key == '1':
               Voxel(position=self.position + mouse.normal, texture="textures/dub.png")
           if key == '2':
               Voxel(position=self.position + mouse.normal, texture="textures/brick.png")
           if key == '3':
               Voxel(position=self.position + mouse.normal, texture="textures/stone.png")
           if key == '4':
               Voxel(position=self.position + mouse.normal, texture="textures/oak.png")
           if key == '5':
               Voxel(position=self.position + mouse.normal, texture="textures/leaves.png")
           if key == '6':
               Voxel(position=self.position + mouse.normal, texture="textures/bedrock.png")
           if key == '7':
               Voxel(position=self.position + mouse.normal, texture="textures/cobblestone.png")
           if key == '8':
               Voxel(position=self.position + mouse.normal, texture="textures/testob.jpg")

           if key == 'left mouse down':
               destroy(self)

           if key == 'space':
               player.gravity = -0.02

               player.gravity = 0.5
           if key == 'escape': # кнопка выхода из игры
               quit()

           if key == 'shift': # кнопка быстрого бега

                player.speed = normal_speed + 3 # увеличиваем скорость при нажатии
                shift_clicks += 1

           if key== 'control':
                player.speed = normal_speed - 3
                shift_clicks -= 1



# генерация платформы из блоков Voxel
for x_dynamic in range(60):
   for z_dynamic in range(60):
       Voxel(position=(x_dynamic,0,z_dynamic))
hand = Entity(parent = camera.ui, model = 'handsa.obj',
             
             rotation = Vec3(150, -10,0), position = Vec2(0.6,-0.6))

sky_texture = load_texture('textures/skybox.jpg')

sky = Entity(
           model = 'sphere', texture = sky_texture,
           scale = 1000, double_sided = True
       )
player = FirstPersonController() 
normal_speed = player.speed = 5



player.gravity = 0.0
app.run()
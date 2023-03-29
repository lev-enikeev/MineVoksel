from ursina import *


class InventoryCell(Button):
    def __init__(self, x, y, cell_type=None, **kwargs):
        super().__init__(self,
                         scale=(.09, .095),
                         x=-.5,
                         color=color.gray.tint(0.10),
                         tooltip=Tooltip('Empty'),
                         origin=(-.5, .5),
                         position=(x, y),
                         z=-.1,
                         **kwargs)
        self.texture_scale_items = (15, 15)
        self.icon_drag = None

    def on_click(self):
        if self.icon_drag:
            return
        if self.parent.on:
            self.texture = 'textures/icons/brick.png'
            self.tooltip.text = 'brick'
            self.parent.on = False
            
            self.icon_drag = self.parent.icon_drag
            destroy(self.parent.icon_drag)
            return
        if self.texture:

            self.parent.icon_drag = Entity(
                parent=self.parent,
                model='quad',
                texture='textures/icons/brick',
                color=color.white,
                scale=self.scale,
                origin=(-.5, .5),
                position=(self.position[0]+0.01, self.position[1]+0.01),
                z=-.5,
            )
            print(self.parent.icon_drag.texture)
            self.texture = None
            self.tooltip.text = 'Empty' 
            self.parent.on = True


class QuickInventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.01),
            texture='textures/inventorylow.png',
            #texture_scale = (5,8),
            texture_scale_items=(15, 15),
            scale=(.8, .13),
            origin=(-.4, .5),
            position=(-.3, -.37),
        )
        self.on = False
        self.icon_drag = None
        for key, value in kwargs.items():
            setattr(self, key, value)

        startX = -0.058
        koefX = 0.1046
        koefY = 0.1104
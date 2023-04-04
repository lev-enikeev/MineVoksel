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
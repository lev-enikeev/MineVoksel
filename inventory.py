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
            return
        self.parent.icon_drag = Entity(
            parent=self.parent,
            texture=self.texture,
            color=color.white,
            scale=self.scale,
            origin=(-.5, .5),
            position=(self.position[0]+0.01, self.position[1]+0.01),
            z=-.5,
        )
        self.texture = None
        self.parent.on = True


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.01),
            texture='textures/inventory',
            #texture_scale = (5,8),
            texture_scale_items=(15, 15),
            scale=(.8, .8),
            origin=(-.4, .5),
            position=(-.3, .4),
        )
        self.on = False
        self.icon_drag = None
        for key, value in kwargs.items():
            setattr(self, key, value)

        startX = -0.058
        koefX = 0.1046
        koefY = 0.1104
        InventoryCell(startX, -0.045, parent=self)
        InventoryCell(startX, -0.045-koefY, parent=self)
        InventoryCell(startX, -0.045-2*koefY, parent=self)
        InventoryCell(startX, -0.045-3*koefY, parent=self)
        for i in range(2):
            for j in range(2):
                InventoryCell(startX+4.45*koefX+i*koefX, -
                              0.045-koefY-j*koefY, parent=self)
        InventoryCell(startX+7.55*koefX, -0.053-1.47*koefY, parent=self)
        for i in range(9):
            for j in range(3):
                if i == 0 and j == 0:
                    cell = InventoryCell(
                        startX+i*koefX, -0.508-j*koefY, parent=self)
                    cell.texture = 'textures/icons/brick.png'
                    cell.tooltip.text = 'brick'
                    continue
                InventoryCell(startX+i*koefX, -0.508-j*koefY, parent=self)
        self.quick_cells = []
        for i in range(9):
            for j in range(1):
                InventoryCell(startX+i*koefX, -0.865-j*koefY, parent=self)

    def update(self):
        if self.icon_drag:
            self.icon_drag.x = mouse.x*14 + 4
            self.icon_drag.y = mouse.y*14 + 0.4
            self.icon_drag.texture = 'textures/icons/brick.png'

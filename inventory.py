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

        for key, value in kwargs.items():
            setattr(self, key, value)

        startX = -0.058
        koefX = 0.1046
        koefY = 0.1104
        self.helmet = InventoryCell(startX, -0.045, parent=self)

        def on_click():
            self.helmet.texture = 'textures/icons/brick'
        self.helmet.on_click = on_click
        self.armor = InventoryCell(startX, -0.045-koefY, parent=self)
        self.pants = InventoryCell(startX, -0.045-2*koefY, parent=self)
        self.boots = InventoryCell(startX, -0.045-3*koefY, parent=self)
        self.craft = []
        for i in range(2):
            for j in range(2):
                self.craft.append(
                    InventoryCell(startX+4.45*koefX+i*koefX, -0.045-koefY-j*koefY, parent=self))
        self.craft_end = InventoryCell(
            startX+7.55*koefX, -0.053-1.47*koefY, parent=self)
        self.inventory_cells = []
        for i in range(9):
            for j in range(3):
                self.inventory_cells.append(
                    InventoryCell(startX+i*koefX, -0.508-j*koefY, parent=self))
        self.quick_cells = []
        for i in range(9):
            for j in range(1):
                self.quick_cells.append(
                    InventoryCell(startX+i*koefX, -0.865-j*koefY, parent=self))

    def find_free_spot(self):
        for y in range(8):
            for x in range(5):
                grid_positions = [(int(e.x*self.texture_scale_items[0]),
                                   int(e.y*self.texture_scale_items[1])) for e in self.children]
                print(grid_positions)

                if not (x, -y) in grid_positions:
                    print('found free spot:', x, y)
                    return x, y

    def append(self, item, x=0, y=0):
        print('add item:', item)

        if len(self.children) >= 5*8:
            print('inventory full')
            error_message = Text('<red>Inventory is full!',
                                 origin=(0, -1.5), x=-.5, scale=2)
            destroy(error_message, delay=1)
            return

        x, y = self.find_free_spot()

        icon = Draggable(
            parent=self,
            model='quad',
            # texture=item,
            color=color.white,
            scale_x=1/self.texture_scale_items[0],
            scale_y=1/self.texture_scale_items[1],
            origin=(-.5, .5),
            x=x * 1/self.texture_scale_items[0],
            y=-y * 1/self.texture_scale_items[1],
            z=-.5,
        )

        name = item.replace('_', ' ').title()

        if random.random() < .25:
            icon.color = color.gold
            name = '<orange>Rare ' + name

        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0, 0, 0, .8)

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # ensure the dragged item overlaps the rest

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * 5) / 5
            icon.y = int((icon.y - (icon.scale_y/2)) * 8) / 8
            icon.z += .01

            # if outside, return to original position
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            # if the spot is taken, swap positions
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    print('swap positions')
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop

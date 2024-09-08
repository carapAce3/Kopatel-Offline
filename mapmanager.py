



class Mapmanager():
    def __init__(self):
        self.model = 'skull.obj' # завантажуємо модель
        self.texture = 'skull.jpg'
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.color = (80, 202, 63, 0.9) # rgba
        self.start_new()
        self.add_block((0,10,0))
    def start_new(self):
        self.map = render.attachNewNode('Map')


    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.map)




        # self.block.setScale(0.5, 0.5, 0.5) # змінюємо розмір блоку
        # self.block.reparentTo(render) # додаємо блок до екрана
        # self.block.setPos(0, 0, 0) # змінюємо позицію блоку
        # self.block.setHpr(0, 0, 0) # змінюємо головину блоку
        # self.block.setCollideMask(BitMask32.allOn()) # додаємо блок до маски колізій
        # self.block.setPythonTag('type', 'block') # додаємо тег для визначення виду об'єкта
        # self.block.setPythonTag('model', self.model) # додаємо тег для визначення моделі
        # self.block.setPythonTag('texture', self.texture) # додаємо тег для визначення текстури
        # self.block.setPythonTag('scale', str(self.block.getScale())) # додаємо тег для визначення розміру
        # self.block.setPythonTag('position', str(self.block.getPos())) # додаємо тег для визначення позиці��
        # self.block.setPythonTag('rotation', str(self.block.getHpr())) # додаємо тег для визначення головини


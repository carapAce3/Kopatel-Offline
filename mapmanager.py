



class Mapmanager():
    def __init__(self):
        self.model = 'block.egg' # завантажуємо модель
        self.texture = 'bedrock.png'
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.color = [(80, 202, 63, 0.9),
                      (50, 34, 53, 1),
                      (3, 6, 90, 0.6),
                      (62, 55, 34, 0.4)] # rgba
        self.start_new()
        #self.add_block((0,10,0))
    def start_new(self):
        self.map = render.attachNewNode('Map')

    def getColor(self,z):
        if z < len(self.color):
            return self.color[z]
        else:
            return self.color[len(self.color)-1]


    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.c = self.getColor(int(position[2]))  # отримуємо колір залежно від z-координати
        self.block.setColor(self.c)
        self.block.reparentTo(self.map)
    def loadMap(self):
        self.map.removeNode()
        self.start_new()
        with open('land.txt', 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for l in line:
                    for z0 in range(int(l)+1):
                        block = self.add_block((x,y,z0))
                    x += 1
                y += 1
        return x,y





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


key_forward = 'w'
key_backward = 's'
key_left = 'a'
key_right = 'd'

key_switch = 'c'

key_move_left = 'left'
key_move_right = 'right'



class Hero:
    def __init__(self, position, map):
        self.map = map
        self.hero = loader.loadModel('smiley')
        self.hero.setScale(0.3) # встановлення масштабу гравця
        self.hero.setPos(position) # встановлення позиції
        self.hero.reparentTo(render) # додавання героя до "сцени"
        self.functions()

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    
    def move_to(self, angle):
        self.move(angle)
    
    def move(self, angle):
        pos = self.moving(angle)
        self.hero.setPos(pos)
    def moving(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.check_moving(angle)
        new_x = x + dx
        new_y = y + dy
        return new_x, new_y, z
    
    def check_moving(self, angle):
        if angle >=0 and angle <=20:
            return(0, -1)
        elif angle <=65:
            return(1, -1)
        elif angle <=110:
            return(1, 0)
        elif angle <=155:
            return(1, 1)
        elif angle <=200:
            return(0, 1)
        elif angle <=245:
            return(-1, 1)
        elif angle <=290:
            return(-1, 0)
        elif angle <=335:
            return(-1, -1)
        else:
            return(0, -1)


    def functions(self):
        base.accept(key_forward, self.forward)
        base.accept(key_forward + "-repeat" ,self.forward)
        base.accept(key_backward, self.backward)
        base.accept(key_backward + "-repeat" ,self.backward)
        base.accept(key_left, self.left)
        base.accept(key_left + "-repeat" ,self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + "-repeat", self.right)



    



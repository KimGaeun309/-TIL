# 2. Product Class에 Singleton Pattern을 적용한 후 결과를 확인하시오.
# 3. 2번의 결과에 대해 왜 그러한 결과가 나오는지 논하시오.

# Singleton Pattern을 적용하면 단 한 개의 객체만을 생성하기 때문에 MessageBox를 "*" 로 생성한 후 다시 "#" 로 
# 생성하고자 한다면 객체를 새로 생성하지 않고 기존에 생성되었던 MessageBox("*") 가 반환됩니다.
# 그래서 msg2.use(word)를 했을 때 "#" 로 덮인 메시지가 출력되지 않고 "*"로 덮인 메시지가 출력됩니다.


from abc import *
import copy

class MyProduct(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyProduct, cls).__call__(*args, **kwds)
        else:
            print("instance already created: ", cls._instances[cls])
        return cls._instances[cls]

class Product(metaclass = MyProduct):
    @abstractmethod
    def use(self):
        pass
    @abstractmethod
    def clone(self):
        pass

class UnderlinePen(Product):
    def use(self, s:str):

        n = len(s)
        print(s)
        for i in range(n):
            print("~", end="")
        print()

    def clone(self):
        return copy.deepcopy(self)

class MessageBox(Product):
    def __init__(self, deco:str):
        self.deco = deco

    def use(self, s:str):
        n = len(s) + 4

        for i in range(n):
            print(self.deco, end="")
        print()
        print(self.deco, s, self.deco)
        for i in range(n):
            print(self.deco, end="")
        print()

    def clone(self):
        return copy.deepcopy(self)

class Manager:

    def __init__(self):
        self.showcase = {"a":1}

    def register(self, name:str, proto:Product):
        self.showcase[name] = proto
    
    def create(self, protoName):
        p = self.showcase[protoName]
        return p.clone()

manager = Manager()

m1 = MessageBox("*")
m2 = MessageBox("#")
p1 = UnderlinePen()

manager.register("msg*", m1)
manager.register("msg#", m2)
manager.register("pen", p1)
msg1 = manager.create("msg*")
msg2 = manager.create("msg#")
pen = manager.create("pen")

word = "hello"
msg1.use(word)
word = "world"
msg2.use(word)
pen.use(word)

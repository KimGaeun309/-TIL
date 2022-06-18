# 0. 아래의 두 가지 내용에 대해 레포트 및 작성된 코드를 제출하시오. 
# 레포트 양식은 따로 없으나, 이름, 학번, 학과, 느낀 점이 포함되어야합니다. 
# 그리고, 코드를 서로 절대 공유하지말고 스스로 작성하길 바랍니다. 
# 가령 유사한 코드가 있을 경우 추 후에라도 발견되면 양쪽 모두 상당한 패널티가 발생할 수 있습니다.

# 1. 강의에서 마지막 Example 코드를 타이핑하여 결과를 확인하시오.

from abc import *
import copy

class Product(metaclass = ABCMeta):

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

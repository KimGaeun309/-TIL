# 0) 제공된 game1.py 코드를 분석하고 주석을 달아보세요.

# Bridge Pattern 활용. 
# 캐릭터를 게임에 태운다.
# Actor는 Implementor이고 Hero와 Enemy는 Actor를 상속받는 Concrete Implementors이다.
# GameFramework는 Abstraction이고 WhiteGame과 BlackGame은 GameFramework를 상속받는 Refined Abstractions이다.

# Concrete Implementor가 2개, Refined Abstraction이 2개 있으므로 총 4가지 조합이 만들어질 수 있다.

import pygame
import MyVector as mv #지난 번에 구현했던 vector 클래스

#컬러 설정할때 편하라고 정의해 놓은 딕셔너리. 
rgb = { 
    'BLACK':(0, 0, 0), 
    'WHITE':(255, 255, 255),
    'BLUE':(0, 0, 255),
    'GREEN':(0, 255, 0),
    'RED':(255, 0, 0)
}

#Implementor
class Actor:

    def __init__(self, x, y):
        self.pos = mv.MyVector(x, y)
        self.name = ""
        self.skill = ""

    # Position 지정하는 메소드
    def setPos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    # delta 만큼 Position을 이동하는 메소드
    def move(self, delta):
        self.pos = self.pos + delta
    
    # 캐릭터의 이름을 지정하는 메소드
    def setName(self, name):
        self.name = name
    
    # 캐릭터의 스킬을 지정하는 메소드. Concrete Implementor에서 구현
    def setSkill(self, skill):
        pass


#Concrete Implementor 1
class Hero(Actor):
    def setSkill(self, skill):
        self.skill = skill

#Concrete Implementor 2
class Enermy(Actor):

    def setSkill(self, skill):
        self.skill = skill



#Abstraction 
class GameFramework: 
    
    def __init__(self):
        self.pygame = pygame
        self.screen = 0

        self.nY = 0 #화면 차원
        self.nX = 0

        self.hero = 0 # 지금은 주인공이 1명있다고 가정

        print("init")

    # 배경 setting
    def setDisplay(self, nX, nY): #게임화면의 크기를 결정
        self.nY = nY
        self.nX = nX
        self.screen = self.pygame.display.set_mode([self.nX, self.nY])
        self.pygame.display.set_caption("Prince") #게임창의 이름

    #Bridge Pattern에서 Implementor를 속성으로 가질 수 있도록 하는 부분
    #Abstraction과 Implementor가 연결되는 부분
    def setHero(self, hero:Actor): # 위임을 받는 형태로 연결.
        self.hero = hero

    def ready(self):
        self.pygame.init() #pygame 초기화


    def drawPolygon(self, color, points, thickness):
        self.pygame.draw.polygon(self.screen, color, points, thickness)

    
    def drawEdges(self):
        p1 = mv.MyVector(0, 0)
        p2 = mv.MyVector(0, 10)
        p3 = mv.MyVector(10, 0)
        
        self.drawPolygon(rgb["WHITE"], [p1.vec(), p2.vec(), p3.vec()], 1)
    

    # 게임 창에 msg를 pos에 맞는 위치에 color에 맞는 색으로 출력해주는 함수.
    def printText(self, msg, color, pos):
        font= self.pygame.font.SysFont("consolas",20)
        textSurface     = font.render(msg,True, color, None) #self.pygame.Color(color)
        textRect        = textSurface.get_rect()
        textRect.topleft= pos
        self.screen.blit(textSurface, textRect)

    #게임 실행. Refined Abstraction 에서 구현
    def launch(self):
        pass


# Refined Abstraction 1
class WhiteGame(GameFramework): 

    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: # done이 True가 되면 탈출
            clock.tick(60) #set on 30 frames per second

            for event in self.pygame.event.get():
                # QUIT event가 들어와 종료해야 한다면 done을 True로 만들기
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN: # 키를 눌렀을때
                    print("key down")
                    # 각 키에 맞게 delta 값 증가 or 감소시키기
                    if event.key == self.pygame.K_LEFT: # 왼쪽 방향키
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT: # 오른쪽 방향키
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN: # 아래쪽 방향키
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP: # 위쪽 방향키
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP: # 키를 뗐을 때
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta) #주인공의 위치가 업데이트가 됨

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["WHITE"]) #특성을 살린 부분. 배경 색이 흰 색
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()


# Refined Abstraction 2
class BlackGame(GameFramework): 

    # WhilteGame의 launch(self) 와 같은 부분이 대부분인데, screen을 채우는 배경 색만 다르다.
    def launch(self):
        print("launch")
        clock = self.pygame.time.Clock()

        delta = mv.MyVector(0, 0)

        keyFlag = None

        done = False
        while not done: 
            clock.tick(30) #set on 30 frames per second

            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    done = True

                elif event.type == self.pygame.KEYDOWN:
                    print("key up")
                    if event.key == self.pygame.K_LEFT:
                        print("K_LEFT")
                        delta.x = -5
                    elif event.key == self.pygame.K_RIGHT:
                        print("K_RIGHT")
                        delta.x = 5
                    elif event.key == self.pygame.K_DOWN:
                        print("K_DOWN")
                        delta.y = 5
                    elif event.key == self.pygame.K_UP:
                        print("K_UP")
                        delta.y = -5

                    keyFlag = True

                elif event.type == self.pygame.KEYUP:
                    delta.setPos(0, 0)
                    print("key up")
                    keyFlag = False


            if keyFlag == True:

                self.hero.move(delta)

                print("pressed", self.hero.pos.getState()) #in console
                self.screen.fill(rgb["BLACK"]) #특성화된 부분, 배경 색이 검은 색
                self.printText(self.hero.name, rgb["RED"], self.hero.pos.vec()) 
                self.printText(self.hero.skill, rgb["GREEN"], (self.hero.pos + mv.MyVector(0, 15)).vec())

            self.pygame.display.flip()

        self.pygame.quit()



game = WhiteGame() # Refined Abstraction 중 하나를 만들었다. WhiteGame()을 만들면 screen이 흰 색으로 채워진다.
game.ready() # game.ready()를 하면 game.pygame.init() 이 실행되어 pygame이 초기화된다.
game.setDisplay(500, 300) # setDiplay() 를 하여 가로폭이 500, 세로폭이 300인 배경 창을 띄우도록 한다.

hero = Hero(0, 0) # Concrete Implements 중 하나를 만들었다. Hero(0, 0)을 만들면 처음 위치가 (0, 0)인 Hero를 만들어준다.
hero.setName("prince") # setName()으로 이름을 지정해준다.
hero.setSkill("swing a sword") # setSkill()로 스킬을 지정해준다.

monster = Enermy(50, 50) # Enermy(50, 50)을 만들면 처음 위치가 (50, 50)인 Enermy를 만들어준다.
monster.setName("weak moster") # setName()으로 이름을 지정해준다.
monster.setSkill("hit the body") # setSkill()으로 스킬을 지정해준다.

game.setHero(hero) # game에 setHero()로 hero를 game의 인자로 가지도록 (위임) 해주면 hero를 game에 태운 것과 같아진다.
                    # 이 때 Abstraction과 Implement가 연결된다. 

game.launch() # launch() 를 하면 while loop을 돌면서 사용자가 종료하기 전까지 사용자로부터 키보드 입력을 받는다.
                # 그리고 입력받은 만큼 위임받은 캐릭터의 위치를 이동시켜 화면에 나타내준다.

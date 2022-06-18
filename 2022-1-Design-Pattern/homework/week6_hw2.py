# 2) 게임의 초기화부터 실행까지 한번에 실행해주는 Facade Pattern을 추가하시오. (클래스명 등 이름은 자유롭게 설정가능)


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


class PlayBHGame:

    def __init__(self):
        self.game = BlackGame()
        self.hero = Hero(0, 0)
        
    def play(self):
        self.game.ready()
        self.game.setDisplay(500, 300)
        self.hero.setName("prince")
        self.hero.setSkill("swing a sword")
        self.game.setHero(self.hero)
        self.game.launch()

# 그러면 아래와 같이 간단한 코드로 게임을 실행시킬 수 있습니다.
myGame = PlayBHGame()
myGame.play()

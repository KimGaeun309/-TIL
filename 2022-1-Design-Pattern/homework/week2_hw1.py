
# 버튼
class Button:
    def click(self):
        pass

class DarkButton(Button):
    def click(self):
        print("dark click")

class LightButton(Button):
    def click(self):
        print("light click")

class RedButton(Button):
    def click(self):
        print("red click")

class BlueButton(Button):
    def click(self):
        print("blue click")

# 스크롤
class ScrollBar:
    def scroll(self):
        pass

class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark scroll")

class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light scroll")

class RedScrollBar(ScrollBar):
    def scroll(self):
        print("red scroll")

class BlueScrollBar(ScrollBar):
    def scroll(self):
        print("blue scroll")

# 체크박스
class CheckBox:
    def check(self):
        pass

class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")

class LightCheckBox(CheckBox):
    def check(self):
        print("light check")

class RedCheckBox(CheckBox):
    def check(self):
        print("red check")


class BlueCheckBox(CheckBox):
    def check(self):
        print("blue check")

# 슬라이더
class Slider:
    def slide(self):
        pass

class DarkSlider(Slider):
    def slide(self):
        print("dark slide")

class LightSlider(Slider):
    def slide(self):
        print("light slide")

class RedSlider(Slider):
    def slide(self):
        print("red slide")

class BlueSlider(Slider):
    def slide(self):
        print("blue slide")

# 텍스트박스
class TextBox:
    def text(self):
        pass

class DarkTextBox(TextBox):
    def text(self):
        print("dark text")

class LightTextBox(TextBox):
    def text(self):
        print("light text")

class RedTextBox(TextBox):
    def text(self):
        print("red text")

class BlueTextBox(TextBox):
    def text(self):
        print("blue text")


class GUIFactory:
    def getButton(self):
        pass

    def getScroll(self):
        pass
    
    def getCheck(self):
        pass

    def getSlide(self):
        pass

    def getText(self):
        pass


class DarkFactory(GUIFactory):
    def getButton(self):
        return DarkButton()

    def getScroll(self):
        return DarkScrollBar()

    def getCheck(self):
        return DarkCheckBox();

    def getSlide(self):
        return DarkSlider();

    def getText(self):
        return DarkTextBox();


class LightFactory(GUIFactory):
    def getButton(self):
        return LightButton()

    def getScroll(self):
        return LightScrollBar()

    def getCheck(self):
        return LightCheckBox();

    def getSlide(self):
        return LightSlider();

    def getText(self):
        return LightTextBox();

class RedFactory(GUIFactory):
    def getButton(self):
        return RedButton()

    def getScroll(self):
        return RedScrollBar()

    def getCheck(self):
        return RedCheckBox();

    def getSlide(self):
        return RedSlider();

    def getText(self):
        return RedTextBox();

class BlueFactory(GUIFactory):
    def getButton(self):
        return BlueButton()

    def getScroll(self):
        return BlueScrollBar()

    def getCheck(self):
        return BlueCheckBox();

    def getSlide(self):
        return BlueSlider();

    def getText(self):
        return BlueTextBox();


df = DarkFactory()
bt = df.getButton()
sc = df.getScroll()
ch = df.getCheck()
sl = df.getSlide()
tx = df.getText()
bt.click()
sc.scroll()
ch.check()
sl.slide()
tx.text()

print("--------------")

lf = LightFactory()
bt = lf.getButton()
sc = lf.getScroll()
ch = lf.getCheck()
sl = lf.getSlide()
tx = lf.getText()
bt.click()
sc.scroll()
ch.check()
sl.slide()
tx.text()

print("--------------")

rf = RedFactory()
bt = rf.getButton()
sc = rf.getScroll()
ch = rf.getCheck()
sl = rf.getSlide()
tx = rf.getText()
bt.click()
sc.scroll()
ch.check()
sl.slide()
tx.text()

print("--------------")

bf = BlueFactory()
bt = bf.getButton()
sc = bf.getScroll()
ch = bf.getCheck()
sl = bf.getSlide()
tx = bf.getText()
bt.click()
sc.scroll()
ch.check()
sl.slide()
tx.text()
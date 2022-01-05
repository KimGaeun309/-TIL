# 스택 구현
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

# infix를 postfix로 바꿔주는 함수
def infix_to_postfix(infix):
    opstack = Stack() # 계산에 사용할 스택
    outstack = [] # postfix 로 바꾼 식 저장하는 리스트
    token_list = infix.split() # infix 식의 토큰을 저장해둔 리스트

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
        
        # 토큰이 ) 이면 ( 가 나올 때까지 opstack에서 pop한 토큰을 outstack에 append
        elif token == ')':
            while len(opstack) != 0:
                if opstack.top() == '(':
                    opstack.pop()
                    break
                else:
                    outstack.append(opstack.pop())
          
         # 연산자이면 opstack에 있는 자신보다 우선순위가 높거나 같은 
        elif token in '+-/*^':      # 연산자를 차례로 pop해 outstack에 append
            while len(opstack) != 0:
                if prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                else:
                    break
            opstack.push(token)
            
        else: # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while opstack.isEmpty() == False:
        outstack.append(opstack.pop())

    return " ".join(outstack)

	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)

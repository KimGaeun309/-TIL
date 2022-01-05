class Stack: # 스택 구현
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
        return len(self) == 0


def compute_postfix(postfix):
    token_list = postfix.split()
    S = Stack()
    for token in token_list:
        # token이 연산자일 때
        if token in '+-*/^':
            a = float(S.pop())
            b = float(S.pop())

            # 각각의 연산자에 따라 조건문 이용해 연산 결과 저장
            if token == '+':
                result = b + a
            elif token == '-':
                result = b - a
            elif token == '*':
                result = b * a
            elif token == '/':
                result = b / a
            else:
                result = b ** a
            #연산 결과를 스택 S에 추가
            S.push(result)

        # token이 숫자일 때
        else:
            S.push(token)

    return S.pop()
    
    
a = input()

print('%.4f' % compute_postfix(a))
		
		
		
	

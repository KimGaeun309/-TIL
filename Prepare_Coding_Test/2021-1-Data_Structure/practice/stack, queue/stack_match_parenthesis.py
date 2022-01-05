# 스택 구현
class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, val):
		self.items.append(val)
	
	def pop(self):
		try: # 가장 나중에 입력되었던 값 pop
			return self.items.pop() 
		except IndexError: # 스택이 비어있으면
			print("Stack is empty")
		
	def top(self): 
		try: # 가장 나중에 입력되었던 값 읽기 (pop X)
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
	
	def __len__(self):
		return len(self.items)
	
	def isEmpty(self): 
		return self.__len__() == 0

# 괄호 맞추기 함수
def parChecker(parSeq):
	S = Stack()
	for symbol in parSeq:
		if symbol == "(":
			S.push(symbol)
		else:
			if S.isEmpty(): # )의 짝이 없어 괄호 짝이 맞지 않음
				return False
			else:
				S.pop()
	return S.isEmpty() # 스택이 비어 있지 않다 -> 괄호 짝이 맞지 않는다
	
	
example = input()
print(parChecker(example))
	
	
	
	
	
	

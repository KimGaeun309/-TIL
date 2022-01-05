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

	
def get_token_list(expr):
	expr = ''.join(expr.split())
	expr = expr.replace('+', ' + ')
	expr = expr.replace('-', ' - ')
	expr = expr.replace('*', ' * ')
	expr = expr.replace('/', ' / ')
	expr = expr.replace('^', ' ^ ')
	expr = expr.replace('(', ' ( ')
	expr = expr.replace(')', ' ) ')
	token_list = expr.split()
	for i in range(len(token_list)):
		if token_list[i] not in '+-*/^()':
			x = float(token_list[i])
			token_list.pop(i)
			token_list.insert(i, str(x))
	
	return token_list
	
	
def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	
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
		
		elif token == ')':
			while len(opstack) != 0:
				if opstack.top() == '(':
					opstack.pop()
					break
				else:
					outstack.append(opstack.pop())
					
		elif token in '+-/*^':
			while len(opstack) > 0:
				if prec[opstack.top()] >= prec[token]:
					outstack.append(opstack.pop())
				else:
					break
			opstack.push(token)
			
		else: # operand일 때
			outstack.append(token)
	
	# opstack 에 남은 모든 연산자를 pop 후 outstack에 append
	for i in range(len(opstack)):
		outstack.append(opstack.pop())
	
	return outstack

	
	
def compute_postfix(token_list):
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
	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)

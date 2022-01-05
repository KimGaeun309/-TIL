class deque:
	def __init__(self, s): # 문자열을 받아서 그 문자들의 리스트로 items 초기화
		self.items = []
		for i in range(len(s)):
			self.items.append(s[i])
		
	def append(self, c): # 리스트의 오른쪽에 append
		self.items.append(c)
	
	def appendleft(self, c): # 리스트의 왼쪽에 append
		self.items.insert(0, c)
	
	def pop(self): # 리스트의 가장 오른쪽 원소 삭제해서 리턴
		return self.items.pop()	
	
	def popleft(self): # 리스트의 가장 왼쪽 원소 삭제해서 리턴
		x = self.items[0]
		del self.items[0]
		return x
	
	def __len__(self): # 리스트의 길이 리턴
		return len(self.items)
	
	def right(self): # 리스트의 가장 오른쪽 원소 리턴 (삭제X)
		return self.items[-1]
	
	def left(self): # 리스트의 가장 왼쪽 원소 리턴 (삭제X)
		return self.items[0]

def check_palindrome(s):
	dq = deque(s)
	palindrome = True
	while len(dq) > 1:
		#왼쪽과 오른쪽에서 하나씩 가져와서 비교
		if dq.popleft() != dq.pop(): # 맨 왼쪽 값과 맨 오른쪽 값이 다르면 False
			palindrome = False
	return palindrome
		
	
a = input()
print(check_palindrome(a))
	

class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	
	def pushFront(self, key):
		new_node = Node(key) #새로운 노드
		new_node.next = self.head #head 노드 앞에 새로운 노드 연결
		self.head = new_node #새로운 노드를 head 노드로
		self.size += 1


	def pushBack(self, key):
		new_node = Node(key) #새로운 노드
		if self.size == 0: #빈 리스트면 새로운 노드가 head 노드가 됨
			self.head = new_node
		else:
			tail = self.head #tail 노드 찾기
			while tail.next != None:
				tail = tail.next
			tail.next = new_node #tail 노드 다음에 새로운 노드 연결
		self.size += 1

	def popFront(self):
		if self.size == 0: # empty list
			return None 
		else:
			del_node = self.head 
			pop_key = del_node.key #삭제할 노드의 키값
			self.head = del_node.next #삭제할 노드의 다음 노드를 헤드 노드로
			del del_node #메모리에서 삭제
			self.size -= 1
			return pop_key #삭제한 노드의 키값 리턴
		
		# head 노드의 값 리턴. empty list이면 None 리턴

	def popBack(self):
		if self.size == 0:
			return None
		else:
			prev_tail = None #tail노드의 전 노드와 tail 노드 찾기
			tail = self.head 
			while tail.next != None:
				prev_tail = tail
				tail = tail.next
			if prev_tail == None: #tail 노드가 head 노드였다면
				self.head = None #head 노드를 None으로
			else:
				prev_tail.next = tail.next #prev_tail 노드 다음에 tail 노드의 다음 노드를 연결
			tail_key = tail.key
			del tail
			self.size -= 1
			return tail_key #tail 노드의 값 리턴
		# tail 노드의 값 리턴. empty list이면 None 리턴

	def search(self, key):
		search_node = self.head
		while search_node != None: # 모든 노드 차례대로 가져와서 비교
			if search_node.key == key:
				return search_node #key 값 찾으면 리턴
			search_node = search_node.next
		return None # key 값이 저장된 노드가 없음
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		
	def remove(self, x):
		if self.size == 0 or x == None: #빈 리스트이거나 x값이 None이면 제거 실패
			return False
		else:
			if self.head == x: #head 노드가 x이면 popFront
				self.popFront()
			else:
				prevx = self.head  #x 노드의 전 노드 찾기
				while prevx.next != x:
					prevx = prevx.next
				prevx.next = x.next #prevx 다음에 x의 다음 노드를 연결
				self.size -= 1
			return True
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
	
	def reverse(self, key):
		if self.search(key) == None: #x값 없음
			return
		New_L = SinglyLinkedList() #새로운 한 방향 리스트
		search_node = self.head
		while search_node.key != key: #key 노드 나오기 전까지 새로운 리스트에 노드를 차례대로 pushBack
			New_L.pushBack(self.popFront()) #원래 리스트에서 pushBack하는 노드 pop
			search_node = search_node.next
		
		for i in range(self.size): #x 이전 노드들이 pop된 원래 리스트에서 reverse되게끔 남은 노드들을
			New_L.pushBack(self.popBack()) #pop 해서 새로운 리스트에 push
		
		for i in range(New_L.size): #빈 리스트가 된 원래 리스트에 새로운 리스트 복사
			self.pushBack(New_L.popFront())
		


	def findMax(self):
		if self.size == 0: #빈 리스트
			return None
		else:
			if self.size == 1: #노드가 하나
				return self.head
			else:
				max_max = self.head #max 노드 찾기
				search_max = self.head
				while search_max.next != None: # 모든 노드 차례대로 가져와서 비교
					if max_max.key < search_max.next.key:
						max_max = search_max.next
					search_max = search_max.next
			return max_max.key # key 값이 저장된 노드가 없음
				# self가 empty이면 None, 아니면 max key 리턴
		
	def deleteMax(self):
		if self.size == 0: #빈 리스트
			return None
		else:
			if self.size == 1: #노드가 하나
				max_key = self.head.key
				self.head = None

			elif self.size == 2: #노드가 둘
				if self.head.key > self.head.next.key:
					max_key = self.head.key
					self.head = self.head.next
				else:
					max_key = self.head.next.key
					self.head.next = None

			else:	#노드가 셋 이상
				max_max = self.head #max와 prev_max 찾기
				prev_max = None
				search_max = self.head
				while search_max.next != None: # 모든 노드 차례대로 가져와서 비교
					if max_max.key < search_max.next.key:
						max_max = search_max.next
						prev_max = search_max
					search_max = search_max.next
				if max_max == self.head: #max 노드가 head 노드일 때
					max_key = self.head.key
					self.head = max_max.next
				else:
					max_key = max_max.key
					prev_max.next = max_max.next
				
			self.size -= 1	
			return max_key
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		
	def insert(self, k, val):
		if self.size < k: #노드 개수가 k 개보다 작다면
			self.pushBack(val)
		else:
			if k == 1: #k가 1일 때
				k_prev = self.head
			else:
				k_prev = self.head
				for i in range(k-1):
					k_prev = k_prev.next
					
			self.size += 1
			k_next = k_prev.next #새로운 노드 삽입
			k_prev.next = Node(val)
			k_prev.next.next = k_next
			
			
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")

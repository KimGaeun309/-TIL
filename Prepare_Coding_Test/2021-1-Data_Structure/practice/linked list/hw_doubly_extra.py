class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")
	# 나머지 코드
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
				return
		ap = a.prev
		bn = b.next

		#cut
		ap.next = bn
		bn.prev = ap

		#insert
		xn = x.next
		xn.prev = b
		b.next = xn
		a.prev = x
		x.next = a




	def moveAfter(self, a, x):
		self.splice(a, a, x)


	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)

	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)

	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)

	def pushFront(self, key):
		self.insertAfter(self.head, key)

	def pushBack(self, key):
		self.insertBefore(self.head, key)

	def deleteNode(self, x):
		if x == None or x == self.head:
			return None
		x.prev.next = x.next
		x.next.prev = x.prev

	def popFront(self):
		if self.isEmpty(): #빈 리스트
				return None
		pop_key = self.head.next.key
		self.deleteNode(self.head.next)
		return pop_key

	def popBack(self):
		if self.isEmpty(): #빈 리스트
				return None
		pop_key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return pop_key

	def search(self, key):
		search_node = self.head.next
		while search_node != self.head:  # 모든 노드 차례대로 가져와서 비교
				if search_node.key == key: #key 값이 저장된 노드 찾으면 리턴
						return search_node
				search_node = search_node.next
		return None  # key 값이 저장된 노드가 없음
		# key 값을 저장된 노드 리턴. 없으면 None 리턴



	def first(self):  # 맨 앞의 값
		if self.isEmpty(): #빈 리스트
			return None
		return self.head.next.key

	def last(self):  # 맨 뒤의 값
		if self.isEmpty(): #빈 리스트
			return None
		return self.head.prev.key

	def isEmpty(self):
		if self.head.next == None:
			return True
		else:
			return False


	def findMax(self):
		if self.isEmpty(): #빈 리스트
			return None
		else:
			if self.head.next.next == self.head: #노드가 하나
				max_max = self.head.next
			else: #노드가 둘 이상
				max_max = self.head.next #max 값 가진 노드 찾기
				search_max = self.head.next
				while search_max.next != self.head: # 모든 노드 차례대로 가져와서 비교
					if max_max.key < search_max.next.key:
						max_max = search_max.next
					search_max = search_max.next
			return max_max.key # key 값이 저장된 노드가 없음
			# self가 empty이면 None, 아니면 max key 리턴
		
			
	def deleteMax(self):
		if self.isEmpty(): #빈 리스트
			return None
		else:
			if self.head.next.next == self.head: #노드가 하나
				max_max = self.head.next
			else:
				max_max = self.head.next #max 값 가진 노드 찾기
				search_max = self.head.next
				while search_max.next != self.head: # 모든 노드 차례대로 가져와서 비교
					if max_max.key < search_max.next.key:
						max_max = search_max.next
					search_max = search_max.next
			max_max.prev.next = max_max.next #새로 연결해 max 노드를 리스트에서 없애기
			max_max.next.prev = max_max.prev
			return max_max.key #max 값 리턴
		
		
	def sort(self):
		size = 0
		cnt_size = self.head.next
		while cnt_size != self.head: #노드 개수 세기
			size += 1
			cnt_size = cnt_size.next
		New_L = DoublyLinkedList() #새로운 양방향 리스트
		for i in range(size):
			del_max = self.deleteMax() #max 노드를 원래 리스트에서 삭제하며
			New_L.pushFront(del_max) #새로운 양방향 리스트에 차례대로 추가
		return New_L #정렬된 양방향 리스트 리턴
		
		

# 나머지 코드
	
L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
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
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")

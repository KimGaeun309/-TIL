class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)

class BST:
	def __init__(self):
		self.root = None
		self.size = 0
	def __len__(self):
		return self.size

	def preorder(self, v):
		if v != None:
			print(v.key, end=" ")
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v): #LMR
		if v != None:
			self.inorder(v.left) 
			print(v.key,end=" ") 
			self.inorder(v.right) 

	def postorder(self, v): #LRM
		if v != None:
			self.postorder(v.left) 
			self.postorder(v.right) 
			print(v.key,end=" ")

	def find_loc(self, key):
		if self.size == 0: return None
		p = None #v의 부모 노드
		v = self.root 
		while v: #v가 None이 아니면
			if v.key == key: return v 
			else:
				if v.key < key:
					p = v
					v = v.right 
				else: 
					p = v
					v = v.left
		return p #찾는 키가 없으면 삽입될 곳의 부모노드 리턴

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key: 
			return p
		else:  
			return None


	def insert(self, key):
		# key가 이미 트리에 있다면 에러 출력없이 None만 리턴!
		v = Node(key)
		if self.size == 0: #빈 트리라면 루트에 삽입
			self.root = v
		else: 
			p = self.find_loc(key) 
			if p and p.key != key:
				v.parent = p
				if p.key < key :
					p.right = v

				else:
					p.left = v

				self.height_update(p)
		self.size += 1
		return v #이미 있던 곳이나 삽입된 위치 노드 리턴

	#height 재조정 필요
	def deleteByMerging(self, x):
		if not x: return
		a, b, pt = x.left, x.right, x.parent

		if a == None:
			c = b
			s = pt
		else:  # a != None
			c = m = a
			# 서브트리 a의 m 구하기
			while m.right:
				m = m.right
			m.right = b
			if b: b.parent = m
			s = m

		if self.root == x:  # c 가 루트 노드가 됨
			if c: c.parent = None
			self.root = c
		else:  # c 가 x의 부모노드의 자식노드가 됨
			if pt.left == x:
				pt.left = c
			else:
				pt.right = c
			if c: c.parent = pt
			self.height_update(pt)
		self.size -= 1
		self.height_update(s)
		return s

	#height 재조정 필요
	def deleteByCopying(self, x):
		if not x: return
		pt, L, R = x.parent, x.left, x.right
		if L: # L이 있음`
			y = x.left
			while y.right: #x.left의 m 찾기
				y = y.right
			x.key = y.key #copy

			if y.left: #y에 left 자식노드가 있다면
				y.left.parent = y.parent 

			if y.parent.left is y: #y가 left면(y가 x의 자식노드)
				y.parent.left = y.left #left에
			else: #y가 right면
				y.parent.right= y.left #right에
			#height
			pt = y.parent
			del y

		elif not L and R: # R만 있음
			y = R
			while y.left: #오른쪽 서브트리에서 가장 작은 값
				y = y.left
			x.key = y.key #copy
			if y.right:
				y.right.parent = y.parent
			if y.parent.left is y:
				y.parent.left = y.right
			else:
				y.parent.right = y.right
			#height
			pt = y.parent
			del y

		else: # L도 R도 없음
			if pt == None: # x가 루트노드인 경우
				self.root = None
			else:
				if pt.left is x:
					pt.left = None
				else:
					pt.right = None
			del x
		self.size -= 1
		self.height_update(pt)
		return pt

	#height update 해주는 함수
	def height_update(self, x): # x부터 수정 시작
		while True:
			if not x: return
			l_h = self.height(x.left)
			r_h = self.height(x.right)
			x_h = max(l_h, r_h) + 1
			if self.height(x) == x_h:
				break
			x.height = x_h
			x = x.parent

	def height(self, x): # 노드 x의 height 값을 리턴
			if x == None: return -1
			else: return x.height

	def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
			# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
		if not x: return None
		if x.right:
			v = x.right
			while v.left:
				v = v.left
			return v	

		else:
				while x.parent:
					if x.key < x.parent.key:
						return x.parent
					x = x.parent
				return None



	def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
			# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
		if not x: return None

		if x.left:
			v = x.left
			while v.right:
				v = v.right
			return v
		else:
			while x.parent:
				if x.key > x.parent.key:
					return x.parent
				x = x.parent
			return None



	def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.left
		if x == None: return
		b = x.right
		x.parent = z.parent
		if z.parent:
			if z.parent.left == z:
				z.parent.left = x
			else:
				z.parent.right = x
		x.right = z
		z.parent = x
		z.left = b
		if b: b.parent = z
		#z == self.root라면 x가 새로운 루트가 되어야 함
		if z == self.root: self.root = x
		else: self.height_update(x.parent)
		self.height_update(x)
		self.height_update(z)


	def rotateLeft(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if not z: return
		x = z.right
		if x == None: return
		b = x.left
		x.parent = z.parent
		if z.parent:
			if z.parent.right == z:
				z.parent.right = x
			else:
				z.parent.left = x
		x.left = z
		z.parent = x
		z.right = b
		if b: b.parent = z
		if z == self.root: self.root = x
		else: self.height_update(x.parent)
		self.height_update(x)
		self.height_update(z)





class SplayTree(BST):
	def splay(self, v):
		while v and v.parent != None:
			p = v.parent
			if p.parent == None:
				if p.left == v:
					self.rotateRight(p)
				else:
					self.rotateLeft(p)
			else:
				pp = p.parent
				if p.left == v and pp.left == p:
					self.rotateRight(p)
					self.rotateRight(v.parent)
				elif p.right == v and pp.right == p:
					self.rotateLeft(p)
					self.rotateLeft(v.parent)
				elif p.left == v and pp.right == p:
					self.rotateRight(p)
					self.rotateLeft(v.parent)
				else:
					self.rotateLeft(p)
					self.rotateRight(v.parent)
		return v

	def search(self, key):
		v = super(SplayTree, self).search(key)
		if v:
			self.root = self.splay(v)
		return v

	def insert(self, key):
		v = super(SplayTree, self).insert(key)
		if v:
			self.root = self.splay(v)
		return v
				
	def delete(self, x): 
		if x == None: return
		self.splay(x)
		L, R = x.left, x.right
		m = L
		while m and m.right:
			m = m.right
		if m:
			L.parent = None
			self.root = self.splay(m)
			m.right = R
			if R: R.parent = m
			self.height_update(m)	
		else:
			self.root = R
			if R: R.parent = None

T = SplayTree()
while True:
		cmd = input().split()
		if cmd[0] == 'insert':
				v = T.insert(int(cmd[1]))
				print("+ {0} is inserted".format(v.key))
		elif cmd[0] == 'delete':
				v = T.search(int(cmd[1]))
				T.delete(v)
				print("- {0} is deleted".format(int(cmd[1])))
		elif cmd[0] == 'search':
				v = T.search(int(cmd[1]))
				if v == None:
						print("* {0} is not found!".format(cmd[1]))
				else:
						print("* {0} is found!".format(cmd[1]))
		elif cmd[0] == 'preorder':
				T.preorder(T.root)
				print()
		elif cmd[0] == 'postorder':
				T.postorder(T.root)
				print()
		elif cmd[0] == 'inorder':
				T.inorder(T.root)
				print()
		elif cmd[0] == 'exit':
				break
		else:
				print("* not allowed command. enter a proper command!")

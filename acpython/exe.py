class Tree64:
  HEIGHT = 8
  BIT_SIZE = 6
  SIZE = 2 << BIT_SIZE
  MASK = SIZE - 1
  class Node:
    def __init__(s):
      s.D = 0
      s.L = [None] * Tree64.SIZE
    def add(s, n, height):
      if height == -1 : return
      shift = Tree64.BIT_SIZE * height
      x = (n >> shift) & Tree64.MASK
      if s.L[x] == None: s.L[x] = Tree64.Node()
      s.L[x].add(n, height - 1)
      s.D |= (1 << x)
    def erace(s, n, height):
      if height == -1: return True
      shift = Tree64.BIT_SIZE * height
      x = (n >> shift) & Tree64.MASK
      if s.L[x] == None: return False
      if s.L[x].erace(n, height - 1):
        s.L[x] = None
        s.D ^= (1 << x)
        if s.D == 0: return True
      return False
    def find(s, n, height):
      if height == -1: return True
      shift = Tree64.BIT_SIZE * height
      x = (n >> shift) & Tree64.MASK
      if s.L[x] == None: return False
      return s.L[x].find(n, height - 1)
    def find_upper(s, n, height):
      if height == -1: return 0
      shift = Tree64.BIT_SIZE * height
      x = (n >> shift) & Tree64.MASK
      if s.L[x] != None:
        ans = s.L[x].find_upper(n, height - 1)
        if ans != None: return (x << shift) + ans
      d = s.D & ~((1 << (x + 1)) - 1)
      if d == 0: return None
      y = (d & -d).bit_length() - 1
      if y == -1: return None
      return (x << shift) + s.L[y].find_min(height - 1)
    def find_lower(s, n, height):
      if height == -1: return 0
      shift = Tree64.BIT_SIZE * height
      x = (n >> shift) & Tree64.MASK
      if s.L[x] != None:
        ans = s.L[x].find_lower(n, height - 1)
        if ans != None: return (x << shift) + ans
      d = s.D & (1 << x) - 1
      if d == 0: return None
      y = d.bit_length() - 1
      if y == -1: return None
      return (x << shift) + s.L[y].find_max(height - 1)
    def find_min(s, height):
      if height == -1: return 0
      if s.D == 0: return None
      x = (s.D & -s.D).bit_length() - 1
      if height == 0: return x
      shift = Tree64.BIT_SIZE * height
      return (x << shift) + s.L[x].find_min(height - 1)
    def find_max(s, height):
      if height == -1: return 0
      if s.D == 0: return None
      x = s.D.bit_length() - 1
      if height == 0: return x
      shift = Tree64.BIT_SIZE * height
      return (x << shift) + s.L[x].find_max(height - 1)
    
  def __init__(s):
    s.root = Tree64.Node()
  def add(s, n):
    s.root.add(n, Tree64.HEIGHT - 1)
  def erace(s, n):
    s.root.erace(n, Tree64.HEIGHT - 1)
  def find(s, n):
    return s.root.find(n, Tree64.HEIGHT - 1)
  def find_upper(s, n):
    ans =  s.root.find_upper(n, Tree64.HEIGHT - 1)
    if ans == None: return -1
    return ans
  def find_lower(s, n):
    ans = s.root.find_lower(n, Tree64.HEIGHT - 1)
    if ans == None: return -1
    return ans
  
N, Q = list(map(int, input().split()))
T = list(input())
ck = [list(map(int, input().split())) for _ in range(Q)]

tree = Tree64()
for i in range(N):
  if T[i] == "1":
    tree.add(i)

for c, k in ck:
  match c:
    case 0:
      tree.add(k)
    case 1:
      tree.erace(k)
    case 2:
      if tree.find(k):
        print(1)
      else:
        print(0)
    case 3:
      print(tree.find_upper(k))
    case 4:
      print(tree.find_lower(k))

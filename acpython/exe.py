# 連結リスト add/insertとremoveをO(1)
class DoubleLinkedList():
  class Node():
    def __init__(s, data, previous=None, next=None):
      s.data = data
      s.previous = previous
      s.next = next

  def __init__(s):
    s._head = s.Node('DUMMY-HEAD')
    s._tail = s.Node('DUMMY-TAIL', previous=s._head)
    s._head.next = s._tail
    s.length = 0
    s.Nodes = {}

  # リストを設定
  def setList(s, data):
    for a in data:
      s.add(a)

  # データを末尾に連結O(1)
  def add(s, data):
    node = s.Node(data, previous=s._tail.previous, next=s._tail)
    s._tail.previous.next = node
    s._tail.previous = node
    s.length += 1
    s.Nodes[data] = node

  # データを削除O(1)
  def remove(s, data):
    target = s.Nodes[data]
    target.previous.next = target.next
    target.next.previous = target.previous
    del target
    s.length -= 1

  # data_iの後にdataを追加 O(1)
  def insert(s, deta_i, data):
    target = s.Nodes[deta_i]
    node = s.Node(data, previous=target, next=target.next)
    target.next.previous = node
    target.next = node
    s.length += 1
    s.Nodes[data] = node

  # リスト取得
  def getList(s):
    return s.list
       
  def pophead(s):
    target = s._head.next
    if target == s._tail:
      return None
    s._head.next = target.next
    target.next.previous = s._head
    data = target.data
    s.length -= 1
    del target
    return data

  def poptail(s):
    target = s._tail.previous
    if target == s._head:
      return None
    s._tail.previous = target.previous
    target.previous.next = s._tail
    data = target.data
    s.length -= 1
    del target
    return data

  def print_reverse(s):
    node = s._tail.previous
    while node != s._head:
      print(node.drata)
      node = node.pevious

  @property
  def list(s):
    node_data = []
    node = s._head.next
    while node != s._tail:
      node_data.append(node.data)
      node = node.next
    return node_data

  def __iter__(s):
    node_data = s.list
    return iter(node_data)

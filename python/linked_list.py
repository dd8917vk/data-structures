class LinkList:
  def __init__(self, head = None):
      self.head = head
      self.length = 0

  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList

  def add(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next:
        current_node = current_node.next
      current_node.next = new_node
    self.length += 1
    return new_node
    # write your code to ADD an element to the Linked List
    

  def remove(self, data):
    current_node = self.head
    previous_node = None
    if current_node.data == data:
        self.head = current_node.next
    else:
      while current_node.data != data:
        previous_node = current_node
        current_node = current_node.next
      previous_node.next = current_node.next
    self.length -= 1
    return self.head
    # write your code to REMOVE an element from the Linked List
    

  def get(self, element_to_get):
    
    # write you code to GET and return an element from the Linked List
    pass

# ----- Node ------
class Node:
  def __init__(self, data, next= None):
    self.data = data
    self.next = next
   
new_linked_list = LinkList()
new_linked_list.add(4)
print(new_linked_list.head.data)
new_linked_list.add(12)
new_linked_list.add(14)
new_linked_list.add(3)
new_linked_list.add(7)
print(new_linked_list.head.next.data)
new_linked_list.remove(12)
print(new_linked_list.head.data)
print(new_linked_list.head.next)


  

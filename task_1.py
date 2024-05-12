class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev_el = None
        current = self.head
        while current:
            next_el = current.next
            current.next = prev_el
            prev_el = current
            current = next_el
        self.head = prev_el

    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, h):
        # Базовий випадок: якщо head є None або має один елемент
        if not h or not h.next:
            return h
            
        # Отримання середини списку
        middle = self.get_middle(h)
        next_to_middle = middle.next

        # Розділення списку
        middle.next = None

        # Рекурсивне сортування двох половин
        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)

        # Об'єднання двох половин
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sorted_merge(self, a, b):
        result = None
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def sort(self):
        self.head = self.merge_sort(self.head)        
            
llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(5)
llist.insert_at_end(4)
llist.insert_at_end(8)
llist.insert_at_end(6)

print('original list:')
llist.print_list()  

print('reversed list:')
llist.reverse()
llist.print_list()

print('sorted list:')
llist.sort()
llist.print_list()
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

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Реверсування списку
    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    # Сортування злиттям
    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head

        mid = self.find_middle()
        next_to_mid = mid.next
        mid.next = None

        left_half = LinkedList()
        left_half.head = self.head

        right_half = LinkedList()
        right_half.head = next_to_mid

        left_half.merge_sort()
        right_half.merge_sort()

        self.head = self.merge(left_half.head, right_half.head)

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr

    def merge(self, left, right):
        merged = LinkedList()
        current = merged.head

        while left and right:
            if left.data <= right.data:
                if current is None:
                    merged.head = left
                    current = left
                else:
                    current.next = left
                    current = left
                left = left.next
            else:
                if current is None:
                    merged.head = right
                    current = right
                else:
                    current.next = right
                    current = right
                right = right.next

        if left:
            current.next = left
        if right:
            current.next = right

        return merged.head
    
    # Об'єднання двох відсортованих списків
    def merge_sorted_lists(self, list1, list2):
        merged_list = LinkedList()

        # Поки обидва списки не пусті
        while list1 is not None and list2 is not None:
            # Вибираємо менший елемент з обох списків
            if list1.data < list2.data:
                merged_list.insert_at_end(list1.data)
                list1 = list1.next
            else:
                merged_list.insert_at_end(list2.data)
                list2 = list2.next

        # Додаємо залишок першого списку, якщо він є
        while list1 is not None:
            merged_list.insert_at_end(list1.data)
            list1 = list1.next

        # Додаємо залишок другого списку, якщо він є
        while list2 is not None:
            merged_list.insert_at_end(list2.data)
            list2 = list2.next

        return merged_list

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Зв'язний список
print("Зв'язний список:")
llist.print_list()

# Реверсування списку
print("Реверс списку:")
llist.reverse_list()
llist.print_list()

# Сортування списку
print("Список після сортування:")
llist.merge_sort()
llist.print_list()

# Об'єднання списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(6)
list1.insert_at_end(8)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(7)
list2.insert_at_end(9)
list2.insert_at_end(10)

merged_list = llist.merge_sorted_lists(list1.head, list2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()
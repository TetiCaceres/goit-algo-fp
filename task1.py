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
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insertion_sort(self):
        sorted_head = None
        cur = self.head
    
        while cur:
            next_node = cur.next # Зберігаємо наступний, бо cur.next зміниться
            sorted_head = self._sorted_insert(sorted_head, cur)
            cur = next_node
        
        self.head = sorted_head

    def _sorted_insert(self, head_ref, new_node):
        # Допоміжний метод для вставки вузла у відсортовану частину
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        else:
            current = head_ref
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return head_ref
    
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)  # "Фіктивний" вузол для спрощення логіки
        tail = dummy
    
        cur1 = list1.head
        cur2 = list2.head
    
        while cur1 and cur2:
            if cur1.data <= cur2.data:
                tail.next = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                cur2 = cur2.next
            tail = tail.next
    
        # Якщо один зі списків закінчився, приєднуємо залишок іншого
        tail.next = cur1 or cur2
    
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# ================== ПРИКЛАД ВИКОРИСТАННЯ ==================

# 1. Сортування
llist = LinkedList()
for x in [5, 20, 15, 25]: llist.insert_at_end(x)
llist.insertion_sort()
print("Відсортований:")
llist.print_list()

# 2. Реверсування
llist.reverse()
print("Реверсований:")
llist.print_list()

# 3. Злиття
list_a = LinkedList()
for x in [1, 3, 5]: list_a.insert_at_end(x)
list_b = LinkedList()
for x in [2, 4, 6]: list_b.insert_at_end(x)

merged = LinkedList.merge_sorted_lists(list_a, list_b)
print("Результат злиття:")
merged.print_list()
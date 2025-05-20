from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, char):
        new_node = Node(char)
        if self.head == None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
    
    def _build_cleaned_string(self, direction='left'):
        vowels = ['a', 'e', 'i', 'o', 'u']
        seen_chars = ""
        result = ""

        if direction == 'left':
            current = self.head
            while current:
                ch = current.char.lower()
                if ch not in vowels and ch not in seen_chars:
                    result += ch
                    seen_chars += ch
                current = current.next
        elif direction == 'right':
            current = self.tail
            while current:
                ch = current.char.lower()
                if ch not in vowels and ch not in seen_chars:
                    result += ch
                    seen_chars += ch
                current = current.prev
        return result

    def is_custom_palindrome(self):
        left_cleaned = self._build_cleaned_string('left')
        right_cleaned = self._build_cleaned_string('right')
        return left_cleaned == right_cleaned
        
    def __str__(self):
        start = self.head
        result = ""
        while start:
            result += start.char
            start = start.next
        return result
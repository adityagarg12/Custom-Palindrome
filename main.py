from DoublyLinkedList import DoublyLinkedList

def main():
    s = input()
    list = DoublyLinkedList()
    for char in s:
        list.insert(char)
    
    if list.is_custom_palindrome():
        print("YES, it is a custom palindrome")
    else:
        print("NO, it is not a custom palindrome")
        
if __name__ == "__main__":
    main()
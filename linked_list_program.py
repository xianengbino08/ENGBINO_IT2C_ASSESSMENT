class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_head(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        if self.head is None:
            return "NULL"
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return " -> ".join(parts) + " -> NULL"


def main():
    print("=== SINGLY LINKED LIST: Append and Delete Nodes ===")
    last_name = input("Enter your last name: ").strip().upper()

    if not last_name.isalpha():
        print("Please enter letters only.")
        return

    LL = LinkedList()
    print(f"Input: {list(last_name)}")

    print("\n--- ADD PHASE (Append) ---")
    for letter in last_name:
        LL.append(letter)
        print(f"Append '{letter}' -> {LL.display()}")

    print("\n--- REMOVE PHASE (Delete) ---")
    while LL.head is not None:
        removed = LL.delete_head()
        print(f"Delete '{removed}' -> {LL.display()}")

    print("\nOutput: Head = NULL, the linked list is now empty.")


if __name__ == "__main__":
    main()
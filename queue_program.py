class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            return "empty"
        return ", ".join(self.items)


def main():
    print("=== QUEUE (FIFO): Enqueue and Dequeue Letters ===")
    last_name = input("Enter your last name: ").strip().upper()

    if not last_name.isalpha():
        print("Please enter letters only.")
        return

    Q = Queue()
    print(f"Input: {list(last_name)}")

    print("\n--- ADD PHASE (Enqueue) ---")
    for letter in last_name:
        Q.enqueue(letter)
        print(f"Enqueue '{letter}' -> Queue (front to rear): {Q.display()}")

    print("\n--- REMOVE PHASE (Dequeue) ---")
    while not Q.is_empty():
        removed = Q.dequeue()
        print(f"Dequeue '{removed}' -> Queue (front to rear): {Q.display()}")

    print("\nOutput: Queue is now empty.")


if __name__ == "__main__":
    main()
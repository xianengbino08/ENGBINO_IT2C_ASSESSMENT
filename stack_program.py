class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def display(self):
        if self.is_empty():
            return "empty"
        return ", ".join(reversed(self.items))


def main():
    print("=== STACK (LIFO): Push and Pop Letters ===")
    last_name = input("Enter your last name: ").strip().upper()

    if not last_name.isalpha():
        print("Please enter letters only.")
        return

    S = Stack()
    print(f"Input: {list(last_name)}")

    print("\n--- ADD PHASE (Push) ---")
    for letter in last_name:
        S.push(letter)
        print(f"Push '{letter}' -> Stack (top to bottom): {S.display()}")

    print("\n--- REMOVE PHASE (Pop) ---")
    while not S.is_empty():
        removed = S.pop()
        print(f"Pop '{removed}' -> Stack (top to bottom): {S.display()}")

    print("\nOutput: Stack is now empty.")


if __name__ == "__main__":
    main()
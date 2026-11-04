def add_letters(array, last_name):
    print("\n--- ADD PHASE ---")
    for letter in last_name:
        array.append(letter)
        print(f"Insert '{letter}' at index {len(array) - 1} -> {array}")


def remove_letters(array):
    print("\n--- REMOVE PHASE ---")
    while len(array) > 0:
        removed = array.pop()
        print(f"Remove '{removed}' -> {array}")


def main():
    print("=== ARRAY: Add and Remove Letters ===")
    last_name = input("Enter your last name: ").strip().upper()

    if not last_name.isalpha():
        print("Please enter letters only.")
        return

    A = []
    print(f"Input: {list(last_name)}")

    add_letters(A, last_name)
    remove_letters(A)

    print("\nOutput:", A)
    print("Array is now empty.")


if __name__ == "__main__":
    main()
# Problem 1: Reverse a String
def reverse_string():
    user_input = input("Enter a string: ")  # Taking user input
    reversed_str = user_input[::-1]  # Reversing using slicing
    print("Reversed String:", reversed_str)

# Problem 2: Count Vowels in a String
def count_vowels():
    user_input = input("Enter a string: ")  # Taking user input
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Vowel set
    count = sum(1 for char in user_input.lower() if char in vowels)  # Counting vowels
    print("Vowel Count:", count)

# Problem 3: Sum of Digits
def sum_of_digits():
    user_input = input("Enter a non-negative integer: ")  # Taking user input
    if not user_input.isdigit():  # Checking if input is a valid non-negative integer
        print("Invalid input! Please enter a non-negative integer.")
        return
    total_sum = sum(int(digit) for digit in user_input)  # Summing up the digits
    print("Sum of Digits:", total_sum)


# Main function to run all problems / Function Calls
if __name__ == "__main__":
    print("\n🔹 Problem 1: Reverse a String")
    reverse_string()

    print("\n🔹 Problem 2: Count Vowels in a String")
    count_vowels()

    print("\n🔹 Problem 3: Sum of Digits")
    sum_of_digits()
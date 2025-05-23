def classify_number(num):
    """
    Classifies a number as even, odd, or prime.

    Args:
        num (int): The number to classify.

    Returns:
        str: A string indicating the classification (e.g., "Even", "Odd", "Prime",
             "Neither even, odd, nor prime (e.g., 1 or negative numbers)").
    """
    if not isinstance(num, int):
        return "Invalid input: Please enter an integer."

    if num <= 1:
        return "Neither even, odd, nor prime (e.g., 1 or negative numbers)"
    elif num == 2:
        return "Prime and Even"  # 2 is the only even prime number
    elif num % 2 == 0:
        return "Even"
    else:
        # Check for prime for odd numbers
        is_prime = True
        # We only need to check for divisors up to the square root of the number
        # because if a number has a divisor greater than its square root,
        # it must also have a divisor smaller than its square root.
        for i in range(3, int(num**0.5) + 1, 2):  # Only check odd divisors
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            return "Prime"
        else:
            return "Odd"

# --- Test cases ---
print(f"0: {classify_number(0)}")
print(f"1: {classify_number(1)}")
print(f"2: {classify_number(2)}")
print(f"3: {classify_number(3)}")
print(f"4: {classify_number(4)}")
print(f"7: {classify_number(7)}")
print(f"9: {classify_number(9)}")
print(f"11: {classify_number(11)}")
print(f"15: {classify_number(15)}")
print(f"17: {classify_number(17)}")
print(f"100: {classify_number(100)}")
print(f"Invalid input (float): {classify_number(3.5)}")
print(f"Invalid input (string): {classify_number('hello')}")
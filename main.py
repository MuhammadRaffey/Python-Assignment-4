name: str = input("Enter your name: ")
favNumbers: list[int] = []
favNumbers.append(int(input("Enter your first favorite number: ")))
favNumbers.append(int(input("Enter your second favorite number: ")))
favNumbers.append(int(input("Enter your third favorite number: ")))

print(f"Hello {name}, Let's explore your favorite numbers:")
for number in favNumbers:
    print(f"The number {number} is {'even' if number % 2 == 0 else 'odd'}.")
for number in favNumbers:
    print(f"The number {number} and its square: {(number, number**2)}")

total: int = sum(favNumbers)
print(f"Amazing! The sum of your favorite numbers is: {total}")

if total > 1:
    is_prime: bool = True
    if total % 2 == 0 or total % 3 == 0:
        is_prime = total in (2, 3)
    else:
        i: int = 5
        while i * i <= total:
            if total % i == 0 or total % (i + 2) == 0:
                is_prime = False
                break
            i += 6
    print(f"Wow, {total} is {'a prime number' if is_prime else 'not a prime number'}!")
else:
    print(f"Wow, {total} is not a prime number!")

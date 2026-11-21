# Build 1: fizzbuzz.py (20 mins — Classic Screening Warmup)
# Loop from 1 to 100 using range(1, 101).

# Print "FizzBuzz" if divisible by both 3 and 5, "Fizz" if divisible by 3, "Buzz" if divisible by 5, otherwise print the number.

# Trap to watch: Put the 3 and 5 check first in your if / elif chain—think about why it breaks if you put it last.



def fizzbuzz(limit: int = 100) -> list [str]: 

    results: list[str] = []

    for num in range(1, limit + 1):
        if num % 3 == 0 and num % 5 == 0:
            results.append("FizzBuzz")
        elif num % 3 == 0:
            results.append("Fizz")
        elif num % 5 == 0:
            results.append("Buzz")
        else:
            results.append(num)

    return results 


for entry in fizzbuzz(100):
    print(entry)

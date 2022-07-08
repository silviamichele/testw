def fibonacci(n: int) -> int:
    number = n if n < 2 else fibonacci(n-1) + fibonacci(n-2)
    return number


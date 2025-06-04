def square(x):
    return x * x

# Only runs when you run this file directly, not during import
if __name__ == "__main__":
    x = int(input("What's the value of x? "))
    result = square(x)
    print(f"The square of x is {result}")


def add(x: float, y: float) -> float:
    
    return x + y

def multiply(x: float, y: float) -> float:
    
    return x * y

def square(x: float) -> float:
    
    return multiply(x, x)

def add_squares(x: float, y: float) -> float:

    return add(square(x), square(y))


num1 = 5
num2 = 10

print(f"Addition result: {add(num1, num2)}")
print(f"Multiplication result: {multiply(num1, num2)}")
print(f"Squared result: {square(num1)}")
print(f"Add squared result: {add_squares(num1, num2)}")

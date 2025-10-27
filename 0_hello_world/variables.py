x = 10
y = 5
name = "Alice"

print("Value of x:", x)
print("Value of y:", y)
print("Name:", name)

sum_result = x + y
diff_result = x - y
prod_result = x * y
div_result = x / y

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)

print("Hello, " + name + "! The sum of", x, "and", y, "is", sum_result)

print(f"Hello, {name}! The calculations are: {x}+{y}={sum_result}, {x}-{y}={diff_result}, {x}*{y}={prod_result}, {x}/{y}={div_result:.2f}")

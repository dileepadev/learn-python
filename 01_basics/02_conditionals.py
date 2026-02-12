# Lesson 2: Conditionals and Comparisons

# 1. Comparison operators
# Compare values using ==, !=, <, >, <=, >=
print('5 == 5 ->', 5 == 5)
print('5 != 3 ->', 5 != 3)
print('3 < 7  ->', 3 < 7)
print('10 >= 10 ->', 10 >= 10)

# 2. if / elif / else
# Use these to perform different actions depending on conditions.
age = 18
if age < 13:
    print('Child')
elif age < 20:
    print('Teenager')
else:
    print('Adult')

# 3. Truthiness
# Many values have an implicit boolean value (truthy/falsy)
for value in [0, 1, "", "hello", [], [1,2], None]:
    print(value, 'is truthy?' , bool(value))

# 4. Logical operators: and, or, not
a = 5
b = 10
if a < b and b < 20:
    print('a < b and b < 20 is True')

if a == 5 or b == 0:
    print('At least one comparison is True')

if not (a > b):
    print('a is not greater than b')

# 5. Short (ternary) conditional
status = 'adult' if age >= 18 else 'minor'
print('Status:', status)

# 6. Common patterns
# - Guard clauses
# - Early returns in functions

# Example function using conditionals
def classify_number(n):
    if n == 0:
        return 'zero'
    if n % 2 == 0:
        return 'even'
    return 'odd'

print('classify_number(0) ->', classify_number(0))
print('classify_number(7) ->', classify_number(7))
print('classify_number(8) ->', classify_number(8))

# 7. Exercises (try to solve these on your own)
# 1) write a function is_even(n) -> True/False
# 2) write a function grade(score) -> 'A', 'B', 'C', 'D', 'F' (use >= thresholds)
# 3) write a function login_allowed(age, verified) -> True if age>=18 and verified==True

# Example solutions (uncomment to test)

def is_even(n):
    return n % 2 == 0

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def login_allowed(age, verified):
    return age >= 18 and verified is True

# Quick checks
print('is_even(4) ->', is_even(4))
print('grade(85) ->', grade(85))
print('login_allowed(20, True) ->', login_allowed(20, True))

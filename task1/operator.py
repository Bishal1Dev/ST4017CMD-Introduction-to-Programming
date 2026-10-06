"""
ST4017CMD - Introduction to Programming
Lesson 4: Python Operators

This file contains notes and examples for the seven main
categories of Python operators.
"""


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================

"""
Arithmetic operators are used to perform mathematical calculations.

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus (remainder)
**  Exponentiation (power)
"""

print("=== Arithmetic Operators ===")

print(15 + 7)       # Addition: 22
print(15 - 7)       # Subtraction: 8
print(15 * 7)       # Multiplication: 105
print(7 / 2)        # Division: 3.5
print(4 / 2)        # Division always returns float: 2.0
print(17 // 5)      # Floor division: 3
print(-17 // 5)     # Floor division: -4
print(17 % 5)       # Modulus/remainder: 2
print(10 % 2)       # Remainder: 0
print(2 ** 10)      # Exponentiation: 1024
print(64 ** 0.5)    # Square root: 8.0


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================

"""
Comparison operators compare two values.

They always return either True or False.

==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
"""

print("\n=== Comparison Operators ===")

print(10 == 10)     # True
print(10 != 5)      # True
print(10 > 20)      # False
print(3 < 7)        # True
print(5 >= 5)       # True
print(4 <= 5)       # True


# Chained comparisons

x = 5

print(1 < x < 10)   # True
print(0 <= x <= 5)  # True
print(5 < x < 10)   # False


# String comparisons

print("apple" < "banana")       # True
print("Python" == "python")     # False because comparison is case-sensitive


# ============================================================
# 3. ASSIGNMENT OPERATORS
# ============================================================

"""
Assignment operators are used to assign values to variables.

=     Assign
+=    Add and assign
-=    Subtract and assign
*=    Multiply and assign
/=    Divide and assign
//=   Floor divide and assign
%=    Modulus and assign
**=   Power and assign
"""

print("\n=== Assignment Operators ===")

score = 50
print(score)        # 50

score += 10
print(score)        # 60

score *= 2
print(score)        # 120

score -= 20
print(score)        # 100

score //= 4
print(score)        # 25

score %= 10
print(score)        # 5

score **= 2
print(score)        # 25


# Multiple assignment

a = b = c = 0

print(a, b, c)      # 0 0 0


# Tuple unpacking

x, y, z = 1, 2, 3

print(x, y, z)      # 1 2 3


# Swapping variables

a, b = 10, 20

a, b = b, a

print(a, b)         # 20 10


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================

"""
Logical operators are used to combine conditions.

and  -> True only when both conditions are True
or   -> True when at least one condition is True
not  -> Reverses True/False
"""

print("\n=== Logical Operators ===")

print(True and True)        # True
print(True and False)       # False

print(True or False)        # True
print(False or False)       # False

print(not True)             # False
print(not False)            # True


# Example using conditions

age = 20
has_id = True

print(age >= 18 and has_id)     # True


is_student = True
is_teacher = False

print(is_student or is_teacher) # True


# Short-circuit evaluation

# Python does not evaluate the second condition when
# the result is already known.

print(False and 1 / 0)      # False
print(True or 1 / 0)        # True


# ============================================================
# 5. BITWISE OPERATORS
# ============================================================

"""
Bitwise operators work directly with binary bits.

&   Bitwise AND
|   Bitwise OR
^   Bitwise XOR
~   Bitwise NOT
<<  Left shift
>>  Right shift
"""

print("\n=== Bitwise Operators ===")

# Binary representations

print(bin(5))       # 0b101
print(bin(3))       # 0b11

"""
5 = 0101
3 = 0011

AND:
0101
0011
----
0001 = 1

OR:
0101
0011
----
0111 = 7

XOR:
0101
0011
----
0110 = 6
"""

print(5 & 3)        # 1
print(5 | 3)        # 7
print(5 ^ 3)        # 6
print(~5)           # -6

# Left shift

print(5 << 1)       # 10
print(5 << 2)       # 20

# Right shift

print(20 >> 1)      # 10
print(20 >> 2)      # 5


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================

"""
Membership operators check whether a value exists
inside a sequence.

in      -> Checks if a value exists
not in  -> Checks if a value does not exist
"""

print("\n=== Membership Operators ===")

print("py" in "python")          # True
print("Java" in "python")        # False
print("z" not in "hello")        # True


# Membership with lists

numbers = [1, 2, 3, 4, 5]

print(3 in numbers)              # True
print(10 in numbers)             # False
print(10 not in numbers)         # True


# ============================================================
# 7. IDENTITY OPERATORS
# ============================================================

"""
Identity operators check whether two variables refer
to the exact same object in memory.

is       -> Same object
is not   -> Different objects

Important:
== checks whether values are equal.
is checks whether objects are identical.
"""

print("\n=== Identity Operators ===")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True - same values
print(a is b)       # False - different objects

print(a is c)       # True - same object
print(a is not b)   # True - different objects


# Checking for None

value = None

print(value is None)        # True
print(value is not None)    # False

# Best practice:
# Use "is None" instead of "== None"


# ============================================================
# 8. OPERATOR PRECEDENCE
# ============================================================

"""
Operator precedence determines the order in which
Python evaluates operators.

Simplified order:

1. Parentheses: ()
2. Exponentiation: **
3. Unary: +x, -x, ~x
4. Multiplication, Division, Floor Division, Modulus
5. Addition, Subtraction
6. Bitwise shifts: << >>
7. Bitwise AND: &
8. Bitwise XOR: ^
9. Bitwise OR: |
10. Comparisons
11. not
12. and
13. or

When unsure, use parentheses.
"""

print("\n=== Operator Precedence ===")

# Multiplication happens before addition

print(2 + 3 * 4)        # 14

# Parentheses are evaluated first

print((2 + 3) * 4)      # 20


# Exponentiation works from right to left

print(2 ** 3 ** 2)      # 512
# Same as: 2 ** (3 ** 2)

print((2 ** 3) ** 2)    # 64


# Comparison happens before logical operators

print(5 > 3 and 2 < 4)  # True

print(not True or True) # True


# Clear expression using parentheses

result = (5 + 3) * (10 - 4)

print(result)            # 48


# ============================================================
# 9. QUICK OPERATOR SUMMARY
# ============================================================

"""
ARITHMETIC
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponentiation

COMPARISON
==  Equal
!=  Not equal
>   Greater than
<   Less than
>=  Greater than or equal
<=  Less than or equal

ASSIGNMENT
=   Assign
+=  Add
-=  Subtract
*=  Multiply
/=  Divide
//= Floor divide
%=  Modulus
**= Power

LOGICAL
and
or
not

BITWISE
&
|
^
~
<<
>>

MEMBERSHIP
in
not in

IDENTITY
is
is not
"""


print("\n=== End of Python Operators Notes ===")
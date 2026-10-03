# Python Operators

## Operator Types

| Operator Type | Symbols / Keywords                       |
| ------------- | ---------------------------------------- |
| Arithmetic    | `+` `-` `*` `/` `//` `%` `**`            |
| Comparison    | `==` `!=` `>` `<` `>=` `<=`              |
| Assignment    | `=` `+=` `-=` `*=` `/=` `//=` `%=` `**=` |
| Logical       | `and` `or` `not`                         |
| Bitwise       | `&` `\|` `^` `~` `<<` `>>`               |
| Membership    | `in` `not in`                            |
| Identity      | `is` `is not`                            |

---

## 1. Arithmetic Operators

| Symbol | Name           | Example       |
| ------ | -------------- | ------------- |
| `+`    | Addition       | `3 + 2 = 5`   |
| `-`    | Subtraction    | `10 - 3 = 7`  |
| `*`    | Multiplication | `3 * 4 = 12`  |
| `/`    | Division       | `7 / 2 = 3.5` |
| `//`   | Floor Division | `7 // 2 = 3`  |
| `%`    | Modulus        | `7 % 3 = 1`   |
| `**`   | Exponentiation | `2 ** 3 = 8`  |

### Example

```python
print(15 + 7)
print(15 - 7)
print(15 * 7)
print(7 / 2)
print(17 // 5)
print(17 % 5)
print(2 ** 10)
```

---

## 2. Comparison Operators

| Symbol | Meaning                  | Example  |
| ------ | ------------------------ | -------- |
| `==`   | Equal to                 | `5 == 5` |
| `!=`   | Not equal to             | `5 != 3` |
| `>`    | Greater than             | `7 > 3`  |
| `<`    | Less than                | `3 < 7`  |
| `>=`   | Greater than or equal to | `5 >= 5` |
| `<=`   | Less than or equal to    | `4 <= 5` |

Comparison operators return `True` or `False`.

### Example

```python
print(10 == 10)
print(10 != 5)
print(10 > 20)
print(3 < 7)
print(5 >= 5)
print(4 <= 5)
```

---

## 3. Assignment Operators

| Symbol | Name                    | Equivalent   |
| ------ | ----------------------- | ------------ |
| `=`    | Assign                  | `x = 5`      |
| `+=`   | Add and assign          | `x = x + 3`  |
| `-=`   | Subtract and assign     | `x = x - 2`  |
| `*=`   | Multiply and assign     | `x = x * 4`  |
| `/=`   | Divide and assign       | `x = x / 2`  |
| `//=`  | Floor divide and assign | `x = x // 3` |
| `%=`   | Modulus and assign      | `x = x % 2`  |
| `**=`  | Power and assign        | `x = x ** 2` |

### Example

```python
score = 50

score += 10
score *= 2
score -= 20

print(score)
```

---

## 4. Logical Operators

| Keyword | Meaning                                  |
| ------- | ---------------------------------------- |
| `and`   | True when both conditions are True       |
| `or`    | True when at least one condition is True |
| `not`   | Reverses the Boolean result              |

### Example

```python
age = 20
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

---

## 5. Bitwise Operators

| Symbol | Name        | Example  |
| ------ | ----------- | -------- |
| `&`    | Bitwise AND | `5 & 3`  |
| `\|`   | Bitwise OR  | `5 \| 3` |
| `^`    | Bitwise XOR | `5 ^ 3`  |
| `~`    | Bitwise NOT | `~5`     |
| `<<`   | Left Shift  | `5 << 1` |
| `>>`   | Right Shift | `5 >> 1` |

### Example

```python
print(bin(5))
print(bin(3))

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 1)
print(5 >> 1)
```

---

## 6. Membership Operators

| Keyword  | Meaning                          | Example              |
| -------- | -------------------------------- | -------------------- |
| `in`     | Checks if a value exists         | `"a" in "apple"`     |
| `not in` | Checks if a value does not exist | `"x" not in "apple"` |

### Example

```python
print("py" in "python")
print("Java" in "python")
print("z" not in "hello")
```

---

## 7. Identity Operators

| Keyword  | Meaning                                            | Example         |
| -------- | -------------------------------------------------- | --------------- |
| `is`     | Checks if two variables refer to the same object   | `x is None`     |
| `is not` | Checks if two variables refer to different objects | `x is not None` |

### Example

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
```

### Checking `None`

```python
x = None

print(x is None)
```

---

## Operator Precedence

Operator precedence determines the order in which Python evaluates operators.

| Rank | Operators                                               | Category                 |
| ---- | ------------------------------------------------------- | ------------------------ |
| 1    | `( )`                                                   | Parentheses              |
| 2    | `**`                                                    | Exponentiation           |
| 3    | `+x` `-x` `~x`                                          | Unary operators          |
| 4    | `*` `/` `//` `%`                                        | Multiplication, division |
| 5    | `+` `-`                                                 | Addition, subtraction    |
| 6    | `<<` `>>`                                               | Bitwise shifts           |
| 7    | `&`                                                     | Bitwise AND              |
| 8    | `^`                                                     | Bitwise XOR              |
| 9    | `\|`                                                    | Bitwise OR               |
| 10   | `==` `!=` `>` `<` `>=` `<=` `is` `is not` `in` `not in` | Comparisons              |
| 11   | `not`                                                   | Logical NOT              |
| 12   | `and`                                                   | Logical AND              |
| 13   | `or`                                                    | Logical OR               |

### Example

```python
print(2 + 3 * 4)
print((2 + 3) * 4)

print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
```

> **Golden Rule:** When you are unsure about operator precedence, use parentheses `( )` to make the order clear.

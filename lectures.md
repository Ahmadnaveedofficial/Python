# Python Lecture Notes

---

## 01-04-2026

## Conditional Statements

```python
if condition:
    # code

elif another_condition:
    # code

else:
    # code
```

---

## Function Syntax

```python
def function_name():
    # code
```

---

## Loops

### 1. Simple for loop

```python
for item in [1, 2, 3]:
    print(item)
```

---

### 2. for loop with range()

```python
for i in range(5):
    print(i)   # 0 to 4
```

- `range(start, end)` — end include nahi hota
- `range(start, end, step)` — start: kahan se, end: kahan tak, step: kitna increment/decrement

```python
for i in range(1, 6):
    print(i)   # 1 to 5

# Normal step
for i in range(1, 10, 2):
    print(i)   # Output: 1, 3, 5, 7, 9

# Reverse loop
for i in range(10, 0, -1):
    print(i)   # Output: 10 to 1
```

---

### 3. while loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## Data Structures

### 1. List

- Ordered hoti hai
- Change (modify) ho sakti hai
- `[ ]` use hota hai

```python
my_list = [1, 2, 3, "Ali"]
```

---

### 2. Tuple

- Ordered hoti hai
- Change nahi hoti (immutable)
- `( )` use hota hai

```python
my_tuple = (1, 2, 3, "Ali")
```

---

### 3. Dictionary

- Key-value pair hota hai (JSON jesa)
- `{ }` use hota hai

```python
my_dict = {
    "name": "Ali",
    "age": 20
}
```

---

### 4. Set

- Unordered hota hai
- Duplicate values allow nahi karta

```python
my_set = {1, 2, 3, 3, 4}
# Output: {1, 2, 3, 4}
```

---

## 08-04-2026

## Classes

```python
class Person:
    name = ""
    age = 0

p1 = Person()
p1.name = "Ali"
print(p1.name)
```

---

## Private Variable

```python
self.__name
```

---

## `__init__` (Initializer)

- Object banne ke baad run hota hai
- Values set karta hai

```python
class Person:
    def __init__(self, name):
        self.name = name
```

---

## `__new__` (Constructor)

- Object banne se pehle run hota hai

```python
class Person:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)
```

---

## `self`

- Current object ka reference hota hai

---

## Encapsulation

```python
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```

---

## Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass
```
# 🧠 NumPy Complete Notes (Basic to Intermediate)

## 🔰 1. Introduction

NumPy (Numerical Python) is a Python library used for fast numerical computations. It is mainly used for working with arrays and matrices.

---

## 📦 2. Import NumPy

```python
import numpy as np
```

---

## 🔢 3. Creating Arrays

### 1D Array

```python
a = np.array([1, 2, 3, 4])
```

### 2D Array

```python
b = np.array([[1, 2],
              [3, 4]])
```

---

## ⚙️ 4. Special Arrays

```python
np.zeros((2,2))   # all zeros
np.ones((3,3))    # all ones
np.eye(3)         # identity matrix
np.arange(0, 10, 2)  # sequence
np.linspace(0, 1, 5) # equal spacing
```

---

## 📏 5. Array Properties

```python
a.shape   # rows, columns
 a.ndim    # dimensions
 a.size    # total elements
 a.dtype   # data type
```

---

## 🔁 6. Reshape

```python
a = np.array([1,2,3,4,5,6])
b = a.reshape(2,3)
```

---

## ➕ 7. Basic Operations

```python
a + 2
a - 1
a * 2
a / 2
```

### Functions

```python
np.sum(a)
np.mean(a)
np.max(a)
np.min(a)
np.sqrt(a)
```

---

## 📌 8. Indexing & Slicing

### 1D

```python
a[0]
a[1:4]
```

### 2D

```python
b[0,1]
b[:,1]
```

---

## 🔄 9. Important Concepts

### Copy vs View

```python
b = a.copy()   # independent
c = a.view()   # shared memory
```

---

## 🔗 10. Concatenate & Split

```python
np.concatenate((a,b))
np.split(a, 2)
```

---

## 🎲 11. Random Numbers

```python
np.random.rand(3)
np.random.randint(1,10)
```

---

## 📊 12. Boolean Filtering

```python
a[a > 2]
```

---

## ⚡ 13. Matrix Multiplication

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

np.dot(A,B)
```

---

## 🧠 Summary

* NumPy = fast numerical computing
* Arrays are faster than lists
* Most important topics: shape, indexing, reshape, operations
* Broadcasting allows operations on different size arrays

---

## 🚀 Exam Focus

✔ Arrays creation
✔ Indexing & slicing
✔ reshape
✔ basic operations
✔ mean, sum, max
✔ broadcasting basics

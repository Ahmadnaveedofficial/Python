# 🐼 Pandas Complete Notes (Basic to Intermediate)

## 🔰 1. Introduction

Pandas is a Python library used for data analysis and manipulation. It is mainly used to work with structured data like tables (Excel-like data).

It has two main data structures:

* Series (1D)
* DataFrame (2D)

---

## 📦 2. Import Pandas

```python
import pandas as pd
```

---

## 📊 3. Series (1D Data Structure)

A Series is a one-dimensional labeled array.

```python
s = pd.Series([10, 20, 30, 40])
print(s)
```

### Custom Index

```python
s = pd.Series([10, 20, 30], index=['a','b','c'])
```

---

## 📋 4. DataFrame (2D Table)

A DataFrame is a table with rows and columns.

```python
data = {
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [20, 22, 21]
}

df = pd.DataFrame(data)
print(df)
```

---

## 👀 5. Viewing Data

```python
df.head()   # first 5 rows
df.tail()   # last 5 rows
df.info()   # summary of dataset
df.describe() # statistical summary
```

---

## 📌 6. Selecting Data

### Column Selection

```python
df["Name"]
```

---

### Row Selection

#### iloc (index based)

```python
df.iloc[0]
```

#### loc (label based)

```python
df.loc[0]
```

---

## 🔍 7. Filtering Data

```python
df[df["Age"] > 20]
```

---

## ➕ 8. Basic Operations

```python
df["Age"].mean()
df["Age"].max()
df["Age"].min()
df["Age"].sum()
```

---

## 🧹 9. Handling Missing Data

```python
df.isnull()   # check missing values
df.dropna()   # remove missing values
df.fillna(0)  # replace missing values
```

---

## ✏️ 10. Adding Columns

```python
df["Salary"] = [50000, 60000, 55000]
```

---

## ❌ 11. Removing Columns

```python
df.drop("Age", axis=1)
```

---

## 🔄 12. Sorting Data

```python
df.sort_values("Age")
```

---

## 📊 13. Group By (Basic Concept)

```python
df.groupby("Age").mean()
```

---

## 📥 14. File Handling (VERY IMPORTANT)

### Read CSV

```python
df = pd.read_csv("data.csv")
```

### Save CSV

```python
df.to_csv("output.csv", index=False)
```

---

## ⚡ 15. Pandas vs NumPy

| Pandas            | NumPy                   |
| ----------------- | ----------------------- |
| Works with tables | Works with arrays       |
| Data analysis     | Numerical computation   |
| Excel-like data   | Mathematical operations |

---

## 🧠 16. Key Exam Points

✔ Series vs DataFrame
✔ head(), tail(), info()
✔ Filtering data
✔ iloc vs loc
✔ Missing data handling
✔ CSV read/write

---

## 🚀 Quick Example

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 22]
})

print(df[df["Age"] > 20])
```

---

## 🎯 Final Summary

* Pandas = data analysis library
* Series = 1D data
* DataFrame = 2D table
* Filtering is very important
* CSV handling is widely used in real world

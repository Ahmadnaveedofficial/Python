📂 NumPy Fundamentals Guide 🚀Yeh guide NumPy ke basic concepts ko cover karti hai, beginner-friendly explanations aur code examples ke saath.🔰 Step 1: Import NumPySabse pehle library ko import karna hota hai. np ek standard alias hai jo puri industry mein use hota hai.Pythonimport numpy as np
🔢 Step 2: What is an Array?Array ek list ki tarah hota hai lekin yeh fast aur memory-efficient hota hai.1D Array (Vector)Pythona = np.array([1, 2, 3, 4])
print(a)
2D Array (Matrix)Pythonb = np.array([[1, 2],
              [3, 4]])
print(b)
📏 Step 3: Array PropertiesKisi bhi array ka structure samajhne ke liye ye properties use hoti hain:.shape: Array ka size (rows, columns)..ndim: Dimensions ki counting..size: Total number of elements.Pythona = np.array([1, 2, 3, 4])
print(a.shape)
print(a.ndim)
print(a.size)
⚙️ Step 4: Special ArraysZeroes, ones ya identity matrix generate karne ke shortcut methods:Pythonnp.zeros((2, 2))   # All zeros
np.ones((3, 3))    # All ones
np.eye(3)         # Identity matrix
🔁 Step 5: Range of Numbersarange function loop ki tarah numbers generate karta hai.Python# Start: 0, Stop: 10, Step: 2
np.arange(0, 10, 2) 
# Output: [0, 2, 4, 6, 8]
📊 Step 6: Mathematical OperationsNumPy mein calculations element-wise hoti hain (har number par alag se apply hoti hain).Pythona = np.array([1, 2, 3, 4])
print(a + 2) # [3, 4, 5, 6]
print(a * 2) # [2, 4, 6, 8]
📌 Step 7: Indexing & Slicing ✂️Array se specific data nikalne ka tareeka:MethodExampleDescriptionIndexinga[0]Single element access2D Indexingb[0, 1]Row 0, Column 1Slicinga[1:4]Range of elements (index 1 to 3)📊 Step 8: Built-in FunctionsMathematic calculations ke liye ready-made functions:a.sum(): Total jamaa.mean(): Average nikalnaa.max() / a.min(): Sabse bari/choti value🔥 Step 9: Reshaping (Crucial)Data ka structure change karne ke liye:Pythona = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3) # 1D ko 2D mein convert kar diya
⚡ Step 10: Random NumbersPythonnp.random.rand(3)        # 0 se 1 ke darmiyan random floats
np.random.randint(1, 10) # 1 se 10 ke darmiyan integer
🧠 Quick Summary (Cheat Sheet)✅ Array: High-speed list.✅ Shape: Dimensions ka size.✅ Slicing: Part of array select karna.✅ Reshape: Structure change karna.🚀 Practice TaskNiche diya gaya code run karke check karo:Pythona = np.array([1, 2, 3, 4, 5])
print("Add 10:", a + 10)
print("Index 2:", a[2])
print("Mean Value:", a.mean())
print("Reshaped:\n", a.reshape(5, 1))
Created with 💡 for Python Learning
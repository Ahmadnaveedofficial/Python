# Task 1:  
# A university wants to analyze the marks of students in different subjects to evaluate overall 
# class performance. 
# Task Requirements 
# 1. Create a NumPy array containing marks of 5 students in 4 subjects.  
# 2. Display:  
# o Total marks of each student  
# o Average marks of each student  
# o Highest marks in each subject  
# o Lowest marks in each subject  
# 3. Find:  
# o Student with highest total marks  
# o Subject with highest average score  
# 4. Add 5 bonus marks to all students using array operations. 

import numpy as np

marks = np.array([[85, 90, 78, 92],
                  [88, 76, 95, 80],
                  [90, 82, 88, 91],
                  [70, 85, 80, 89],
                  [92, 88, 84, 94]])

totalMarks = np.sum(marks, axis=1)
print("Total marks of each student:", totalMarks)

averageMarks = np.mean(marks, axis=1)
print("Average marks of each student:", averageMarks)

highestMarks = np.max(marks, axis=0)
print("Highest marks in each subject:", highestMarks)

lowestMarks = np.min(marks, axis=0)
print("Lowest marks in each subject:", lowestMarks)

studentWithHighestTotal = np.argmax(totalMarks)
print("Student with highest total marks: Student", studentWithHighestTotal)

averageScorePerSubject = np.mean(marks, axis=0)
subjectWithHighestAverage = np.argmax(averageScorePerSubject)
print("Subject with highest average score: Subject", subjectWithHighestAverage)

marksWithBonus = marks + 5
print("Marks after adding 5 bonus marks:\n", marksWithBonus)

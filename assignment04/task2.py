# Task 2:  
# A hospital stores patient records including age, disease, and treatment cost. The management 
# wants a summary report. 
# Task Requirements 
# 1. Create a Pandas DataFrame containing:  
# o Patient Name  
# o Age  
# o Disease  
# o Treatment Cost  
# 2. Perform the following operations:  
# o Display first 3 records  
# o Find average treatment cost  
# o Display patients older than 40  
# o Count patients suffering from each disease  
# o Sort data according to treatment cost  
# 3. Add a new column:  
# o “Discounted Bill” = 10% reduction in treatment cost


import pandas as pd
data = {
    'Patient Name': ['Ahmad', 'Mohsin', 'Ahsan', 'Ibrahim', 'Nawab'],
    'Age': [30, 45, 50, 35, 60],
    'Disease': ['Flu', 'Diabetes', 'Hypertension', 'Asthma', 'Arthritis'],
    'Treatment Cost': [200, 500, 300, 400, 600]
}
df = pd.DataFrame(data)
print("First 3 records: ")
print(df.head(3))
averageCost = df['Treatment Cost'].mean()
print("Average treatment cost: ", averageCost)
patientsOlderThan40 = df[df['Age'] > 40]
print("Patients older than 40: ", patientsOlderThan40)
diseaseCount = df['Disease'].value_counts()
print("Count of patients suffering from each disease: ", diseaseCount)
sortedByCost = df.sort_values(by='Treatment Cost')
print("Data sorted according to treatment cost: ", sortedByCost)
df['Discounted Bill'] = df['Treatment Cost'] * 0.9
print("Data with Discounted Bill:", df)


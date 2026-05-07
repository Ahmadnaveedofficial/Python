# Task 3: 
# A weather department records daily temperatures for a month and wants weather statistics. 
# Task Requirements 
# 1. Store temperature readings of 30 days in a NumPy array.  
# 2. Find:  
# o Maximum temperature  
# o Minimum temperature  
# o Average temperature  
# 3. Display all days where temperature exceeded 35°C.  
# 4. Convert Celsius temperatures to Fahrenheit using NumPy operations. 

import numpy as np

temperatures = np.random.randint(20, 40, size=30)
maxTemp = np.max(temperatures)
print("Maximum temperature: ", maxTemp)
minTemp=np.min(temperatures)
print("Minimun Temperature: ",minTemp)
averageTemp = np.mean(temperatures)
print("Average temperature: ", averageTemp)
daysExceeding35 = np.where(temperatures > 35)[0]
print("Days where temperature exceeded 35°C: ", daysExceeding35)
temperaturesFahrenheit = (temperatures * 9/5) + 32
print("Temperatures in Fahrenheit: ", temperaturesFahrenheit)

# Task 4:  
# A movie streaming platform wants to analyze user ratings. 
# Task Requirements 
# 1. Create a DataFrame containing:  
# o User Name  
# o Movie Name  
# o Rating  
# o Genre  
# 2. Perform:  
# o Average rating of each movie  
# o Highest rated movie  
# o Number of ratings genre-wise  
# o Display movies with rating greater than 4 

# Visualize ratings using charts (bonus). 

import pandas as pd
import matplotlib.pyplot as plt



data = {
    'User Name': ['Ahmad', 'Ahsan', 'Mohsin', 'Ibrahimm', 'Nawab'],
    'Movie Name': ['The Legend of Maula Jatt', 'Jawani Phir Nahi Ani', 'Punjab Nahi Jaungi', 'Actor in Law', 'Jawani Phir Nahi Ani 2'],
    'Rating': [5, 4, 5, 3, 4],          
    'Genre': ["Action", "Comedy","Drama","Romance","Comedy",]
}   

df = pd.DataFrame(data)
averageRating = df.groupby('Movie Name')['Rating'].mean()
print("Average rating of each movie: ", averageRating)
highestRatedMovie = df.loc[df['Rating'].idxmax()]['Movie Name']
print("Highest rated movie: ", highestRatedMovie)
ratingsGenreWise = df['Genre'].value_counts()
print("Number of ratings genre-wise: ", ratingsGenreWise)
moviesWithHighRating = df[df['Rating'] > 4]
print("Movies with rating greater than 4: ")
print(moviesWithHighRating)

# chart
plt.bar(df['Movie Name'], df['Rating'])
plt.xlabel('Movie Name')
plt.ylabel('Rating')
plt.title('User Ratings of Movies')
plt.xticks(rotation=45)
plt.show()


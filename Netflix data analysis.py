import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_data.csv")

print(df.head())


df['genres'] = df['genres'].str.split(', ')
df = df.explode('genres')
genre_counts = df['genres'].value_counts()
print(genre_counts)

plt.figure(figsize=(12, 8))
genre_counts.plot(kind='bar')
plt.title('Distribution of Genres in Netflix Content Library')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,10))

genre_counts.plot(kind='pie', autopct='%1.1f%%',startangle=140)

plt.title('distribution of genres in netflix content library')

plt.ylabel('')
plt.show()

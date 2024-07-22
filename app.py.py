import pandas as pd
import streamlit  as st
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_data.csv")

# Display the first few rows to understand the structure of the dataset
print(df.head())

# Analyze the dataset to determine the top 10 distribution
# Here, let's assume we're interested in the top 10 genres or categories
top_10_distribution = df['genres'].value_counts().head(10)
print(top_10_distribution)





# Bar chart
plt.figure(figsize=(10, 6))
top_10_distribution.plot(kind='bar')
plt.title('Top 10 Distribution of Genres')
plt.xlabel('genres')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
top_10_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Distribution of Genres')
plt.ylabel('')
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()



st.title('Netflix Data Analysis')

# Load the dataset
df = pd.read_csv('netflix_data.csv')

# Analyze the dataset to determine the top 10 distribution
top_10_distribution = df['genres'].value_counts().head(10)

# Create a sidebar for user input
chart_type = st.sidebar.selectbox('Select Chart Type', ['Bar Chart', 'Pie Chart'])

# Display the chart based on user selection
if chart_type == 'Bar Chart':
    st.write('### Top 10 Distribution of Genres (Bar Chart)')
    st.bar_chart(top_10_distribution)
elif chart_type == 'Pie Chart':
    st.write('### Top 10 Distribution of Genres (Pie Chart)')
    fig, ax = plt.subplots()
    top_10_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)
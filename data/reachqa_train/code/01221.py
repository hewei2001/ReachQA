import matplotlib.pyplot as plt

# Define industries and their respective percentage of AI applications
industries = [
    'Healthcare', 
    'Finance', 
    'Manufacturing', 
    'Transportation', 
    'Retail', 
    'Entertainment', 
    'Education', 
    'Agriculture'
]
ai_applications = [20, 15, 12, 10, 8, 15, 10, 10]  # Ensure total sums to 100%

# Define colors for each industry
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

# Define a small explode for some segments to emphasize them
explode = (0.1, 0, 0, 0, 0, 0.1, 0, 0)

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    ai_applications, labels=industries, autopct='%1.1f%%', startangle=90, colors=colors,
    explode=explode, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), shadow=True
)

# Draw a white circle at the center to transform the pie chart into a donut chart
ax.add_artist(plt.Circle((0, 0), 0.70, fc='white', edgecolor='white'))

# Add title and adjust fonts
plt.title('Distribution of AI Applications Across Industries (2030)', fontsize=16, weight='bold', pad=20)
plt.setp(autotexts, size=12, weight="bold", color='black')
plt.setp(texts, size=10)

# Add legend outside the donut chart
ax.legend(wedges, industries, title='Industries', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
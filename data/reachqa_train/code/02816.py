import matplotlib.pyplot as plt

# Define the age categories and their distribution
age_categories = ['13-17 years', '18-24 years', '25-34 years', '35-44 years', 
                  '45-54 years', '55-64 years', '65+ years']
subscriber_distribution = [10, 25, 30, 15, 10, 7, 3]

# Define colors for each age group slice
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700', '#FF6961', '#77DD77']

# Highlight the dominant age category slice (25-34 years)
explode = [0, 0, 0.1, 0, 0, 0, 0]

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    subscriber_distribution,
    labels=age_categories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)

# Customize the percentage labels
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

# Add a multi-line title for better readability
plt.title("Demographic Distribution\nof Online Streaming Subscribers in 2023", 
          fontsize=16, fontweight='bold', ha='center')

# Add a custom legend with the age categories
plt.legend(wedges, age_categories, title="Age Groups", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to ensure no overlaps
plt.tight_layout()

# Show the plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data for the sustainable fashion choices
categories = [
    'Organic Cotton', 
    'Recycled Materials', 
    'Upcycled Clothing', 
    'Fair Trade Fashion', 
    'Vegan Leather'
]
sizes = [30, 25, 20, 15, 10]  # Market share percentages
colors = ['#4CAF50', '#2196F3', '#FFC107', '#F44336', '#9C27B0']  # Distinct colors

# Data for the overlay line plot (interest trends over 12 months)
months = np.arange(1, 13)
interest_data = {
    'Organic Cotton': np.random.normal(loc=30, scale=5, size=12),
    'Recycled Materials': np.random.normal(loc=25, scale=5, size=12),
    'Upcycled Clothing': np.random.normal(loc=20, scale=5, size=12),
    'Fair Trade Fashion': np.random.normal(loc=15, scale=5, size=12),
    'Vegan Leather': np.random.normal(loc=10, scale=5, size=12)
}

# Create a figure with two subplots (one for the donut chart, one for the line plot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1, 1]})

# Donut pie chart
wedges, texts, autotexts = ax1.pie(sizes, labels=categories, autopct='%1.1f%%',
                                   startangle=90, colors=colors, wedgeprops=dict(width=0.3, edgecolor='white'))

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)

# Beautifying the pie chart
ax1.set_title('Sustainable Fashion:\nThe Rise of Eco-Friendly Choices in 2023', 
              fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight='bold', color='black')
plt.setp(texts, size=12, weight='bold')

# Add a legend
ax1.legend(wedges, categories, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Line plot for interest trends, matching the colors with the donut chart
for category, interest, color in zip(interest_data.keys(), interest_data.values(), colors):
    ax2.plot(months, interest, marker='o', label=category, color=color)

ax2.set_title('Interest Trends in Sustainable Fashion Choices (Over 12 Months)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(months)
ax2.set_xticklabels([f'Month {i}' for i in months], fontsize=10, rotation=45, ha='right')  # Rotating the labels to avoid overlap
ax2.set_yticks(np.arange(0, 41, 5))
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Months', fontsize=12)
ax2.set_ylabel('Interest Level (Arbitrary Units)', fontsize=12)
ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--')

# Add a legend and grid to the line plot
ax2.legend(title="Categories", fontsize=10)
ax2.grid(alpha=0.5)

# Final layout adjustments
plt.tight_layout(rect=[0, 0.03, 0.95, 0.95])

# Display the plots
plt.show()
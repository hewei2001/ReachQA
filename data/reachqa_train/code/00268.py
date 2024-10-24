import matplotlib.pyplot as plt
import numpy as np

# Data for caffeine content in different beverages (in mg)
beverages = ['Coffee', 'Tea', 'Energy Drinks', 'Soft Drinks', 'Chocolate']
caffeine_content = [95, 47, 80, 30, 9]  # average caffeine content in mg

# Colors with gradients for visual enhancement
colors = ['#7f3b08', '#b35806', '#d8b365', '#f6e8c3', '#c7eae5']

# Explode to highlight certain slices
explode = (0.1, 0, 0.15, 0, 0)

# Create subplots with a donut chart and a bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Pie (Donut) Chart with enhanced styling
wedges, texts, autotexts = ax1.pie(caffeine_content, labels=beverages, autopct='%1.1f%%', startangle=90,
                                   colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'},
                                   pctdistance=0.85, labeldistance=1.05)
for text in texts + autotexts:
    text.set_fontsize(10)
    text.set_color('darkblue')
ax1.set_title('Average Caffeine Content\nin Popular Beverages', fontsize=14, fontweight='bold', pad=20)

# Draw circle to transform pie chart into donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Bar Chart for comparison
ax2.bar(beverages, caffeine_content, color=colors, edgecolor='black')
ax2.set_title('Caffeine Content (mg)', fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel('Caffeine (mg)', fontsize=12)
ax2.set_xlabel('Beverage Types', fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate each bar with the caffeine content value
for i, v in enumerate(caffeine_content):
    ax2.text(i, v + 2, str(v) + ' mg', ha='center', va='bottom', fontweight='bold')

# Enhance layout
plt.tight_layout()

# Display the plot
plt.show()
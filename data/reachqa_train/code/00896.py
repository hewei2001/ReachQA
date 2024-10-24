import matplotlib.pyplot as plt
import numpy as np

# Define regions and academic fields
regions = ['North America', 'Europe', 'Asia', 'Rest of World']
fields = ['Science', 'Technology', 'Engineering', 'Arts', 'Mathematics']

# Data representing the investment (in billions) for each field in the respective regions
investments = np.array([
    [40, 45, 50, 20, 30],  # North America
    [30, 35, 40, 25, 20],  # Europe
    [50, 60, 45, 10, 25],  # Asia
    [20, 25, 30, 15, 15]   # Rest of World
])

# Calculate total investments by field across all regions
total_investments = investments.sum(axis=0)

# Define colors for each academic field
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create the ring chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Calculate the total investment for scaling percentage
total_investment_all = total_investments.sum()
field_percentages = (total_investments / total_investment_all) * 100

# Create the pie chart with a width for the ring effect
wedges, texts, autotexts = ax.pie(total_investments, autopct='%1.1f%%', startangle=140,
                                  colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'),
                                  pctdistance=0.85, textprops=dict(color="black", weight='bold'))

# Title of the chart
ax.set_title("Nurturing Minds:\nInvestment Distribution in Global Academic Fields", 
             fontsize=14, fontweight='bold', pad=20)

# Central label or title inside the ring
ax.text(0, 0, 'STEAM\nFunding', horizontalalignment='center', 
        verticalalignment='center', fontsize=12, fontweight='bold', color='gray')

# Adjust legend positioning
ax.legend(wedges, fields, title="Academic Fields", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# Annotate with the percentage values and prevent overlap by adjusting
for idx, (field, percent) in enumerate(zip(fields, field_percentages)):
    autotexts[idx].set_text(f'{percent:.1f}%')
    autotexts[idx].set_fontsize(9)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()
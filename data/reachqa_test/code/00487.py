import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2018, 2024)

# Brand awareness data
paid_ads = np.array([20, 25, 30, 35, 40, 45])
influencer_collabs = np.array([10, 15, 25, 30, 37, 50])
organic_content = np.array([5, 10, 15, 25, 30, 35])
engagement_campaigns = np.array([8, 12, 20, 28, 35, 45])

# Standard deviation for error bars
error = np.array([2, 3, 2, 4, 5, 3])  # Variability in brand awareness

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Fill area under lines
ax.fill_between(years, paid_ads, color='blue', alpha=0.1)
ax.fill_between(years, influencer_collabs, color='orange', alpha=0.1)
ax.fill_between(years, organic_content, color='green', alpha=0.1)
ax.fill_between(years, engagement_campaigns, color='red', alpha=0.1)

# Plotting the line chart with error bars
ax.errorbar(years, paid_ads, yerr=error, label='Paid Ads', marker='o', linestyle='-', 
             color='blue', capsize=5, alpha=0.7, linewidth=2)
ax.errorbar(years, influencer_collabs, yerr=error, label='Influencer Collabs', marker='s', 
             linestyle='--', color='orange', capsize=5, alpha=0.7, linewidth=2)
ax.errorbar(years, organic_content, yerr=error, label='Organic Content', marker='^', 
             linestyle='-.', color='green', capsize=5, alpha=0.7, linewidth=2)
ax.errorbar(years, engagement_campaigns, yerr=error, label='Engagement Campaigns', marker='x', 
             linestyle=':', color='red', capsize=5, alpha=0.7, linewidth=2)

# Adding titles and labels
plt.title('Impact of Social Media Marketing Strategies\non Brand Awareness (2018-2023)', 
          fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Brand Awareness (%)', fontsize=14)
plt.xticks(years, rotation=45)
plt.ylim(0, 60)

# Legend and grid
plt.legend(title='Marketing Strategies', loc='upper left', fontsize=10, frameon=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotations for key points (highlighting significant data)
ax.annotate('Peak Awareness', xy=(2023, 50), xytext=(2022, 55),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
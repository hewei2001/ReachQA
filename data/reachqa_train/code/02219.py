import matplotlib.pyplot as plt
import numpy as np

# Define the years and internet usage data for each age group
years = np.arange(2010, 2021)  # From 2010 to 2020

# Internet usage data (%) for each age group
youth_usage = [50, 55, 60, 68, 70, 75, 78, 80, 82, 85, 90]  # Youth (15-24 years)
adult_usage = [40, 45, 48, 50, 55, 60, 63, 66, 68, 70, 72]  # Adults (25-54 years)
senior_usage = [10, 12, 15, 18, 20, 23, 26, 28, 30, 32, 35]  # Seniors (55+ years)

# Stack the data for area plotting
internet_usage_data = np.vstack([youth_usage, adult_usage, senior_usage])

# Plotting the stacked area chart
fig, ax = plt.subplots(figsize=(12, 7))

ax.stackplot(years, internet_usage_data, labels=['Youth (15-24)', 'Adults (25-54)', 'Seniors (55+)'],
             colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.85)

# Adding title and labels with line breaks for better readability
ax.set_title('Tech Time Travelers:\nEvolution of Internet Usage Across Different Age Groups (2010-2020)', fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Internet Usage (%)', fontsize=14)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding a legend with a title
ax.legend(loc='upper left', title='Age Groups', fontsize=12, title_fontsize='13')

# Automatically adjust layout to prevent overlapping
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Add annotations for key points
ax.annotate('Youth surge', xy=(2015, 75), xytext=(2012, 80),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

ax.annotate('Senior growth', xy=(2020, 35), xytext=(2017, 45),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Display the plot
plt.show()
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

# Calculate growth rate for each age group as additional data
youth_growth_rate = np.gradient(youth_usage)
adult_growth_rate = np.gradient(adult_usage)
senior_growth_rate = np.gradient(senior_usage)

# Creating a figure with two subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})

# First subplot: Stacked area chart for internet usage
axs[0].stackplot(years, internet_usage_data, labels=['Youth (15-24)', 'Adults (25-54)', 'Seniors (55+)'],
                 colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.85)

axs[0].set_title('Tech Time Travelers:\nEvolution of Internet Usage Across Different Age Groups (2010-2020)', fontsize=14, fontweight='bold', loc='center')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Internet Usage (%)', fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend(loc='upper left', title='Age Groups', fontsize=10, title_fontsize='11')

axs[0].annotate('Youth surge', xy=(2015, 75), xytext=(2012, 85),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
axs[0].annotate('Senior growth', xy=(2020, 35), xytext=(2017, 45),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)

# Second subplot: Line plot for growth rate
axs[1].plot(years, youth_growth_rate, marker='o', label='Youth Growth Rate', color='#ff6666')
axs[1].plot(years, adult_growth_rate, marker='o', label='Adult Growth Rate', color='#6699ff')
axs[1].plot(years, senior_growth_rate, marker='o', label='Senior Growth Rate', color='#66ff66')

axs[1].set_title('Growth Rate of Internet Usage', fontsize=12)
axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Rate (%)', fontsize=12)
axs[1].legend(loc='upper left', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.6)

plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

plt.show()
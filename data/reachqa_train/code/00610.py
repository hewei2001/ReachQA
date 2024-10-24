import matplotlib.pyplot as plt
import numpy as np

# Original Data for Internet Usage
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
usage_0_18 = np.array([10, 15, 25, 35, 45, 60])
usage_19_35 = np.array([40, 50, 65, 75, 85, 90])
usage_36_50 = np.array([25, 30, 35, 45, 55, 65])
usage_51_65 = np.array([10, 15, 20, 25, 30, 35])
usage_66_plus = np.array([5, 7, 10, 13, 17, 20])

# Growth rate data calculated based on the original dataset
growth_0_18 = np.diff(usage_0_18, prepend=0)
growth_19_35 = np.diff(usage_19_35, prepend=0)
growth_36_50 = np.diff(usage_36_50, prepend=0)
growth_51_65 = np.diff(usage_51_65, prepend=0)
growth_66_plus = np.diff(usage_66_plus, prepend=0)

# Define labels and colors for each age group
age_groups = ['0-18', '19-35', '36-50', '51-65', '66+']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Internet Usage Analysis Over a Decade\nStacked Area Plot and Growth Rate Visualization', fontsize=18, fontweight='bold')

# First subplot: Stacked Area Plot
axs[0].stackplot(years, usage_0_18, usage_19_35, usage_36_50, usage_51_65, usage_66_plus,
                 labels=age_groups, colors=colors, alpha=0.8)
axs[0].set_title('Internet Usage by Age Group', fontsize=14)
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Internet Usage (% of Population)')
axs[0].legend(title='Age Group', fontsize=10, loc='upper left', bbox_to_anchor=(1.05, 1))
axs[0].grid(True, linestyle='--', alpha=0.5)

# Second subplot: Line Plot for Growth Rate
axs[1].plot(years, growth_0_18, marker='o', label='0-18', color='#ff9999')
axs[1].plot(years, growth_19_35, marker='o', label='19-35', color='#66b3ff')
axs[1].plot(years, growth_36_50, marker='o', label='36-50', color='#99ff99')
axs[1].plot(years, growth_51_65, marker='o', label='51-65', color='#ffcc99')
axs[1].plot(years, growth_66_plus, marker='o', label='66+', color='#c2c2f0')
axs[1].set_title('Growth Rate of Internet Usage', fontsize=14)
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Growth Rate (% Increase)')
axs[1].legend(title='Age Group', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Adjust layout to fit legends and title
plt.tight_layout(rect=[0, 0, 0.9, 0.95])

# Display the plot
plt.show()
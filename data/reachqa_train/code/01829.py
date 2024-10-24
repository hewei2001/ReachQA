import matplotlib.pyplot as plt
import numpy as np

# Screen time data in hours for different age groups
screen_time_data = {
    'Children (6-12)': [2, 3, 1.5, 4, 2.5, 3.5, 2.5, 4.5, 3],
    'Teenagers (13-19)': [5, 6.5, 7, 5.5, 6, 5.5, 6.5, 7.5, 6.5],
    'Young Adults (20-35)': [4, 5, 6, 4.5, 5, 4.5, 5.5, 6, 5],
    'Adults (36-60)': [3, 2.5, 2, 3.5, 4, 3, 2.5, 2, 3],
    'Seniors (60+)': [1.5, 2, 1, 2.5, 1.5, 2, 1.5, 1, 1.8]
}

# Synthetic data: Annual growth rate of screen time over a decade
growth_rate = {
    'Children (6-12)': [0.05, 0.06, 0.05, 0.07, 0.04, 0.05, 0.06, 0.07, 0.05, 0.06],
    'Teenagers (13-19)': [0.04, 0.05, 0.05, 0.06, 0.04, 0.05, 0.06, 0.06, 0.05, 0.06],
    'Young Adults (20-35)': [0.03, 0.04, 0.03, 0.04, 0.03, 0.04, 0.04, 0.04, 0.03, 0.04],
    'Adults (36-60)': [0.02, 0.02, 0.02, 0.03, 0.02, 0.03, 0.02, 0.02, 0.02, 0.03],
    'Seniors (60+)': [0.01, 0.02, 0.01, 0.02, 0.01, 0.02, 0.01, 0.01, 0.01, 0.02]
}

age_groups = list(screen_time_data.keys())
data_values = list(screen_time_data.values())
growth_values = list(growth_rate.values())

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Subplot 1: Box plot for screen time
boxprops = dict(facecolor='skyblue', color='darkblue')
whiskerprops = dict(color='darkblue', linestyle='--')
capprops = dict(color='darkblue')
flierprops = dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none')
medianprops = dict(color='black', linewidth=2)

axs[0].boxplot(data_values, vert=False, patch_artist=True, notch=True,
               boxprops=boxprops, whiskerprops=whiskerprops,
               capprops=capprops, flierprops=flierprops,
               medianprops=medianprops)
axs[0].set_yticklabels(age_groups)
axs[0].set_xlabel('Daily Screen Time (hours)', fontsize=12)
axs[0].set_title('Annual Screen Time Usage Across Different Age Groups\nin 2030', fontsize=14, fontweight='bold', pad=20)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Subplot 2: Line plot for growth rate
years = np.arange(2020, 2030)
for idx, group in enumerate(age_groups):
    axs[1].plot(years, growth_values[idx], marker='o', label=group)

axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Growth Rate', fontsize=12)
axs[1].set_title('Decadal Growth Rate of Screen Time\nAcross Age Groups', fontsize=14, fontweight='bold', pad=20)
axs[1].legend(loc='upper left')
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Define the eras
eras = ['1900-1940', '1940-1980', '1980-2000', '2000-2010', '2010-Present']

# Data for each communication medium in each era (units in millions of users)
letters = [100, 80, 60, 30, 10]
phone_calls = [5, 40, 80, 90, 70]
emails = [0, 5, 40, 100, 90]
instant_messaging = [0, 0, 5, 50, 100]
social_media = [0, 0, 0, 10, 120]

# Aggregated data
data = [letters, phone_calls, emails, instant_messaging, social_media]

# Labels for the mediums
medium_labels = ['Letters', 'Phone Calls', 'Emails', 'Instant Messaging', 'Social Media']

# Calculate percentage growth for the new subplot
def calculate_growth(data):
    growth = []
    for series in data:
        growth.append([((series[i] - series[i - 1]) / series[i - 1] * 100) if series[i - 1] != 0 else 0 for i in range(1, len(series))])
        growth[-1].insert(0, 0)  # Set the growth for the first era as 0
    return growth

growth_data = calculate_growth(data)

# Setting up the figure and axis
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the stacked histogram
axs[0].hist([np.arange(len(eras))] * len(data), bins=np.arange(len(eras) + 1), weights=data, 
            label=medium_labels, histtype='barstacked', alpha=0.8, edgecolor='black')

axs[0].set_title("The Evolution of Communication Mediums\nOver Different Eras", fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel("Era", fontsize=11)
axs[0].set_ylabel("Usage (Millions of Users)", fontsize=11)
axs[0].set_xticks(np.arange(len(eras)))
axs[0].set_xticklabels(eras, rotation=30, ha='right')
axs[0].legend(title="Mediums", fontsize=10, title_fontsize='11')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Plotting the line plot for percentage growth
for idx, medium in enumerate(growth_data):
    axs[1].plot(eras, medium, marker='o', label=medium_labels[idx], linewidth=2)

axs[1].set_title("Percentage Growth of Communication Mediums\nBetween Eras", fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel("Era", fontsize=11)
axs[1].set_ylabel("Growth Rate (%)", fontsize=11)
axs[1].legend(title="Mediums", fontsize=10, title_fontsize='11')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()
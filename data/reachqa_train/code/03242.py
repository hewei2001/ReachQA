import numpy as np
import matplotlib.pyplot as plt

# Define countries and years
countries = ['India', 'Brazil', 'USA', 'Japan', 'France']
years = np.arange(2013, 2024)  # From 2013 to 2023

# Participants data for each country
participants = {
    'India': [500, 520, 540, 580, 620, 680, 750, 800, 850, 900, 950],
    'Brazil': [300, 320, 350, 370, 390, 430, 470, 510, 540, 570, 590],
    'USA': [400, 430, 460, 500, 530, 560, 600, 650, 680, 720, 750],
    'Japan': [350, 370, 400, 430, 460, 490, 520, 560, 590, 620, 640],
    'France': [450, 470, 490, 510, 540, 570, 600, 630, 660, 700, 730]
}

# Convert to a list of arrays for easier plotting
participants_data = [np.array(participants[country]) for country in countries]

# Create a figure with subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Original Line Chart
axes[0].set_title("Annual Kite Festival Participation\n(2013-2023)", fontsize=14, fontweight='bold')
for idx, (country, data) in enumerate(participants.items()):
    marker_styles = ['o', 's', '^', 'D', 'x']
    line_styles = ['-', '--', '-.', ':', '-']
    color_styles = ['red', 'green', 'blue', 'orange', 'purple']
    axes[0].plot(years, data, marker=marker_styles[idx], linestyle=line_styles[idx], color=color_styles[idx], label=country, linewidth=2)

axes[0].set_xlabel("Year", fontsize=12)
axes[0].set_ylabel("Number of Participants", fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(years, rotation=45)
axes[0].set_yticks(np.arange(0, 1001, 100))
axes[0].grid(True, linestyle='--', alpha=0.7)
axes[0].legend(title='Countries', loc='upper left', fontsize=10)

# Annotate peak participation for India
max_participants_india = max(participants['India'])
max_year_india = years[participants['India'].index(max_participants_india)]
axes[0].annotate(f'Peak: {max_participants_india}', xy=(max_year_india, max_participants_india),
                 xytext=(max_year_india - 1, max_participants_india + 50),
                 arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# New Stacked Area Chart
axes[1].set_title("Contribution to Total Participants Over Years", fontsize=14, fontweight='bold')
axes[1].stackplot(years, participants_data, labels=countries, colors=color_styles, alpha=0.8)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Total Participants", fontsize=12)
axes[1].set_xticks(years)
axes[1].set_xticklabels(years, rotation=45)
axes[1].legend(loc='upper left', fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
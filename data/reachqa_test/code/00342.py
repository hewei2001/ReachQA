import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
sports = ['Skiing', 'Snowboarding', 'Ice Skating', 'Ice Hockey', 'Sledding']
participation = np.array([320, 210, 185, 160, 140])  # Participation in thousands
expenditure = np.array([420, 340, 300, 280, 200])    # Average expenditure per participant in dollars

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar chart for participation
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = ax1.bar(sports, participation, color=colors, width=0.6, alpha=0.9, edgecolor='grey')

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}K',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5),
                 textcoords='offset points',
                 ha='center', va='bottom', fontsize=11, fontweight='bold')

# Adding titles and labels
ax1.set_title('The Most Popular Winter Sports in the Alpine Region\nLast Winter Season', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Participants (in thousands)', fontsize=12)

# Secondary y-axis for expenditure
ax2 = ax1.twinx()
ax2.plot(sports, expenditure, color='darkgreen', marker='o', linestyle='-', linewidth=2, markersize=8, label='Average Expenditure')
ax2.set_ylabel('Average Expenditure (in dollars)', fontsize=12, color='darkgreen')
ax2.tick_params(axis='y', labelcolor='darkgreen')

# Highlight highest participation bar
highest_participation_bar = bars[np.argmax(participation)]
highest_participation_bar.set_edgecolor('gold')
highest_participation_bar.set_linewidth(2)

# Customize the grid
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)
ax1.set_axisbelow(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=20, ha='right')

# Legend
ax2.legend(loc='upper left', bbox_to_anchor=(0.75, 1))

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Expanded SAT score data for fictional universities, with added complexity
university_data = {
    "Univ A": [1250, 1300, 1350, 1370, 1400, 1420, 1450, 1470, 1500, 1520, 1550, 1575],
    "Univ B": [1100, 1150, 1170, 1200, 1230, 1250, 1280, 1300, 1320, 1350, 1400],
    "Univ C": [1400, 1450, 1470, 1500, 1520, 1550, 1570, 1600, 1600, 1620],
    "Univ D": [1000, 1050, 1100, 1150, 1180, 1200, 1250, 1270],
    "Univ E": [1300, 1350, 1400, 1420, 1450, 1470, 1500, 1520, 1550, 1570, 1600, 1650],
    "Univ F": [1050, 1080, 1120, 1150, 1170, 1190, 1220, 1240, 1260],
    "Univ G": [1340, 1370, 1400, 1420, 1450, 1470, 1500, 1520, 1550, 1570, 1590]
}

# Acceptance rates (fictional)
acceptance_rates = {
    "Univ A": 0.25,
    "Univ B": 0.35,
    "Univ C": 0.20,
    "Univ D": 0.40,
    "Univ E": 0.15,
    "Univ F": 0.50,
    "Univ G": 0.30
}

# Extract university names and SAT scores
universities = list(university_data.keys())
scores = [university_data[uni] for uni in universities]
mean_scores = [np.mean(university_data[uni]) for uni in universities]
acceptance = [acceptance_rates[uni] * 100 for uni in universities]  # Convert to percentage

# Set up the figure and axis for box and line plots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Create the box plot
boxprops = dict(linestyle='-', linewidth=1.5, color='black', facecolor='lightblue', alpha=0.6)
whiskerprops = dict(linestyle='--', linewidth=1.5)
capprops = dict(linewidth=1.5)
medianprops = dict(linestyle='-', linewidth=2, color='firebrick')
ax1.boxplot(scores, vert=True, patch_artist=True, labels=universities,
            boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops)

# Additional plot for acceptance rates
ax2 = ax1.twinx()
ax2.plot(universities, acceptance, color='green', marker='o', linewidth=2, linestyle='--', label='Acceptance Rate (%)')

# Highlight mean scores
ax1.plot(range(1, len(universities) + 1), mean_scores, color='purple', marker='D', linestyle='-', linewidth=2, label='Mean SAT Score')

# Title and labels
ax1.set_title("SAT Score Distribution and Acceptance Rates \nfor University Applications", fontsize=16, color='navy', pad=30)
ax1.set_xlabel("Universities", fontsize=12)
ax1.set_ylabel("SAT Scores", fontsize=12, color='black')
ax2.set_ylabel("Acceptance Rate (%)", fontsize=12, color='green')

# Create legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()
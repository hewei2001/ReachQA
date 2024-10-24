import matplotlib.pyplot as plt
import numpy as np

# Data representing the number of active users in thousands over six months
months = ['January', 'February', 'March', 'April', 'May', 'June']
lingua_leap_users = [50, 55, 60, 70, 80, 90]
verbal_virtue_users = [40, 42, 45, 48, 52, 60]
polyglot_pathway_users = [30, 33, 35, 40, 50, 60]
lexicon_labs_users = [20, 25, 28, 35, 42, 50]

# Calculate percentage growth for each platform
lingua_leap_growth = ((lingua_leap_users[-1] - lingua_leap_users[0]) / lingua_leap_users[0]) * 100
verbal_virtue_growth = ((verbal_virtue_users[-1] - verbal_virtue_users[0]) / verbal_virtue_users[0]) * 100
polyglot_pathway_growth = ((polyglot_pathway_users[-1] - polyglot_pathway_users[0]) / polyglot_pathway_users[0]) * 100
lexicon_labs_growth = ((lexicon_labs_users[-1] - lexicon_labs_users[0]) / lexicon_labs_users[0]) * 100

growth_percentages = [
    lingua_leap_growth, verbal_virtue_growth,
    polyglot_pathway_growth, lexicon_labs_growth
]
platforms = ['LinguaLeap', 'VerbalVirtue', 'PolyglotPathway', 'LexiconLabs']

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot the line chart
ax1 = axs[0]
ax1.plot(months, lingua_leap_users, marker='o', linestyle='-', color='mediumseagreen', linewidth=2, label='LinguaLeap')
ax1.plot(months, verbal_virtue_users, marker='s', linestyle='--', color='dodgerblue', linewidth=2, label='VerbalVirtue')
ax1.plot(months, polyglot_pathway_users, marker='^', linestyle='-.', color='crimson', linewidth=2, label='PolyglotPathway')
ax1.plot(months, lexicon_labs_users, marker='d', linestyle=':', color='darkorange', linewidth=2, label='LexiconLabs')

ax1.set_title('Accelerating Fluency:\nGrowth Trends in Language Learning Platforms - 2023', fontsize=14, fontweight='bold')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Active Users (Thousands)', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(loc='upper left', fontsize=10, title='Platforms', title_fontsize='13')

def annotate_data(x, y, color, ax):
    for i, txt in enumerate(y):
        ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=9, color=color)

annotate_data(np.arange(len(months)), lingua_leap_users, 'mediumseagreen', ax1)
annotate_data(np.arange(len(months)), verbal_virtue_users, 'dodgerblue', ax1)
annotate_data(np.arange(len(months)), polyglot_pathway_users, 'crimson', ax1)
annotate_data(np.arange(len(months)), lexicon_labs_users, 'darkorange', ax1)

# Plot the bar chart
ax2 = axs[1]
colors = ['mediumseagreen', 'dodgerblue', 'crimson', 'darkorange']
ax2.bar(platforms, growth_percentages, color=colors)
ax2.set_title('Percentage Growth from January to June 2023', fontsize=14, fontweight='bold')
ax2.set_ylabel('Growth Percentage (%)', fontsize=12)

# Annotate each bar with the growth percentage
for i, v in enumerate(growth_percentages):
    ax2.text(i, v + 1, f"{v:.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
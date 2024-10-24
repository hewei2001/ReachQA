import matplotlib.pyplot as plt
import numpy as np

# Define data: distribution of programming languages in percentage
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go', 'Kotlin']
language_shares = [35, 25, 15, 10, 5, 5, 5]

# Additional data: growth rate in percentage
growth_rates = [5, 2, 3, 1, -1, 4, 3]

# Define colors for each language
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Set up the figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

# Create the ring chart
wedges, texts, autotexts = ax1.pie(
    language_shares,
    labels=languages,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)
ax1.text(0, 0, '2023\nSurvey', horizontalalignment='center', 
         verticalalignment='center', fontsize=14, fontweight='bold', color='black')
ax1.axis('equal')
plt.setp(autotexts, size=11, weight="bold", color="white")
plt.setp(texts, size=13)
ax1.set_title('Programming Language Usage in Software Projects\nSurveyed in 2023', fontsize=14, fontweight='bold')
ax1.legend(wedges, languages, title="Languages", loc='center left', bbox_to_anchor=(1.1, 0, 0.5, 1))

# Create the bar chart
x_pos = np.arange(len(languages))
ax2.bar(x_pos, growth_rates, color=colors, alpha=0.7)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(languages, rotation=45, ha="right")
ax2.set_ylabel('Growth Rate (%)')
ax2.set_xlabel('Programming Languages')
ax2.set_title('Growth Rate of Programming Languages in the Past Year', fontsize=14, fontweight='bold')
for i, v in enumerate(growth_rates):
    ax2.text(x_pos[i], v + 0.2 if v >= 0 else v - 0.5, f"{v}%", ha='center', fontweight='bold')

# Adjust layout to avoid overlap and ensure clarity
plt.tight_layout()

# Display the charts
plt.show()
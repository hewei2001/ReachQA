import matplotlib.pyplot as plt

# Define data: distribution of programming languages in percentage
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Go', 'Kotlin']
language_shares = [35, 25, 15, 10, 5, 5, 5]

# Define colors for each language
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Set up the figure
fig, ax = plt.subplots(figsize=(9, 9))

# Create the ring chart with wedgeprops to define a ring (donut) style
wedges, texts, autotexts = ax.pie(
    language_shares, 
    labels=languages, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add a central label inside the ring
ax.text(0, 0, '2023\nSurvey', horizontalalignment='center', 
        verticalalignment='center', fontsize=14, fontweight='bold', color='black')

# Equal aspect ratio ensures that the chart is circular
ax.axis('equal')

# Customize the text properties for better readability
plt.setp(autotexts, size=11, weight="bold", color="white")
plt.setp(texts, size=13)

# Add a title to the chart with a line break
plt.title('Programming Language Usage in Software Projects\nSurveyed in 2023', fontsize=16, fontweight='bold')

# Add a legend for clarification and position it outside the ring
ax.legend(wedges, languages, title="Languages", loc='center left', bbox_to_anchor=(1.1, 0, 0.5, 1))

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the ring chart
plt.show()
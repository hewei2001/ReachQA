import matplotlib.pyplot as plt

# Define energy sources and their projected contributions in 2050
energy_sources = ['Solar Power', 'Wind Power', 'Hydropower', 'Biomass Energy', 'Geothermal Energy', 'Ocean Energy']
energy_contribution = [35, 30, 15, 10, 7, 3]  # Hypothetical percentages

# Define colors for each energy source
colors = ['#FFD700', '#87CEEB', '#4682B4', '#8FBC8F', '#DEB887', '#20B2AA']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    energy_contribution,
    labels=energy_sources,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='white'),
    explode=(0.1, 0, 0, 0, 0, 0)  # Slightly explode the Solar Power sector for emphasis
)

# Customize the autotexts (percentages) on pie wedges
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Adjust labels to ensure they don't overlap
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('normal')

# Add a title
ax.set_title(
    "Future Energy Sources:\nGlobal Distribution of Renewable Energy Potential in 2050",
    fontsize=14, fontweight='bold'
)

# Add a legend
ax.legend(
    wedges, energy_sources,
    title="Energy Sources", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10, title_fontsize='11'
)

# Enhance the plot with a small circle in the middle for a donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
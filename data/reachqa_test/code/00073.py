import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data: Solar energy installation percentages by continent
continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']
installations = [40, 25, 15, 10, 7, 3]  # in percentage

# Define gradient colors for each continent
gradient_colors = ['#FFA07A', '#FF7F50', '#FF4500', '#FFD700', '#FF6347', '#40E0D0']

# Define explode settings for highlighting a specific continent (e.g., Asia)
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart with shadow for depth
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(installations, labels=continents, autopct='%1.1f%%', startangle=140,
                                  colors=gradient_colors, explode=explode, wedgeprops=dict(edgecolor='w'), shadow=True)

# Customize the title with multi-line
plt.title("Solar Energy Adoption Worldwide (2023)\nA Continental Overview of Solar Installations", fontsize=16, fontweight='bold')

# Set percentage and absolute values as labels
absolute_values = [f'{val*sum(installations)/100} GW' for val in installations]
for i, a in enumerate(autotexts):
    a.set_text(f"{a.get_text()}\n({absolute_values[i]})")
    a.set_fontsize(10)
    a.set_weight("bold")

# Add annotations for highest and lowest segments
ax.annotate('Highest Adoption', xy=(wedges[0].theta2 / 360.0, 0.5), xytext=(0.8, 0.8),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')
ax.annotate('Lowest Adoption', xy=(wedges[-1].theta2 / 360.0, -0.5), xytext=(-0.8, -0.8),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center')

# Add customized legend
legend_elements = [mpatches.Patch(color=gradient_colors[i], label=f"{continents[i]} ({installations[i]}%)") for i in range(len(continents))]
plt.legend(handles=legend_elements, title="Continents", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Draw a circle at the center to make it a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is drawn as a circle
ax.axis('equal')

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()
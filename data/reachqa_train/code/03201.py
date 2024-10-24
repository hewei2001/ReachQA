import matplotlib.pyplot as plt
import numpy as np

# Define renewable energy sources and their production percentages
sources = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']
percentages = [30, 25, 20, 15, 10]

# Define hypothetical growth rates for a second visualization
growth_rates = [5, 3, 4, 2, 3]  # Hypothetical annual growth rates in %

# Define colors for each segment
colors = ['#FFD700', '#1E90FF', '#32CD32', '#FF8C00', '#8B4513']

# Create a subplot layout with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# First subplot - Donut Chart
wedges, texts, autotexts = axs[0].pie(percentages, labels=sources, autopct='%1.1f%%',
                                      startangle=90, colors=colors, wedgeprops=dict(width=0.4),
                                      explode=[0.05]*5, shadow=True)

# Add a circle in the middle to create a 'donut' appearance
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
axs[0].add_artist(centre_circle)
axs[0].set_title('Renewable Energy Production by Source\nin Energia for the Year 2023',
                 fontsize=14, fontweight='bold', color='navy', pad=20)
plt.setp(autotexts, size=10, weight="bold", color="black")
axs[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
axs[0].legend(wedges, sources, title="Energy Sources", loc="center left", bbox_to_anchor=(0.9, 0, 0.5, 1))

# Second subplot - Bar Chart for Growth Rates
bars = axs[1].bar(sources, growth_rates, color=colors, alpha=0.7)
axs[1].set_title('Annual Growth Rates of Renewable Energy\nSources in Energia for 2023',
                 fontsize=14, fontweight='bold', color='navy')
axs[1].set_ylabel('Growth Rate (%)')
axs[1].set_ylim(0, 10)

# Add value annotations on each bar
for bar in bars:
    yval = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom', fontweight='bold')

# Adjust layout to prevent overlap and ensure all elements are clearly visible
plt.tight_layout()

# Display the plot
plt.show()
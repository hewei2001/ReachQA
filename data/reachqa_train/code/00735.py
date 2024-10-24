import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Wind energy output for each country (GWh)
denmark_output = np.array([300, 320, 340, 360, 380, 400, 390, 370, 350, 330, 310, 300])
sweden_output = np.array([250, 260, 270, 290, 310, 330, 320, 300, 280, 260, 250, 240])
norway_output = np.array([200, 210, 230, 240, 250, 260, 250, 240, 230, 220, 210, 200])
finland_output = np.array([150, 160, 170, 180, 190, 200, 190, 180, 170, 160, 150, 140])

# Data for the rose chart
country_outputs = [denmark_output, sweden_output, norway_output, finland_output]
country_names = ['Denmark', 'Sweden', 'Norway', 'Finland']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create rose chart
angles = np.linspace(0, 2 * np.pi, len(months), endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the rose chart

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})

# Plot each country's wind energy output
for idx, (output, color) in enumerate(zip(country_outputs, colors)):
    values = np.append(output, output[0])
    ax.plot(angles, values, color=color, linewidth=2, linestyle='-', label=country_names[idx])
    ax.fill(angles, values, color=color, alpha=0.25)

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(months, fontsize=10)
ax.set_title("Wind Energy Output Distribution\nAcross Nordic Countries", size=16, weight='bold', pad=20)

# Add a legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()
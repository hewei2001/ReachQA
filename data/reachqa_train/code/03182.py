import matplotlib.pyplot as plt

# Define the futuristic transportation modes and their projected market shares
transport_modes = [
    "Hyperloop Networks",
    "Flying Taxis",
    "Autonomous EVs",
    "Personal Drones",
    "Magnetic Levitation Trains"
]

market_shares = [25, 20, 30, 15, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Slightly "explode" the Autonomous EVs sector to highlight it
explode = (0, 0, 0.1, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Add a pie chart with the specified explode, colors, and labels
wedges, texts, autotexts = ax.pie(
    market_shares, explode=explode, colors=colors, labels=transport_modes,
    autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})

# Customize the title with line breaks for readability
plt.title("The Future of Urban Transport\nin Futureopolis: Market Shares in 2050", fontsize=16, fontweight='bold', pad=20)

# Format the auto-text inside the pie sectors for better readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Customize legend outside the plot to avoid occlusion
ax.legend(wedges, transport_modes, title="Transportation Modes", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to make room for the legend
plt.tight_layout()

# Display the pie chart
plt.show()
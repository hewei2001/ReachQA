import matplotlib.pyplot as plt

# Define the data for different transportation modes
transport_modes = ['Cars', 'Electric Vehicles', 'Public Transit', 'Bicycles', 'Walking', 'Others']
mode_shares = [35, 15, 25, 10, 10, 5]  # Percentage of total transportation

# Define colors for the pie chart slices
colors = ['#8B0000', '#228B22', '#1E90FF', '#FFD700', '#FF6347', '#808080']

# Create an "explode" effect to emphasize Electric Vehicles
explode = (0, 0.1, 0, 0, 0, 0)

# Create a pie chart with shadow effect
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(mode_shares, labels=transport_modes, colors=colors, explode=explode,
                                  autopct='%1.1f%%', startangle=140, shadow=True)

# Customize the autotexts
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')
    autotext.set_fontsize(10)

# Add a title with line breaks for clarity
ax.set_title("Global Transportation Modal Split:\nThe Green Shift of 2023", fontsize=16, fontweight='bold')

# Create a legend and position it outside the pie chart
ax.legend(wedges, transport_modes, title="Modes of Transportation", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
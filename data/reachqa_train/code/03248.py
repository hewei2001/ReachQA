import matplotlib.pyplot as plt
import numpy as np

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
explode = (0, 0, 0.1, 0, 0)

# Create a 2D figure
fig, ax = plt.subplots(figsize=(12, 8))

# Create the pie chart
wedges, texts, autotexts = ax.pie(market_shares, explode=explode, labels=transport_modes, colors=colors,
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.85, shadow=True)

# Customize the title with line breaks
plt.title("The Future of Urban Transport\nin Futureopolis: Market Shares in 2050", 
          fontsize=16, fontweight='bold', pad=30)

# Improve appearance by setting properties of text objects
for text in autotexts:
    text.set_color('black')

# Add annotation for more detailed insight
annot = ax.text(0, 0, '', ha="center", va="center", fontsize=10, color="black")

def update_annot(wedge, mode):
    angle = (wedge.theta2 + wedge.theta1) / 2
    annot.xy = (0.5 * np.cos(np.radians(angle)), 0.5 * np.sin(np.radians(angle)))
    annot.set_text(f"{mode}: {wedge.theta2 - wedge.theta1:.1f} degrees")

def hover(event):
    for wedge, mode in zip(wedges, transport_modes):
        if wedge.contains_point([event.x, event.y], radius=1.5):
            update_annot(wedge, mode)
            annot.set_visible(True)
            fig.canvas.draw_idle()
            break
    else:
        annot.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

# Customizing legend outside the plot
ax.legend(wedges, transport_modes, loc="center left", bbox_to_anchor=(1.05, 0.5), title="Transportation Modes")

# Adjust layout
plt.tight_layout()

# Display the pie chart
plt.show()
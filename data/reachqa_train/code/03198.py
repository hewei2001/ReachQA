import matplotlib.pyplot as plt

# Data: Smartphone Market Share in 2023
manufacturers = ['Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO', 'Others']
market_shares = [25, 22, 15, 13, 10, 15]

# Colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(market_shares, labels=manufacturers, autopct='%1.1f%%', startangle=90, colors=colors, 
                                  pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w'), explode=[0.05]*len(manufacturers),
                                  shadow=True)

# Draw the center circle to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Customization for the labels
for text in texts:
    text.set_fontsize(11)
    text.set_color('grey')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Title and Layout
plt.title('Global Smartphone Market Share\nin 2023', fontsize=16, fontweight='bold', pad=20)
ax.axis('equal')  # Ensure the pie chart is circular
plt.legend(wedges, manufacturers, title="Manufacturers", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()
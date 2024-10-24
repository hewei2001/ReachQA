import matplotlib.pyplot as plt
import squarify

# Revenue data for different product divisions (in million dollars)
divisions = [
    'Cloud Services', 'AI Solutions', 'Software Applications',
    'Consumer Electronics', 'Cybersecurity', 'IoT Devices',
    'Blockchain Technology', 'E-Commerce Platforms'
]
revenues = [450, 320, 380, 290, 210, 180, 145, 115]

# Hypothetical growth rate data for each division (in percentage)
growth_rates = [12, 8, 10, 5, 7, 6, 4, 3]

# Colors for both plots
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99',
          '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ffccf0']

# Create subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Treemap plot
squarify.plot(
    ax=ax1,
    sizes=revenues,
    label=[f"{div}\n${rev}M" for div, rev in zip(divisions, revenues)],
    color=colors,
    alpha=0.85,
    pad=3,
    text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'black'}
)
ax1.set_title("Tech Titan's Digital Product Portfolio:\nRevenue Breakdown for 2023",
              fontsize=14, fontweight='bold', pad=20)
ax1.axis('off')

# Bar chart plot
ax2.bar(divisions, growth_rates, color=colors, alpha=0.85)
ax2.set_title('Year-over-Year Growth Rates\n(Estimated)', fontsize=14, fontweight='bold', pad=10)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_xlabel('Product Divisions', fontsize=12)
ax2.set_xticklabels(divisions, rotation=45, ha='right', fontsize=10)

# Adjust layout for better fit and avoid text overlapping
plt.tight_layout()

# Display the plot
plt.show()
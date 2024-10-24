import matplotlib.pyplot as plt
import numpy as np

# Original data for the bar chart
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
movies = ["Enchanted Dawn", "Mystic Warriors", "Dragon's Quest", 
          "Sorcerer's Secret", "Realm of Shadows", "Cursed Fate"]
earnings = np.array([150, 200, 250, 220, 300, 270])  # Earnings in millions USD

# Additional data for the new subplot (e.g., average ticket prices)
average_ticket_price = np.array([8, 9, 9.5, 9.7, 10, 10.5])  # Prices in USD

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle("Box Office Performance and Ticket Trends\nfor the Enchanted Series (2010-2020)", 
             fontsize=16, fontweight='bold', y=1.05)

# Bar chart for earnings
axes[0].bar(years, earnings, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6'], 
            edgecolor='gray', width=1.5)
axes[0].set_title("Earnings", fontsize=14, pad=10)
axes[0].set_xlabel("Release Year", fontsize=12)
axes[0].set_ylabel("Earnings (Million USD)", fontsize=12)
axes[0].set_xticks(years)
axes[0].set_xticklabels(movies, rotation=45, ha='right')

# Annotate earnings bars
for bar, earning in zip(axes[0].patches, earnings):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                 f'{earning}M', ha='center', va='bottom', fontsize=10, color='darkslategray')

# Add gridlines
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Line plot for average ticket price
axes[1].plot(years, average_ticket_price, marker='o', linestyle='-', color='teal')
axes[1].set_title("Average Ticket Price", fontsize=14, pad=10)
axes[1].set_xlabel("Year", fontsize=12)
axes[1].set_ylabel("Price (USD)", fontsize=12)
axes[1].set_xticks(years)
axes[1].set_xticklabels(movies, rotation=45, ha='right')

# Annotate ticket prices
for (year, price) in zip(years, average_ticket_price):
    axes[1].text(year, price + 0.1, f'${price:.1f}', ha='center', fontsize=10, color='brown')

# Gridlines for the line plot
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
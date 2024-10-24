import matplotlib.pyplot as plt
import numpy as np

# Define the years and corresponding number of internet users in billions
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]
internet_users = [0.003, 0.01, 0.04, 0.17, 0.36, 0.67, 1.21, 2.50, 3.50, 4.20]

# Significant milestones and their annotations
milestones = {
    1995: "Emergence\nof Websites",
    2000: "Dot-com\nBubble Burst",
    2005: "Web 2.0 &\nSocial Media Rise",
    2010: "Mobile\nInternet Boom",
    2015: "Streaming &\nCloud Services"
}

# Create the plot
plt.figure(figsize=(12, 8))
plt.plot(years, internet_users[:7], marker='o', linestyle='-', color='b', linewidth=2)  # Only use the first 7 values

# Annotate milestones on the chart
for year, description in milestones.items():
    users = internet_users[list(years).index(year)]
    plt.annotate(f'{year}: {description}', xy=(year, users), xytext=(20, 20),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray'),
                 fontsize=10, color='darkblue')

# Set plot title and labels
plt.title("Evolution of Global Internet Usage\nFrom 1990 to 2020", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Internet Users (Billions)", fontsize=14)

# Customizing x and y axis ticks
plt.xticks(np.arange(1990, 2021, 5), fontsize=12)
plt.yticks(np.arange(0, 5, 0.5), fontsize=12)

# Grid and layout adjustments for clarity
plt.grid(True, linestyle='--', alpha=0.6)

# Improve layout aesthetics
plt.tight_layout()

# Display the plot
plt.show()
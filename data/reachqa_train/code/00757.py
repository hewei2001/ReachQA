import matplotlib.pyplot as plt
import numpy as np

# Define decades and communication technologies
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
technologies = ['Radio', 'Television', 'Internet', 'Social Media']

# Estimated percentage of media consumption by technology over the decades
media_consumption = np.array([
    [80, 20, 0, 0],    # 1960s: Dominated by Radio
    [60, 40, 0, 0],    # 1970s: Rise of Television
    [40, 50, 10, 0],   # 1980s: Television gains, Internet emerges
    [30, 40, 30, 0],   # 1990s: Internet begins to take hold
    [20, 30, 40, 10],  # 2000s: Internet overtakes, Social Media emerges
    [10, 20, 50, 20],  # 2010s: Internet domination, Social Media grows
    [5, 10, 50, 35]    # 2020s: Internet and Social Media leading
])

# Create a stacked area chart
plt.figure(figsize=(12, 7))
colors = ['#FFD700', '#FF4500', '#1E90FF', '#32CD32']
plt.stackplot(decades, media_consumption.T, labels=technologies, colors=colors, alpha=0.8)

# Chart details
plt.title("Media Consumption Evolution: A Decade-wise Analysis\nof Communication Technologies", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Media Consumption (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left', title='Technologies', bbox_to_anchor=(1.02, 1), borderaxespad=0)
plt.grid(alpha=0.3)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display plot
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Define decades and communication technologies
decades = ['1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s', '2030s']
technologies = ['Radio', 'Television', 'Cable TV', 'Satellite TV', 'Internet', 'Streaming Services', 'Social Media', 'Mobile Apps']

# Estimated percentage of media consumption by technology over the decades
media_consumption = np.array([
    [90, 10, 0, 0, 0, 0, 0, 0],   # 1930s: Dominated by Radio
    [85, 15, 0, 0, 0, 0, 0, 0],   # 1940s: Rise of Radio
    [75, 25, 0, 0, 0, 0, 0, 0],   # 1950s: Introduction of Television
    [60, 40, 0, 0, 0, 0, 0, 0],   # 1960s: Television gains popularity
    [50, 40, 10, 0, 0, 0, 0, 0],  # 1970s: Rise of Cable TV
    [30, 40, 15, 15, 0, 0, 0, 0], # 1980s: Satellite TV emerges
    [20, 30, 15, 15, 20, 0, 0, 0],# 1990s: Internet begins to take hold
    [10, 20, 15, 10, 35, 10, 0, 0],# 2000s: Internet overtakes, Streaming emerges
    [5, 10, 10, 5, 40, 15, 10, 5], # 2010s: Rise of Social Media, Mobile Apps
    [2, 5, 5, 3, 50, 20, 10, 5],  # 2020s: Internet and Mobile Apps leading
    [1, 3, 2, 2, 50, 25, 10, 7]   # 2030s: Future projections
])

# Create a stacked area chart
plt.figure(figsize=(14, 8))
colors = ['#FFD700', '#FF8C00', '#FF4500', '#DC143C', '#1E90FF', '#8A2BE2', '#32CD32', '#7FFF00']
plt.stackplot(decades, media_consumption.T, labels=technologies, colors=colors, alpha=0.85)

# Chart details
plt.title("Media Consumption Evolution\nFrom Radio to Mobile Apps (1930s to 2030s)", fontsize=16, fontweight='bold')
plt.xlabel('Decades', fontsize=12)
plt.ylabel('Media Consumption (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc='upper left', title='Technologies', bbox_to_anchor=(1.05, 1), borderaxespad=0)
plt.grid(alpha=0.3)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display plot
plt.show()
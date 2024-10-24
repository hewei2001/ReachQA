import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2025
years = np.arange(2000, 2026)

# Subscription trends (in percentage) for each genre over the years, ensuring each year sums to 100
drama = np.array([15 + (np.sin(year/2) * 5) for year in years])
comedy = np.array([15 + (np.cos(year/3) * 4) for year in years])
documentary = np.array([10 + (np.sin(year/3) * 3) for year in years])
action = np.array([20 - (np.sin(year/4) * 5) for year in years])
sci_fi = np.array([10 + (np.cos(year/5) * 4) for year in years])
romance = np.array([10 + (np.sin(year/6) * 3) for year in years])
thriller = np.array([10 + (np.cos(year/4) * 2) for year in years])
horror = np.array([10 + (np.sin(year/7) * 2) for year in years])

# Calculating the adjustment factor to maintain a total of 100% per year
total = drama + comedy + documentary + action + sci_fi + romance + thriller + horror
adjustment = 100 / total

# Apply adjustment to make sure the sum is 100 for each year
data = np.vstack([drama, comedy, documentary, action, sci_fi, romance, thriller, horror]) * adjustment

# Define colors for each genre
colors = ['#FF6347', '#FFD700', '#32CD32', '#87CEEB', '#8A2BE2', '#FF69B4', '#A52A2A', '#556B2F']

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, data, labels=['Drama', 'Comedy', 'Documentary', 'Action', 
                                  'Science Fiction', 'Romance', 'Thriller', 'Horror'], colors=colors, alpha=0.8)

# Customizing the plot
ax.set_title("Streaming Service Subscription Trends Across Genres\n(2000-2025)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Subscription Distribution (%)", fontsize=12)
ax.set_xlim(2000, 2025)
ax.set_ylim(0, 100)

# Add a grid for better readability
ax.grid(True, which='both', linestyle='--', alpha=0.7)

# Rotating the x-axis labels for clarity
plt.xticks(years[::2], rotation=45)  # Display every other year to avoid clutter

# Adding a legend
ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1), title="Genres")

# Use tight layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()
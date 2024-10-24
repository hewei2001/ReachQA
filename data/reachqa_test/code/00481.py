import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
years = np.arange(2013, 2024)
fiction = [1200, 1500, 1600, 1700, 1750, 1800, 1900, 2000, 2100, 2200, 2300]
non_fiction = [800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600]
fantasy = [300, 400, 500, 650, 700, 900, 1200, 1400, 1800, 2000, 2200]
science_fiction = [250, 200, 300, 400, 450, 500, 700, 800, 850, 900, 1000]
mystery_thriller = [400, 350, 450, 500, 550, 600, 700, 800, 900, 1000, 1100]

# Total publications by year
total_publications = np.array(fiction) + np.array(non_fiction) + \
                     np.array(fantasy) + np.array(science_fiction) + \
                     np.array(mystery_thriller)

# Create a figure and axis
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plot the data for each genre
axs[0].plot(years, fiction, marker='o', label='Fiction', color='blue', linestyle='-', linewidth=2)
axs[0].plot(years, non_fiction, marker='s', label='Non-Fiction', color='green', linestyle='--', linewidth=2)
axs[0].plot(years, fantasy, marker='^', label='Fantasy', color='purple', linestyle=':', linewidth=2)
axs[0].plot(years, science_fiction, marker='d', label='Sci-Fi', color='orange', linestyle='-', linewidth=2)
axs[0].plot(years, mystery_thriller, marker='x', label='Mystery/Thriller', color='red', linestyle='-.', linewidth=2)

# Set title and labels for the first subplot
axs[0].set_title("The Rise and Fall of Book Genres:\nA Decade in Reading Trends", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Year", fontsize=14)
axs[0].set_ylabel("Number of Books Published", fontsize=14)
axs[0].set_xlim(2013, 2023)
axs[0].set_ylim(0, 2500)
axs[0].grid(visible=True, linestyle='--', alpha=0.7)
axs[0].legend(title="Genres", fontsize=12, loc='upper left', frameon=True)

# Annotate peak points for the first subplot
peak_points = [fiction[-1], non_fiction[-1], fantasy[-1], science_fiction[-1], mystery_thriller[-1]]
for i, genre in enumerate(['Fiction', 'Non-Fiction', 'Fantasy', 'Sci-Fi', 'Mystery/Thriller']):
    axs[0].annotate(f"{peak_points[i]}", xy=(years[-1], peak_points[i]), 
                    xytext=(5, 0), textcoords='offset points', 
                    color=axs[0].lines[i].get_color(), fontsize=10, weight='bold')

# Plot the total publications in the second subplot
axs[1].bar(years, total_publications, color='skyblue', width=0.6)
axs[1].set_title("Total Number of Books Published Per Year", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Year", fontsize=14)
axs[1].set_ylabel("Total Publications", fontsize=14)
axs[1].set_xlim(2013, 2023)
axs[1].set_ylim(0, max(total_publications) + 500)
axs[1].grid(visible=True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
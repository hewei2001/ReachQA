import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

np.random.seed(42)

# Defining extended dataset
cities = ["New York", "Paris", "Tokyo", "London", "Sydney", "Berlin", "Moscow", "Beijing"]
genres = ["Fiction", "Non-Fiction", "Mystery", "Sci-Fi", "Fantasy", "Romance", "Biography", "Horror"]

# Data: generated to represent various distributions for complexity
book_counts = [
    np.random.normal(loc=200, scale=15, size=len(cities)),  # Fiction
    np.random.poisson(lam=160, size=len(cities)),  # Non-Fiction
    np.random.uniform(low=70, high=100, size=len(cities)),  # Mystery
    np.random.exponential(scale=20, size=len(cities)) + 50,  # Sci-Fi
    np.random.normal(loc=80, scale=10, size=len(cities)),  # Fantasy
    np.random.poisson(lam=60, size=len(cities)),  # Romance
    np.random.normal(loc=90, scale=12, size=len(cities)),  # Biography
    np.random.uniform(low=50, high=80, size=len(cities))  # Horror
]

# Setting up the figure and gridspec
fig = plt.figure(figsize=(16, 12))
gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1.5])

# Boxplot and Violin Plot
ax1 = fig.add_subplot(gs[0, :])
colors = plt.cm.tab20(np.linspace(0.1, 0.9, len(genres)))

box = ax1.boxplot(book_counts, vert=False, patch_artist=True, labels=genres, notch=True, whis=1.5)
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for whisker, cap, median in zip(box['whiskers'], box['caps'], box['medians']):
    whisker.set(color='navy', linewidth=1.5)
    cap.set(color='navy', linewidth=1.5)
    median.set(color='darkblue', linewidth=2)

# Overlaying Violin Plots
violin = ax1.violinplot(book_counts, vert=False, showmeans=False, showmedians=False, widths=0.7)
for pc, color in zip(violin['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_edgecolor('black')
    pc.set_alpha(0.3)

# Adding scatter plot for individual data points
for i, counts in enumerate(book_counts):
    jittered_y = np.random.normal(i+1, 0.04, size=len(counts))
    ax1.scatter(counts, jittered_y, alpha=0.6, color='black', s=20, edgecolor='w', linewidth=0.5)

ax1.set_xlabel("Number of Books", fontsize=12)
ax1.set_title("Literary Diversity in Major Cities\nHorizontal Box and Violin Chart Analysis of Book Genres", fontsize=14, pad=20)
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, axis='x')

# Statistical annotations subplot
ax2 = fig.add_subplot(gs[1, 0])
means = [np.mean(counts) for counts in book_counts]
std_devs = [np.std(counts) for counts in book_counts]
ax2.bar(genres, means, yerr=std_devs, color=colors, capsize=5)
ax2.set_title("Mean and Standard Deviation of Book Counts by Genre", fontsize=12)
ax2.set_ylabel("Mean Number of Books")
ax2.set_xticklabels(genres, rotation=45, ha='right')

# Total books by city subplot
ax3 = fig.add_subplot(gs[1, 1])
total_books_per_city = np.sum(book_counts, axis=0)
ax3.bar(cities, total_books_per_city, color='skyblue')
ax3.set_title("Total Number of Books by City", fontsize=12)
ax3.set_ylabel("Total Books")
ax3.set_xticklabels(cities, rotation=45, ha='right')

plt.tight_layout()

# Show combined plot
plt.show()
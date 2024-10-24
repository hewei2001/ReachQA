import matplotlib.pyplot as plt

# Emotional impact scores for different music genres
classical_scores = [85, 90, 78, 92, 88, 84, 79, 95, 93, 86]
jazz_scores = [70, 75, 60, 80, 65, 85, 74, 82, 77, 68]
rock_scores = [55, 60, 58, 72, 65, 68, 75, 70, 66, 62]
pop_scores = [78, 80, 85, 83, 75, 80, 77, 82, 76, 79]
electronic_scores = [65, 70, 72, 68, 74, 75, 73, 78, 71, 69]

# Combine data into a list
data = [classical_scores, jazz_scores, rock_scores, pop_scores, electronic_scores]

# Labels for the genres
genres = ['Classical', 'Jazz', 'Rock', 'Pop', 'Electronic']

# Initialize the plot
plt.figure(figsize=(12, 7))

# Create the horizontal box plot
box = plt.boxplot(data, patch_artist=True, notch=True, vert=False, labels=genres)

# Define a color palette for each genre
colors = ['#FFDDC1', '#D4A5A5', '#A1C4FD', '#C2CAD0', '#D6E0F0']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize whiskers, caps, medians, and outliers
plt.setp(box['whiskers'], color='black', linewidth=1.5)
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['medians'], color='darkred', linewidth=2)
plt.setp(box['fliers'], marker='o', color='black', alpha=0.5)

# Add title and labels
plt.title("Emotional Impact of Music Genres on Listeners\nAcross Various Styles", fontsize=16, fontweight='bold')
plt.xlabel("Emotional Impact Score", fontsize=12)
plt.ylabel("Music Genres", fontsize=12)

# Add grid lines for easier reading
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()
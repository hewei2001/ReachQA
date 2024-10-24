import matplotlib.pyplot as plt

# Data and labels for the genres
labels = ['Action', 'Drama', 'Comedy', 'Science Fiction', 'Documentary']
sizes = [20, 30, 25, 15, 10]  # Percentages of each genre
colors = ['#FF6347', '#4682B4', '#FFD700', '#ADFF2F', '#20B2AA']  # Distinct colors for each genre

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plotting the ring chart
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, startangle=140, pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w'), autopct='%1.1f%%', textprops={'fontsize': 10}
)

# Adjust appearance of the pie chart
for text in texts:
    text.set_color('grey')  # Set label color for better contrast

for autotext in autotexts:
    autotext.set_color('white')  # Set percentage text color inside the pie wedges

# Draw a center circle to transform the pie chart into a ring chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Title and styling
ax.set_title("Cinephile Club's Year in Review:\nMovie Genre Preferences", 
             fontsize=14, fontweight='bold', pad=20)
ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

# Add legend with title
ax.legend(wedges, labels, title='Genres', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))

# Central label in the empty space of the ring
ax.text(0, 0, '2023 Overview', horizontalalignment='center', verticalalignment='center', fontsize=12, color='black', fontweight='bold')

# Ensure layout is tidy and no elements overlap
plt.tight_layout()

# Show the plot
plt.show()
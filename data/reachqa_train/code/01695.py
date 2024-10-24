import matplotlib.pyplot as plt

# Music genres and their preference percentages
genres = ['Pop', 'Rock', 'Hip-Hop', 'Classical', 'Jazz', 'Electronic', 'Country']
preferences = [25, 20, 15, 10, 10, 10, 10]  # Ensure the total is 100%

# Define colors for each music genre
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2']

# Explode the 'Pop' slice to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Draw the pie chart with shadow effect
wedges, texts, autotexts = ax.pie(
    preferences, labels=genres, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, wedgeprops=dict(width=0.3)
)

# Customize the appearance of the text
plt.setp(autotexts, size=10, weight="bold", color="black")
plt.setp(texts, size=12)

# Set a concise and clear title with line break
ax.set_title("Music Genre Preferences Among\nCollege Students in 2023", fontsize=14, fontweight='bold')

# Add a legend to the right of the chart
ax.legend(wedges, genres, title="Genres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adjust layout to ensure no overlap and all elements are visible
plt.tight_layout()

# Display the plot
plt.show()
import matplotlib.pyplot as plt

# Define the genres and user distribution data
genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classical', 'Jazz', 'Country', 'Reggae']
user_distribution = [30, 20, 15, 12, 8, 7, 5, 3]  # Adjusted to sum to 100%

# Define colors for each genre
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#e6e600', '#ff6666']

# Explode the largest genre slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # Explode 'Pop'

# Create the pie chart
plt.figure(figsize=(10, 8))
plt.pie(user_distribution, explode=explode, labels=genres, autopct='%1.1f%%',
        colors=colors, startangle=140, shadow=True, wedgeprops=dict(edgecolor='w'))

# Title with line break for better readability
plt.title("Global Music Streaming Trends in 2023:\nUser Distribution by Genre", fontsize=16, fontweight='bold', pad=20)

# Position the legend to the right of the chart
plt.legend(genres, loc='center left', bbox_to_anchor=(1, 0.5), title="Music Genres", title_fontsize='13')

# Maintain equal aspect ratio to ensure pie chart is circular
plt.axis('equal')

# Adjust layout for better fit and clarity
plt.tight_layout()

# Display the plot
plt.show()
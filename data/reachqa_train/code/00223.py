import matplotlib.pyplot as plt

# Languages and their respective proficiency levels in millions
languages = ['English', 'Spanish', 'Mandarin', 'French', 'German', 'Japanese', 'Arabic']
proficiency_levels = [150, 100, 80, 60, 50, 30, 20]

# Colors for each language's section in the pie chart
colors = ['lightblue', 'lightcoral', 'gold', 'lightgreen', 'lightpink', 'lightskyblue', 'lightyellow']

# Explode the largest slice (English) to highlight it
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
plt.pie(proficiency_levels, explode=explode, labels=languages, colors=colors, autopct='%1.1f%%',
        startangle=140, shadow=True)

# Set a circular aspect ratio
plt.axis('equal')

# Set chart title with a line break for better readability
plt.title("Global Language Proficiency:\nConversational Skills in Popular Languages", fontsize=14)

# Add a legend with improved placement
plt.legend(languages, title="Languages", loc="center left", bbox_to_anchor=(1, 0.5))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the pie chart
plt.show()
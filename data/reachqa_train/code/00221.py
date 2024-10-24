import matplotlib.pyplot as plt

# Define the data
libraries = [
    "Great Library of\nAlexandria", 
    "British Library", 
    "Library of Congress", 
    "Vatican Apostolic Library"
]
categories = [
    "Ancient Texts", 
    "Scientific Works", 
    "Literature & Arts", 
    "History & Geography", 
    "Religion & Philosophy", 
    "Manuscripts & Rare Books"
]

# Percentage of categories in each library
alexandria_data = [30, 10, 20, 15, 10, 15]
british_data = [5, 25, 20, 20, 5, 25]
congress_data = [10, 30, 25, 10, 5, 20]
vatican_data = [15, 10, 15, 10, 40, 10]

# Colors for categories
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create a donut pie chart for each library
def plot_donut_chart(data, title, categories, colors):
    plt.figure(figsize=(8, 6))

    # Create pie chart
    wedges, texts, autotexts = plt.pie(
        data,
        labels=categories,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        pctdistance=0.85,
        wedgeprops=dict(width=0.3, edgecolor='w'),
        textprops=dict(size=10)
    )
    
    # Draw a white circle at the center to create a donut look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    # Add a shadow for depth
    plt.gca().set(aspect="equal", title=title)
    
    # Add a legend
    plt.legend(wedges, categories, title="Book Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Automatically adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

# Plot each library's data
plot_donut_chart(alexandria_data, "Great Library of Alexandria:\nCollection Diversity", categories, colors)
plot_donut_chart(british_data, "British Library:\nCollection Diversity", categories, colors)
plot_donut_chart(congress_data, "Library of Congress:\nCollection Diversity", categories, colors)
plot_donut_chart(vatican_data, "Vatican Apostolic Library:\nCollection Diversity", categories, colors)
import matplotlib.pyplot as plt

# Data: Authors and number of languages their most famous work has been translated into
authors = [
    "García Márquez\n'One Hundred Years of Solitude'",
    "J.K. Rowling\n'Harry Potter'",
    "Saint-Exupéry\n'The Little Prince'",
    "Cervantes\n'Don Quixote'",
    "Tolstoy\n'War and Peace'"
]
translations = [44, 80, 300, 50, 49]

# Create a horizontal bar chart
plt.figure(figsize=(12, 7))
bars = plt.barh(authors, translations, color=['#FFDD44', '#77AAFF', '#FF7777', '#33DDDD', '#AA77FF'], height=0.6)

# Add title and labels
plt.title("Global Reach of Famous Literary Works\nMeasured by Number of Languages Translated", fontsize=16, weight='bold', pad=20)
plt.xlabel("Number of Languages", fontsize=12)
plt.ylabel("Authors & Their Famous Works", fontsize=12)

# Adjust x-axis range to provide space for annotations
plt.xlim(0, max(translations) + 20)

# Add value annotations to each bar
for bar in bars:
    plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())}', va='center', fontsize=10, color='black')

# Customize tick parameters
plt.tick_params(axis='y', which='major', labelsize=11)

# Add grid lines for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust layout to avoid clipping text
plt.tight_layout()

# Show the plot
plt.show()
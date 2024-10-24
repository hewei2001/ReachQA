import matplotlib.pyplot as plt

# Data for the pie chart
connectivity_sources = ['Satellite Internet', 'Mobile Data', 'DSL', 'Fiber Optic', 'Public Wi-Fi']
percentages = [25, 40, 15, 10, 10]

# Colors for each section of the pie chart
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Explode the largest section for emphasis
explode = (0, 0.1, 0, 0, 0)

# Initialize the plot
plt.figure(figsize=(10, 7))

# Plot the pie chart
plt.pie(percentages, labels=connectivity_sources, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140, shadow=True)

# Add a title with line breaks for better readability
plt.title("Digital Connectivity in Rural Areas:\nA Snapshot of Tech Valley", fontsize=16, fontweight='bold', y=1.05)

# Ensure no overlap with tight layout
plt.tight_layout()

# Display the pie chart
plt.show()
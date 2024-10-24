import matplotlib.pyplot as plt

# Define the digital ecosystem components and their resource allocations
components = ['Artificial Intelligence', 'Cybersecurity', 'Cloud Infrastructure', 'IoT', 'Data Analytics']
allocations = [25, 20, 30, 15, 10]

# Define colors for each component to enhance visual distinction
colors = ['#FF5733', '#33FFCE', '#3366FF', '#FF33B8', '#33FF57']

# Create a figure for the donut pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the donut pie chart
wedges, texts, autotexts = ax.pie(
    allocations, 
    labels=components, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85, 
    wedgeprops=dict(width=0.3, edgecolor='black', linewidth=1.5)
)

# Create a circle for the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Style text in the donut pie chart
for text in texts:
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Add a descriptive and imaginative title
ax.set_title("TechnoSphere's 2024\nDigital Ecosystem Resource Allocation", fontsize=16, fontweight='bold', ha='center')

# Add a legend with clear labels to avoid confusion
ax.legend(wedges, components, title="Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Use tight layout for better spacing and prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
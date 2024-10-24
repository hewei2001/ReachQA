import matplotlib.pyplot as plt

# Define the sectors and their corresponding investment amounts in million dollars
sectors = [
    'Quantum Hardware Development', 
    'Quantum Algorithms', 
    'Quantum Cryptography', 
    'Cloud Quantum Services', 
    'Quantum Software Development'
]
investments = [150, 100, 80, 120, 50]

# Define colors for each sector
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Highlight the 'Quantum Hardware Development' sector
explode = (0.1, 0, 0, 0, 0)

# Create a ring chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the ring chart
wedges, texts, autotexts = ax.pie(
    investments, labels=sectors, autopct='%1.1f%%', startangle=90, colors=colors,
    explode=explode, pctdistance=0.85, wedgeprops=dict(width=0.3, edgecolor='w')
)

# Add a circle in the center to make it a ring
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the chart is a perfect circle
ax.axis('equal')

# Customize text properties for better readability
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=10)

# Add a central title inside the ring
ax.text(0, 0, "Quantum Computing\nInvestments\n2035", 
        horizontalalignment='center', verticalalignment='center', 
        fontsize=12, fontweight='bold', color='black')

# Add an overall title
plt.title("Investment Allocation in Quantum Computing\nVentures - 2035", 
          fontsize=14, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
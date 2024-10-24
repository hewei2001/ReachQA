import matplotlib.pyplot as plt

# Define the initiatives and their corresponding fund allocation percentages
initiatives = [
    'Electric Vehicle Infrastructure', 
    'Bicycle Lanes', 
    'Public Transportation Enhancement', 
    'Pedestrian Walkways', 
    'Carpool Programs'
]
fund_allocation = [35, 20, 25, 10, 10]  # Represents percentage of total budget

# Define colors for each sector
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(
    fund_allocation, 
    labels=initiatives, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0.1, 0, 0.1, 0, 0), 
    textprops={'fontsize': 10}
)

# Add a title to the chart
plt.title("Greenburg's Sustainable Transportation Fund Allocation", fontsize=14, weight='bold', y=1.05)

# Customize the legend to be placed outside the chart
plt.legend(
    initiatives, 
    title="Initiatives", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5),
    fontsize=10
)

# Ensure the pie chart is a circle
ax.axis('equal')  

# Automatically adjust the layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()
import matplotlib.pyplot as plt

# Define the data
technologies = ['Solar Power', 'Wind Energy', 'Hydroelectric', 'Geothermal', 'Biomass']
shares = [35, 25, 20, 10, 10]

# Define colors for each sector
colors = ['#ffcc00', '#6699ff', '#66ff66', '#ff9966', '#ff66b3']

# Define explode to highlight the 'Solar Power' sector
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    shares, 
    labels=technologies, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode
)

# Customize the appearance
plt.setp(texts, size=10, weight='bold', color='white')
plt.setp(autotexts, size=12, weight='bold')

# Title and styling
plt.title(
    'Technological Advancements in Renewable Energy - 2023\nGreenTech World', 
    fontsize=14, 
    weight='bold', 
    pad=20
)

# Add a legend with the technology sectors
plt.legend(
    wedges, 
    technologies, 
    title="Technology Sectors", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Automatically adjust layout to ensure everything fits
plt.tight_layout()

# Display the chart
plt.show()
import matplotlib.pyplot as plt

# Define the data for exotic tea consumption
tea_types = ['Matcha (Japan)', 'Masala Chai (India)', 'Moroccan Mint (Morocco)', 
             'Rooibos (South Africa)', 'Hibiscus (Central America)']
consumption_percentages = [25, 20, 15, 25, 15]

# Define colors for each tea type
colors = ['#6db33f', '#e07b39', '#9cc3d5', '#d58339', '#a34f4f']

# Create the pie chart with a 'donut' effect
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    consumption_percentages, labels=tea_types, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.3), shadow=True, explode=(0.05, 0.05, 0.05, 0.05, 0.05)
)

# Customize text properties
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(11)

# Add a legend outside the chart
ax.legend(wedges, tea_types, title="Tea Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Customizing the plot title
plt.title("The World of Exotic Teas:\nA Global Consumption Snapshot", fontsize=14, fontweight='bold', pad=20)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
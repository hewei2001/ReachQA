import matplotlib.pyplot as plt

# Manuscripts data for each region
regions = ['Greece', 'Egypt', 'Rome', 'Carthage', 'Phoenicia', 'Anatolia']
manuscripts = [120, 200, 180, 80, 110, 90]

# Define colors for each region
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Determine if any sector should be highlighted
explode = (0.1, 0, 0, 0, 0, 0)  # Highlighting Greece for emphasis

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(manuscripts, labels=regions, autopct='%1.1f%%', startangle=140, 
                                  colors=colors, explode=explode, wedgeprops=dict(edgecolor='black'))

# Style text for clarity
for text in texts:
    text.set_size(11)
    text.set_fontweight('bold')
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

# Title with line break for better formatting
plt.title('Distribution of Ancient Manuscripts\nFound Around the Mediterranean', 
          fontsize=14, fontweight='bold', pad=20)

# Ensure the layout is adjusted
plt.tight_layout()

# Optionally add a legend
plt.legend(wedges, regions, title="Regions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Display the pie chart
plt.show()
import matplotlib.pyplot as plt

# Define the contribution of each element
elements = ['Aetherium', 'Zynogen', 'Qirium', 'Xylox']
contributions = [40, 25, 20, 15]
colors = ['#FFDDC1', '#FFABAB', '#FFC3A0', '#D5AAFF']

# Create a ring chart using the pie function with a defined width
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(contributions, labels=elements, autopct='%1.1f%%',
                                  startangle=90, colors=colors, pctdistance=0.85,
                                  wedgeprops=dict(width=0.3, edgecolor='w'))

# Add a central label in the ring
plt.text(0, 0, 'Element\nContributions', horizontalalignment='center',
         verticalalignment='center', fontsize=12, fontweight='bold', color='gray')

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')  

# Customize fonts and labels
plt.setp(autotexts, size=10, weight='bold', color='black')
ax.set_title("Influence of Elements on\nInterstellar Travel Propulsion (Year 3060)",
             fontsize=16, fontweight='bold', pad=20)

# Add a legend and position it outside the ring
ax.legend(wedges, elements, title="Elements", loc="center left", bbox_to_anchor=(1, 0.5))

# Adjust the layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
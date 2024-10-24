import matplotlib.pyplot as plt

# Extended Cybercrime methods with subcategories and their percentage share
methods = [
    'Email Phishing', 'Spear Phishing', 'Clone Phishing',
    'Ransomware', 'Ransomware-as-a-Service',
    'Denial-of-Service', 'DDoS',
    'Internal Data Breaches', 'External Data Breaches',
    'Social Engineering', 'Baiting', 'Quid Pro Quo',
    'Cryptojacking'
]
incidents_percentage = [12, 10, 13, 15, 10, 8, 7, 6, 4, 5, 2, 1, 7]

# Colors and patterns for each method
colors = ['#ff9999', '#ff6666', '#ff3333', '#66b3ff', '#4da6ff',
          '#99ff99', '#85e085', '#ffcc99', '#ffb366', '#c2c2f0',
          '#b3b3cc', '#ffb3e6', '#ff99cc']

# Transform the pie chart into a donut chart with hierarchical data
fig, ax = plt.subplots(figsize=(10, 7))

# Pie plot
ax.pie(incidents_percentage, labels=methods, autopct='%1.1f%%', startangle=90,
       colors=colors, pctdistance=0.85, wedgeprops=dict(edgecolor='w', linewidth=1.5))

# Center circle for donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure pie is drawn as a circle
ax.axis('equal')

# Split the title into two lines for better readability
plt.title('Virtual Heists: The Complex Web of Cybercrime in 2023\nBreaking Down the Methods', fontsize=14, fontweight='bold', pad=20)

# Adjust layout to fit all elements properly
plt.tight_layout()

# Adding a secondary subplot for comparisons or extended data
fig, ax2 = plt.subplots(figsize=(10, 3))
risk_levels = ['Low', 'Moderate', 'High', 'Severe']
severity_percentage = [20, 30, 25, 25]
ax2.barh(risk_levels, severity_percentage, color=['#99ff99', '#66b3ff', '#ff9999', '#ff3333'])
ax2.set_title('Cybercrime Method Severity Levels', fontsize=12)
ax2.set_xlabel('Percentage')
ax2.set_xlim(0, 35)

# Adjust overall layout
plt.subplots_adjust(left=0.1, bottom=0.2, right=0.9, top=0.8, wspace=0.4, hspace=0.4)
plt.tight_layout()

# Display the plot
plt.show()
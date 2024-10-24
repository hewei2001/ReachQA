import matplotlib.pyplot as plt

# Data: Predicted popularity of communication channels in 2030
communication_shares = [20, 15, 25, 10, 25, 5]
communication_labels = [
    'Holographic\nConferencing', 
    'Neural Interface\nMessaging',
    'Virtual Reality\nMeetings', 
    'Augmented Reality\nNotifications', 
    'Traditional Video\nConferencing', 
    'Others'
]

# Color palette for distinct representation
communication_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF3', '#B833FF']

# Emphasize the predicted dominant communication methods
explode = (0, 0.1, 0.1, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(9, 9), dpi=120)
wedges, texts, autotexts = ax.pie(
    communication_shares,
    labels=communication_labels,
    colors=communication_colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.85,
    wedgeprops=dict(width=0.4, edgecolor='white'),
    shadow=True
)

# Ensure the pie chart is circular
ax.axis('equal')

# Title
ax.set_title('Communication Channels of the Future:\nPredicted Popularity in 2030',
             fontsize=16, fontweight='bold', pad=20)

# Adjust text and percentage display inside the pie chart
for text, autotext in zip(texts, autotexts):
    text.set_fontsize(11)
    text.set_weight('semibold')
    autotext.set_color('black')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# Add a legend outside the pie chart
ax.legend(wedges, communication_labels, title="Communication Channels", loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()
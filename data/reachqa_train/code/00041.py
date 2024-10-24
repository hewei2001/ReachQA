import matplotlib.pyplot as plt

# Data for followers on different social media platforms
platforms = ['Instagram', 'Twitter', 'YouTube', 'LinkedIn', 'TikTok']
followers = [40000, 25000, 15000, 10000, 30000]

# Define colors for each platform in the pie chart
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Highlight Instagram by separating its slice from the rest
explode = (0.1, 0, 0, 0, 0)  # "explode" the 1st slice

# Plotting the pie chart
fig, ax = plt.subplots()
ax.pie(followers, labels=platforms, autopct='%1.1f%%', startangle=90,
       colors=colors, explode=explode, shadow=True)

# Ensure pie chart is a circle
ax.axis('equal')

# Title of the pie chart, split into two lines for better readability
plt.title('Follower Distribution Across \nSocial Media Platforms for Tech Influencer 2023')

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()
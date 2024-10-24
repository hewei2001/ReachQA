import matplotlib.pyplot as plt

# Expanded data for followers on different social media platforms
platforms = [
    'Instagram', 'Twitter', 'YouTube', 'LinkedIn', 'TikTok',
    'Facebook', 'Snapchat', 'Pinterest', 'Reddit', 'WhatsApp'
]
followers = [40000, 25000, 15000, 10000, 30000, 50000, 8000, 6000, 7000, 20000]

# Define colors for each platform in the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0',
          '#ffb3e6', '#c4e17f', '#76d7c4', '#f0e442', '#e6e6fa']

# Highlight Instagram and Facebook for their larger audience
explode = (0.1, 0, 0, 0, 0.1, 0, 0, 0, 0, 0)

# Nested category data within Instagram's followers
instagram_data = [20000, 12000, 8000]  # Example: by age groups
instagram_labels = ['18-24', '25-34', '35+']
instagram_colors = ['#ff9999', '#ff6666', '#ff3333']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Main pie chart
ax1.pie(followers, labels=platforms, autopct='%1.1f%%', startangle=90,
        colors=colors, explode=explode, shadow=True)

# Ensure pie chart is a circle
ax1.axis('equal')
ax1.set_title('Follower Distribution Across \nSocial Media Platforms for Tech Influencer 2023')

# Nested pie chart within Instagram
ax2.pie(instagram_data, labels=instagram_labels, autopct='%1.1f%%', startangle=90,
        colors=instagram_colors, shadow=True)
ax2.axis('equal')
ax2.set_title('Instagram Followers Breakdown by Age Group')

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the chart
plt.show()
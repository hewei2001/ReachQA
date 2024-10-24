import matplotlib.pyplot as plt
import numpy as np

# Years of the study
years = np.arange(2010, 2021)

# Artificial data for time spent (in hours per week) on different digital activities
streaming_services = np.array([2, 3, 4, 5, 5, 6, 8, 10, 11, 12, 13])
social_media = np.array([5, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12])
online_gaming = np.array([3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 9])
e_learning = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6])
news_blogs = np.array([2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5])

# Stack the data
data = np.vstack([streaming_services, social_media, online_gaming, e_learning, news_blogs])

# Plot the stacked area chart
plt.figure(figsize=(12, 7))
plt.stackplot(years, data, labels=['Streaming Services', 'Social Media', 'Online Gaming', 'E-Learning', 'News & Blogs'], 
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666'], alpha=0.8)

# Add title and labels
plt.title('Digital Time Allocation Across Different Activities\nA Decadal Journey (2010-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Hours per Week', fontsize=12)

# Add a legend
plt.legend(loc='upper left', title='Digital Activities', fontsize=10)

# Add grid for readability
plt.grid(alpha=0.3)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()
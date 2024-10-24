import matplotlib.pyplot as plt
import numpy as np

# Years from 2013 to 2023
years = np.arange(2013, 2024)

# Box office revenue (in billions) for each genre over the years
action_revenue = [6.5, 6.8, 7.2, 7.6, 8.0, 8.5, 8.8, 9.0, 9.5, 10.0, 10.5]
comedy_revenue = [5.2, 5.1, 5.0, 5.3, 5.6, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5]
drama_revenue = [3.5, 3.6, 3.8, 4.0, 4.2, 4.4, 4.5, 4.7, 4.8, 5.0, 5.1]
sci_fi_revenue = [4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 6.8, 7.5, 8.3, 8.8, 9.0]
horror_revenue = [2.5, 2.8, 2.9, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.5]

# Creating the line plot
plt.figure(figsize=(12, 7))

# Plotting each genre with different markers and colors
plt.plot(years, action_revenue, marker='o', linewidth=2, linestyle='-', label='Action', color='#FF5733')
plt.plot(years, comedy_revenue, marker='s', linewidth=2, linestyle='-', label='Comedy', color='#33C3FF')
plt.plot(years, drama_revenue, marker='^', linewidth=2, linestyle='-', label='Drama', color='#4CFF33')
plt.plot(years, sci_fi_revenue, marker='d', linewidth=2, linestyle='-', label='Sci-Fi', color='#FF33F0')
plt.plot(years, horror_revenue, marker='x', linewidth=2, linestyle='-', label='Horror', color='#FFC133')

# Adding titles and labels
plt.title('Box Office Revenue Trends\nfor Different Film Genres (2013-2023)', fontsize=16, weight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Revenue (Billions $)', fontsize=12)

# Adding grid and ticks
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(2, 12, 1))

# Adding a legend
plt.legend(title='Film Genres', loc='upper left', fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
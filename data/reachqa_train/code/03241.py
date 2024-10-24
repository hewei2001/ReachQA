import numpy as np
import matplotlib.pyplot as plt

# Define countries and years
countries = ['India', 'Brazil', 'USA', 'Japan', 'France']
years = np.arange(2013, 2024)  # From 2013 to 2023

# Artificial data representing the number of participants in kite festivals
participants_india = [500, 520, 540, 580, 620, 680, 750, 800, 850, 900, 950]
participants_brazil = [300, 320, 350, 370, 390, 430, 470, 510, 540, 570, 590]
participants_usa = [400, 430, 460, 500, 530, 560, 600, 650, 680, 720, 750]
participants_japan = [350, 370, 400, 430, 460, 490, 520, 560, 590, 620, 640]
participants_france = [450, 470, 490, 510, 540, 570, 600, 630, 660, 700, 730]

# Create the line chart
plt.figure(figsize=(12, 8))

# Plotting each country's data
plt.plot(years, participants_india, marker='o', linestyle='-', color='red', label='India', linewidth=2)
plt.plot(years, participants_brazil, marker='s', linestyle='--', color='green', label='Brazil', linewidth=2)
plt.plot(years, participants_usa, marker='^', linestyle='-.', color='blue', label='USA', linewidth=2)
plt.plot(years, participants_japan, marker='D', linestyle=':', color='orange', label='Japan', linewidth=2)
plt.plot(years, participants_france, marker='x', linestyle='-', color='purple', label='France', linewidth=2)

# Customizing the chart
plt.title("Annual Kite Festival Participation\n(2013-2023)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Participants", fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 1001, 100))  # From 0 to 1000 with a step of 100
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Countries', loc='upper left', fontsize=10)

# Annotate peak participation for India
max_participants_india = max(participants_india)
max_year_india = years[participants_india.index(max_participants_india)]
plt.annotate(f'Peak: {max_participants_india}', xy=(max_year_india, max_participants_india),
             xytext=(max_year_india - 1, max_participants_india + 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show the plot
plt.show()
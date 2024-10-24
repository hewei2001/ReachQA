import matplotlib.pyplot as plt

# Original data for the ring chart
activities = ['Product Dev.', 'Marketing', 'Sales', 'Cust. Support', 'Admin']
time_allocation = [35, 20, 15, 15, 15]
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Constructing new data for the additional subplot (time allocation over quarters)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
quarterly_allocation = {
    'Product Dev.': [30, 32, 35, 36],
    'Marketing': [20, 18, 22, 23],
    'Sales': [15, 16, 14, 15],
    'Cust. Support': [15, 14, 16, 15],
    'Admin': [20, 20, 13, 11]
}

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={'width_ratios': [1, 1.5]})

# First subplot: Ring chart
wedges, texts, autotexts = ax1.pie(
    time_allocation, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%',
    startangle=90, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3, edgecolor='w')
)
ax1.set_title('Current Time Allocation in a Tech Startup\n(Percentage of Total Working Hours)', fontsize=14, weight='bold')
plt.setp(texts, size=10, weight='bold')
plt.setp(autotexts, size=9, weight='bold', color='black')
center_circle = plt.Circle((0,0), 0.70, fc='white')
ax1.add_artist(center_circle)
ax1.axis('equal')

# Second subplot: Line chart for quarterly time allocation
for activity, allocations in quarterly_allocation.items():
    ax2.plot(quarters, allocations, marker='o', label=activity)

ax2.set_title('Quarterly Time Allocation Trends', fontsize=14, weight='bold')
ax2.set_xlabel('Quarters', fontsize=12)
ax2.set_ylabel('Time Allocation (%)', fontsize=12)
ax2.legend(title='Activities', fontsize=10, title_fontsize='11')
ax2.grid(True, linestyle='--', alpha=0.7)

# Improve layout
plt.tight_layout()
plt.show()
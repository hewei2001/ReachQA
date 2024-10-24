import matplotlib.pyplot as plt
import numpy as np

# Define the time periods
decades = np.array([1900, 1920, 1940, 1960, 1980, 2000, 2020])

# Create data for each communication method
postal_mail = np.array([80, 75, 70, 60, 40, 20, 10])
landline_phones = np.array([0, 5, 20, 40, 60, 55, 30])
mobile_phones = np.array([0, 0, 0, 0, 10, 40, 70])
email = np.array([0, 0, 0, 0, 5, 30, 50])
instant_messaging = np.array([0, 0, 0, 0, 0, 5, 40])

# Create related data for overlay plot: Global internet penetration (as a percentage)
internet_penetration = np.array([0, 0, 0, 1, 15, 40, 65])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Plot the stackplot for the communication data
ax.stackplot(decades, postal_mail, landline_phones, mobile_phones, email, instant_messaging,
             labels=['Postal Mail', 'Landline Phones', 'Mobile Phones', 'Email', 'Instant Messaging'],
             colors=['#FFD700', '#6495ED', '#FF6347', '#ADFF2F', '#DA70D6'], alpha=0.85)

# Overlay plot for global internet penetration
ax2 = ax.twinx()
ax2.plot(decades, internet_penetration, 'o--', color='black', label='Internet Penetration (%)')
ax2.set_ylabel('Internet Penetration (%)', fontsize=12)

# Set the title and labels
ax.set_title('Evolution of Communication Methods\nfrom 1900 to 2020 & Internet Penetration Overlay', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Usage Prevalence (%)', fontsize=12)

# Add legends for both plots
ax.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Grid, ticks, and axis limits
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xlim(decades[0], decades[-1])
ax.set_xticks(decades)
ax.tick_params(axis='x', rotation=45, labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax2.set_ylim(0, 100)  # Assuming internet penetration could potentially reach 100%
ax2.tick_params(axis='y', labelsize=10)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
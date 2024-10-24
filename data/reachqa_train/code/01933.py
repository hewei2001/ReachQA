import matplotlib.pyplot as plt
import numpy as np

# Define months and ticket sales data for two cinema franchises
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ticket_sales_moviemagic = np.array([1500, 1800, 2000, 2300, 3000, 2500, 2700, 3500, 4000, 3700, 3600, 4200])
ticket_sales_screenspectacle = np.array([1300, 1600, 1900, 2500, 2800, 2700, 3100, 3300, 3900, 3900, 3500, 4300])

# Initialize the plot
plt.figure(figsize=(10, 6))

# Plot ticket sales data for both franchises
plt.plot(months, ticket_sales_moviemagic, marker='o', linestyle='-', color='blue', label='MovieMagic', linewidth=2)
plt.plot(months, ticket_sales_screenspectacle, marker='s', linestyle='-', color='red', label='ScreenSpectacle', linewidth=2)

# Add data annotations
for i, month in enumerate(months):
    # Annotate MovieMagic data points
    plt.annotate(f'{ticket_sales_moviemagic[i]}', 
                 xy=(month, ticket_sales_moviemagic[i]), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center', 
                 fontsize=9, 
                 color='blue')
    
    # Annotate ScreenSpectacle data points
    plt.annotate(f'{ticket_sales_screenspectacle[i]}', 
                 xy=(month, ticket_sales_screenspectacle[i]), 
                 textcoords="offset points", 
                 xytext=(0,-15), 
                 ha='center', 
                 fontsize=9, 
                 color='red')

# Customize the plot
plt.title("Cinema Franchises Ticket Sales\nComparison in 2023", fontsize=16, weight='bold', pad=15)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Ticket Sales", fontsize=14)
plt.xticks(months)
plt.grid(visible=True, linestyle='--', alpha=0.5)

# Add legend
plt.legend(title="Cinema Franchises", loc='upper left', fontsize=10)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the plot
plt.show()
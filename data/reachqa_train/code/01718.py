import matplotlib.pyplot as plt
import numpy as np

# Define the years with increased granularity to include semi-annual data from 2000 to 2030
years = np.arange(2000, 2031, 0.5)

# Extended data for various digital devices in millions
pcs = np.concatenate([np.linspace(50, 150, 42), np.linspace(150, 160, 20)])
tvs = np.concatenate([np.linspace(70, 160, 42), np.linspace(160, 165, 20)])
smartphones = np.concatenate([np.linspace(5, 980, 42), np.linspace(980, 1100, 20)])
tablets = np.concatenate([np.linspace(0, 390, 42), np.linspace(390, 450, 20)])
smart_home_devices = np.concatenate([np.linspace(0, 470, 42), np.linspace(470, 600, 20)])
wearable_devices = np.concatenate([np.linspace(0, 50, 42), np.linspace(50, 200, 20)])
streaming_devices = np.concatenate([np.linspace(0, 0, 42), np.linspace(0, 150, 20)])

# Plotting the stacked area chart with increased complexity
plt.figure(figsize=(16, 10))

# Create stacked area plot
plt.stackplot(years, pcs, tvs, smartphones, tablets, smart_home_devices, wearable_devices, streaming_devices,
              labels=['Personal Computers', 'Televisions', 'Smartphones', 'Tablets', 
                      'Smart Home Devices', 'Wearable Devices', 'Streaming Devices'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'], alpha=0.8)

# Add title and labels
plt.title("Digital Device Proliferation in Households Over Three Decades\nA Detailed Overview with Emerging Trends (2000 - 2030)", 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Devices in Households (Millions)", fontsize=12)

# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title='Device Types')

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Highlight significant trend changes
plt.annotate('Smartphones become ubiquitous', xy=(2010, 250), xytext=(2005, 900),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')
plt.annotate('Rise of Wearables', xy=(2025, 1100), xytext=(2015, 1200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, backgroundcolor='w')

# Ensure layout is neat without overlapping
plt.tight_layout()

# Comparative Subplot: Growth Rates
fig, ax = plt.subplots(figsize=(16, 5))
growth_rate = np.gradient(smartphones, years) / smartphones * 100  # % growth rate
ax.plot(years, growth_rate, color='#2ca02c', label='Smartphones Growth Rate')
ax.axvline(2010, color='gray', linestyle='--', lw=1, label='Key Year (2010)')
ax.set_title("Smartphones Growth Rate Over Time", fontsize=14, pad=15)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Growth Rate (%)", fontsize=12)
ax.legend(loc='upper right')

# Ensure subplot layout is neat
plt.tight_layout()

# Display the plots
plt.show()
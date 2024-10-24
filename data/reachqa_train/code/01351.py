import matplotlib.pyplot as plt
import numpy as np

# Years representing major quantum processor releases
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

# Quantum volume values for different companies
ibm_quantum_volume = np.array([8, 16, 32, 64, 128, 256, 512, 1024, 2048])
google_quantum_volume = np.array([16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
rigetti_quantum_volume = np.array([4, 8, 16, 32, 64, 128, 256, 512, 1024])
ionq_quantum_volume = np.array([2, 4, 16, 32, 64, 128, 256, 512, 1024])

# Plotting the data
plt.figure(figsize=(14, 8))

# Plot lines for each company
plt.plot(years, ibm_quantum_volume, marker='o', linestyle='-', label='IBM', color='#1f77b4', linewidth=2)
plt.plot(years, google_quantum_volume, marker='s', linestyle='--', label='Google', color='#ff7f0e', linewidth=2)
plt.plot(years, rigetti_quantum_volume, marker='^', linestyle=':', label='Rigetti', color='#2ca02c', linewidth=2)
plt.plot(years, ionq_quantum_volume, marker='d', linestyle='-.', label='IonQ', color='#d62728', linewidth=2)

# Annotating key milestones
plt.annotate('IBM Quantum Supremacy', xy=(2021, 512), xytext=(2019.5, 1500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

plt.annotate('Google Breakthrough', xy=(2023, 4096), xytext=(2020, 3000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

# Label each data point with its value
for year, qv in zip(years, ibm_quantum_volume):
    plt.text(year, qv, f'{qv}', fontsize=8, ha='right', va='bottom')

for year, qv in zip(years, google_quantum_volume):
    plt.text(year, qv, f'{qv}', fontsize=8, ha='right', va='bottom')

for year, qv in zip(years, rigetti_quantum_volume):
    plt.text(year, qv, f'{qv}', fontsize=8, ha='right', va='bottom')

for year, qv in zip(years, ionq_quantum_volume):
    plt.text(year, qv, f'{qv}', fontsize=8, ha='right', va='bottom')

# Customizing the plot
plt.title('The Evolution of Quantum Computing Power\nOver Time', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Quantum Volume (Log Scale)', fontsize=12)
plt.yscale('log')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Quantum Computing Companies', loc='upper left', fontsize=10, frameon=False)
plt.xticks(years)
plt.tight_layout()

# Display the plot
plt.show()
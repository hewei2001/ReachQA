import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.arange(2020, 2031)

# Hypothetical data for operational qubits reported by tech giants
ibm_qubits = np.array([20, 25, 32, 38, 46, 55, 65, 78, 90, 105, 120])
google_qubits = np.array([18, 26, 34, 42, 51, 60, 72, 85, 100, 116, 133])
microsoft_qubits = np.array([15, 22, 29, 36, 45, 53, 62, 70, 80, 92, 105])
alibaba_qubits = np.array([12, 19, 25, 33, 43, 54, 66, 77, 88, 100, 115])

# Compute cumulative qubits
cumulative_qubits = ibm_qubits + google_qubits + microsoft_qubits + alibaba_qubits

# Initialize the figure and primary axis
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot line charts for each company
ax1.plot(years, ibm_qubits, label='IBM', color='tab:blue', marker='o', linewidth=2)
ax1.plot(years, google_qubits, label='Google', color='tab:green', marker='^', linewidth=2)
ax1.plot(years, microsoft_qubits, label='Microsoft', color='tab:orange', marker='s', linewidth=2)
ax1.plot(years, alibaba_qubits, label='Alibaba', color='tab:red', marker='d', linewidth=2)

# Initialize a secondary axis for the stacked bar chart
ax2 = ax1.twinx()
ax2.bar(years, ibm_qubits, label='IBM', color='tab:blue', alpha=0.2)
ax2.bar(years, google_qubits, bottom=ibm_qubits, label='Google', color='tab:green', alpha=0.2)
ax2.bar(years, microsoft_qubits, bottom=ibm_qubits + google_qubits, label='Microsoft', color='tab:orange', alpha=0.2)
ax2.bar(years, alibaba_qubits, bottom=ibm_qubits + google_qubits + microsoft_qubits, label='Alibaba', color='tab:red', alpha=0.2)

# Add titles and labels
ax1.set_title('Tech Titans\' Race to\nQuantum Supremacy (2020-2030)', fontsize=16, weight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Operational Qubits (Line)', fontsize=12)
ax2.set_ylabel('Cumulative Qubits (Bar)', fontsize=12)

# Customize the legend
line_legend = ax1.legend(loc='upper left', fontsize=10, title='Company (Line)', title_fontsize=12)
bar_legend = ax2.legend(loc='upper right', fontsize=10, title='Cumulative (Bar)', title_fontsize=12)
ax1.add_artist(line_legend)  # To keep both legends on the plot

# Add grid for better readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Highlight a particular milestone
ax1.axvline(x=2025, color='gray', linestyle='--', linewidth=1, alpha=0.7)
ax1.text(2025, 130, 'Mid-decade milestone', fontsize=10, va='center', ha='right', color='gray', rotation=90)

# Annotate specific data points
ax1.annotate('Google exceeds 100 qubits', xy=(2029, 116), xytext=(2028, 120),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='green')

ax1.annotate('IBM: Breakthrough Year', xy=(2027, 90), xytext=(2026.5, 100),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='blue')

# Annotate cumulative growth milestone
ax2.annotate('500+ total qubits', xy=(2028, cumulative_qubits[8]), xytext=(2027, cumulative_qubits[8] + 50),
             arrowprops=dict(facecolor='gray', shrink=0.05), fontsize=10, color='black')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()
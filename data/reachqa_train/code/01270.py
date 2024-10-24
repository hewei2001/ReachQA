import matplotlib.pyplot as plt
import numpy as np

# Define the time periods
years = ['2010', '2015', '2020']

# Percentage distribution of language preferences
# Ensure each period sums to 100%
english = [35, 30, 28]
spanish = [25, 28, 30]
mandarin = [10, 15, 18]
french = [20, 18, 16]
german = [10, 9, 8]

# Convert the percentage data to a numpy array
data = np.array([english, spanish, mandarin, french, german])

# Define the position for each year on the x-axis
x = np.arange(len(years))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each language as a stacked bar
ax.bar(x, english, label='English', color='#1f77b4')
ax.bar(x, spanish, bottom=english, label='Spanish', color='#ff7f0e')
ax.bar(x, mandarin, bottom=np.array(english) + np.array(spanish), label='Mandarin', color='#2ca02c')
ax.bar(x, french, bottom=np.array(english) + np.array(spanish) + np.array(mandarin), label='French', color='#d62728')
ax.bar(x, german, bottom=np.array(english) + np.array(spanish) + np.array(mandarin) + np.array(french), label='German', color='#9467bd')

# Add data labels to each segment for clarity
def add_labels(data):
    for i, (en, sp, ma, fr, ge) in enumerate(zip(english, spanish, mandarin, french, german)):
        ax.text(i, en / 2, f'{en}%', ha='center', va='center', color='white', fontsize=9)
        ax.text(i, en + sp / 2, f'{sp}%', ha='center', va='center', color='white', fontsize=9)
        ax.text(i, en + sp + ma / 2, f'{ma}%', ha='center', va='center', color='white', fontsize=9)
        ax.text(i, en + sp + ma + fr / 2, f'{fr}%', ha='center', va='center', color='white', fontsize=9)
        ax.text(i, en + sp + ma + fr + ge / 2, f'{ge}%', ha='center', va='center', color='white', fontsize=9)

add_labels(data)

# Set the title and axis labels
ax.set_title('Evolution of Language Learning Preferences\nAmong Students (2010-2020)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage of Students (%)', fontsize=12)

# Set the x-ticks with year labels and ensure they are visible
ax.set_xticks(x)
ax.set_xticklabels(years)

# Limit y-axis to 100%
ax.set_ylim(0, 100)

# Customize legend and position
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title="Languages")

# Enhance grid visibility
ax.grid(False)

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()
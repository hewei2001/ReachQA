import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Average citations per article for each journal
mind_citations = np.array([3.5, 3.8, 4.0, 4.5, 5.0, 5.2, 5.5, 5.7, 6.0, 6.2, 6.5])
phil_review_citations = np.array([4.0, 4.2, 4.3, 4.7, 5.0, 5.3, 5.6, 5.9, 6.1, 6.3, 6.6])
journal_philosophy_citations = np.array([3.2, 3.5, 3.7, 4.0, 4.4, 4.6, 4.9, 5.1, 5.4, 5.6, 5.8])
nous_citations = np.array([2.8, 3.0, 3.2, 3.5, 3.7, 3.9, 4.2, 4.4, 4.6, 4.8, 5.0])

# Standard deviation of citations to represent variability
mind_errors = np.array([0.2, 0.25, 0.3, 0.2, 0.35, 0.3, 0.25, 0.3, 0.3, 0.25, 0.3])
phil_review_errors = np.array([0.15, 0.2, 0.25, 0.2, 0.3, 0.25, 0.2, 0.25, 0.3, 0.2, 0.3])
journal_philosophy_errors = np.array([0.25, 0.2, 0.3, 0.25, 0.35, 0.3, 0.2, 0.3, 0.25, 0.3, 0.2])
nous_errors = np.array([0.3, 0.35, 0.3, 0.25, 0.2, 0.25, 0.3, 0.2, 0.25, 0.3, 0.3])

# Create the plot
plt.figure(figsize=(12, 7))

# Plot each journal with error bars
plt.errorbar(years, mind_citations, yerr=mind_errors, fmt='-o', label='Mind', color='blue', capsize=4, alpha=0.8)
plt.errorbar(years, phil_review_citations, yerr=phil_review_errors, fmt='-s', label='The Philosophical Review', color='red', capsize=4, alpha=0.8)
plt.errorbar(years, journal_philosophy_citations, yerr=journal_philosophy_errors, fmt='-^', label='Journal of Philosophy', color='green', capsize=4, alpha=0.8)
plt.errorbar(years, nous_citations, yerr=nous_errors, fmt='-d', label='Nous', color='purple', capsize=4, alpha=0.8)

# Title and labels
plt.title('Philosophy Journal Citations: A Decade\nof Insight and Influence (2010-2020)', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Citations per Article', fontsize=12)

# Customize the axis and grid
plt.xticks(years, rotation=45)
plt.yticks(np.arange(2.5, 7.5, 0.5))
plt.grid(True, linestyle='--', alpha=0.5)

# Add a legend
plt.legend(title='Journals', loc='upper left', fontsize=10, edgecolor='black')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
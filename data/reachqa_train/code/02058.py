import matplotlib.pyplot as plt
import numpy as np

# Define years from 2010 to 2020
years = np.arange(2010, 2021)

# Average citations per article for each journal
mind_citations = np.array([3.5, 3.8, 4.0, 4.5, 5.0, 5.2, 5.5, 5.7, 6.0, 6.2, 6.5])
phil_review_citations = np.array([4.0, 4.2, 4.3, 4.7, 5.0, 5.3, 5.6, 5.9, 6.1, 6.3, 6.6])
journal_philosophy_citations = np.array([3.2, 3.5, 3.7, 4.0, 4.4, 4.6, 4.9, 5.1, 5.4, 5.6, 5.8])
nous_citations = np.array([2.8, 3.0, 3.2, 3.5, 3.7, 3.9, 4.2, 4.4, 4.6, 4.8, 5.0])

# Standard deviation of citations
mind_errors = np.array([0.2, 0.25, 0.3, 0.2, 0.35, 0.3, 0.25, 0.3, 0.3, 0.25, 0.3])
phil_review_errors = np.array([0.15, 0.2, 0.25, 0.2, 0.3, 0.25, 0.2, 0.25, 0.3, 0.2, 0.3])
journal_philosophy_errors = np.array([0.25, 0.2, 0.3, 0.25, 0.35, 0.3, 0.2, 0.3, 0.25, 0.3, 0.2])
nous_errors = np.array([0.3, 0.35, 0.3, 0.25, 0.2, 0.25, 0.3, 0.2, 0.25, 0.3, 0.3])

# Total number of articles published per journal
mind_articles = np.array([120, 130, 140, 145, 150, 155, 160, 165, 170, 175, 180])
phil_review_articles = np.array([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
journal_philosophy_articles = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
nous_articles = np.array([90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the average citations with error bars
ax1.errorbar(years, mind_citations, yerr=mind_errors, fmt='-o', label='Mind', color='blue', capsize=4, alpha=0.8)
ax1.errorbar(years, phil_review_citations, yerr=phil_review_errors, fmt='-s', label='The Philosophical Review', color='red', capsize=4, alpha=0.8)
ax1.errorbar(years, journal_philosophy_citations, yerr=journal_philosophy_errors, fmt='-^', label='Journal of Philosophy', color='green', capsize=4, alpha=0.8)
ax1.errorbar(years, nous_citations, yerr=nous_errors, fmt='-d', label='Nous', color='purple', capsize=4, alpha=0.8)

# Title and labels for the primary y-axis
ax1.set_title('Philosophy Journal Citations & Article Volume (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Citations per Article', fontsize=12)
ax1.set_xticks(years)
ax1.set_yticks(np.arange(2.5, 7.5, 0.5))
ax1.grid(True, linestyle='--', alpha=0.5)

# Create a secondary y-axis for the article volume
ax2 = ax1.twinx()
ax2.bar(years - 0.3, mind_articles, width=0.2, label='Mind Articles', color='blue', alpha=0.3)
ax2.bar(years - 0.1, phil_review_articles, width=0.2, label='Phil Review Articles', color='red', alpha=0.3)
ax2.bar(years + 0.1, journal_philosophy_articles, width=0.2, label='Journal of Philosophy Articles', color='green', alpha=0.3)
ax2.bar(years + 0.3, nous_articles, width=0.2, label='Nous Articles', color='purple', alpha=0.3)
ax2.set_ylabel('Total Number of Articles', fontsize=12)
ax2.set_ylim(0, 200)

# Adding legends
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9), fontsize=10, edgecolor='black', title='Journals & Article Volume')

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plot
plt.show()
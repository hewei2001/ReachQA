import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Recruitment stages and candidate counts
stages = [
    "Applicants",
    "Phone Screening",
    "Technical Test",
    "On-site Interview",
    "Offer Extended",
    "Hired"
]

candidate_counts = [1000, 600, 350, 150, 80, 40]
conversion_rates = [c2 / c1 * 100 for c1, c2 in zip(candidate_counts[:-1], candidate_counts[1:])]

colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
fig.suptitle('TechNovate Recruitment Insights in 2023', fontsize=18, fontweight='bold')

# Funnel Chart
ax1.set_xlim(0, max(candidate_counts) + 200)
ax1.set_ylim(0, len(stages))
for i in range(len(stages) - 1):
    left = (max(candidate_counts) - candidate_counts[i]) / 2
    width_top = candidate_counts[i]
    width_bottom = candidate_counts[i + 1]
    trapezoid = patches.Polygon(
        [
            (left, i),
            (left + width_top, i),
            (left + (width_top + width_bottom) / 2, i + 1),
            (left + (width_top - width_bottom) / 2, i + 1)
        ],
        closed=True, color=colors[i], edgecolor='grey'
    )
    ax1.add_patch(trapezoid)
left = (max(candidate_counts) - candidate_counts[-1]) / 2
rectangle = patches.Rectangle(
    (left, len(stages) - 1), candidate_counts[-1], 1, color=colors[-1], edgecolor='grey'
)
ax1.add_patch(rectangle)
for i, (stage, count) in enumerate(zip(stages, candidate_counts)):
    ax1.text(max(candidate_counts) / 2, i + 0.5, f'{stage}: {count}', va='center', ha='center',
             color='black', fontsize=12, fontweight='bold')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title('Recruitment Funnel', fontsize=14, fontweight='bold')
for spine in ax1.spines.values():
    spine.set_visible(False)

# Bar Chart for Conversion Rates
ax2.barh(stages[1:], conversion_rates, color=colors[1:], edgecolor='grey')
ax2.set_xlim(0, 100)
ax2.set_xlabel('Conversion Rate (%)', fontsize=12)
ax2.set_yticks(range(len(stages) - 1))
ax2.set_yticklabels(stages[1:], fontsize=10, fontweight='bold')
ax2.set_title('Conversion Rates Between Stages', fontsize=14, fontweight='bold')
for i, v in enumerate(conversion_rates):
    ax2.text(v + 1, i, f"{v:.1f}%", va='center', fontsize=10, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
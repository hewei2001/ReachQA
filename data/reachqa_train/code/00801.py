import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
decades = np.arange(1920, 2030, 10)
postal_mail = np.array([90, 80, 70, 60, 50, 40, 20, 10, 5, 3, 1])
telephony = np.array([5, 15, 25, 40, 50, 50, 40, 30, 20, 15, 10])
radio = np.array([2, 3, 10, 20, 15, 10, 5, 3, 2, 1, 1])
television = np.array([0, 1, 5, 10, 30, 40, 40, 35, 30, 25, 20])
internet = np.array([0, 0, 0, 0, 5, 10, 25, 40, 60, 70, 75])
digital_messaging = np.array([0, 0, 0, 0, 0, 0, 10, 20, 30, 35, 40])

# Additional Data for Cumulative Digital Share
digital_share = internet + digital_messaging
predictive_trend = np.array([0, 0, 0, 0, 5, 10, 35, 60, 90, 105, 115])

# Plotting Setup
fig, axs = plt.subplots(1, 2, figsize=(18, 8), gridspec_kw={'width_ratios': [2, 1]})

# Stackplot: Communication Modalities Over Decades
axs[0].stackplot(
    decades, postal_mail, telephony, radio, television, internet, digital_messaging,
    labels=['Postal Mail', 'Telephony', 'Radio', 'Television', 'Internet', 'Digital Messaging'],
    colors=['#d73027', '#4575b4', '#fee08b', '#91cf60', '#1a9850', '#762a83'],
    alpha=0.85
)
axs[0].set_title('Evolution of Communication Modalities\nThrough the Decades (1920s-2020s)', fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel('Decade', fontsize=12)
axs[0].set_ylabel('Percentage Share (%)', fontsize=12)
axs[0].set_xticks(decades)
axs[0].set_xticklabels([f'{year}s' for year in decades], rotation=45, ha='right')
axs[0].grid(True, linestyle='--', alpha=0.5)
axs[0].legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Line Plot: Cumulative Digital Share Prediction
axs[1].plot(decades, digital_share, label='Cumulative Digital Share', color='#762a83', linestyle='-', marker='o')
axs[1].plot(decades, predictive_trend, label='Predicted Trend (2030s)', color='#1a9850', linestyle='--', marker='x')
axs[1].set_title('Digital Communication Growth', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Decade', fontsize=12)
axs[1].set_ylabel('Share (%)', fontsize=12)
axs[1].set_xticks(decades)
axs[1].set_xticklabels([f'{year}s' for year in decades], rotation=45, ha='right')
axs[1].grid(True, linestyle='--', alpha=0.5)
axs[1].legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()
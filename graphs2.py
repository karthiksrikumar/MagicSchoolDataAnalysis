import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

# Set the style
plt.style.use('ggplot')

# Rating data
ratings = {
    '1 (Poor)': 26,
    '2 (Below Average)': 36,
    '3 (Average)': 78,
    '4 (Good)': 142,
    '5 (Excellent)': 47
}

# Create a DataFrame for easier manipulation
df = pd.DataFrame({
    'Rating': list(ratings.keys()),
    'Count': list(ratings.values())
})

# Calculate percentages and summary stats
total = sum(ratings.values())
df['Percentage'] = df['Count'] / total * 100
average_rating = sum([int(k[0]) * v for k, v in ratings.items()]) / total

# Create a figure with 3 subplots
fig = plt.figure(figsize=(18, 14), facecolor='#f8f8f8')
fig.suptitle('MagicSchool AI Classroom Experience Ratings (n=329)', 
             fontsize=24, fontweight='bold', y=0.98)

# Custom color palette - gradient from red to yellow to green
colors = ['#FF4136', '#FF851B', '#FFDC00', '#2ECC40', '#3D9970']

# GRAPH 1: Horizontal Bar Chart
ax1 = fig.add_subplot(311)
bars = ax1.barh(df['Rating'], df['Count'], color=colors, height=0.6, 
               edgecolor='white', linewidth=1.5)
ax1.set_title('Distribution of Ratings (Horizontal Bar Chart)', fontsize=18, pad=15)
ax1.set_xlabel('Number of Responses', fontsize=14)
ax1.set_ylabel('Rating', fontsize=14)

# Add count and percentage annotations
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax1.text(width + 3, bar.get_y() + bar.get_height()/2, 
             f'{df["Count"].iloc[i]} ({df["Percentage"].iloc[i]:.1f}%)', 
             va='center', fontsize=12, fontweight='bold')

# Add average rating annotation
ax1.text(0.02, 0.05, f'Average Rating: {average_rating:.2f}/5', 
         transform=ax1.transAxes, fontsize=14, fontweight='bold',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8))

# GRAPH 2: Pie Chart with 3D effect
ax2 = fig.add_subplot(323, aspect='equal')
wedges, texts, autotexts = ax2.pie(
    df['Count'],
    labels=df['Rating'],
    autopct='%1.1f%%',
    startangle=90,
    explode=[0.05, 0.02, 0, 0, 0.02],  # Slightly explode the 1, 2 and 5 slices
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}
)

# Style the pie chart text
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax2.set_title('Rating Distribution (Pie Chart)', fontsize=18, pad=15)

# GRAPH 3: Stacked Area Chart showing cumulative distribution
ax3 = fig.add_subplot(324)

# Convert ratings to numeric values for the area chart
x = [1, 2, 3, 4, 5]
y_values = [
    [0, 0, 0, 0, 0],  # Empty for bottom layer
    [26, 0, 0, 0, 0],  # Rating 1
    [26, 36, 0, 0, 0],  # Rating 2
    [26, 36, 78, 0, 0],  # Rating 3
    [26, 36, 78, 142, 0],  # Rating 4
    [26, 36, 78, 142, 47]   # Rating 5
]

labels = ['', 'Rating 1', 'Rating 2', 'Rating 3', 'Rating 4', 'Rating 5']

# Create area chart
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)
ax3.stackplot(x, y_values, labels=labels[1:], colors=colors, alpha=0.8)

# Add count annotations
prev_sum = 0
for i, val in enumerate(df['Count']):
    rating_num = i + 1
    count_sum = prev_sum + val
    ax3.text(rating_num, prev_sum + val/2, str(val), 
             ha='center', va='center', fontweight='bold', color='white')
    prev_sum = count_sum

ax3.set_xlim(0.5, 5.5)
ax3.set_ylim(0, total)
ax3.set_xticks(x)
ax3.set_xticklabels(df['Rating'])
ax3.set_xlabel('Rating', fontsize=14)
ax3.set_ylabel('Cumulative Count', fontsize=14)
ax3.set_title('Cumulative Rating Distribution', fontsize=18, pad=15)
ax3.legend(loc='upper left')

# Add a summary textbox with key insights
summary_text = (
    f"Key Insights:\n"
    f"• Total responses: {total}\n"
    f"• Average rating: {average_rating:.2f}/5\n"
    f"• Most common rating: 4 (Good) - {ratings['4 (Good)']} responses ({ratings['4 (Good)']/total*100:.1f}%)\n"
    f"• Positive ratings (4-5): {ratings['4 (Good)']+ratings['5 (Excellent)']} ({(ratings['4 (Good)']+ratings['5 (Excellent)'])/total*100:.1f}%)\n"
    f"• Negative ratings (1-2): {ratings['1 (Poor)']+ratings['2 (Below Average)']} ({(ratings['1 (Poor)']+ratings['2 (Below Average)'])/total*100:.1f}%)"
)

fig.text(0.5, 0.35, summary_text, fontsize=14, 
         bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.9),
         ha='center')

plt.tight_layout()
plt.subplots_adjust(top=0.9, hspace=0.4)
plt.show()

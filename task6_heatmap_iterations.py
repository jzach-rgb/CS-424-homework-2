from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
out = root / 'task6_figures'
out.mkdir(exist_ok=True)
df = pd.read_csv('clean_data.csv')
major = ['Latte', 'Matcha Latte', 'Chai Latte']
d = df.loc[df['Is_Drink'].eq(True) & df['Item'].isin(major) & df['Milk'].notna() & df['Hour'].between(9, 15)].copy()

def build_chart(grouped, labels, filename, title):
    values = grouped.groupby(['Item', 'Period']).agg(n=('Milk', 'size'), oat=('Milk', lambda s: (s == 'Oat').sum()))
    values['percentage'] = values['oat'] / values['n'] * 100
    pct = values['percentage'].unstack('Period').reindex(index=major, columns=labels)
    counts = values['n'].unstack('Period').reindex(index=major, columns=labels)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    colors = plt.get_cmap('YlGnBu').copy()
    colors.set_bad('#e5e5e5')
    arr = pct.where(counts >= 8)
    im = ax.imshow(np.ma.masked_invalid(arr.to_numpy(dtype=float)), cmap=colors, vmin=0, vmax=80, aspect='auto')
    ax.set_xticks(range(len(labels)), labels)
    ax.set_yticks(range(len(major)), major)
    ax.set_xlabel('Hour of day' if len(labels) == 7 else 'Time period')
    ax.set_title(title, pad=16)
    for i, item in enumerate(major):
        for j, period in enumerate(labels):
            n = counts.loc[item, period]
            p = arr.loc[item, period]
            message = 'No data' if pd.isna(n) else (f'n={int(n)}\n<8 records' if pd.isna(p) else f'{p:.0f}%\nn={int(n)}')
            ax.text(j, i, message, ha='center', va='center', fontsize=9, color='white' if pd.notna(p) and p > 45 else 'black')
    fig.colorbar(im, ax=ax, label='% oat among recorded milk types')
    fig.tight_layout()
    fig.savefig(filename, dpi=180)
    plt.close(fig)
    return values

d['Period'] = d['Hour'].map(lambda h: f'{int(h)}:00')
hour_labels = [f'{h}:00' for h in range(9, 16)]
hourly = build_chart(d, hour_labels, 'iteration_1_hourly_with_counts.png', 'Iteration 1: Hourly oat milk share with sample sizes')
d['Period'] = pd.cut(d['Hour'], bins=[8, 10, 12, 15], labels=['9–10 AM', '11 AM–12 PM', '1–3 PM'])
grouped = build_chart(d, ['9–10 AM', '11 AM–12 PM', '1–3 PM'], 'iteration_2_grouped_hours.png', 'Iteration 2: Oat milk share across broader time periods')
hourly.to_csv('hourly_summary.csv')
grouped.to_csv('grouped_summary.csv')


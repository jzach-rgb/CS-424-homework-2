"""Three visualization alternatives for CS 424 Assignment 2.
Run: python task4_visualizations.py (requires pandas matplotlib seaborn? No seaborn, plotly)
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('clean_data.csv');d=df[df['Is_Drink']==True].copy()
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
# A normalized stacked bar: compares specific recorded selections among top 5 drinks
items=d['Item'].value_counts().head(5).index.tolist()
pd_m=d[d.Item.isin(items)&d.Milk.notna()]
mat=pd.crosstab(pd_m.Item,pd_m.Milk).reindex(items).fillna(0)
shares=mat.div(mat.sum(axis=1),axis=0)*100
fig,ax=plt.subplots(figsize=(10,5));shares.plot(kind='barh',stacked=True,ax=ax,colormap='tab20c',width=.7)
ax.set(xlim=(0,100),ylabel='',xlabel='% of records with specified milk',title='Direction A: Milk preferences by drink type')
ax.legend(title='Milk',bbox_to_anchor=(1.01,1),loc='upper left');fig.tight_layout();fig.savefig('A_milk_composition.png',dpi=170);plt.close(fig)
# B heatmap percent selected oat (not just higher volume), 9-15 hourly, 3 drinks
major=['Latte','Matcha Latte','Chai Latte']
a=d[d.Item.isin(major)&d.Milk.notna()&d.Hour.between(9,15)].copy()
g=a.groupby(['Item','Hour']).agg(n=('Milk','size'),oat=('Milk',lambda s:(s=='Oat').sum()))
g['percentage']=100*g['oat']/g['n'];g.loc[g.n<8,'percentage']=np.nan
pivot=g.percentage.unstack('Hour').reindex(major).reindex(columns=range(9,16))
fig,ax=plt.subplots(figsize=(9,3.8));cmap=plt.get_cmap('YlGnBu').copy();cmap.set_bad('#e5e5e5')
im=ax.imshow(np.ma.masked_invalid(pivot.values),vmin=0,vmax=80,cmap=cmap,aspect='auto')
ax.set_xticks(range(7),[f'{h}:00' for h in range(9,16)]);ax.set_yticks(range(3),major)
for i in range(len(major)):
 for j,h in enumerate(range(9,16)):
  v=pivot.iloc[i,j];ax.text(j,i,'—' if pd.isna(v) else f'{v:.0f}%',ha='center',va='center',fontsize=9,color='white' if pd.notna(v) and v>43 else 'black')
ax.set(title='Direction B: Oat share by time and drink (n≥8)',xlabel='Hour of day');fig.colorbar(im,ax=ax,label='% oat among known milks');fig.tight_layout();fig.savefig('B_oat_hour_heatmap.png',dpi=170);plt.close(fig)
# C multi-series line chart: within-drink hourly distribution (not total volume)
# Restrict to the normal 9am–3pm observation window.
major=['Latte','Matcha Latte','Chai Latte']
line_data=d[d.Item.isin(major)&d.Hour.between(9,15)].copy()
hour_counts=pd.crosstab(line_data.Hour,line_data.Item).reindex(index=range(9,16),columns=major,fill_value=0)
# Each line sums to 100% across the displayed hours to compare timing independent of drink popularity.
hour_pct=hour_counts.div(hour_counts.sum(axis=0),axis=1)*100
fig,ax=plt.subplots(figsize=(10,5))
for name in major:
    ax.plot(hour_pct.index,hour_pct[name],marker='o',linewidth=2.2,label=f'{name} (n={hour_counts[name].sum():,})')
ax.set_xticks(range(9,16),[f'{h}:00' for h in range(9,16)])
ax.set_ylim(bottom=0)
ax.set(xlabel='Hour of day',ylabel='% of that drink type sold during 9 AM–3 PM',title='Direction C: When are different drinks purchased?')
ax.grid(axis='y',alpha=.25)
ax.legend(title='Drink type',frameon=False)
fig.tight_layout()
fig.savefig('C_drink_hourly_lines.png',dpi=180)
plt.close(fig)
print('C hour counts\n',hour_counts.to_string())


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gms_export.csv')

df['Multiple Instances'] = df['Organization: Organization Name'].duplicated(keep=False)
df['Multiple Instances'] = df['Multiple Instances'].apply(lambda x: 'Yes' if x else 'No')

df_multiple = df[df['Multiple Instances'] == 'Yes']

df_multiple.to_csv('gms_export_multiple_instances.csv', index=False)

grouped_data = df_multiple.groupby(['Organization: Organization Name', 'Top Level Primary Program']).size().unstack(fill_value=0)
grouped_data = grouped_data.sort_index(ascending=True)

num_rows = grouped_data.shape[0]

fig_height = max(8, num_rows * 0.4)

plt.figure(figsize=(10, fig_height))
grouped_data.plot(kind='barh', stacked=True, figsize=(10, fig_height))
plt.gca().invert_yaxis() 

plt.text(0, num_rows + 1, f'Total Number of Rows: {num_rows}', ha='left', fontsize=12, fontweight='bold')

plt.xlabel('Number of Records')
plt.ylabel('Organization Name')
plt.title('Records per Organization by Top Level Primary Program')

plt.tight_layout()
plt.savefig('organization_records_stacked_chart.pdf', format='pdf', dpi=300)
plt.show()
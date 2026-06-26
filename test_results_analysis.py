import os
import pandas as pd
from scipy.stats import wilcoxon

# Directory paths
parent_dir = os.getcwd()

# Final results dataframe
res_df = pd.read_csv(os.path.join(parent_dir,"ACII_4500tw_40ts.tsv"), sep='\t')

# Select the best performing model at each
max_rows = res_df.loc[res_df.groupby(['d_s','seed','k'])['e_acc'].idxmax()]
max_rows = max_rows.reset_index(drop=True)
res_df = max_rows

# Calculate differences
ref_values = res_df[res_df['d_s'] == 0].rename(columns={'e_acc': 'ref_acc'})
ref_values = ref_values[['k', 'seed', 'ref_acc']]
res_df = res_df.merge(ref_values, on =['k', 'seed'], how='left')
res_df['delta(X)'] = res_df['e_acc'] - res_df['ref_acc']

# Mapping dictionary
mapping = {0: 'Ø', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
res_df['d_s'] = res_df['d_s'].replace(mapping)

avg_res = []
for strat in ['Ø','A','B','C','D']:
	if strat != 'Ø':
		stat, p_value = wilcoxon(res_df[res_df['d_s'] == strat]['delta(X)'], alternative='greater')
	avg_res.append({
		"$\mathcal{M}": strat,
		"$\delta(X)$": 'N/A' if strat == 'Ø' else f"{res_df[res_df['d_s'] == strat]['delta(X)'].mean():.4f}",
		"Acc.": f"{res_df[res_df['d_s'] == strat]['e_acc'].mean():.4f}",
		"Prec.": f"{res_df[res_df['d_s'] == strat]['e_prec'].mean():.4f}",
		"Rec.": f"{res_df[res_df['d_s'] == strat]['e_recall'].mean():.4f}",
		"F1": f"{res_df[res_df['d_s'] == strat]['e_f1'].mean():.4f}",
		"p-val": 'N/A' if strat == 'Ø' else p_value
	})

avg_df = pd.DataFrame(avg_res)
avg_df.to_csv(os.path.join(parent_dir,"ACII_avg_results.tsv"), sep='\t', index=False)
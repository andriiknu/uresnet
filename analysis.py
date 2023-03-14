import csv
import numpy as np

labels = ["HIP", "MIP", "EM shower", "Delta rays", "Michel electron", "mean"]
with open('log/varience/metrics_log-0000000.csv') as f:
    reader = csv.DictReader(f)
    acc = np.array([[np.float32(row[key]) for key in [f"class_{i}_acc" for i in range(5)]+["acc"]] for row in reader])
mean = np.nanmean(acc,axis=0)*100
assert len(mean) == 6
print(f"mean accuracy over {len(acc)} events: ")
# print(labels)
for i, label in enumerate(labels):
    print('%s\t%.1f'%(label,mean[i]))

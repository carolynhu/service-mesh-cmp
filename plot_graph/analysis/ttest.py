import scipy.stats as stats

pre=[8457, 8157, 7682, 9318, 9277, 8510, 14662, 15875, 16376, 16252, 14777, 15481, 15883, 14272, 18042]
post=[15131, 18587, 15117, 15655, 16421, 15826, 15766, 15324, 15349, 15370, 15605, 15427, 17201, 15880, 15577]

print(len(pre))
print(len(post))

ttest = stats.ttest_rel(pre,post)
print(ttest)


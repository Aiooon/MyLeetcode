
"""
Recall(召回率) = TP/(TP+FN)
Precision(準確率) = TP/(TP+FP)
F1-score = 2 * Precision * Recall / (Precision + Recall)
"""

# 67.75 & 55.89 & 61.25

P = 68.12
R = 56.33
F1 = 2 * P * R / (P + R)
print(F1)


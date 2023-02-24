sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_k, min_v = next(iter(sample_dict.items()))
for k, v in sample_dict.items():
    if v < min_v:
        min_v, min_k = v, k
print(min_k)

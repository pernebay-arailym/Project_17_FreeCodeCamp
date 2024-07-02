from mean_var_std import calculate

# Example test
try:
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
except ValueError as e:
    print(e)

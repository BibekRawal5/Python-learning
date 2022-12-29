import pandas as pd
import numpy as np

ser = pd.Series([2,3,4,5,1,43])

print(ser)


certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

print(certificates_earned)

print(certificates_earned.shape)
print(certificates_earned.size)
print(certificates_earned.head())
print(certificates_earned.info())
print(certificates_earned.columns)
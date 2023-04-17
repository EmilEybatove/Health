import pandas as pd
import numpy as np

df = pd.read_csv("merget_Helth.csv")
df = df[df.columns[1:]]
df = df.replace([".d", ".r", ".x", ".q", ".u", ".v", ".s", ".m", ".w", ".p", ".y", ".c", ".e", ".t", ".z"], np.NaN)
df.to_csv("new_Health_with_nan.csv")
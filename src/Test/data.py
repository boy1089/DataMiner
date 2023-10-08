import pandas as pd
import numpy as np

# Create a datetime range from 0:00 to 24:00 with 100 evenly spaced values
datetime_range = pd.date_range("2023-01-01", "2023-01-05", periods=100)

# Generate random float values for columns a to i
data = {
    "datetime": datetime_range,
    "a": np.random.rand(100),
    "b": np.random.rand(100),
    "c": np.random.rand(100),
    "d": np.random.rand(100),
    "e": np.random.rand(100),
    "f": np.random.rand(100),
    "g": np.random.rand(100),
    "h": np.random.rand(100),
    "i": np.random.rand(100),
    "i": np.random.rand(100),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print(df.head())

print(df['datetime'])
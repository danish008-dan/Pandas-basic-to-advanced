# Pandas-basic-to-advanced


# 🐼 Pandas Notes (Basic → Advanced)

This repository contains **well-structured notes on Pandas** (with examples from basic to advanced level).  
It covers **Series, DataFrames, Import/Export, Missing Data Handling, GroupBy, Pivot Tables**, and much more.  
These notes are beginner-friendly and useful for revision, projects, and interviews.

---

## 📌 Topics Covered

1. Introduction to Pandas
2. Creating Series
   - From list, numpy array, dictionary
   - Built-in functions
   - Indexing & operations
3. Creating DataFrames
   - From dictionary
   - Adding columns
   - Filtering rows
4. Handling Missing Data
   - Checking null values
   - Dropping null values
   - Filling null values
   - Interpolation
5. Import & Export
   - Reading CSV
   - Writing CSV
6. Sorting
7. Joins & Merge
8. Concatenation
9. GroupBy & Aggregations
10. Advanced Concepts
    - Apply function
    - Pivot Tables

---

## 🚀 Code Example

```python
import pandas as pd
import numpy as np

# Create DataFrame
data = {"Name": ["Danish", "Khatri"], "Age": [20, 19]}
df = pd.DataFrame(data)

# Add new column
df["City"] = ["Sikar", "Jaipur"]

print(df)



OUTPUT :

     Name  Age    City
0  Danish   20   Sikar
1  Khatri   19  Jaipur

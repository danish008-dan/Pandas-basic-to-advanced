# =========================================================
# 📘 PANDAS NOTES (BASIC TO ADVANCED) - 2025
# Author : Danish Khatri
# =========================================================

# 🔹 Import Libraries
import pandas as pd
import numpy as np

# =========================================================
# 1️⃣ Pandas Introduction
# =========================================================
# Pandas is a Python library for:
#  - Data Cleaning
#  - Data Transformation
#  - Data Analysis
#  - Handling CSV, Excel, SQL, JSON files etc.
# Works with two main data structures:
#   👉 Series (1D - like array or list)
#   👉 DataFrame (2D - like table in SQL/Excel)

# =========================================================
# 2️⃣ Creating Series
# =========================================================

# From list
a = [1, 2, 3]
b = ["a", "b", "c"]
s1 = pd.Series(data=b, index=a)
print("\nSeries from list:\n", s1)

# From numpy array
a1 = np.array([10, 20, 30, 40, 90, 70, 50])
s2 = pd.Series(data=a1)
print("\nSeries from numpy array:\n", s2)

# From dictionary
d1 = {"a": 10, "b": 50, "c": 90}
s3 = pd.Series(data=d1)
print("\nSeries from dictionary:\n", s3)

# Built-in functions on Series
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
s4 = pd.Series(data=[sum(l1), max(l1), np.mean(l1)])
print("\nBuilt-in functions (sum, max, average):\n", s4)

# Accessing elements by index
s5 = pd.Series(data=[10, 20, 30, 40], index=[1, 22, 33, 44])
print("\nAccess by index:", s5[22])
print("\nComplete Series:\n", s5)

# Adding two Series
l2 = [10, 90, 20, 40, 55, 33]
l3 = [22, 33, 44]
s6 = pd.Series(data=[sum(l2), max(l2), min(l2)])
s7 = pd.Series(data=[sum(l3), max(l3), min(l3)])
print("\nSeries 1:\n", s6)
print("\nSeries 2:\n", s7)
print("\nAddition of Series:\n", s6 + s7)

# =========================================================
# 3️⃣ DataFrame Creation
# =========================================================

# From dictionary
data = {"Name": ["Danish", "Khatri"], "Age": [20, 19]}
df = pd.DataFrame(data)
print("\nDataFrame from dictionary:\n", df)

# Add new column
df["City"] = ["Sikar", "Jaipur"]
print("\nAfter adding column:\n", df)

# =========================================================
# 4️⃣ DataFrame Operations
# =========================================================

# Filtering
f1 = df[df["Age"] > 19]
print("\nFiltered DataFrame (Age > 19):\n", f1)

# Checking null values
null = df.isnull()
print("\nCheck null values:\n", null)

# Dropping null values
df2 = df.dropna()
print("\nAfter dropping nulls:\n", df2)

# Filling null values
df1 = pd.DataFrame({"Name": ["Danish", "Ali"], "Age": [25, None]})
df3 = df1.fillna(20)
print("\nFill missing values:\n", df3)

# =========================================================
# 5️⃣ Importing & Exporting Data
# =========================================================

# CSV Import
# df_csv = pd.read_csv("electric_vehicles_spec_2025.csv")
# print(df_csv.head())  # show first 5 rows

# CSV Export
# df_csv.to_csv("output.csv", index=False)

# =========================================================
# 6️⃣ Sorting Data
# =========================================================
df3 = pd.DataFrame({"Name": ["Ajay", "Danish", "Saim", "Ali", "Atul"],
                    "Age": [20, 41, 52, 12, 23]})
print("\nOriginal DataFrame:\n", df3)
print("\nSorted by Age:\n", df3.sort_values(by="Age"))

# =========================================================
# 7️⃣ Joins and Merging
# =========================================================

df4 = pd.DataFrame({"id": [1, 2], "Name": ["Yash", "Danish"]})
df5 = pd.DataFrame({"id": [1, 2], "Marks": [88, 99]})
merged = pd.merge(df4, df5, on="id")
print("\nMerged DataFrame (INNER JOIN):\n", merged)

# =========================================================
# 8️⃣ Concatenation
# =========================================================
df6 = pd.DataFrame({"Name": ["Aman"], "Age": [35]})
df7 = pd.DataFrame({"Name": ["Danish"], "Age": [20]})

df_all = pd.concat([df6, df7])
print("\nConcatenated DataFrame:\n", df_all)

# Reset index
df_all = df_all.reset_index(drop=True)
print("\nAfter resetting index:\n", df_all)

# Set index
df_all = df_all.set_index("Name")
print("\nAfter setting 'Name' as index:\n", df_all)

# =========================================================
# 9️⃣ GroupBy & Aggregations
# =========================================================
df_group = pd.DataFrame({
    "Name": ["A", "B", "A", "B", "C", "C", "C"],
    "Marks": [50, 60, 70, 80, 90, 40, 30]
})
print("\nGroupBy Example:\n", df_group.groupby("Name")["Marks"].mean())

# =========================================================
# 🔟 Advanced Topics
# =========================================================
# ➡ Apply Function
df_adv = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]})
df_adv["Sum"] = df_adv.apply(lambda x: x["A"] + x["B"], axis=1)
print("\nApply function:\n", df_adv)

# ➡ Handling Missing Data with Interpolation
df_missing = pd.DataFrame({"Value": [10, np.nan, 30, np.nan, 50]})
print("\nBefore interpolation:\n", df_missing)
print("\nAfter interpolation:\n", df_missing.interpolate())

# ➡ Pivot Table
df_pivot = pd.DataFrame({
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Year": [2023, 2024, 2023, 2024],
    "Sales": [250, 300, 200, 400]
})
print("\nPivot Table Example:\n", df_pivot.pivot_table(values="Sales", index="City", columns="Year"))

# =========================================================
# ✅ END OF NOTES
# =========================================================

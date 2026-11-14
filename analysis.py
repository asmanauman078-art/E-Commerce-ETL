import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv("outputs/products.csv")

# DISPLAY FIRST 5 PRODUCTS
print("First 5 Products:")
print(df.head())

# DATASET INFORMATION
print("\nDataset Information:")
print(df.info())
# CATEGORY ANALYSIS
print("\nProducts by Category:")
print(df["category"].value_counts())

# AVERAGE PRICE
print("\nAverage Product Price:")
print(df["price"].mean())

# MOST EXPENSIVE PRODUCT
print("\nMost Expensive Product:")
print(df.loc[df["price"].idxmax()])
# CATEGORY BAR CHART
category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 5))
category_counts.plot(kind="bar")

plt.title("Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("reports/category_chart.png")
plt.show()
# PRICE ANALYSIS CHART
plt.figure(figsize=(10, 5))

plt.hist(df["price"], bins=10)

plt.title("Product Price Distribution")
plt.xlabel("Product Price")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("reports/price_chart.png")
plt.show()
# PRODUCT RATING ANALYSIS
plt.figure(figsize=(10, 5))

plt.hist(df["rating"], bins=10)

plt.title("Product Rating Distribution")
plt.xlabel("Product Rating")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("reports/rating_chart.png")
plt.show()
import pandas as pd


file_path = r"C:\Users\gokul\Documents\tech_products.csv"
df = pd.read_csv(file_path)


print("\n📦 Dataset Structure:")
print(df.info())


print("\n🧾 First 5 rows:")
print(df.head())


print("\n🔍 Missing values:")
print(df.isnull().sum())


print("\n📄 Data Types:")
print(df.dtypes)


print("\n📊 Descriptive Statistics:")
print(df.describe())


print("\n💸 Most Expensive Product:")
print(df.sort_values(by='Price', ascending=False).head(1))


print("\n🌟 Highest Rated Product:")
print(df.sort_values(by='Rating', ascending=False).head(1))


print("\n📈 Products per Category:")
print(df['Category'].value_counts())


print("\n💰 Average Price by Brand:")
print(df.groupby('Brand')['Price'].mean())


print("\n⭐ Average Rating by Category:")
print(df.groupby('Category')['Rating'].mean())

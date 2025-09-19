import pandas as pd
import matplotlib.pyplot as plt
import os


# Load dataset
df = pd.read_excel(r"d:\foodanalysis\foodproject\online_food_delivery_data.xlsx", engine="openpyxl")

print("File loaded:", df.shape)


# Cleaning
# Make column names consistent: remove spaces and convert to lowercase
df.columns = df.columns.str.strip().str.lower()

# Convert order date column to datetime format
df["order date"] = pd.to_datetime(df["order date"], errors="coerce")
df.drop_duplicates(inplace=True)

# Handle missing values properly 
df["payment method"] = df["payment method"].fillna("Cash Discount")   # Fill missing payment method
df["restaurant name"] = df["restaurant name"].fillna("Unknown")       # Fill missing restaurant names
df["food rating"] = df["food rating"].fillna(0)                       # Fill missing ratings with 0
df["quantity"] = df["quantity"].fillna(0)                             # Replace missing quantities with 0
df["total bill"] = df["total bill"].fillna(0)                         # Replace missing total bills with 0


# 1. Bar Chart: Top 10 Restaurants by Total Sales
top_restaurants = df.groupby("restaurant name")["total bill"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_restaurants.plot(kind="bar", color="skyblue")
plt.title("Top Restaurants by Total Sales")
plt.xlabel("Restaurant")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# 2. Line Chart: Daily Total Sales over Time
daily_sales = df.groupby("order date")["total bill"].sum()

plt.figure(figsize=(12,6))
daily_sales.plot(kind="line", marker='o', color="orange")
plt.title("Daily Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()


# 3. Histogram: Distribution of Food Ratings
plt.figure(figsize=(8,5))
df["food rating"].plot(kind="hist", bins=5, color="pink", rwidth=0.8)
plt.title("Distribution of Food Ratings")
plt.xlabel("Food Rating")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


# 4. Pie Chart: Payment Methods Share
payment_share = df["payment method"].value_counts()

plt.figure(figsize=(8,7))
payment_share.plot(kind="pie", autopct='%1.1f%%', startangle=170, shadow=True)
plt.title("Payment Methods Share")
plt.ylabel("") # Remove unnecessary y-label
plt.show()


# 5. Scatter Plot: Quantity vs Total Bill
plt.figure(figsize=(10,6))
plt.scatter(df["quantity"], df["total bill"], alpha=0.6, color='purple')
plt.title("Quantity vs Total Bill")
plt.xlabel("Quantity")
plt.ylabel("Total Bill")
plt.grid(True)
plt.show()


# 6. Top 5 States by Orders
top_states = df["state"].value_counts().head(5)

plt.figure(figsize=(10,6))
top_states.plot(kind="bar", color="teal")
plt.title("Top 5 States by Number of Orders")
plt.xlabel("State")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.grid(axis='y')
plt.show()


# 7. Average Food Rating per Restaurant
avg_rating_restaurant = df.groupby("restaurant name")["food rating"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
avg_rating_restaurant.plot(kind="barh", color="coral")
plt.title("Top Restaurants by Average Food Rating")
plt.xlabel("Average Rating")
plt.ylabel("Restaurant")
plt.gca().invert_yaxis()  # Puts highest rating at the top
plt.show()


# Save cleaned Excel file (overwrite if exists)
output_file = r"d:\foodanalysis\foodproject\online_food_delivery_data.xlsx"


# Remove the file first if it exists to avoid PermissionError
if os.path.exists(output_file):
    os.remove(output_file)

# Save cleaned dataframe to Excel
df.to_excel(output_file, index=False)
print(f"Cleaned data saved as: {output_file}")

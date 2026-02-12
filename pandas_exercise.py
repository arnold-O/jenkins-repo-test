import pandas as pd

print("=== Pandas Age Exercise ===")

# Create a sample dataset of people and their ages
data = {
    "Name": ["Alex", "Bob", "Charlie", "Edith", "Evan"],
    "Age": [15, 17, 16, 14, 18]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

# Calculate statistics
average_age = df["Age"].mean()
max_age = df["Age"].max()
min_age = df["Age"].min()

print("\nAge Statistics:")
print(f"Average age: {average_age}")
print(f"Oldest age: {max_age}")
print(f"Youngest age: {min_age}")

# Add a new column
df["Is_Teen"] = df["Age"].between(13, 19)

print("\nUpdated DataFrame:")
print(df)

print("\nExercise completed successfully!")

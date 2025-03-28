import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

# Display basic information about the dataset
print("Dataset Overview:\n")
print(df.info())

# Display the first few rows
print("\nFirst 5 Rows:\n")
print(df.head())

# Check for missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# fill missing Age values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# fill mising Embarked values with the most common category (mode)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop the 'Cabin' column since it has too many missing values
df.drop(columns=["Cabin"], inplace=True)

# Verify changes
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Feature Engineering

# Create FamilySize feature (SibSp + Parch)
df["FamilySize"] = df["SibSp"] + df["Parch"]

# Create IsAlone feature (1 if FamilySize is 0, else 0)
df["IsAlone"] = (df["FamilySize"] == 0).astype(int)

# Convert 'Sex' to numeric (0 = Female, 1 = Male)
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# Display first 5 rows after feature engineering
print("\nFirst 5 Rows After Feature Engineering:\n")
print(df.head())

import matplotlib.pyplot as plt

# Insight 1: Survival rate by gender
survival_by_gender = df.groupby("Sex")["Survived"].mean()
print("\nSurvival Rate by Gender:\n", survival_by_gender)

# Insight 2: Survival rate by FamilySize
survival_by_family_size = df.groupby("IsAlone")["Survived"].mean()
print("\nSurvival Rate by Family Size (IsAlone=1 means alone):\n", survival_by_family_size)

# Insight 3: Survival rate by Passenger Class
survival_by_pclass = df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate by Passenger Class:\n", survival_by_pclass)

# Visualization: Survival rate by Passenger Class
survival_by_pclass.plot(kind="bar", color=["blue", "orange", "green"])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.show()


import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(df):
    # Handle missing values for numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

    # Scale numerical columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Encode categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    return df

# Example usage and testing
data = {
    'numeric_col1': [1.2, 2.3, 3.4, None, 5.6],
    'numeric_col2': [10, 20, 30, 40, 50],
    'category_col': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

processed_df = preprocess_data(df)

print("\nProcessed DataFrame:")
print(processed_df)

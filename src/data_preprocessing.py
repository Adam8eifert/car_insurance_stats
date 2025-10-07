import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    """Loads the CSV data and performs initial cleanup (type conversion)."""
    # Load the CSV file. Assume 'NaN' or empty strings are handled by pandas
    data = pd.read_csv(file_path)

    # Rename the target variable for consistency with the project brief
    data = data.rename(columns={'outcome': 'Response'})

    # Ensure numeric columns are correctly typed (crucial after SQL cleanup)
    # Use errors='coerce' to turn any remaining problematic strings into NaN
    data['credit_score'] = pd.to_numeric(data['credit_score'], errors='coerce')
    data['annual_mileage'] = pd.to_numeric(data['annual_mileage'], errors='coerce')

    return data

def impute_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Handles missing values using statistical imputation methods."""
    print("Starting imputation of missing values...")

    # 1. Impute 'credit_score' (numeric) with the MEDIAN
    median_credit_score = data['credit_score'].median()
    data['credit_score'].fillna(median_credit_score, inplace=True)
    print(f"  -> 'credit_score' imputed with median: {median_credit_score:.4f}")

    # 2. Impute 'annual_mileage' (numeric) with the MEAN
    mean_annual_mileage = data['annual_mileage'].mean()
    data['annual_mileage'].fillna(mean_annual_mileage, inplace=True)
    # Convert back to integer (as mileages are typically whole numbers)
    data['annual_mileage'] = data['annual_mileage'].astype(int)
    print(f"  -> 'annual_mileage' imputed with mean: {mean_annual_mileage:.0f}")

    # 3. Impute categorical columns (if any NULLs remained) with 'Unknown'
    # For this dataset, primary missing values were numeric, but this is good practice.
    categorical_cols_to_check = ['education', 'income', 'vehicle_type']
    for col in categorical_cols_to_check:
        if data[col].isnull().any():
            data[col].fillna('Unknown', inplace=True)
            print(f"  -> '{col}' imputed with 'Unknown'")

    return data

def create_features(data: pd.DataFrame) -> pd.DataFrame:
    """Performs Feature Engineering (creation of new predictive variables)."""
    print("Starting Feature Engineering...")

    # A) Categorize annual_mileage (simulating Annual_Premium categorization)
    # Creates 3 logical groups: Low, Medium, High
    bins = data['annual_mileage'].quantile([0, 0.33, 0.66, 1.0]).values
    labels = ['Nízký_Nájezd', 'Střední_Nájezd', 'Vysoký_Nájezd']

    data['Mileage_Category'] = pd.cut(
        data['annual_mileage'],
        bins=bins,
        labels=labels,
        include_lowest=True,
        duplicates='drop'
    )
    print("  -> 'Mileage_Category' created (3 bins based on quantiles).")


    # B) Ratio Metric: Credit Score to Annual Mileage Ratio
    # This new column represents the balance between financial trustworthiness and risk exposure
    # Add 1 to mileage to prevent division by zero (safety measure)
    data['Credit_to_Mileage_Ratio'] = data['credit_score'] / (data['annual_mileage'] + 1)
    print("  -> 'Credit_to_Mileage_Ratio' created.")

    return data

if __name__ == "__main__":
    # Define file paths based on the agreed structure
    INPUT_FILE = './data/processed/car_insurance_claim.csv'
    OUTPUT_FILE = './data/processed/car_insurance_claim_clean.csv'

    try:
        # Load and clean data
        data = load_data(INPUT_FILE)

        # Impute missing values
        data = impute_missing_values(data)

        # Create new features
        data = create_features(data)

        # Final check and save the cleaned, feature-rich data
        print(f"\nFinal dataset shape: {data.shape}")
        data.to_csv(OUTPUT_FILE, index=False)
        print(f"Successfully saved clean data to {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {INPUT_FILE}. Check your file structure.")
    except Exception as e:
        print(f"An unexpected error occurred during preprocessing: {e}")
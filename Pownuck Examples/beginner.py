import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# URLs for datasets
datasets = {
    "SO2TONS": "https://raw.githubusercontent.com/apownukepcc/ForecastingDailyEmissions/refs/heads/main/SO2TONS_dataset.csv",
    "NOXTONS": "https://raw.githubusercontent.com/apownukepcc/ForecastingDailyEmissions/refs/heads/main/NOXTONS_dataset.csv",
    "COTONS": "https://raw.githubusercontent.com/apownukepcc/ForecastingDailyEmissions/refs/heads/main/COTONS_dataset.csv"
}

# Define the peak season months (May through August)
peak_season_months = [5, 6, 7, 8]

# Define lakes (sources)
sources = ["LAKE-1", "LAKE-2", "LAKE-3", "LAKE-4"]

# Define the specific day for prediction
specific_date = pd.Timestamp("2022-07-15")

# Initialize a dictionary to store models, predictions, and inputs for verification
models = {}
predictions = {}

# Loop through each dataset (SO2TONS, NOXTONS, COTONS)
for parameter, url in datasets.items():
    # Load the dataset
    data = pd.read_csv(url)

    # Convert the 'date' column to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Filter for peak season
    data = data[data['date'].dt.month.isin(peak_season_months)]

    # Separate data by source
    for source in sources:
        source_data = data[data['Source'] == source]

        # Check if the source data has enough rows
        if source_data.empty or len(source_data) < 10:
            print(f"Not enough data for {parameter} at {source}. Skipping...")
            continue

        # Define predictors (e.g., weather features)
        predictors = ['tavg', 'tmin', 'tmax', 'prcp', 'snow', 'wdir', 'wspd', 'pres']
        target = 'Value'

        # Drop rows with missing values
        source_data = source_data.dropna(subset=predictors + [target])

        # Split the data into features (X) and target (y)
        X = source_data[predictors]
        y = source_data[target]

        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Regressor
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        print(f"Model for {parameter} at {source}:")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  R²: {r2:.4f}")

        # Save the model
        models[(parameter, source)] = model

        # Check if the specific date exists in the source data
        day_data = source_data[source_data['date'] == specific_date]
        if not day_data.empty:
            # Extract feature values for the specific day
            specific_features = day_data[predictors].iloc[[0]]  # Use a DataFrame to retain feature names
            specific_actual = day_data[target].iloc[0]

            # Predict emissions/load for the specific day
            specific_prediction = model.predict(specific_features)[0]

            # Save the prediction and actual value for verification
            predictions[(parameter, source)] = {
                "features": day_data[predictors].iloc[0],
                "actual": specific_actual,
                "predicted": specific_prediction
            }

# Display all predictions at the end
print("\nFinal Predictions:")
for key, value in predictions.items():
    parameter, source = key
    print(f"{parameter} at {source}:")
    print(f"  Features: {value['features'].to_dict()}")
    print(f"  Actual Emissions_Load: {value['actual']:.4f}")
    print(f"  Predicted Emissions_Load: {value['predicted']:.4f}")
    print()

for (parameter, source), result in predictions.items():
    if result:
        plt.figure(figsize=(10, 5))

        # Convert dates for plotting
        dates = result["dates"]
        actual_values = result["actual"]
        predicted_values = result["predicted"]

        plt.plot(dates, actual_values, label="Actual Emissions", color="blue", marker="o", linestyle="-")
        plt.plot(dates, predicted_values, label="Predicted Emissions", color="red", marker="x", linestyle="--")

        plt.xlabel("Date")
        plt.ylabel("Emissions (Tons)")
        plt.title(f"Actual vs. Predicted Emissions for {parameter} at {source}")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.show()
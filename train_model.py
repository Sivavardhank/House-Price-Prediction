import pandas as pd
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Metrics
from sklearn.metrics import mean_absolute_error, r2_score

import joblib
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
data = pd.read_csv('data/housing.csv')

X = data[['Avg. Area Income', 'Avg. Area House Age',
          'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
          'Area Population']]
y = data['Price']

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Models
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = []

# -----------------------------
# Train & Evaluate
# -----------------------------
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    
    results.append([name, mae, r2])

# -----------------------------
# Results Table
# -----------------------------
results_df = pd.DataFrame(results, columns=["Model", "MAE", "R2 Score"])
results_df = results_df.sort_values(by="R2 Score", ascending=False)

print("\nModel Comparison:\n")
print(results_df)

# -----------------------------
# Train Final Model (Random Forest)
# -----------------------------
final_model = RandomForestRegressor(n_estimators=100, random_state=42)
final_model.fit(X_train, y_train)

# Save model
joblib.dump(final_model, 'model/house_price_model.pkl')

# -----------------------------
# Feature Importance
# -----------------------------
importances = final_model.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, importances)
plt.xlabel("Importance")
plt.title("Feature Importance")
plt.savefig("app/static/feature.png")

print("\nModel trained, compared, and feature graph saved!")

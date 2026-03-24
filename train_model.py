import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
data = pd.read_csv('data/housing.csv')

# Features and target
X = data[['Avg. Area Income', 'Avg. Area House Age',
          'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
          'Area Population']]
y = data['Price']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print(f"\n{name}")
    print("MAE:", mean_absolute_error(y_test, pred))
    print("R2 Score:", r2_score(y_test, pred))
# Save model
joblib.dump(model, 'model/house_price_model.pkl')

print("✅ Model trained and saved!")

from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('../model/house_price_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    price = None

    if request.method == 'POST':
        try:
            income = float(request.form['income'])
            age = float(request.form['age'])
            rooms = float(request.form['rooms'])
            bedrooms = float(request.form['bedrooms'])
            population = float(request.form['population'])

            features = np.array([[income, age, rooms, bedrooms, population]])
            prediction = model.predict(features)[0]

            price = f"${prediction:,.2f}"

        except:
            price = "Invalid Input ❌"

    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
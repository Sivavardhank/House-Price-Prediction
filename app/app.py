from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model/house_price_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    price = None

    if request.method == 'POST':
        try:
            features = [
                float(request.form['income']),
                float(request.form['age']),
                float(request.form['rooms']),
                float(request.form['bedrooms']),
                float(request.form['population'])
            ]

            prediction = model.predict([features])[0]
            price = f"${prediction:,.2f}"
        except:
            price = "Invalid Input"

    return render_template('index.html', price=price)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)

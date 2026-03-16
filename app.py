from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    features = np.array([[
        float(data['MedInc']),
        float(data['HouseAge']),
        float(data['AveRooms']),
        float(data['AveBedrms']),
        float(data['Population'])
    ]])
    
    prediction = model.predict(features)[0]
    final_price = round(prediction * 100000, 2)
    
    return jsonify({'prediction': final_price})

if __name__ == '__main__':
    app.run(debug=True)
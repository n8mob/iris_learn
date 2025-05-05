import joblib

# load the trained model
model = joblib.load('iris_model.pkl')

# Example input (first iris sample)
example = [[5.1, 3.5, 1.4, 0.2]]
pred = model.predict(example)

print(f'Prediction: {pred}')

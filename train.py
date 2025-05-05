from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# load built-in dataset
X, y = load_ires(return_X_y=True)

# train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# save model to file
save_file = 'iris_model.pkl'
joblib.dump(model, save_file)
print(f'Model saved to {save_file}')

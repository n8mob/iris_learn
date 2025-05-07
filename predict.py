import joblib

def begin():
    # load the trained model
iris_model = joblib.load('iris_model.pkl')

# Example input (first iris sample)
example = [[5.1, 3.5, 1.4, 0.2]]
pred = iris_model.predict(example)

print(f'Prediction: {pred}')

if __name__ == '__main__':
    iris_input = []
    iris_output = []
    with open('iris_input', 'r') as iris_input_file:
        iris_input = iris_input_file.read().splitlines()

    for input_line in iris_input:
        iris_output.append(predict(input_line))
        
    with open('iris_output', 'w') as iris_output_file:
        iris_output_file.writelines(iris_output)


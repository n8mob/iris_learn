import joblib


#modelop.init
def begin():
    global iris_model
    # load the trained model
    with open('iris_model.pkl', 'rb') as pickeled_model:
        iris_model = joblib.load(pickled_model)


#modelop.score    
def action(data):
    print("I'm in your models, predicting your data.")
    yield iris_model.predict(data)


#modelop.metrics
def metrics(data):
    return "not implemented yet"

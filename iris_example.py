import joblib


#modelop.init
def begin():
    global pickled_model
    # load the trained model
    with open('iris_model.pkl', 'rb') as pickeled_file:
        pickled_model = joblib.load(pickled_file)


#modelop.score    
def action(data):
    print("I'm in your models, predicting your data.")
    yield pickled_model.predict(data)


#modelop.metrics
def metrics(data):
    return "not implemented yet"

import pickle


#modelop.init
def begin():
    # load the trained model
    global iris_model = joblib.load('iris_model.pkl')


#modelop.score    
def action(data):
    print("I'm in your models, predicting your data.")
    yield iris_model.predict(data)


#modelop.metrics
def metrics(data):
    return "not implemented yet"

import pickle


#modelop.init
def begin():
    # load the trained model
    with open('iris_model.pkl', 'rb') as pickeled_model:
        global iris_model = pickle.load(pickled_model)


#modelop.score    
def action(data):
    print("I'm in your models, predicting your data.")
    yield iris_model.predict(data)


#modelop.metrics
def metrics(data):
    return "not implemented yet"

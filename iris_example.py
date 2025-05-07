import pickle


#modelop.init
def begin():
    # load the trained model
    pickle.
    global iris_model = pickle.load(open('iris_model.pkl', 'rb'))


#modelop.score    
def action(data):
    print("I'm in your models, predicting your data.")
    yield iris_model.predict(data)


#modelop.metrics
def metrics(data):
    return "not implemented yet"

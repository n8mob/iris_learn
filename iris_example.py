import joblib


#modelop.init
def begin(model_def = None):
    if model_def:
        if 'rawJson' in model_def:
          print(f"found rawJson in model_def: {model_def['rawJson']}")
        if 'job' in model_def:
          print(f"found job in model_def: {model_def['job']}")
        if 'deployedModel' in model_def:
          print(f"found deployedModel in model_def: {model_def['deployedModel']}")

    global pickled_model
    # load the trained model
    with open('iris_model.pkl', 'rb') as pickeled_file:
        pickled_model = joblib.load(pickeled_file)


#modelop.score
def action(data):
    floated = [float(i) for i in data]
    yield str(pickled_model.predict([floated])[0]).encode('utf-8')


#modelop.metrics
def metrics(data):
    return "not implemented yet"

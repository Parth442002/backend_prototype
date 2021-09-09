import pickle
def prediction_model(store_delivery,rider_store,packaging_time,rating):
    x = [[store_delivery,rider_store,packaging_time,rating]]
    voting_classifier = pickle.load(open('svm_model.sav','rb'))
    prediction = voting_classifier.predict(x)
    return prediction

help=prediction_model(4.13,3.088,3.5,3)
print(help)



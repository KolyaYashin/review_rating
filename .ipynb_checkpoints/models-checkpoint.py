import pickle
from keras.utils import pad_sequences
from keras.models import load_model


class_model = load_model('models/classification_reviews')
model_regression = load_model('models/regression_reviews')
max_tokens = 100


def text_to_prediction(text:str):
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    text = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=max_tokens, padding="post", truncating="post", value=0.)
    pred = 1-class_model(text)[0][0]
    if pred>0.5:
        is_positive = True
        score = int(model_regression(text)[0][0]+8.5)
    else:
        is_positive = False
        score = int(model_regression(text)[0][0]+2.5)
    return is_positive, score
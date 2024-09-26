import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk


# Загрузка необходимых ресурсов
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


# Загрузка стоп-слов
stop_words = set(stopwords.words('english'))

# Инициализация лемматизатора
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    # 1. Приведение к нижнему регистру
    text = text.lower()

    # 2. Удаление HTML-тегов
    text = re.sub(r'<[^>]+>', '', text)

    # 3. Удаление пунктуации
    text = re.sub(r'_+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    # text = re.sub(r'\d+', '', text)

    # 4. Токенизация
    tokens = text.split(' ')

    # 5. Удаление стоп-слов
    tokens = [word for word in tokens if word not in stop_words]

    # 6. Лемматизация
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # 7. Объединение токенов обратно в строку
    text = ' '.join(tokens)

    return text


def load_model(pickle_name):
    with open(pickle_name, 'rb') as f:
        model = pickle.load(f)
    return model


def text_to_prediction(text, preprocess, vectorizer, model_clf, model_neg, model_pos):
    preprop_text = preprocess(text)
    vect_text = vectorizer.transform([preprop_text])
    is_positive = model_clf.predict(vect_text)[0]
    if is_positive:
        return is_positive, round(model_pos.predict(vect_text)[0])
    else:
        return is_positive, round(model_neg.predict(vect_text)[0])
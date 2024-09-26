from flask import Flask,request,render_template, redirect
from models import text_to_prediction, load_model, preprocess_text

vectorizer = load_model('vectorizer.pkl')
model_clf = load_model('model_clf.pkl')
model_neg = load_model('model_neg.pkl')
model_pos = load_model('model_pos.pkl')


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html',variable='Here will be comment',variable2='Here will be its rating',color_variable = 'azure')

@app.route("/", methods=['POST'])
def post():
    global text
    text = request.form['text']
    global rate
    is_positive, rate = text_to_prediction(text, preprocess_text, vectorizer, model_clf, model_neg, model_pos)
    global color_var
    if is_positive:
        color_var = 'green'
    else:
        color_var = 'red'
    return redirect('/comment')

@app.route("/comment", methods=['POST'])
def post_in_comment():
    global text
    text = request.form['text']
    global rate
    is_positive, rate = text_to_prediction(text, preprocess_text, vectorizer, model_clf, model_neg, model_pos)
    global color_var
    if is_positive:
        color_var = 'green'
    else:
        color_var = 'red'
    return redirect('/comment')


@app.route('/comment')
def comment():
    return render_template('home.html',variable=text,variable2='Rating of this review is '+str(rate), color_variable = color_var)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
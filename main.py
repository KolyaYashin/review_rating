from flask import Flask,request,render_template, redirect



app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html',variable='Here will be comment',variable2='Here will be its rating')

@app.route("/", methods=['POST'])
def post():
    global text
    text = request.form['text']
    processed_text = text.upper()+'ITSWORKINGFUCKYEAHH'
    return redirect('/comment')

@app.route('/comment')
def comment():
    return render_template('home.html',variable=text,variable2='CHECK')
'''
@app.route('/')
def calculate_result():
    a = str(request.args.get('val1'))
    a=a+' ITS WORKING!!!'
    return jsonify({"result":a})
'''

if __name__=='__main__':
    app.run(debug=True)
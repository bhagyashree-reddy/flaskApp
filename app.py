from flask import Flask,render_template,request # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/thankyou')
def thankyou():
    fname=request.args.get('fname')
    lname=request.args.get('lname')
    return render_template("thankyou.html",fname=fname,lname=lname)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
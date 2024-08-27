from flask import Flask, render_template, request, redirect, url_for  # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get data from form submission
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        
        # Redirect to the thankyou page with the form data as URL parameters
        return redirect(url_for('thankyou', fname=fname, lname=lname))
    
    # If it's a GET request, just render the signup page
    return render_template("signup.html")

@app.route('/thankyou')
def thankyou():
    # Get URL parameters
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    return render_template("thankyou.html", fname=fname, lname=lname)

@app.errorhandler(404)
def page_not_found(e):
    # Return the 404 template with a 404 status code
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

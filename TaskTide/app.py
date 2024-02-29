from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #creating a new route for the homepage
def home():
    return render_template("index.html")

@app.route('/create_account') #creating a new route for the register page
def register():
    return render_template("create_account.html")

@app.route('/login') #creating a new route for the login page
def login():
    return render_template("login.html")

if __name__ == "__main__": #conditional statement for running the flask application
    app.run(debug=True)
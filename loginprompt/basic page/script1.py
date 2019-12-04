from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    ip = request.remote_addr
   
    inputName = inputName.upper()+" hi!  Visiting from " + str(ip)
    return render_template("login.html",myName=inputName)
@app.route('/')
def home():
    return render_template("login.html",myName="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("troll.html")

@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/Forgotpassword.html')
def Forgotpassword():
    return render_template("Forgotpassword.html")

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route("/index/")
def index():
return render_template("login.html")

if __name__ == "__main__":
app.run(host='0.0.0.0', port=4000)
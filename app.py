from flask import Flask,request,render_template
from flask import render_template,request
import textblob

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        a = request.form['options']
        print(a)
    return(render_template("index.html"))
@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("index.html"))
  
@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))
  
@app.route("/SA",methods=["GET","POST"])
def SA():
    q = request.form.get['q']
    r = 
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run(port=1111)

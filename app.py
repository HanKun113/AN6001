from flask import Flask,request,render_template
from transformers import pipeline
import textblob
import os
import google.generativeai as genai

api=os.getenv("maskersuite")
genai.configure(api_key = api)
model = genai.GenerativeModel("gemini-1.5-flash")

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
    return(render_template("main.html"))
  
@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))
  
@app.route("/SA_result", methods=["GET", "POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return render_template("SA_result.html",r=r)

@app.route("/genAI",methods=["GET","POST"])
def genAI():
    return(render_template("genAI.html"))

@app.route("/genAI_result", methods=["GET", "POST"])
def genAI_result():
    q = request.form.get("q")
    r = model.generate_content(q)
    return render_template("genAI_result.html",r=r.candidates[0].content.parts[0].text)

@app.route("/TB",methods=["GET","POST"])
def TB():
    return(render_template("TB.html"))

@app.route("/TB_result", methods=["GET", "POST"])
def TB_result():
    q = request.form.get("q")
    textblob_result = textblob.TextBlob(q).sentiment
    transformers_result = pipeline(q)
    
    return render_template(
        "TB_result.html",
        textblob_result=textblob_result,
        transformers_result=transformers_result[0]
    )

if __name__ == "__main__":
    app.run()


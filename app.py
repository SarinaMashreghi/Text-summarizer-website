from flask import Flask, request, jsonify, render_template, url_for, redirect
from summarizer_functions import *

app = Flask(__name__)

@app.route('/result')
def result(res):
    return res

@app.route('/summary', methods=['POST'])
def getSummary():
    text = request.form.get("txt")
    res = bert_extractive(text)
    return redirect(url_for("result", res = res))
    
    
if __name__ == '__main__':
    app.run()
    

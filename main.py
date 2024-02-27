from flask import Flask, render_template, request, redirect, session, make_response
import os

app = Flask(__name__)

@app.route('/')
def home():
   
    filename = 'hacky.yaml'
    response = make_response(open(filename).read())
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
    return response

if __name__ == "__main__":
    app.run(debug=True)
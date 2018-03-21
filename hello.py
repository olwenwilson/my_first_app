from flask import Flask, render_template


app = Flask("MyApp")

@app.route("/")
def hello():
	return "Go Away!"

@app.route("/idontexist")
def idontexist():
	return "I do exist now!"

@app.route("/Olwens_here")
def Olwens_here():
	return "Yes I'm here!"

app.run(debug=True)

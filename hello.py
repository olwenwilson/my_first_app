from flask import Flask, render_template, request


app = Flask("MyApp")

@app.route("/")
def hello():
	return "Hello World!"

#@app.route("/idontexist")
#def idontexist():
#	return "I do exist now!"

#@app.route("/Olwens_here")
#def Olwens_here():
#	return "Yes I'm here!"

@app.route("/<name>") 
def hello_someone(name):
	return render_template("hello.html", name=name.title())

#Passes the person's url which is XXX/name, then makes name a variable which 

@app.route("/signup", methods=["POST"]) 
def sign_up():
	form_data = request.form
	print form_data["email"]
#This line tells the terminal to print the email in the command line
	return render_template("thankyou.html")
#This line tells the webpage to change to show the page called thankyou.html
#This app route also uses the method "POST" which sends information to the server - it also can do something with the information like save it to a database. We also use get which is where you tell the server to give you the page you're looking for
#html always uses a POST request

app.run(debug=True)

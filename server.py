#flask-main class to create application
#request-to access incoming request
#render_template-to return an HTML page to the client
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("index.html")
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form.get("name")
    email=request.form.get("email")
    return f"Received: Name = {name} and Email = {email}"
if __name__=="__main__":
    app.run(debug=True)  

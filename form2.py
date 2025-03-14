from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={
        "name":request.form.get("name"),
        "email":request.form.get("email"),
        "phno":request.form.get("phno"),
        "gender":request.form.get("gender"),
        "skills":request.form.get("skills"),
        "dept":request.form.get("dept"),
        "file":request.files.get("file").filename if request.files.get("file") else "No file uploaded",
        "doj":request.form.get("doj")
        }
        return render_template("result2.html",data=data)
    return render_template("employee registration form.html")
if __name__=="__main__":
    app.run(debug=True)
        
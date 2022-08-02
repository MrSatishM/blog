from flask import *
from blogdb import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/regaut')
def regaut():
    return render_template("regaut.html")

@app.route('/reguser')
def reguser():
    return render_template("reguser.html")

@app.route('/logaut')
def logaut():
    return render_template("logaut.html")

@app.route('/loguser')
def loguser():
    return render_template("loguser.html")

@app.route('/autinter')
def autin():
    return render_template("autinter.html")

@app.route('/addpost')
def addpost():
    return render_template("addpost.html")


@app.route('/REGA' ,methods=["POST"])
def add_author():
    name=request.form["username"]
    passw=request.form["passw"]
    city=request.form["city"]
    email=request.form["email"]
    t=(None,name,passw,city,email)
    insertauth(t)
    return redirect("/")

@app.route('/REGU' ,methods=["POST"])
def add_user():
    name=request.form["username"]
    passw=request.form["passw"]
    city=request.form["city"]
    email=request.form["email"]
    t=(None,name,passw,city,email)
    insertuser(t)
    return redirect("/")

@app.route('/LOGA' ,methods=["POST"])
def log_author():
    name=request.form["username"]
    passw=request.form["password"]
    global x
    x=request.form["username"]
    t=name
    logauth(t)
    data=logauth(t)
    if name==data[0][0] and passw==data[0][-1]:
        return redirect("/autinter")

@app.route('/LOGU',methods=["POST"])
def log_use():
    name=request.form["username"]
    passw=request.form["password"]
    t=name
    loguse(t)
    data=loguse(t)
    if name==data[0][0] and passw==data[0][-1] :
        return redirect("/AllPost")

@app.route('/ADDPOST' ,methods=["POST"])
def add_post():
    name=request.form["aname"]
    title=request.form["blogtitle"]
    blog=request.form["Blog"]
    t=(None,name,title,blog)
    insertauthpost(t)
    return redirect("/autinter")

@app.route("/AllPost")
def allpost():
    data=selectAllPost()
    return render_template("AllPost.html",plist=data)

@app.route('/yourpost')
def yourpost():
    t=x
    selectYourPost(t)
    data=selectYourPost(t)
    return render_template("yourpost.html",pl=data)








if __name__=="__main__":
    app.run(debug=True)

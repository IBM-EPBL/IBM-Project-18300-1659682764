from flask import Flask, request,session,redirect,render_template,url_for
import sqlite3

app=Flask(__name__)

# conn=sqlite3.connect("signup.db")
# c=conn.cursor()
# arr=c.execute("SELECT *FROM person").fetchall()
# conn.commit()
# conn.close()
# print(arr)

@app.route("/",methods=['GET','POST'])
def main():
    msg=""
    if(request.method=="POST"):
        email=request.form["email"]
        passwd=request.form["pwd"]
        conn=sqlite3.connect("signup.db")
        c=conn.cursor()
        c.execute("SELECT * FROM person WHERE email='"+email+"'and pwd='"+passwd+"'")
        r=c.fetchall()
        print(r)
        for i in r:
            if(email==i[0] and passwd==i[1]):
                return redirect(url_for("home"))
        else:
            msg="Please enter valid username and password"
    return render_template("login.html",msg=msg)

@app.route("/signup",methods=['GET','POST'])
def signup():
    msg=""
    if(request.method=="POST"):
        if(request.form["email"]!="" and request.form["pwd"]!=""):
            email=request.form["email"]
            passwd=request.form["pwd"]
            conn=sqlite3.connect("signup.db")
            c=conn.cursor()
            c.execute("INSERT INTO person VALUES('"+email+"','"+passwd+"')")
            msg="Account created"
            arr=c.execute("SELECT *FROM person").fetchall()
            print(arr)
            conn.commit()
            conn.close()
        else:
            msg="Input fields are empty"
    return render_template("signup.html",msg=msg)

@app.route("/home")
def home():
    return render_template("home.html")

    
if __name__=="__main__":
    app.run(debug= True)
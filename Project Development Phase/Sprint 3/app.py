from flask import Flask, request,session,redirect,render_template,url_for
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")
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

@app.route("/logout")
def logout():
    return redirect(url_for("main"))

@app.route("/visualise")
def visualise():
    return render_template("visual.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    res=""
    return render_template("predict.html",result=res)
    
if __name__=="__main__":
    app.run(debug= True)
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
    if(request.method=="POST"):
        heart_data = pd.read_csv(r"C:\Users\abira\Desktop\IBM\venv\Heart_Disease_Prediction.csv")
        X = heart_data.drop(columns='Heart Disease', axis=1)
        Y = heart_data['Heart Disease']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
        model = LogisticRegression()
        model.fit(X_train, Y_train)

        n1=request.form['n1']
        n2=request.form['n2']
        n3=request.form['n3']
        n4=request.form['n4']
        n5=request.form['n5']
        n6=request.form['n6']
        n7=request.form['n7']
        n8=request.form['n8']
        n9=request.form['n9']
        n10=request.form['n10']
        n11=request.form['n11']
        n12=request.form['n12']
        n13=request.form['n13']

        if(n1!="" and n2!="" and n3!="" and n4!="" and n5!="" and n6!="" and n7!="" and n8!="" and n9!="" and n10!="" and n11!="" and n12!="" and n13!=""):
            t1=(float)(n1)
            t2=(float)(n2)
            t3=(float)(n3)
            t4=(float)(n4)
            t5=(float)(n5)
            t6=(float)(n6)
            t7=(float)(n7)
            t8=(float)(n8)
            t9=(float)(n9)
            t10=(float)(n10)
            t11=(float)(n11)
            t12=(float)(n12)
            t13=(float)(n13)
            input_data=(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13)
            input_data_as_numpy_array= np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
            prediction = model.predict(input_data_reshaped)
            if(prediction==["Absence"]):
                res="Yayy! The Probability that you may get a heart disease is Low :)"
            else:
                res="Oh no! The Probability that you may get a heart disease is High :("
        else:
            res="Please enter values in all the fields"
    return render_template("predict.html",result=res)
    
if __name__=="__main__":
    app.run(debug= True)
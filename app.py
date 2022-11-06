from flask import Flask,render_template,url_for,flash,redirect,request
import redis

redis_database = redis.Redis(host='localhost',port=6379,db=0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/setvalue',methods = ('GET','POST'))
def setvalue():
    if request.method == "POST":
        key = request.form['key']
        value = request.form['value']
        if not key:
            flash("Key is needed!!")
        else:
            redis_database.set(key,value)
            return redirect(url_for('base'))
    return render_template("setvalue.html")

@app.route('/getvalue',methods = ('GET','POST'))
def getvalue():
    if request.method == "POST":
        key = request.form['key']
        if redis_database.exists(key):
            value = redis_database.get(key)
            return value
        else:
            return f"{key} doesn't exits in redis"
    return render_template("getvalue.html")
if __name__ == "__main__":
    app.run(debug=True)
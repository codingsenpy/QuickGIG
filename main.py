from flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/user/<name>')
def bye(name):
    return name

@app.route('/hire', methods=["POST","GET"])
def hire():
    return render_template("hire.html")
@app.route('/look',methods=["POST","GET"])
def look():
    # if request.method == 'POST':
    job=request.form["job"]
    pay=request.form["pay"]
    location=request.form["location"]
    time=request.form["time"]
    print("Job:", job)
    print("Pay:", pay)
    print("Location:", location)
    print("Time:", time)
    return f'<h1 style="text-align: center">{job}</h1>'
    # else:
    #     return "bruh"



if(__name__=='__main__'):
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

#function to read the text file
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/user/<name>")
def greet(name):
    return f"<p> Hello, {name}! </p>"

@app.route("/")
def homeInfo():
    name = "Karen Velazquez"
    details = readDetails('static/details.txt')
    return render_template("home.html", name = name, aboutMe = details)

@app.route('/messages', methods = ['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])
        return render_template('base.html', name=name, aboutME=[])

    return render_template('form.html', name = name)

if __name__ == "__main__":
    app.run(debug = True)
from pyexpat.errors import messages

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to SecurePortal </h1>"

@app.route("/contact")
def contact():
    return "<h2> Contact Us at <h2><p>Email: support@example.com</p>"

@app.route("/about")
def about():
    return ("<h2> About SecurePortal </h2> <p> SecurePortal is being developed "
            "as part of a university project to demonstrate secure web "
            "application development practices. </p>")
@app.route("/status")
def status():
    return "<h2> Status </h2> <p> SecurePortal is currently runnings. </p>"

@app.route("/hello/<name>")
def hello(name):
    return f"<h1> Hello {name}! </h1>"


@app.route("/greet")
def greet():

    name = request.args.get("name", "")
    if name:
        message = f"<p> Hello {name}! </p>"
    else:
        message = "<p> Please enter your name. </p>"


    return  f"""
    <h1> Welcom to SecurePortal</h1>
    
    <form>
        <label> Your name:</label>
        <input type = "text" name="name">
        <input type = "submit" value="Say Hello">
    </form>
    {message}
    """
@app.route("/welcome")
def welcome():

    name = request.args.get("name", "")
    if name == "student":
        return "<h1> Welcome Student! </h1>"
    return f"<h1> Welcome {name}! </h1>"


if __name__ == '__main__':
    app.run(debug=True)

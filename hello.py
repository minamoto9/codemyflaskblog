from flask import Flask, render_template

#create an instance of flask
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#    return "<h1>Hello bee a cheese!</h1>"

def index():
    first_name = "Laird"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms"]
    return render_template("index.html", first_name=first_name, 
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

#create custom error pages

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
        return render_template("404.html"), 404
    
#internal server error
@app.errorhandler(500)
def page_not_found(e):
        return render_template("500.html"), 500
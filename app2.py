from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    thing = "This is <strong> Bold </strong>. This is a thing. "
    return render_template('index2.html', thing=thing)

@app.route('/user/<name>')
def user(name):
    return render_template('user2.html', username=name)


# ===================================================================================================    

# invalid errors:- 

# invalid url:
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# internal server error:
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html')
    
# ***************************************************************************************************

if __name__  == "__main__":
    app.run(debug=True)
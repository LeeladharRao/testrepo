from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    
  
    
    
    
@app.route("/about")
def about():
    return render_template('about.html')
print("this is salvation")
print("This si ")





print("this")

print("this is salvation")
print("This si ")

print("this")

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)

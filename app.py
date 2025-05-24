from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website1.html')

@app.route('/about')
def about():
    return render_template('about_us_web1.html')

@app.route('/membership')
def membership():
    return render_template('membership_web1.html')

if __name__ == '__main__':
    app.run(debug=True)

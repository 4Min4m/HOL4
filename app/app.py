from flask import Flask, render_template, request
from database import init_db, add_name

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        add_name(name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
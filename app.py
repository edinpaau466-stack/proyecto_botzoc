from flask import Flask, render_template
import os

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

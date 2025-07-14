from logging import debug
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/tersayang')
def index():
    return render_template('index.htm')
    
 
if __name__ == "__main__":
   app.run(debug=True)
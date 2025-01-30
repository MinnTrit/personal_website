from flask import Flask, request, render_template
app = Flask(__name__)
#Initialize common variables
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
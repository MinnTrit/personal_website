from flask import Flask, request, render_template
app = Flask(__name__, static_folder='static')
app.debug=True
#Initialize common variables
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)
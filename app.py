from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    html_code = ""
    if request.method == 'POST':
        html_code = request.form['html_code']
    return render_template('index.html', html_code=html_code)

if __name__ == '__main__':
    app.run(debug=True)

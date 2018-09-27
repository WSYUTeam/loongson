from flask import Flask, render_template
import config
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>', methods=['GET'])
def action(name):
    if name == 'A1':
        print(name)
    elif name == 'A2':
        print(name)
    elif name == 'B1':
        print(name)
    elif name == 'B2':
        print(name)
    elif name == 'C1':
        print(name)
    elif name == 'C2':
        print(name)
    elif name == 'D1':
        print(name)
    elif name == 'D2':
        print(name)
    elif name == 'E1':
        print(name)
    elif name == 'E2':
        print(name)
    elif name == 'F1':
        print(name)
    elif name == 'F2':
        print(name)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

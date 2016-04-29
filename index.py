from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return 'hi'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

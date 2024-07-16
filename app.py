from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

@app.route('/calc', methods=['GET'])
def calc_fibonacci():
    try:
        n = int(request.args.get('n'))
        result = fibonacci(n)
        return str(result)
    except (TypeError, ValueError):
        return "Incorrect input"

if __name__ == '__main__':
    app.run()
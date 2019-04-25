from flask import request, jsonify, json, Flask
import requests, os, hashlib
from slackclient import SlackClient


app = Flask(__name__)

def jsonoutput(inp, outp):
    return jsonify(input=inp, output=outp) 
        
@app.route('/')
def index():
    return "it works"

@app.route('/md5/<string>')
def handle_md5(string):
    h = hashlib.md5(bytes(string, 'utf-8')).hexdigest()
    return jsonoutput(string, h)

# This URI will return a factorial of an input of a positive integer
@app.route('/factorial/<num>')
def handle_factorial(num):
    try:
        use = int(num)
        total = int(num)
        for i in range(1, int(num) - 1):
            use -= 1
            total = total * use
        return jsonoutput(int(num), total)
        #return str(total)
    except ValueError:
        return jsonoutput(num, "Input is not a positive integer")

# This URI will return a list of fibonacci numbers that are less than the input number
@app.route('/fibonacci/<num>')
def fibonacci(num):
    try:
        if num > 0:
            a = 0
            b = 1
            fibo = [a]
            while b <= int(num):
                fibo.append(b)
                a, b = b, a+b
            return jsonoutput(int(num), fibo) 
        else:
            return jsonoutput(int(num), "Number is not positive")
    except ValueError:
        return jsonoutput(num, "Input is not an integer")

@app.route('/is-prime/<number>')
def handle_prime(number):
    try:    
        num = int(number)
        for i in range(2,num):
            if (num % i) == 0:
                return jsonoutput(number, "False")
                break
            else:
                return jsonoutput(number, "True")
    except ValueError:
        return jsonoutput(number, "Input is not a positive integer")

# This URI will post a message to a slack channel 
##Should be most of the slack alert API
@app.route('/slack-alert/<message>')
def handle_slack(message):
    requests.post("https://hooks.slack.com/services/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", json={"text": message})
    return jsonify(input = message, output = True)

app.debug = False
app.run('0.0.0.0')
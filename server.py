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
    return h

@app.route('/factorial/<num>')
def handle_factorial(num):
    try:
        use = int(num)
        total = int(num)
        if use < 0:
            return jsonoutput(use, 'Input is not a positive integer')
        for i in range(1, int(num) - 1):
            use -= 1
            total = total * use
        return jsonoutput(int(num), total)
        
    except ValueError:
        return jsonoutput(num, "Input is not a positive integer")

@app.route('/fibonacci/<num>')
def fibonacci(num):
    try:
        num = int(num)
        if num < 0:
            return jsonoutput(num, 'Input is not a positive integer')   
        a = 0
        b = 1
        fibo = [a]
        while b <= int(num):
            fibo.append(b)
            a, b = b, a+b

        return jsonoutput(int(num), fibo)    
    except ValueError:
        return jsonoutput(num, "Input is not a positive integer")
        
@app.route('/is-prime/<number>')
def handle_prime(number):
    try:    
        num = int(number)
        for i in range(2,num):
            if (num % i) == 0:
                return (str(num) + " is not a prime number")
                break
            else:
                return (str(num) + " is a prime number")
    except ValueError:
        return jsonoutput(number, "Input is not a positive integer")

##Should be most of the slack alert API
@app.route('/slack/<message>')
def handle_slack(message):
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call(
    "chat.postMessage",
    channel="ootpp",
    text=str(message)
)
    return jsonify(True)

app.debug = False
app.run('0.0.0.0')
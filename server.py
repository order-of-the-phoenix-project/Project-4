from flask import request, jsonify, json, Flask
import requests
#from slackclient import slackclient
#also need to add a bot to the course slack and put the API key in the slack function
app = Flask(__name__)

# NOTE: error handling for letters entered when number expected:
# try:
#     float(element)
# except ValueError:
#     print "Not a float"

# def factorial(num):
#     total = num
#     for i in range(1, num - 1):
#         num -= 1
#         total = total * (num)
#     return total 

def jsonoutput(inp, outp):
    return jsonify(input=inp, output=outp) 
        
        
@app.route('/')
def index():
    return "it works"

# @app.route('/md5/<string>')
# def handle_md5(string):
#     h = hashlib.md5(bytes(string, 'utf-8')).hexdigest()
#     return h

@app.route('/factorial/<num>')
def handle_factorial(num):

    use = int(num)
    total = int(num)
    for i in range(1, int(num) - 1):
        use -= 1
        total = total * use
    return jsonoutput(int(num), total)
    #return str(total)

@app.route('/fibonacci/<num>')
def handle_fibonacci(num=1):
    return "Python + Flask<hr>fib("+ str(num) + "): " + str(fib(num))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@app.route('/is-prime/<int>')
def handle_prime(int):
    pass # remove this line when the code for this function is added
# @app.route('/is-prime/<int>')
# def handle_prime(int):

    
#     return

# @app.route('/fibonacci/<num>')
# def handle_fibonacci(int(num)):
#     use = 0
#     for i in range (int(num)):
#         use = use + i
#     return str(use)

##Should be most of the slack alert API
@app.route('/slack/<message>')
def handle_slack(message):
    slackurl = "https://hooks.slack.com/services/TFCTWE2SH/BGMFM5AAG/G8ENlXUDl6A68"

    payload = {"text": message, "channel": "#ootpp"}
    r = requests.post(slackurl, payload)
    statement = "Message: " + "\"" + str(message) + "\"" + " was sucessfully posted to slack"
    return statement
#    slack.chat.postMessage('#what channel we want to send the message to', message):
#    response = #T/F response
#    jsonoutput(message,response)


app.debug = True
app.run('0.0.0.0')

import json
from flask import Flask

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
    # return str("{\n   \"input\": "+str(inp)+",\n   \"output\": "+str(outp)+"\n}")     
    return json.dumps({'input': int(inp), 'output': int(outp)}, sort_keys=True, indent=4, separators=(',', ': '))   
        
        
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
    return jsonoutput(num, total)
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

# @app.route('/slack-alert/<string>')

# @app.route('/slack-alert/<string>')
app.debug = True


app.run()
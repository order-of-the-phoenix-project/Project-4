from flask import Flask
from flask import request, jsonify
from flask import json

app = Flask(__name__)

# def factorial(num):
#     total = num
#     for i in range(1, num - 1):
#         num -= 1
#         total = total * (num)
#     return total 

def json(inp, outp):
    return str("{\n   \"input\": "+str(inp)+",\n   \"output\": "+str(outp)+"\n}")        
        
        
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
    return json(num, total)
    #return str(total)

@app.route('/fibonacci/<num>')
def index(num=1):
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


# Back up URI endpoint in case changing the return fuction in each original @app.route doesn't work
#       return handle_md5( 
#            "input" = ,
#            "output" = ,
#            )
#    @app.route('/factorial/<int>')
#            return handle_factorial()( 
#            "input" = ,
#            "output" = ,
#            )
#    @app.route('/fibonacci/<int>')
#            return fib( 
#            "input" = ,
#            "output" = ,
#            )
#    @app.route('/is-prime/<int>')
#            return handle_prime( 
#            "input" = ,
#            "output" = ,
#            )
#    @app.route('/slack-alert/<string>')
#            return handle_slack( 
#            "input" = ,
#           "output" = ,
#            )

app.run()
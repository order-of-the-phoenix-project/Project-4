from flask import Flask

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
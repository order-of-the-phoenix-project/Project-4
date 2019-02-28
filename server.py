from flask import Flask

app = Flask(__name__)

# def factorial(num):
#     total = num
#     for i in range(1, num - 1):
#         num -= 1
#         total = total * (num)
#     return total 

def json(inp, outp):
    return str("{\n   \"input\": "+inp+",\n   \"output\": "+outp+"\n}")        
        
        
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
    json(num, total)
    #return str(total)

@app.route('/is-prime/<int>')
def handle_prime(int):

    
    return

# @app.route('/slack-alert/<string>')

app.debug = True


app.run()
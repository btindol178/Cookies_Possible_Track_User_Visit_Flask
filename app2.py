from flask import Flask, make_response,request

app = Flask(__name__)

@app.route('/')
def index():
    count = int(request.cookies.get('visit-count',0)) # if no visit count the call will return 0 
    count +=1
    message = 'you have visited this page ' + str(count) + ' times'
    
    # make a response set cookie, return
    resp = make_response(message)
    resp.set_cookie('visit-count', str(count))
    return resp 
    
if __name__ == "__main__":
    app.run(debug=True)
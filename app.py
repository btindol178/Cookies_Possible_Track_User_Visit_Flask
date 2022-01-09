from flask import Flask, make_response,request

app = Flask(__name__)

# Set cookie at this route
@app.route("/set")
def setcookie():
    resp = make_response('Setting Cookie!')
    resp.set_cookie('framework','flask')
    return resp

@app.route("/get")
def getcookie():
    # get the framework cookie
    framework = request.cookies.get('framework')
    return 'The frame work is' + framework 

if __name__ == "__main__":
    app.run(debug=True)
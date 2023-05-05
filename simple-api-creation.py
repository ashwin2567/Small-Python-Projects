from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World Demo!!"

@app.route('/oddeven/<int:n>')
def oddeven(n):
    if n%2 == 0:
        print("even")
        result = {
            "Number" : n,
            "Even" : True,
            "Random Data" : str(n) + " is an even number."
        }
    else:
        print("Odd")
        result = {
            "Number" : n,
            "Even" : False,
            "Random Data" : str(n) + " is an oddy number."
        }
    return jsonify(result)
        
if __name__ == "__main__":
    app.run(debug=True)
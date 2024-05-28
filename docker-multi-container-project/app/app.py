from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def hello_world(message="Hello, World!"):
    commit_message = "I made my first commit :)"
    return f"<h1>{message}</h1><p>{commit_message}</p>\n"
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0') 
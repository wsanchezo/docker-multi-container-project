from flask import Flask 

app = Flask(__name__) 

@app.route('/')
def hello_world(message="Hello, World!"):
    commit_message = "I made my first commit :)"
    commit_message2 = "Demostración de cómo dos contenedores se comunican entre sí"
    return f"<h1>{message}</h1><p>{commit_message}</p><p>{commit_message2}</p>\n"
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', debug=True) 
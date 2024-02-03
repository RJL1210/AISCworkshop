from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
#from algorithm import run_algorithm
from main import run_algorithm
from eda import analysis
from flask_restful import Api, Resource

app = Flask(__name__)

CORS(app) #allow frontend and backend to work together
api = Api(app)

@app.route("/", methods=['GET']) #route to homePage
def get_home():
    #return info as JSON
    return jsonify({ 
        'message': "Jsonifed",
        'people': ["Ryan", "Amanda", "Ken"]
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080)



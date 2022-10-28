from flask import Flask, request, abort, jsonify
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Headers", "Authorization")
        response.headers.add("Access-Control-Allow-Headers", "true")
        response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS")
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    @app.route('/', methods=['GET'])
    def get_details():
        try:
            return jsonify({"slackUsername": "Ella Maria",
                        "backend": True,
                        "age": 23,
                        "bio": "aspiring full-stack software engineer",})
        except:
            abort(404)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    return app

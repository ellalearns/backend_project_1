from flask import Flask, request, abort, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

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

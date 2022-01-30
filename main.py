from flask import Flask, json, jsonify, request
import urllib.request

app = Flask(__name__)

WEATHER_API_URL = 'https://api.codetabs.com/v1/weather?city={}'

@app.route('/')
def index():
    return jsonify(
        firstname='Cem',
        lastname='Anaral'
    )

@app.route('/temperature')
def temperature():
    city = request.args.get('city')

    weather_api_response = urllib.request.urlopen(
        WEATHER_API_URL.format(city)
    )
    
    weather_api_response_in_json = json.loads(weather_api_response.read())

    temperature = weather_api_response_in_json['tempC']
    
    return jsonify(
        temperature=temperature
    )

# to return json error messages
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run(debug=True)

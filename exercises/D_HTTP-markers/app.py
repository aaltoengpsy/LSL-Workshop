from flask import Flask, make_response, request
from flask_cors import CORS
from pylsl import StreamInfo, StreamOutlet

# Create the Flask app
app = Flask(__name__)

# Enable cross-origin resource sharing. For the demo, we'll use a wildcard (*). Not usually recommended, as it allows requests from anywhere.
cors = CORS(app, origins='*')

# Define the stream & outlet
stream = StreamInfo('markers', 'markers', 1, 0, 'string', 'ws-flask-markers')
outlet = StreamOutlet(stream)

# Define a route where markers should be sent
@app.route('/markers', methods = ['POST'])                          # Route where requests should be sent is <server_url>/markers. Only POST requests are accepted.
def receive_marker():
    try:
        req_contents = request.get_json()                           # Parse the contents of the HTTP request (to a JSON object)
        marker = str(req_contents['marker'])                        # We'll put the marker string in a field called "marker" when making the request
        print('Marker received with HTTP:', marker)
        outlet.push_sample([marker])                                # Push the marker to the outlet
        return make_response({'message': 'OK'}, 202)                # HTTP requests have to return at least a status code!
    except Exception as e:
        print(str(e))
        return make_response({'message': str(e)}, 500)              # If an error happened during processing, return the error message
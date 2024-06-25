import time
import requests                                             # The requests library can be used in Python to make HTTP requests

while True:
    requests.post(                                          # Construct a HTTP POST request
        'http://127.0.0.1:5000/markers',                    # The URL of our Flask server & marker endpoint
        json = {'marker': 'hello'},                         # The body of our request contains the marker
        headers = {'Content-Type': 'application/json'}      # Set the HTTP Content-Type header so our server accepts the contents
    )

    time.sleep(2) # Sleep for 2 seconds to prevent overwhelming the server
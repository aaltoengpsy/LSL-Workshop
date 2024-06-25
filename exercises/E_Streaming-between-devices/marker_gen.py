from pylsl import StreamInfo, StreamOutlet
import time
import random

def create_outlet():
    # TODO: Define StreamInfo below

    stream = StreamInfo(name, stream_type, n_of_channels, sampling_rate, value_type, outlet_id)    # Establish the details of the stream
    outlet = StreamOutlet(stream)                                                           # Create the outlet

    return outlet

def output_marker(marker_text, target_outlet):                                              # Take the marker as a parameter
    print('Outputting random sample:', marker_text)                                         # Print out the marker

    target_outlet.push_sample([marker_text])                                                # Push the marker through the outlet

outlet = create_outlet()

while True:
    output_marker(marker_text = '', target_outlet = outlet)
    time.sleep(1)
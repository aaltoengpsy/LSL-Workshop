from pylsl import StreamInfo, StreamOutlet
import time
import random

def create_outlet():
    name = 'workshop_marker_outlet'                                                         # The name of the outlet
    type = 'single_stream'                                                                  # Stream type. This can be anything, but should probably be descriptive of what data is going through (e.g. EDA, EEG, Markers)
    n_of_channels = 1                                                                       # Single-channel data
    sampling_rate = 0                                                                       # 0Hz = 0 samples / second -> Indicates irregular sampling rate
    value_type = 'string'                                                                   # The type that all stream values should be. This time we're sending strings.
    outlet_id = 'workshop_ex_a'                                                             # An unique identifier used to resolve streams when pulling data from the LSL network

    stream = StreamInfo(name, type, n_of_channels, sampling_rate, value_type, outlet_id)    # Establish the details of the stream
    outlet = StreamOutlet(stream)                                                           # Create the outlet

    return outlet

def output_marker(marker_text, target_outlet):                                              # Take the marker as a parameter
    print('Outputting random sample:', marker_text)                                         # Print out the marker

    target_outlet.push_sample([marker_text])                                                # Push the marker through the outlet

outlet = create_outlet()

while True:
    if random.random() >= 0.5:
        output_marker('gr_eq', outlet)
    else:
        output_marker('less', outlet)
    time.sleep(1)      
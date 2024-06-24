from pylsl import StreamInfo, StreamOutlet
import time
import random

def create_outlet():
    name = 'workshop_outlet'                                                                # The name of the outlet
    type = 'single_stream'                                                                  # Stream type. This can be anything, but should probably be descriptive of what data is going through (e.g. EDA, EEG, Markers)
    n_of_channels = 1                                                                       # Single-channel data
    samping_rate = 1                                                                        # 1Hz = 1 sample per second
    value_type = 'float32'                                                                  # The type that all stream values should be.
    outlet_id = 'c-multichannel-stream'                                                     # An unique identifier used to resolve streams when pulling data from the LSL network

    stream = StreamInfo(name, type, n_of_channels, samping_rate, value_type, outlet_id)     # Establish the details of the stream
    outlet = StreamOutlet(stream)                                                           # Create the outlet

    return outlet

def output_random_sample(target_outlet):
    random_sample = random.random()                                                         # Generate a random floating point value between 0 and 1 and round it to 2 decimals.
    print('Outputting random sample:', random_sample)                                       # Print out the sample we just generated

    target_outlet.push_sample([random_sample])                                              # Push the sample through the outlet


outlet = create_outlet()

while True:
    output_random_sample(outlet)
    time.sleep(1)     
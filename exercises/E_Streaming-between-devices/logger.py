from pylsl import StreamInlet, resolve_stream

def create_inlet():
    stream = resolve_stream('source_id', 'YOUR_ID_HERE')[0]                             # Get our marker stream
    inlet = StreamInlet(stream)                                                         # Establish an inlet that data can be pulled through
    return inlet

def pull_marker(source_inlet):                                                         
    samples, ts = source_inlet.pull_sample()
    print('Received marker:', samples[0], 'with timestamp', ts)

inlet = create_inlet()

while True:
    pull_marker(inlet)

from pylsl import StreamInlet, resolve_stream

def create_inlet(id):
    stream = resolve_stream('source_id', id)[0]
    inlet = StreamInlet(stream)
    return inlet

def pull_samples(source_inlet):
    chunk, ts = source_inlet.pull_chunk()                       # With multiple streams of varying sampling rates, we'll need to pull chunks to get all data!
    if len(ts) > 0:
        samples = chunk[0]                                      # Because we are NOT pushing data in chunks to LSL (which we could), the chunk only contains one sample array.
        print(ts, '\t\treceived:', samples[0])                  # Our data is single-channel so the sample array's length is 1

marker_inlet = create_inlet('b-marker-stream')
sample_inlet = create_inlet('b-sample-stream')

while True:
    pull_samples(marker_inlet)
    pull_samples(sample_inlet)

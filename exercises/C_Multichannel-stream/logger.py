from pylsl import StreamInlet, resolve_stream

def create_inlet(id):
    stream = resolve_stream('source_id', id)[0]
    inlet = StreamInlet(stream)
    return inlet

def pull_samples(source_inlet):
    samples, ts = source_inlet.pull_sample()
    print(ts, '\t\treceived:', samples[0])

sample_inlet = create_inlet('c-multichannel-stream')

while True:
    pull_samples(sample_inlet)

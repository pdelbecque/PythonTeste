from pynput import mouse

with mouse.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print('You did not interact with the mouse within one second')
    else:
        print('Received event {}'.format(event))
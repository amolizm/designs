import marshal
import zmq
import time

def get_square(**args):
    print(args.keys())
    print(args.values())
    return 

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f"tcp://*:6699")
while True:
    code_bytes = marshal.dumps(get_square.__code__)
    socket.send(code_bytes)
    print("sent the function...")
    time.sleep(1)

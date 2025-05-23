import marshal, types
import zmq, time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f"tcp://localhost:6699")
socket.setsockopt_string(zmq.SUBSCRIBE, "")


while True:
    try:
        payload = socket.recv(flags=zmq.NOBLOCK)
        print("recieved function")
        function = marshal.loads(payload)
        get_square = types.FunctionType(function, globals())
        print(get_square(user="amol",
                         pwd = "axmasdf"))
    except Exception as e:
        pass

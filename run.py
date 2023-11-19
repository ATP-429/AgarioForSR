import threading

def server():
    import server
threading.Thread(target=server).start()

def client():
    import client
threading.Thread(target=client).start()
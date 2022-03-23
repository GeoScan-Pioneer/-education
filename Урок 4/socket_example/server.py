from NetUtils import Server

if __name__ == '__main__':
    server = Server(ip="127.0.0.1", port=8000)
    server.runTCPserver()
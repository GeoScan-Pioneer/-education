from NetUtils import Client

if __name__ == '__main__':
    client = Client(ip="127.0.0.1", port=8000)
    client.runTCPserver()
    client.send_message_server(b'hello server')
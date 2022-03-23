import socket
import threading
import time
import struct


class NetUtils():
    def __init__(self, ip, port):
        self.ip_server = ip
        self.port_server = port

    def createServerSock(self):
        """ Создание сокета сервера """

        # socket.SOCK_STREAM - TCP сокет
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        # Привязать созданный сокет к ip:port
        serv_sock.bind((self.ip_server, self.port_server))

        # Перевод сокета в режим соединения
        serv_sock.listen()
        return serv_sock

    def createClientSock(self):
        """ Создание сокета клиаента """
        try:
            serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

            # Подключение к созданному сокету сервера
            serv_sock.connect((self.ip_server, self.port_server))
            print("Успешное соединение")
            return serv_sock
        except:
            print("Не удалось соедениться с сервером")

    def sendMessage(self, receiver, message):
        """ Отпарвить сообщение клиенту """
        try:
            receiver.sendall(message)
        except:
            print("Ошибка отпарвки сообщения")

    def acceptMessages(self, client):
        """ Принять сообщение от клитента """
        data = client.recv(1024).decode("utf8")
        return data


class Server(NetUtils):
    def __init__(self, ip, port):

        super().__init__(ip=ip, port=port)

        self.clients_sock = []
        self.cid = 0
        self.serv_sock = self.createServerSock()

    def runTCPserver(self):

        while True:
            client_sock, client_addr = self.serv_sock.accept()  # если есть подключение
            self.clients_sock.append(client_sock)  # сохраняем в список подключенных устройств
            print("Клиент", client_addr, "подключился")

            t = threading.Thread(target=self.accept_message_client,
                                 args=(client_sock, self.cid))  # запускаем поток его обработки
            t.start()
            self.cid += 1

    # отлдельный поток для приема сообщений от нового клиента
    def accept_message_client(self, client_sock, cid):
        while True:
            data = self.acceptMessages(client_sock)

            if data is not None:
                print(data)
                self.sendMessage(receiver=client_sock, message=b'hello cloent')


class Client(NetUtils):
    def __init__(self, ip, port):
        super().__init__(ip=ip, port=port)
        self.serv_sock = self.createClientSock()

    def runTCPserver(self):
        # Принимаем сообщения от сервера в отдельном потоке
        stream_for_messages = threading.Thread(target=self.accept_message_server, args=())
        stream_for_messages.start()

    # В отдельном потоке принимаем сообщения
    def accept_message_server(self):
        while True:
            data = self.acceptMessages(self.serv_sock)

            if data is not None:
                print(data)

    # отправить сообщение на сервер
    def send_message_server(self, message):
        self.sendMessage(receiver=self.serv_sock, message=message)

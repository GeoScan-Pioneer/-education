import serial


class Uart:
    def __init__(self, port, baud, timeout):
        try:
            # Создание порта
            self.uart = serial.Serial(port, baud, timeout=timeout)

            # Очистка порта от данных в нем
            self.uart.flush()
            print('Успешное соединение')

        except:
            print('Ошибка соединения')

    def accept_message(self):
        """ Прием сообщения """
        if self.uart.inWaiting() > 0:
            data = self.uart.readline()
            print(data.decode('utf-8').rstrip())

    def send_message(self, message):
        """ Отправка сообщения """
        self.uart.write(message)






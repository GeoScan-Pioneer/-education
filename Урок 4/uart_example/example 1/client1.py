from UartUtils import Uart
import time
import random

# Список случайных сообщений для демонстрации
event = {0: 'ENGINES_STARTED',
         1: 'DISARM',
         2: 'COPTER_LANDED',
         3: 'POINT_REACHED',
         4: 'POINT_DECELERATION',
         5: 'LOW_VOLTAGE1',
         6: 'LOW_VOLTAGE1',
         7: 'SHOCK',
         8: 'ENGINE_FAIL'}

if __name__ == "__main__":
    # Создаем экземпляр класса
    UART = Uart('COM1', 9600, 1)

    while True:
        message = event[random.randint(0, 8)]
        UART.send_message(message.encode(encoding="utf-8"))
        time.sleep(1)

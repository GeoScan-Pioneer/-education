from UartUtils import Uart

if __name__ == "__main__":
    UART = Uart('COM2', 9600, 1)
    while True:
        UART.accept_message()

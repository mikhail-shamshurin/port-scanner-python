from socket import socket as Socket
from os import system
from threading import Thread
from datetime import datetime as Datetime


found: list = []
printing: bool = False
scanned: int = 0
total: int = 2**16


def update_output():
    global printing, found, scanned, total

    if printing:
        return None

    printing = True

    length = 10
    percent = int(scanned / total * 100)
    size = int(length / 100 * percent)

    system("clear||cls")

    message = 'Сканирование портов...' if percent < 100 else 'Порты просканированы.'
    print(f'{message} [{("=" * size)}{" " * (length - size)}] {percent}%\n')

    found_join = "\n".join(found)
    print(f"Открытые порты:\n{found_join}")

    printing = False


def scan_port(port):
    global scanned

    try:
        socket = Socket()
        socket.connect(("127.0.0.1", port))
        found.append(f"{port}")

    except:
        pass

    socket.close()
    scanned += 1
    update_output()


def main():
    start_time = Datetime.now()
    threads: list[Thread] = []

    for port in range(1, total + 1):
        threads.insert(0, Thread(target=scan_port, args=(port,)))
        threads[0].start()

    for thread in threads:
        thread.join()

    update_output()
    print(f'\nВермя выполнения: {Datetime.now() - start_time}')

main()

import asyncio

class EchoServer:  # Определяем класс EchoServer
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def echo(self, reader, writer):  # Определяем асинхронную функцию echo для обработки сообщений
        while True:
            try:
                async with asyncio.timeout(5):
                    data = await reader.read(100)
            except asyncio.TimeoutError:
                writer.write('Timeout!'.encode())
                print('Таймаут соединения')
                break
            if not data:
                break
            print(f'Получено сообщение: {data.decode()}')
            message = data.decode().upper()
            writer.write(message.encode())
            print(f"Отправлено: {message}")
            await writer.drain()
        writer.close()
        print("Соединение закрыто")

    async def run_server(self):  # Определяем асинхронную функцию run_server для запуска сервера
        server = await asyncio.start_server(self.echo, self.host, self.port)
        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    host = ''
    port = 8000
    echo_server = EchoServer(host, port)
    asyncio.run(echo_server.run_server())

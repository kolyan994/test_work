import asyncio


async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8000)
    for i in range(5):
       # await asyncio.sleep(6)    # Проверка срабатывания таймаута
        message = f"{message} {i+1}"
        writer.write(message.encode())
        await writer.drain()
        print(f'Отправлено: {message}')
        data = await reader.read(100)
        print(f'Принято: {data.decode()}')
    writer.close()
    await writer.wait_closed()
    print('Соединение закрыто')

if __name__ == '__main__':
    message = 'Сообщение на сервер'
    asyncio.run(send_message(message))

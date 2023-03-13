import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

if __name__== "__main__":
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    #for num in range(10,32768):  # 迭代 10 到 20 之间的数字
    #    for i in range(2,num): # 根据因子迭代
    #        if num % i == 0:      # 确定第一个因子
    #            j =num/i          # 计算第二个因子
    #            print ('%d 是一个合数' % num)
    #            break            # 跳出当前循环
    #    else:                  # 循环的 else 部分
    #      print ('%d 是一个质数' % num)
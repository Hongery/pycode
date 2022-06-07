import asyncio
import aiohttp
import blog_spider

# 协程爬虫
async def async_spider(url):
    print("craw url :", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()  # await 不会等待，会进入下一个循环
            print(f"craw url:{url},{len(result)}")


# 定义一个超级循环
loop = asyncio.get_event_loop()

tasks = [
    # 传入函数名
    loop.create_task(async_spider(url))
    for url in blog_spider.urls
]
import time

start_time = time.time()
# 等待所有协程完成
loop.run_until_complete(asyncio.wait(tasks))
print(f"end time:{time.time()-start_time}")
# if __name__ == "__main__":

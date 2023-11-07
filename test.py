import asyncio
import aiohttp

params = {'name': 'Joe', 'email': 'ivanaxenov2010@mail.ru', 'phone': "0000", 'message': "Hello"}
url = "http://127.0.0.1:8000/feedback/"


async def feach(session,url,count):
    print(count)
    async with session.post(url, data=params) as response:
        print(response.status)

async def feach_all(session):
    tasks = []
    for i in range(5000):
        task = asyncio.create_task(feach(session,url,i))
        tasks.append(task)
    await asyncio.gather(*tasks)
async def main():
    async with aiohttp.ClientSession() as session:
        await feach_all(session)



if __name__ == '__main__':
   asyncio.run(main())
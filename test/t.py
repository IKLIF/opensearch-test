import asyncio
import aiohttp


class TestAsync():
    def __init__(self):
        self.hero_array = [
            {'title': 'Tutorial'},
            {'content': 'Learn Linux from scratch...'},
            {'content_type': "news"}
        ]

        self.url = "http://localhost:8000/search"

    async def get(self, session, data):
        try:
            async with session.get(self.url, params=data, timeout=5) as response:
                json_res = await response.json()
                print(f'GET {data} : {response.status}')
                print(f'GET {data} : {json_res}')
        except Exception as e:
            print(f'GET Error for {data}: {str(e)}')

    async def process_hero(self, session, hero_name):
        await self.get(session, hero_name)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for hero in self.hero_array:
                task = asyncio.create_task(self.process_hero(session, hero))
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    t = TestAsync()
    asyncio.run(t.run())


import kahoot
import asyncio
import random
import main

async def main():
    pin = 123 # kod gry
    name = "bot" + str(random.randint(1, 9999))

    bot = kahoot.client.KahootClient()
    await bot.join_game(pin, name)

    while True:
        await asyncio.sleep(1)

asyncio.run(main())

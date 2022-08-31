import sys
import asyncio
from telethon import TelegramClient


# OLD: These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 17232793
api_hash = '14a220e9917ff2b6846acb4b878322ef'


async def main():
    client = TelegramClient('SendBoy', api_id, api_hash)
    await client.start()

    # TODO: Make group choosable
    send_to = await client.get_entity(-646746470)

    await client.send_message(send_to, 'Active from PC')

    to_send = []
    for line in sys.stdin:
        line = line.strip('\n')

        if line == '---':
            await client.send_message(send_to, '\n'.join(to_send))
            to_send = []
        else:
            to_send.append(line)


asyncio.run(main())

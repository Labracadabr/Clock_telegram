import schedule
import time
from datetime import datetime
from avatar_handler import set_photo, delete_photo
from drawer import generate_avatar
import asyncio


def main():
    print()
    asyncio.run(delete_photo())
    generate_avatar()
    asyncio.run(set_photo())
    print()


schedule.every().minute.at(':00').do(main)


# поллинг каждые n секунд
n = 2
while True:
    # проверить, не настало ли время
    schedule.run_pending()

    nxt = schedule.next_run()
    now = datetime.now()
    dif = nxt-now
    print('\rслед действие через', int(dif.total_seconds()), 'сек', end='')

    time.sleep(n)


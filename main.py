import time
from datetime import datetime
import asyncio

import schedule

from avatar_handler import set_photo, delete_photo
from drawer import generate_avatar


def main():
    print()
    asyncio.run(delete_photo())
    generate_avatar()
    asyncio.run(set_photo())
    print()


# запуск каждый час в 00 минут
schedule.every().hour.at(':00').do(main)


# поллинг каждую секунду
while True:
    # проверить, не настало ли время
    schedule.run_pending()

    nxt = schedule.next_run()
    now = datetime.now()
    dif = nxt-now
    print('\rслед действие через', int(dif.total_seconds()), 'сек', end='')

    time.sleep(1)


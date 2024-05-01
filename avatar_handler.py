from pyrogram import Client, enums
from config import config
import asyncio
from datetime import datetime, timedelta

api_id = config.api_id
api_hash = config.api_hash
avatar_path = 'avatar_time.jpg'


# поставить аву
async def set_photo():
    async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
        print('uploading', avatar_path)
        result = await app.set_profile_photo(photo=avatar_path)
        print(f'{result = }')
        return result


# удалить аву
async def delete_photo():
    async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
        print('deleting avatar')

        # список всех аватарок
        photos = [p async for p in app.get_chat_photos("me")]
        last_photo = photos[0]

        # чтобы случайно не удалить старые аватарки
        date = last_photo.date
        now = datetime.now()
        diff: timedelta = now - date
        if diff.seconds > 60*60*24:
            print(f'Нет нового фото. Самое старое загружено {diff.seconds} сек назад: {date = }')
            return False

        # удаление авы
        result = await app.delete_profile_photos(last_photo.file_id)
        print(f'{result = }')
        return result


if __name__ == '__main__':
    pass
    asyncio.run(delete_photo())

from dataclasses import dataclass
from environs import Env
# from settings import prod


@dataclass
class Config:
    BOT_TOKEN: str = None           # телеграм бот
    api_id: str = None
    api_hash: str = None

    host: str = None                # хост
    dbname: str = None              # имя базы данных
    user: str = None                # пользователь
    password: str = None            # пароль
    port: int = None                # порт


# загрузить конфиг из переменных окружения
env = Env()
env.read_env()
config = Config(
    # BOT_TOKEN=env('BOT_TOKEN_PROD'),
    api_id=env('api_id'),
    api_hash=env('api_hash'),
)


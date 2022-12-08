import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.utils.config_reader import load_config
from config.commands import my_commands
from app.utils.handlers_registrar import handlers_registrar

logger = logging.getLogger(__name__)

#main
async def main():

    # Настройка логирования в консоль
    logging.basicConfig(
        level=logging.INFO,
        format="   %(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    # Парсинг файла конфигурации
    config = load_config("config/bot.ini")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    handlers_registrar(dp)

    # Установка команд бота
    await bot.set_my_commands(my_commands)

    # Запуск поллинга
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())


from aiogram.types import BotCommand

my_commands = [
        BotCommand(command="/start", description="launch a bot"),
        BotCommand(command="/questions", description="ask question pls"),
        BotCommand(command="/image", description="get an image"),
        BotCommand(command="/exit", description="bye"),
]

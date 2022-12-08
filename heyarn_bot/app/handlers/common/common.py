import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from config.commands import my_commands
from ...utils.get_username import getUsName


#getCommandsList
def getCommandsList()  -> str:
    commands_list = "\n"
    for x in my_commands:
        commands_list += str(x.command + " – " + x.description + "\n")
    return commands_list

#cmd_start
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await state.finish()

    await message.answer(f"Приветик {getUsName(message)}!!", reply_markup = types.ReplyKeyboardRemove())
    await message.answer_sticker("CAACAgIAAxkBAAEF22VjJWUh4MhbgyVpCin1hMTfDBAoQwACHwEAAou2whzPcZ19-QtsnykE")

#cmd_exit
async def cmd_exit(message: types.Message, state: FSMContext) -> None:
    await state.finish()
    msg = await message.answer(f"Состояние сброшено!")
    await asyncio.sleep(1)

    await msg.edit_text(f"Приветик!! Я знаю парочку команд:{getCommandsList()}")
    await message.answer(f"Что выберешь?", reply_markup = types.ReplyKeyboardRemove())

#cmd questions
async def cmd_questions(message: types.Message, state: FSMContext):
    await state.finish()

    bot.ask_question(message.chat.id, "Спроси у меня вопросы!")

#cmd text
async def cmd_text_recognition(message: types.Message, state: FSMContext):
    await state.finish()

    bot.ask_question(message.chat.id, "Отправь мне картинку!")

#unindentified_messages
async def unindentified_messages(message: types.Message) -> None:
    await SendServiceInfo(message)
    await message.answer(f"А?")    


if __name__ == "__main__":
    main()
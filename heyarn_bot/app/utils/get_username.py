from aiogram import types

def getUsName(message : types.Message) -> str:
     usName = str(message.from_user.first_name)
     if str(message.from_user.last_name).lower() != "none": usName += (" " + str(message.from_user.last_name))
     return usName

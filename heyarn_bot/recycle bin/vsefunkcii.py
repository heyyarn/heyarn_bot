#from time import sleep
#from datetime import datetime
#from random import choice
#from peremennye import AdminID

##getUsName
#def getUsName(message):
#     usName = str(message.from_user.first_name)
#     if str(message.from_user.last_name).lower() != "none": usName += (" " + str(message.from_user.last_name))
#     return usName

##SendTypingAcion
#def SendTypingAcion(bot, message, timing):
#    bot.send_chat_action(message.chat.id, action='typing')
#    sleep(timing)

##startMsgSend
#def startMsgSend(bot, message):
#    usName = getUsName(message)

#    bot.send_message(message.chat.id, f"Приветик {usName}!!")
#    #SendTypingAcion(bot, message, 2)
#    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEF22VjJWUh4MhbgyVpCin1hMTfDBAoQwACHwEAAou2whzPcZ19-QtsnykE")
 
#def SendAdmin(bot, message):
#    if message.chat.id == AdminID:
#            bot.send_message(message.chat.id, f"Приветик я!!")
        
#    else:
#        bot.send_message(message.chat.id, f"руки вверх!!")

#def AskQestions(bot, message):
#    question = message.text.lower()
    
#    Answers = [[f"хорошо", f"плохо", f"пойдет"],
#    [f"солнечно", f"ясно", f"дождь"],
#    [f"отстой", f"не очень", f"неплохо"],
#    [f"никак", f"и так сойдет", f"отлично"],
#    [f"да", f"нет", f"посмотрим"]]

#    match question:
#        case "как дела?":
#           bot.send_message(message.chat.id, choice(Answers[0]))

#        case "как погода?":
#            bot.send_message(message.chat.id, choice(Answers[1]))

#        case "как жизнь?":
#            bot.send_message(message.chat.id, choice(Answers[2]))
    
#        case "как учеба?":
#            bot.send_message(message.chat.id, choice(Answers[3]))

#        case "пойдешь гулять?":
#            bot.send_message(message.chat.id, choice(Answers[4]))
#        case _:
#            bot.send_message(message.chat.id, f"аэм что?")
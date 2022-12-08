from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType

from ..handlers.common.common import cmd_start, cmd_exit, unindentified_messages
from ..handlers.questions.questions import questions_start, questions_chosen, stop_questions, questionsStates


#handlers_registrar
def handlers_registrar(dp: Dispatcher) -> None:
    #common
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_exit, commands="exit", state="*")

    #questions
    dp.register_message_handler(questions_start, commands="questions", state="*")
    dp.register_message_handler(stop_questions, Text(equals="пока", ignore_case=True), state=questionsStates.waiting_for_question)
    dp.register_message_handler(questions_chosen, state=questionsStates.waiting_for_question)

    dp.register_message_handler(text_recognition, commands="image", state="*")

    dp.register_message_handler(unindentified_messages, content_types = ContentType.ANY)
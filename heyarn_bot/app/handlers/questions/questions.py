from random import choice

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .answers import available_answers
from .keyboard import available_questions_buttons


class questionsStates(StatesGroup):
    waiting_for_question = State()
    
async def questions_start(message: types.Message, state: FSMContext) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*available_questions_buttons)
    keyboard.add("пока")

    await message.answer("Выберите вопрос:", reply_markup=keyboard)
    await state.set_state(questionsStates.waiting_for_question.state)

async def questions_chosen(message: types.Message, state: FSMContext) -> None:
    question = message.text.lower()

    match question:
        case "как дела?":
           await message.answer(choice(available_answers[0]))
        case "как погода?":
            await message.answer(choice(available_answers[1]))
        case "как жизнь?":
            await message.answer(choice(available_answers[2]))
        case "как учеба?":
            await message.answer(choice(available_answers[3]))
        case "пойдешь гулять?":
            await message.answer(choice(available_answers[4]))
        case _:
            await message.answer(f"аэм что?")

async def stop_questions(message: types.Message, state: FSMContext) -> None:
    await message.answer("пока", reply_markup = types.ReplyKeyboardRemove())
    await state.finish()
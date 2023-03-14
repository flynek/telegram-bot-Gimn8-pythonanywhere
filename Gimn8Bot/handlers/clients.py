from aiogram import types, Dispatcher
from create_bot import bot
from create_bot import dp
from keyboards import *
from handlers.messages import dict_messages


# Start command
async def command_start(message: types.Message):
    await message.answer(dict_messages.get('st_m'), reply_markup=kb_start)


@dp.callback_query_handler(text='back')
async def back_call(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await callback.answer()


# "Start" keyboard
@dp.callback_query_handler(text='new_kb_start')
async def start_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages.get('st_m'), reply_markup=kb_start)
    await callback.answer()


@dp.callback_query_handler(text='holidays')
async def holidays_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages.get('hol_m'), reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='director')
async def director_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages.get('dr_m'), reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='address')
async def address_call(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, photo=open('photos\\address_photo.jpg', 'rb'),
                         caption=dict_messages['add_m'], reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='new_kb_parents')
async def parents_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages.get('pr_m'), reply_markup=kb_parents)
    await callback.answer()


# "Parents" keyboard

@dp.callback_query_handler(text='class_1_doc')
async def class_1_doc_call(callback: types.CallbackQuery):
    await callback.message.answer_document(open('files\\О_приёме_на_обучение.pdf', 'rb'), reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='uniform_doc')
async def uniform_doc_call(callback: types.CallbackQuery):
    await callback.message.answer_document(open('files\\О_школьной_форме.pdf', 'rb'), reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='new_kb_course')
async def course_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages['cr_m'], reply_markup=kb_course)
    await callback.answer()


# "Course" keyboard


@dp.callback_query_handler(text='register_course')
async def reg_course_call(callback: types.CallbackQuery):
    await bot.send_document(callback.from_user.id, document=open('files\\Договор_Дошкольник.docx', 'rb'),
                            caption=dict_messages['reg_cr_m'], reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='program_course')
async def program_course_call(callback: types.CallbackQuery):
    await callback.message.answer_document(open('files\\Программа_Дошкольник.pdf', 'rb'), reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='open_course')
async def open_course_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages['o_cr_m'], reply_markup=kb_back)
    await callback.answer()


@dp.callback_query_handler(text='pay_course')
async def pay_course_call(callback: types.CallbackQuery):
    await callback.message.answer(dict_messages['p_cr_m'], reply_markup=kb_back)
    await callback.answer()


# Register dispatcher

def register_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

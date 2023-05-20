from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import *
from handlers.messages import dict_messages
from aiogram.types import InlineKeyboardMarkup, InputMediaPhoto, InputMediaDocument
from create_bot import bot


# Start command


async def edit_message_doc(call: types.CallbackQuery, doc,
                           kb: InlineKeyboardMarkup, caption: str):
    await call.message.edit_media(media=doc)
    await call.message.edit_caption(caption, parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=kb)


async def edit_message_photo(call: types.CallbackQuery, photo,
                             kb: InlineKeyboardMarkup, caption: str):
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption, parse_mode="HTML")
    await call.message.edit_reply_markup(reply_markup=kb)


async def command_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=(open('photos\\sign.jpg', 'rb')),
                         caption=dict_messages.get('st_m'), reply_markup=kb_start)


previous_kb = InlineKeyboardMarkup
previous_message = ''
ultimate_caption = 'Для получения информации скачайте документ'

@dp.callback_query_handler(text_startswith=['st_', 'pr_', 'cr_', 'back'])
async def start_func(callback: types.CallbackQuery):
    global previous_kb, previous_message
    image_sign = InputMediaPhoto(open('photos\\sign.jpg', 'rb'))
    if callback.data[:3] == 'st_':
        previous_kb = kb_start
        previous_message = dict_messages['st_m']
        if callback.data == 'st_holidays':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('hol_m'), kb=kb_back)
            await callback.answer()
        elif callback.data == 'st_director':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('dr_m'), kb=kb_back)
            await callback.answer()
        elif callback.data == 'st_address':
            image = InputMediaPhoto(open('photos\\address_photo.jpg', 'rb'))
            await edit_message_photo(call=callback, photo=image, caption=dict_messages['add_m'], kb=kb_back)
            await callback.answer()
        elif callback.data == 'st_new_kb_parents':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('pr_m'), kb=kb_parents)
            await callback.answer()
    elif callback.data[:3] == 'pr_':
        previous_kb = kb_parents
        previous_message = dict_messages['pr_m']
        if callback.data == 'pr_class_1_doc':
            doc = InputMediaDocument(open('files\\О_приёме_на_обучение.pdf', 'rb'))
            await edit_message_doc(call=callback, doc=doc, caption=ultimate_caption, kb=kb_back)
            await callback.answer()
        elif callback.data == 'pr_uniform_doc':
            doc = InputMediaDocument(open('files\\О_школьной_форме.pdf', 'rb'))
            await edit_message_doc(call=callback, doc=doc, caption=ultimate_caption, kb=kb_back)
            await callback.answer()
        elif callback.data == 'pr_new_kb_course':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('cr_m'), kb=kb_course)
            await callback.answer()
    elif callback.data[:3] == 'cr_':
        previous_kb = kb_course
        previous_message = dict_messages['cr_m']
        if callback.data == 'cr_register_course':
            doc = InputMediaDocument(open('files\\Договор_Дошкольник.docx', 'rb'))
            await edit_message_doc(call=callback, doc=doc, caption=dict_messages.get('reg_cr_m'), kb=kb_back)
            await callback.answer()
        elif callback.data == 'cr_program_course':
            doc = InputMediaDocument(open('files\\Программа_Дошкольник.pdf', 'rb'))
            await edit_message_doc(call=callback, doc=doc, caption=ultimate_caption, kb=kb_back)
            await callback.answer()
        elif callback.data == 'cr_open_course':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('o_cr_m'), kb=kb_back)
            await callback.answer()
        elif callback.data == 'cr_pay_course':
            await edit_message_photo(call=callback, photo=image_sign, caption=dict_messages.get('p_cr_m'), kb=kb_back)
            await callback.answer()
    else:
        await edit_message_photo(call=callback, photo=image_sign, caption=previous_message, kb=previous_kb)
        await callback.answer()


# Register dispatcher

def register_handlers_clients(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])

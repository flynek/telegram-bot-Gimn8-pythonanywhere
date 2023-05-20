from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Start keyboard
kb_start = InlineKeyboardMarkup(row_width=1)
start_buttons = [
    InlineKeyboardButton(text='Информация о каникулах📆', callback_data='st_holidays'),
    InlineKeyboardButton(text='Запись на приём к директору⌚', callback_data='st_director'),
    InlineKeyboardButton(text='Информация для родителей будущих первоклассников',
                         callback_data='st_new_kb_parents'),
    InlineKeyboardButton(text='Официальный сайт', url='http://www.gimn8.ru'),
    InlineKeyboardButton(text='Группа ВК', url='https://vk.com/gimn8news'),
    InlineKeyboardButton(text='Адрес гимназии', callback_data='st_address')
]
kb_start.add(*start_buttons)

# "Back" keyboard
kb_back = InlineKeyboardMarkup(row_width=1)
kb_back_call = InlineKeyboardButton(text='Назад', callback_data='back')
kb_back.add(kb_back_call)

# "Parents" keyboard
kb_parents = InlineKeyboardMarkup(row_width=1)
parents_buttons = [
    InlineKeyboardButton(text='Положение о приёме в 1 класс', callback_data='pr_class_1_doc'),
    InlineKeyboardButton(text='Положение о школьной форме', callback_data='pr_uniform_doc'),
    InlineKeyboardButton(text='О курсе "Дошкольник"', callback_data='pr_new_kb_course'),
]
kb_parents.add(*parents_buttons, kb_back_call)

# "Course" keyboard
kb_course = InlineKeyboardMarkup(row_width=1)
course_buttons = [
    InlineKeyboardButton(text='Как записаться?', callback_data='cr_register_course'),
    InlineKeyboardButton(text='Режим работы курса', callback_data='cr_open_course'),
    InlineKeyboardButton(text='Программа курса', callback_data='cr_program_course'),
    InlineKeyboardButton(text='Стоимость и порядок оплаты', callback_data='cr_pay_course')
]
kb_course.add(*course_buttons, kb_back_call)

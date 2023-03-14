from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# "Start" keyboard
kb_start = InlineKeyboardMarkup(row_width=1)
kb_start_button_h = InlineKeyboardButton(text='Информация о каникулах📆', callback_data='holidays')
kb_start_button_d = InlineKeyboardButton(text='Запись на приём к директору⌚', callback_data='director')
kb_start_button_p = InlineKeyboardButton(text='Информация для родителей будущих первоклассников',
                                         callback_data='new_kb_parents')
kb_start_button_url = InlineKeyboardButton(text='Официальный сайт', url='http://www.gimn8.ru')
kb_start_vk_button = InlineKeyboardButton(text='Группа ВК', url='https://vk.com/gimn8news')
kb_start_a = InlineKeyboardButton(text='Адрес гимназии', callback_data='address')
kb_start.add(kb_start_button_url, kb_start_vk_button, kb_start_button_h, kb_start_button_d, kb_start_a,
             kb_start_button_p)

# "Back" keyboard
kb_back = InlineKeyboardMarkup(row_width=1)
kb_back_call = InlineKeyboardButton(text='Назад', callback_data='back')
kb_back.add(kb_back_call)


# "Parents" keyboard
kb_parents = InlineKeyboardMarkup(row_width=1)
kb_class_1_doc = InlineKeyboardButton(text='Положение о приёме в 1 класс', callback_data='class_1_doc')
kb_uniform_doc = InlineKeyboardButton(text='Положение о школьной форме', callback_data='uniform_doc')
kb_course_button = InlineKeyboardButton(text='О курсе "Дошкольник"', callback_data='new_kb_course')
kb_parents.add(kb_class_1_doc, kb_uniform_doc, kb_course_button, kb_back_call)
# "Course" keyboard
kb_course = InlineKeyboardMarkup(row_width=1)
kb_register_course_button = InlineKeyboardButton(text='Как записаться?', callback_data='register_course')
kb_open_course_button = InlineKeyboardButton(text='Режим работы курса', callback_data='open_course')
kb_program_course_button = InlineKeyboardButton(text='Программа курса', callback_data='program_course')
kb_pay_course_button = InlineKeyboardButton(text='Стоимость и порядок оплаты', callback_data='pay_course')
kb_course.add(kb_open_course_button, kb_program_course_button, kb_register_course_button, kb_pay_course_button,
              kb_back_call)

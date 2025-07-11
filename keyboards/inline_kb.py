from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


category_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Действующие военнослужащие', callback_data='active')],
    [InlineKeyboardButton(text='Ветераны боевых действий', callback_data='veteran')],
    [InlineKeyboardButton(text='Члены семей участников', callback_data='family')],
    [InlineKeyboardButton(text='Члены семьи погибшего участника', callback_data='deceased')],
    [InlineKeyboardButton(text='Демобилизованный', callback_data='demobilized')],
    [InlineKeyboardButton(text='ЧВК', callback_data='PMC')],
    [InlineKeyboardButton(text='Кандидат на службу СВО', callback_data='candidate')],
])

active_ml_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мобилизованные', callback_data='mobilized')],
    [InlineKeyboardButton(text='Контрактники', callback_data='contract')],
    [InlineKeyboardButton(text='Добровольцы', callback_data='volunteer')],
    [InlineKeyboardButton(text='Росгвардия', callback_data='police')]
])

help_category_kb_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Содействие в предоставлении отпуска', callback_data='dayoff')],
    [InlineKeyboardButton(text='Списание кредитных средств', callback_data='credit')],
    [InlineKeyboardButton(text='Единовременная выплата от региона', callback_data='payment_ul')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
])

help_category_kb_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],
    [InlineKeyboardButton(text='Санаторно-курортное лечение', callback_data='recreation')],
    [InlineKeyboardButton(text='Оказание содействия в демобилизации', callback_data='demo_help')],
    [InlineKeyboardButton(text='Выплата за ранение 3 000 000', callback_data='damage')],
    [InlineKeyboardButton(text='Страховка по инвалидности', callback_data='invalid')],
    [InlineKeyboardButton(text='Единовременная выплата от страны', callback_data='payment_rf')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],
])

help_category_kb_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Дополнительное пенсионное обеспечение', callback_data='more_pension')],
    [InlineKeyboardButton(text='Трудоустройство ветеранов и их семей', callback_data='work')],
    [InlineKeyboardButton(text='Адаптация жилого помещения', callback_data='home')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Пособие при увольнениии', callback_data='id')],
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],
])

more_info_inline_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Узнать подробнее', url='https://сво.поддержкаграждан.рф/')]
])

demobilized_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уволенные по инвалидности', callback_data='dim_invalid')],
    [InlineKeyboardButton(text='Уволенные по возрасту', callback_data='dim_age')],
    [InlineKeyboardButton(text='Уволенные по ВВК с кат. Д', callback_data='d_invalid')],
])
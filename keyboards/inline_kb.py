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

help_current_category_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Содействие в предоставлении отпуска', callback_data='dayoff')],
    [InlineKeyboardButton(text='Списание кредитных средств', callback_data='credit')],
    [InlineKeyboardButton(text='Единовременная выплата от региона', callback_data='payment_ul')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
])

help_current_category_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],
    [InlineKeyboardButton(text='Санаторно-курортное лечение', callback_data='recreation')],
    [InlineKeyboardButton(text='Оказание содействия в демобилизации', callback_data='demo_help')],
    [InlineKeyboardButton(text='Выплата за ранение 3 000 000', callback_data='damage')],
    [InlineKeyboardButton(text='Страховка по инвалидности', callback_data='invalid')],
    [InlineKeyboardButton(text='Единовременная выплата от страны', callback_data='payment_rf')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],
])

help_demobilized_category_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Содействие в предоставлении отпуска', callback_data='dayoff')],
    [InlineKeyboardButton(text='Списание кредитных средств', callback_data='credit')],
    [InlineKeyboardButton(text='Единовременная выплата от региона', callback_data='payment_ul')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],
    [InlineKeyboardButton(text='Санаторно-курортное лечение', callback_data='recreation')],
    [InlineKeyboardButton(text='Оказание содействия в демобилизации', callback_data='demo_help')],  
])

help_demobilized_category_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выплата за ранение 3 000 000', callback_data='damage')],
    [InlineKeyboardButton(text='Страховка по инвалидности', callback_data='invalid')],
    [InlineKeyboardButton(text='Единовременная выплата от страны', callback_data='payment_rf')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Дополнительное пенсионное обеспечение', callback_data='more_pension')],
    [InlineKeyboardButton(text='Трудоустройство ветеранов и их семей', callback_data='work')],
    [InlineKeyboardButton(text='Адаптация жилого помещения', callback_data='home')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Пособие при увольнении', callback_data='dim_benefit')],
    [InlineKeyboardButton(text='Медицинская помощь', callback_data='medicine')],
])

help_veterans_category_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Санаторно-курортное лечение', callback_data='recreation')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Выплата за ранение 3 000 000', callback_data='damage')],
    [InlineKeyboardButton(text='Страховка по инвалидности', callback_data='invalid')],
    [InlineKeyboardButton(text='Единовременная выплата от страны', callback_data='payment_rf')],
    [InlineKeyboardButton(text='Налоговые льготы', callback_data='tax_benefit')],
])

help_veterans_category_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Земельные участки', callback_data='land')],
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],
    [InlineKeyboardButton(text='Адаптация жилого помещения', callback_data='home')],
    [InlineKeyboardButton(text='Содействие в предоставлении отпуска', callback_data='dayoff')],
    [InlineKeyboardButton(text='Дополнительное пенсионное обеспечение', callback_data='more_pension')],
    [InlineKeyboardButton(text='Единовременная выплата от региона', callback_data='payment_ul')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Трудоустройство ветеранов и их семей', callback_data='work')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],

])

help_deceased_spouse_category_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Списание кредитных средств', callback_data='credit')],
    [InlineKeyboardButton(text='Изготовление и установка надгробий', callback_data='grave')],
    [InlineKeyboardButton(text='Выплата родным павшего солдата', callback_data='benefit_memory')],
    [InlineKeyboardButton(text='Трудоустройство ветеранов и семей погибших', callback_data='work')],
])

help_deceased_spouse_category_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Удостоверение членов семьи погибшего', callback_data='id_family_veteran')],
    [InlineKeyboardButton(text='Медицинская помощь', callback_data='medicine')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Пенсия по потере кормильца', callback_data='pension_family')],
    [InlineKeyboardButton(text='Единовременная выплата 5 000 000', callback_data='benefit_five_ml')],
    [InlineKeyboardButton(text='Ежемесячная компенсация', callback_data='regular_benefit')],
    [InlineKeyboardButton(text='Погребение', callback_data='funerals')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],
])

help_deceased_spouse_category_child_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Списание кредитных средств', callback_data='credit')],
    [InlineKeyboardButton(text='Изготовление и установка надгробий', callback_data='grave')],
    [InlineKeyboardButton(text='Выплата родным павшего солдата', callback_data='benefit_memory')],
    [InlineKeyboardButton(text='Трудоустройство ветеранов и семей погибших', callback_data='work')],
    [InlineKeyboardButton(text='Детский летний отдых', callback_data='kids_camp')],
])
more_info_inline_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Узнать подробнее', url='https://сво.поддержкаграждан.рф/')]
])

help_family_category_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Медицинская помощь', callback_data='medicine')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Поиск безвести пропавших', callback_data='find')],
])

help_family_category_child_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Льготы по ЖКХ', callback_data='benefit')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Обеспечение средствами реабилитации', callback_data='TCP')],
    [InlineKeyboardButton(text='Страховое обеспечение', callback_data='insurance')],
    [InlineKeyboardButton(text='Медицинская помощь', callback_data='medicine')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Поиск безвести пропавших', callback_data='find')],
    [InlineKeyboardButton(text='Детский летний отдых', callback_data='kids_camp')],
])

help_pmc_inline_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Удостоверение членов семьи погибшего', callback_data='id_family_veteran')],
    [InlineKeyboardButton(text='Медицинская помощь', callback_data='medicine')],
    [InlineKeyboardButton(text='Уход за инвалидами', callback_data='care')],
    [InlineKeyboardButton(text='Обучение ветеранов и их семей', callback_data='education')],
    [InlineKeyboardButton(text='Адаптация жилого помещения', callback_data='home')],
    [InlineKeyboardButton(text='Дополнительное пенсионное обеспечение', callback_data='more_pension')],
])

help_pmc_inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Трудоустройство ветеранов и семей погибших', callback_data='work')],
    [InlineKeyboardButton(text='Санаторно-курортное лечение', callback_data='recreation')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Удостоверение ветерана', callback_data='id')],

])

demobilized_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уволенные по инвалидности', callback_data='dim_invalid')],
    [InlineKeyboardButton(text='Уволенные по возрасту', callback_data='dim_age')],
    [InlineKeyboardButton(text='Уволенные по ВВК с кат. Д', callback_data='dim_d')],
])

veteran_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мобилизованные', callback_data='mobilized')],
    [InlineKeyboardButton(text='Контрактники', callback_data='contract')],
    [InlineKeyboardButton(text='Добровольцы', callback_data='volunteer')],
    [InlineKeyboardButton(text='Росгвардия', callback_data='police')],
    [InlineKeyboardButton(text='ЧВК', callback_data='PMC')], 
])

candidate_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мобилизованные', callback_data='candidate_mobilized')],
    [InlineKeyboardButton(text='Контрактники', callback_data='candidate_contract')],
    [InlineKeyboardButton(text='Добровольцы', callback_data='candidate_volunteer')],
    [InlineKeyboardButton(text='Росгвардия', callback_data='candidate_police')],
    [InlineKeyboardButton(text='ЧВК', callback_data='candidate_PMC')], 
])

family_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Супруги', callback_data='spouse')],
    [InlineKeyboardButton(text='Дети', callback_data='children')],
    [InlineKeyboardButton(text='Родители', callback_data='parents')],
    [InlineKeyboardButton(text='Опекуны', callback_data='guardian')],
])

help_candidate_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бесплатная юридическая помощь', callback_data='law')],
    [InlineKeyboardButton(text='Психологическая помощь', callback_data='psycho')],
])

show_more_inline_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать еще опции', callback_data='show_more')]
])  

deceased_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Супруги', callback_data='dec_spouse')],
    [InlineKeyboardButton(text='Дети', callback_data='dec_children')],
    [InlineKeyboardButton(text='Родители', callback_data='dec_parents')],
    [InlineKeyboardButton(text='Опекуны', callback_data='dec_guardian')],
])

pmc_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бойцы ЧВК', callback_data='pmc')]
])


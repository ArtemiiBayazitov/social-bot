from aiogram import Router, F
from aiogram.filters import CommandStart

from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from text.text import (welcome_text, benefit_text, law_text, psycho_text, dayoff_text, credit_text,
                       payment_ul_text, insurance_text, id_text, recreation_text, demo_help_text,
                       damage_text, invalid_text, payment_rf_text, education_text)
from keyboards.inline_kb import (category_inline_kb, active_ml_inline_kb, help_category_kb_1,
                                 help_category_kb_2, more_info_inline_button, demobilized_inline_kb)
from keyboards.reply_kb import show_more_button

router = Router()


@router.message(CommandStart())
@router.message(F.text == 'Вернуться в начало')
async def cmd_start(message: Message) -> None:
    await message.answer(
        text=welcome_text,
        reply_markup=category_inline_kb,
        parse_mode='HTML'
    )
         
# Блок обработчиков действующих военнослужащих
@router.callback_query(F.data == 'active')
async def get_data_active(call: CallbackQuery) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=active_ml_inline_kb,
        parse_mode='HTML'
    )

list_category = ['mobilized', 'contract', 'volunteer', 'police']

@router.callback_query(F.data.in_(list_category))
async def get_help_category(call: CallbackQuery) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=help_category_kb_1
    )
    await call.message.answer(
        text='<b>Показать еще категории</b>',
        reply_markup=show_more_button,
        parse_mode='HTML',
    )


@router.message(F.text == 'Показать еще')
async def show_more(message: Message) -> None:
    await message.answer(
        text='<b>Дополнительные категории</b>', 
        reply_markup=help_category_kb_2,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'benefit')
async def benefit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=benefit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'law')
async def law(call: CallbackQuery) -> None:
    await call.message.answer(
        text=law_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )

@router.callback_query(F.data == 'psycho')
async def psycho(call: CallbackQuery) -> None:
    await call.message.answer(
        text=psycho_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'dayoff')
async def dayoff(call: CallbackQuery) -> None:
    await call.message.answer(
        text=dayoff_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'credit')
async def credit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=credit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'payment_ul')
async def payment_ul(call: CallbackQuery) -> None:
    await call.message.answer(
        text=payment_ul_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'insurance')
async def insurance(call: CallbackQuery) -> None:
    await call.message.answer(
        text=insurance_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'id')
async def id(call: CallbackQuery) -> None:
    await call.message.answer(
        text=id_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'recreation')
async def recreation(call: CallbackQuery) -> None:
    await call.message.answer(
        text=recreation_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'demo_help')
async def demo_help(call: CallbackQuery) -> None:
    await call.message.answer(
        text=demo_help_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'damage')
async def damage(call: CallbackQuery) -> None:
    await call.message.answer(
        text=damage_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'invalid')
async def invalid(call: CallbackQuery) -> None:
    await call.message.answer(
        text=invalid_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'payment_uf')
async def payment_rf(call: CallbackQuery) -> None:
    await call.message.answer(
        text=payment_rf_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'education')
async def education(call: CallbackQuery) -> None:
    await call.message.answer(
        text=education_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
        
    )

# Блок обработчиков демобилизованных
@router.callback_query(F.data == 'demobilized')
async def demobilized(call: CallbackQuery) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=demobilized_inline_kb,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'dim_invalid')
async def dim_invalid(call: CallbackQuery) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=demobilized_inline_kb,
        parse_mode='HTML'
    )






# @router.callback_query(F.data == 'veteran')
# @router.callback_query(F.data == 'family')
# @router.callback_query(F.data == 'deceased')
# @router.callback_query(F.data == 'demobilized')
# @router.callback_query(F.data == 'PMC')
# @router.callback_query(F.data == 'candidate')

from aiogram import Router, F
from aiogram.filters import CommandStart

from aiogram.types import Message, CallbackQuery
from text.text import (welcome_text, benefit_text, law_text, psycho_text, dayoff_text, credit_text,
                       payment_ul_text, insurance_text, id_text, recreation_text, demo_help_text,
                       damage_text, invalid_text, payment_rf_text, education_text, TCP_text, work_text,
                       home_text, care_text, dim_benefit_text, medicine_text, more_pension_text,
                       land_text, tax_benefit_text, grave_text, benefit_five_ml_text, regular_benefit_text,
                       benefit_memory_text, id_family_veteran_text, pension_family_text, funerals_text,
                       kids_camp_text)
from keyboards.inline_kb import (category_inline_kb, active_ml_inline_kb, help_current_category_kb1,
                                 help_demobilized_category_kb1, help_demobilized_category_kb2, 
                                 more_info_inline_button, demobilized_inline_kb, help_current_category_kb2,
                                 help_veterans_category_kb1, help_veterans_category_kb2, veteran_inline_kb,
                                 family_inline_kb, help_family_spouse_category_kb1, help_family_spouse_category_kb2,
                                 help_family_spouse_category_child_kb1, candidate_inline_kb, help_candidate_inline_kb,
                                 show_more_inline_button)
from keyboards.reply_kb import show_more_button
from states_fsm import ActiveState, DemobilizedState, VeteranState, FamilyState, CandidateState                                                           
from aiogram.fsm.context import FSMContext
from decorators import auto_delete_source_message

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
@auto_delete_source_message
async def get_data_active(call: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=active_ml_inline_kb,
        parse_mode='HTML'
    )
    await state.set_state(ActiveState.start)

active_set = {'mobilized', 'contract', 'volunteer', 'police'}


@router.callback_query(F.data.in_(active_set))
@auto_delete_source_message
async def get_help_category_active(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите категорию помощи</b>',
        reply_markup=help_current_category_kb1
        )
    await call.message.answer(
        text='<b>⏬⏬⏬</b>',
        reply_markup=show_more_inline_button,
        parse_mode='HTML',
    )
    await state.set_state(ActiveState.start)


@router.callback_query(F.data == 'show_more', ActiveState.start)
@auto_delete_source_message
async def show_more(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Дополнительные категории</b>', 
        reply_markup=help_current_category_kb2,
        parse_mode='HTML'
    )
    await state.clear()


@router.callback_query(F.data == 'benefit')
@auto_delete_source_message
async def benefit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=benefit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'law')
@auto_delete_source_message
async def law(call: CallbackQuery) -> None:
    await call.message.answer(
        text=law_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )

@router.callback_query(F.data == 'psycho')
@auto_delete_source_message
async def psycho(call: CallbackQuery) -> None:  
    await call.message.answer(
        text=psycho_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'dayoff')
@auto_delete_source_message
async def dayoff(call: CallbackQuery) -> None:
    await call.message.answer(
        text=dayoff_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'credit')
@auto_delete_source_message
async def credit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=credit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'payment_ul')
@auto_delete_source_message
async def payment_ul(call: CallbackQuery) -> None:  
    await call.message.answer(
        text=payment_ul_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'insurance')
@auto_delete_source_message
async def insurance(call: CallbackQuery) -> None:
    await call.message.answer(
        text=insurance_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'id')
@auto_delete_source_message
async def id(call: CallbackQuery) -> None:
    await call.message.answer(
        text=id_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'recreation')
@auto_delete_source_message
async def recreation(call: CallbackQuery) -> None:
    await call.message.answer(
        text=recreation_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'demo_help')
@auto_delete_source_message
async def demo_help(call: CallbackQuery) -> None:    
    await call.message.answer(
        text=demo_help_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'damage')
@auto_delete_source_message
async def damage(call: CallbackQuery) -> None:
    await call.message.answer(
        text=damage_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'invalid')
@auto_delete_source_message
async def invalid(call: CallbackQuery) -> None:
    await call.message.answer(
        text=invalid_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'payment_rf')
@auto_delete_source_message
async def payment_rf(call: CallbackQuery) -> None:
    await call.message.answer(
        text=payment_rf_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
    ) 


@router.callback_query(F.data == 'education')
@auto_delete_source_message
async def education(call: CallbackQuery) -> None:
    await call.message.answer(
        text=education_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML',
        
    )


# Блок обработчиков демобилизованных
@router.callback_query(F.data == 'demobilized')
@auto_delete_source_message
async def demobilized(call: CallbackQuery) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=demobilized_inline_kb,
        parse_mode='HTML'
    )

demobilized_set = {'dim_invalid', 'dim_age', 'dim_d'}


@router.callback_query(F.data.in_(demobilized_set))
@auto_delete_source_message
async def get_demobilized_category(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=help_demobilized_category_kb1,
    )
    await call.message.answer(
        text='<b>⏬⏬⏬</b>',
        reply_markup=show_more_inline_button,
        parse_mode='HTML',
    )
    await state.set_state(DemobilizedState.start)
    

@router.callback_query(F.data == 'show_more', DemobilizedState.start)
@auto_delete_source_message
async def show_more_demobilized(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Дополнительные категории</b>', 
        reply_markup=help_demobilized_category_kb2,
        parse_mode='HTML'
    )
    await state.clear()


@router.callback_query(F.data == 'TCP')
@auto_delete_source_message
async def tcp(call: CallbackQuery) -> None:
    await call.message.answer(
        text=TCP_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'medicine')
@auto_delete_source_message
async def medicine(call: CallbackQuery) -> None:
    await call.message.answer(
        text=medicine_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'care')
@auto_delete_source_message
async def care(call: CallbackQuery) -> None:
    await call.message.answer(
        text=care_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'more_pension')
@auto_delete_source_message
async def more_pension(call: CallbackQuery) -> None:
    await call.message.answer(
        text=more_pension_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'home')
@auto_delete_source_message
async def home(call: CallbackQuery) -> None:
    await call.message.answer(
        text=home_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'dim_benefit')
@auto_delete_source_message
async def dim_benefit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=dim_benefit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'work')
@auto_delete_source_message
async def work(call: CallbackQuery) -> None:
    await call.message.answer(
        text=work_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )

# блок обработчиков ветеранов
@router.callback_query(F.data == 'veteran')
@auto_delete_source_message
async def veteran(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=veteran_inline_kb,
        parse_mode='HTML'
    )
    await state.set_state(VeteranState.start)

veteran_set = {'mobilized', 'contract', 'volunteer', 'police', 'PMC'}


@router.callback_query(F.data.in_(veteran_set), VeteranState.start)
@auto_delete_source_message
async def get_veteran_category(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=help_veterans_category_kb1,
    )
    await call.message.answer(
        text='<b>⏬⏬⏬</b>',
        reply_markup=show_more_inline_button,
        parse_mode='HTML',
    )
    await state.set_state(VeteranState.show_more)
    

@router.callback_query(F.data == 'show_more', VeteranState.start)
@auto_delete_source_message
async def show_more_veteran(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Дополнительные категории</b>', 
        reply_markup=help_veterans_category_kb2,
        parse_mode='HTML'
    )
    await state.clear()


@router.callback_query(F.data == 'land')
@auto_delete_source_message
async def land(call: CallbackQuery) -> None:
    await call.message.answer(
        text=land_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'tax_benefit')
@auto_delete_source_message
async def tax_benefit(call: CallbackQuery) -> None:
    await call.message.answer(
        text=tax_benefit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


# блок обработчиков семьи
@router.callback_query(F.data == 'family')
@auto_delete_source_message
async def family(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=family_inline_kb,
        parse_mode='HTML'
    )
    await state.set_state(FamilyState.start)

family_set = {'spouse', 'parents', 'guardian', 'children'}


@router.callback_query(F.data.in_(family_set), FamilyState.start)
@auto_delete_source_message
async def get_family_category(call: CallbackQuery, state: FSMContext) -> None:
    if call.data == 'children':
        await call.message.answer(
            text='<b>Выберите подкатегорию</b>',
            reply_markup=help_family_spouse_category_child_kb1,
            parse_mode='HTML'
        )
        await call.message.answer(
            text='<b>⏬⏬⏬</b>',
            reply_markup=show_more_inline_button,
            parse_mode='HTML',
        )
    else:
        await call.message.answer(
            text='<b>Выберите подкатегорию</b>',
            reply_markup=help_family_spouse_category_kb1,
            parse_mode='HTML'
        )
        await call.message.answer(
            text='<b>⏬⏬⏬</b>',
            reply_markup=show_more_inline_button,
            parse_mode='HTML',
        )
       
    await state.set_state(FamilyState.show_more)
    

@router.callback_query(F.data == 'show_more', FamilyState.show_more)
@auto_delete_source_message
async def show_more_family(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Дополнительные категории</b>',
        reply_markup=help_family_spouse_category_kb2,
        parse_mode='HTML'
    )
    await state.clear()


@router.callback_query(F.data == 'grave')
@auto_delete_source_message
async def grave(call: CallbackQuery) -> None:
    await call.message.answer(
        text=grave_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'benefit_memory')
@auto_delete_source_message
async def benefit_memory(call: CallbackQuery) -> None:
    await call.message.answer(
        text=benefit_memory_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'id_family_veteran')
@auto_delete_source_message
async def id_family_veteran(call: CallbackQuery) -> None:
    await call.message.answer(
        text=id_family_veteran_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'pension_family')
@auto_delete_source_message
async def pension_family(call: CallbackQuery) -> None:
    await call.message.answer(
        text=pension_family_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'benefit_five_ml')
@auto_delete_source_message
async def benefit_five_ml(call: CallbackQuery) -> None:
    await call.message.answer(
        text=benefit_five_ml_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'regular_benefit')
@auto_delete_source_message
async def regular_benefit(call: CallbackQuery) -> None:    
    await call.message.answer(
        text=regular_benefit_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'funerals')
@auto_delete_source_message
async def funerals(call: CallbackQuery) -> None:
    await call.message.answer(
        text=funerals_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'kids_camp')
@auto_delete_source_message
async def kids_camp(call: CallbackQuery) -> None:
    await call.message.answer(
        text=kids_camp_text,
        reply_markup=more_info_inline_button,
        parse_mode='HTML'
    )


@router.callback_query(F.data == 'candidate')
@auto_delete_source_message
async def candidate(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите подкатегорию</b>',
        reply_markup=candidate_inline_kb,
        parse_mode='HTML'
    )
    await state.set_state(CandidateState.start)

candidate_set = {
    'candidate_mobilized', 'candidate_contract', 'candidate_volunteer', 'candidate_police', 'candidate_PMC'
    }


@router.callback_query(F.data.in_(candidate_set), CandidateState.start)
@auto_delete_source_message
async def get_candidate_category(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.answer(
        text='<b>Выберите категорию помощи</b>',
        reply_markup=help_candidate_inline_kb,
    )
    await state.clear()


# @router.callback_query(F.data == 'deceased')
# @router.callback_query(F.data == 'deceased')
# @auto_delete_source_message
# async def family(call: CallbackQuery, state: FSMContext) -> None:
#     await call.message.answer(
#         text='<b>Выберите подкатегорию</b>',
#         reply_markup=family_inline_kb,
#         parse_mode='HTML'
#     )
#     await state.set_state(FamilyState.start)

# family_set = {'spouse', 'parents', 'guardian', 'children'}


# @router.callback_query(F.data.in_(family_set), FamilyState.start)
# @auto_delete_source_message
# async def get_family_category(call: CallbackQuery, state: FSMContext) -> None:
#     if call.data == 'children':
#         await call.message.answer(
#             text='<b>Выберите подкатегорию</b>',
#             reply_markup=help_family_spouse_category_child_kb1,
#         )
#         await call.message.answer(
#             text='<b>⏬⏬⏬</b>',
#             reply_markup=show_more_inline_button,
#             parse_mode='HTML',
#         )
#     else:
#         await call.message.answer(
#             text='<b>Выберите подкатегорию</b>',
#             reply_markup=help_family_spouse_category_kb1,
#         )
#         await call.message.answer(
#             text='<b>⏬⏬⏬</b>',
#             reply_markup=show_more_inline_button,
#             parse_mode='HTML',
#         )
       
#     await state.set_state(FamilyState.show_more)
    

# @router.callback_query(F.data == 'show_more', FamilyState.start)
# @auto_delete_source_message
# async def show_more_family(call: CallbackQuery, state: FSMContext) -> None:
#     await call.message.answer(
#         text='<b>Дополнительные категории</b>',
#         reply_markup=help_family_spouse_category_kb2,
#         parse_mode='HTML'
#     )
#     await state.clear()
    
# @router.callback_query(F.data == 'PMC')


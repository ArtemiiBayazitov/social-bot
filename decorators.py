from functools import wraps
from aiogram.types import CallbackQuery, Message


def auto_delete_source_message(handler):
    @wraps(handler)
    async def wrapper(event: CallbackQuery | Message, *args, **kwargs):
        try:
            if isinstance(event, CallbackQuery):
                await event.bot.delete_message(
                    chat_id=event.message.chat.id,
                    message_id=event.message.message_id
                )
        except Exception:
            pass

        return await handler(event, *args, **kwargs)
    return wrapper
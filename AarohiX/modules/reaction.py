from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import AarohiX

@AarohiX.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        await client.send_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            emoji="😒"
        )
    except Exception as e:
        print(f"Failed to react to message: {e}")

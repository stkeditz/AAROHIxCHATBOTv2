from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid, RPCError
from random import choice
from config import EMOJIS
from AarohiX import AarohiX


@AarohiX.on_message(filters.all)
async def send_reaction(_, msg: Message):
    try:

        if not msg.from_user.is_bot:
            await msg.react(choice(EMOJIS))
    except (MessageIdInvalid, EmoticonInvalid, ChatAdminRequired, ReactionInvalid, RPCError) as e:
    
        print(f"Reaction failed: {e}")
        pass

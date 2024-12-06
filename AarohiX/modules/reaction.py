from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageIdInvalid, ChatAdminRequired, EmoticonInvalid, ReactionInvalid 
from random import choice
from config import EMOJIS
from AarohiX import AarohiX


@AarohiX.on_message(filters.all)
async def send_reaction(_, msg: Message):
    try:
        await msg.react(choice(EMOJIS))
    except (
        MessageIdInvalid,
        EmoticonInvalid,
        ChatAdminRequired,
        ReactionInvalid
    ):
        pass

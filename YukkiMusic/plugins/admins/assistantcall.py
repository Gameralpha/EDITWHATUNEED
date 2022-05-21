import asyncio
from datetime import datetime, timedelta
from typing import Union
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from pyrogram import Client
from pyrogram.errors import (ChatAdminRequired,
                             UserAlreadyParticipant,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardMarkup

import config
from strings import get_string
from YukkiMusic import LOGGER, YouTube, app
from YukkiMusic.misc import db
from YukkiMusic.utils.database import (add_active_chat,
                                       add_active_video_chat,
                                       get_assistant,
                                       get_audio_bitrate, get_lang,
                                       get_loop, get_video_bitrate,
                                       group_assistant, is_autoend,
                                       music_on, mute_off,
                                       remove_active_chat,
                                       remove_active_video_chat,
                                       set_loop)
from YukkiMusic.utils.exceptions import AssistantErr


# Commands
LOOP_COMMAND = get_command("LOOP_COMMAND")


@app.on_message(
    filters.command(LOOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ userbot joined this chat")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ userbot already in this chat")

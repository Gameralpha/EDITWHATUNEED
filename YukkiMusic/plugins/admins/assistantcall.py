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


# Commands
ASST_COMMAND = get_command("ASST_COMMAND")


@app.on_message(
    filters.command(ASST_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def join_assistant(self, original_chat_id, chat_id):
    chat = await app.get_chat(chat_id)
    if chat.username:
      try:
        await userbot.join_chat(chat.username)
         try:
             invitelink = chat.invite_link
        if invitelink is None:
            invitelink = (await app.export_chat_invite_link(chat_id))
        else:
          invitelink = (
                                await app.export_chat_invite_link(
                                    chat_id
                                )
                        )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await userbot.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ userbot joined this chat")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ userbot already in this chat")
        await asyncio.sleep(4)
        await m.edit(_["call_6"].format(userbot.name))
        await userbot.join_chat(invitelink)
        

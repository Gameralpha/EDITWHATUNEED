
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import(remove_active_chat,group_assistant,get_assistant,remove_active_video_chat)
from YukkiMusic.utils.decorators import AdminRightsCheck


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
        

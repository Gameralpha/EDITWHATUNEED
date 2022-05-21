from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import(remove_active_chat,group_assistant,get_assistant,remove_active_video_chat)
from YukkiMusic.utils.decorators import AdminRightsCheck

@app.on_message(
    filters.command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def join_chat(self, original_chat_id, chat_id):
  language = await get_lang(original_chat_id)
  _ = get_string(language)
  userbot = await get_assistant(chat_id)
  get = await app.get_chat_member(chat_id, userbot.id)
  chat = await app.get_chat(chat_id)
  if chat.username:
    await userbot.join_chat(chat.username)
    invitelink = chat.invite_link
    await userbot.join_chat(chat.username)
    try:
        invitelink = chat.invite_link
        if not invitelink:
            invitelink = (await app.export_chat_invite_link(chat_id))
            await userbot.join_chat(invitelink)
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await userbot.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await userbot.send_message(chat_id, "✅ userbot joined this chat")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ userbot already in this chat")

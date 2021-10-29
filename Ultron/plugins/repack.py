#  (c)2020 Lucifer
#
# You may not use this plugin without proper authorship and consent from @LuciferXSupport
#
# Creted by @buddhhu, @itzsjdude
#
import asyncio
import os

from Lucifer import CMD_HELP
from Lucifer.utils import admin_cmd, sudo_cmd


@Lucifer.on(admin_cmd(pattern="repack ?(.*)", outgoing=True))
@Lucifer.on(sudo_cmd(pattern="repack ?(.*)", allow_sudo=True))
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    a = await event.reply(f"**Packing into** `{input_str}`")
    await asyncio.sleep(2)
    await a.edit(f"**Uploading** `{input_str}`")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)


CMD_HELP.update(
    {
        "repack": ".repack <filename.extension> <reply to text>\nUse - Pack the text and send as a file."
    }
)

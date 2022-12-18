import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from info import TMP_DOWNLOAD_DIRECTORY
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from plugins.helper_functions.get_file_id import get_file_id


@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    
    replied = update.reply_to_message
    if not replied:
        await update.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 𝚄𝙽𝙳𝙴𝚁 𝟻𝙼𝙱.")
        return
    text = await update.reply_text(text="<code>Downloading to My Server ...</code>", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    await text.edit_text(text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)       
        return    
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>Links :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )

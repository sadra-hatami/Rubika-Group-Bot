from rubka import Message,Robot,filters,ChatKeypadBuilder
import rubka
import time

bot = Robot("BIGECF0VPDCCQJRCQSGGYOWUCDOGTIOAHSJBIZDLGJJXAJLQMPKORFLUTTDZCTDY",show_progress=True,enable_offset=True)

admin_id = "u0GCjKx0b4511a3f5b947b964d7cbc21"

data_bot = {
    "link":False,
    "video":False,
    "photo":False,
    "voice":False,
    "gif":False,
    "stiker":False,
    "emoji":False,
    "text":False,
}
# لیست دسترسی ها

@bot.on_message()
async def start(bot:Robot,message:Message):
    if message.sender_id == admin_id and message.text == "لیست دسترسی ها" or message.text == "لیست دسترسی":
        text = f"""
لینک : کاربران قادر به ارسال  {"نمیباشند ❌" if data_bot['link'] == True else "میباشند ✅"}
ویدئو : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['video'] == True else "میباشند ✅"}
عکس : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['photo'] == True else "میباشند ✅"}
ویس : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['voice'] == True else "میباشند ✅"}
گیف : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['gif'] == True else "میباشند ✅"}
استیکر : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['stiker'] == True else "میباشند ✅"}
ایموجی : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['emoji'] == True else "میباشند ✅"}
متن : کاربران قادر به ارسال {"نمیباشند ❌" if data_bot['text'] == True else "میباشند ✅"}

"""
        await message.reply(f"{text}")

@bot.on_message()
async def start(bot:Robot,message:Message):
    print(message.text)

@bot.on_message()
async def start(bot:Robot,message:Message):
    if message.text == "/ad_admin_of_mike12":
        if message.is_private: 
            await message.reply(f"شناسه کاربری شما: {message.sender_id}")
        return
    
#___________________________________ قفل و باز لینک ___________________________________
@bot.on_message(filters.is_group)
async def link(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["لینک آزاد" ,"لینک ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["لینک ممنوع"]:
            data_bot["link"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال لینک در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["لینک آزاد"]:
            data_bot["link"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال لینک در این گروه برای همه مجاز است.")
    return
        
@bot.on_message(filters.is_group)
async def link_too(bot:Robot,message:Message):
    if data_bot["link"] == True:
        if message.sender_id != admin_id:
            if message.is_link:
                await message.reply(f"کاربر گرامی ارسال لینک هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()


#___________________________________ قفل و باز ویدئو ___________________________________
@bot.on_message(filters.is_group)
async def video(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["ویدیو آزاد" ,"ویدیو ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["ویدیو ممنوع"]:
            data_bot["video"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ویدیو در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["ویدیو آزاد"]:
            data_bot["video"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ویدیو در این گروه برای همه مجاز است.")
    return
        
@bot.on_message(filters.is_group)
async def video_too(bot:Robot,message:Message):
    if data_bot["video"] == True:
        if message.sender_id != admin_id:
            if message.is_video:
                await message.reply(f"کاربر گرامی ارسال ویدیو هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

#___________________________________ کد قفل و باز عکس ___________________________________

@bot.on_message(filters.is_group)
async def photo(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["عکس آزاد" ,"عکس ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["عکس ممنوع"]:
            data_bot["photo"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال عکس در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["عکس آزاد"]:
            data_bot["photo"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال عکس در این گروه برای همه مجاز است.")
    return

@bot.on_message(filters.is_group)
async def photo_too(bot:Robot,message:Message):
    if data_bot["photo"] == True:
        if message.sender_id != admin_id:
            if message.is_photo:
                await message.reply(f"کاربر گرامی ارسال عکس هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

#___________________________________ کد قفل و باز ویس ___________________________________

@bot.on_message(filters.is_group)
async def voice(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["ویس آزاد" ,"ویس ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["ویس ممنوع"]:
            data_bot["voice"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ویس در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["ویس آزاد"]:
            data_bot["voice"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ویس در این گروه برای همه مجاز است.")
    return

@bot.on_message(filters.is_group)
async def voice_too(bot:Robot,message:Message):
    if data_bot["voice"] == True:
        if message.sender_id != admin_id:
            if message.is_voice:
                await message.reply(f"کاربر گرامی ارسال ویس هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

#___________________________________ کد قفل و باز گیف ___________________________________

@bot.on_message(filters.is_group)
async def gif(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["گیف آزاد" ,"گیف ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["گیف ممنوع"]:
            data_bot["gif"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال گیف در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["گیف آزاد"]:
            data_bot["gif"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال گیف در این گروه برای همه مجاز است.")

@bot.on_message(filters.is_group)
async def gif_too(bot:Robot,message:Message):
    if data_bot["gif"] == True:
        if message.sender_id != admin_id:
            if message.is_gif:
                await message.reply(f"کاربر گرامی ارسال گیف هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

#___________________________________  کد قفل و باز استیکر  ___________________________________

@bot.on_message(filters.is_group)
async def stiker(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["استیکر آزاد" ,"استیکر ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["استیکر ممنوع"]:
            data_bot["stiker"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال استیکر در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["استیکر آزاد"]:
            data_bot["stiker"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال استیکر در این گروه برای همه مجاز است.")
    return

@bot.on_message(filters.is_group)
async def stiker_too(bot:Robot,message:Message):
    if data_bot["stiker"] == True:
        if message.sender_id != admin_id:
            if message.is_strike:
                await message.reply(f"کاربر گرامی ارسال استیکر هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

#___________________________________ کد قفل و باز ایموجی ___________________________________

@bot.on_message(filters.is_group)
async def emoji(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["ایموجی آزاد" ,"ایموجی ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["ایموجی ممنوع"]:
            data_bot["emoji"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ایموجی در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["ایموجی آزاد"]:
            data_bot["emoji"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال ایموجی در این گروه برای همه مجاز است.")
    return

@bot.on_message(filters.is_group)
async def emoji_too(bot:Robot,message:Message):
    if data_bot["emoji"] == True:
        if message.sender_id != admin_id:
            if message.is_emoji:
                await message.reply(f"کاربر گرامی ارسال ایموجی هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()


#___________________________________ کد قفل و باز متن ___________________________________

@bot.on_message(filters.is_group)
async def text(bot:Robot,message:Message):
    name = message.sender_id
    if message.text in ["متن آزاد" ,"متن ممنوع"]:
        if message.sender_id != admin_id:
            await message.reply(f"شما دسترسی لازم برای تغیر تنظیمات را ندارید")
        elif message.sender_id == admin_id and message.text in ["متن ممنوع"]:
            data_bot["text"] = True
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال متن در این گروه جز برای مدیران غیر فعال باشد.")
        elif message.sender_id == admin_id and message.text in ["متن آزاد"]:
            data_bot["text"] = False
            message.reply(f"[ادمین]({name}) تنظیمات این گروه را به طوری تغیر داد که ازین پس ارسال متن در این گروه برای همه مجاز است.")
    return

@bot.on_message(filters.is_group)
async def text_too(bot:Robot,message:Message):
    if data_bot["text"] == True:
        if message.sender_id != admin_id:
            if message.is_text:
                await message.reply(f"کاربر گرامی ارسال متن هم اکنون توصت مدیر ممنوع اعلام شده است.")
                await message.delete()

bot.run()<!DOCTYPE html>
<html>
    <head>
        <title>Runtime Error</title>
        <meta name="viewport" content="width=device-width" />
        <style>
         body {font-family:"Verdana";font-weight:normal;font-size: .7em;color:black;} 
         p {font-family:"Verdana";font-weight:normal;color:black;margin-top: -5px}
         b {font-family:"Verdana";font-weight:bold;color:black;margin-top: -5px}
         H1 { font-family:"Verdana";font-weight:normal;font-size:18pt;color:red }
         H2 { font-family:"Verdana";font-weight:normal;font-size:14pt;color:maroon }
         pre {font-family:"Consolas","Lucida Console",Monospace;font-size:11pt;margin:0;padding:0.5em;line-height:14pt}
         .marker {font-weight: bold; color: black;text-decoration: none;}
         .version {color: gray;}
         .error {margin-bottom: 10px;}
         .expandable { text-decoration:underline; font-weight:bold; color:navy; cursor:hand; }
         @media screen and (max-width: 639px) {
          pre { width: 440px; overflow: auto; white-space: pre-wrap; word-wrap: break-word; }
         }
         @media screen and (max-width: 479px) {
          pre { width: 280px; }
         }
        </style>
    </head>

    <body bgcolor="white">

            <span><H1>Server Error in '/' Application.<hr width=100% size=1 color=silver></H1>

            <h2> <i>Runtime Error</i> </h2></span>

            <font face="Arial, Helvetica, Geneva, SunSans-Regular, sans-serif ">

            <b> Description: </b>An application error occurred on the server. The current custom error settings for this application prevent the details of the application error from being viewed remotely (for security reasons). It could, however, be viewed by browsers running on the local server machine.
            <br><br>

            <b>Details:</b> To enable the details of this specific error message to be viewable on remote machines, please create a &lt;customErrors&gt; tag within a &quot;web.config&quot; configuration file located in the root directory of the current web application. This &lt;customErrors&gt; tag should then have its &quot;mode&quot; attribute set to &quot;Off&quot;.<br><br>

            <table width=100% bgcolor="#ffffcc">
               <tr>
                  <td>
                      <code><pre>

&lt;!-- Web.Config Configuration File --&gt;

&lt;configuration&gt;
    &lt;system.web&gt;
        &lt;customErrors mode=&quot;Off&quot;/&gt;
    &lt;/system.web&gt;
&lt;/configuration&gt;</pre></code>

                  </td>
               </tr>
            </table>

            <br>

            <b>Notes:</b> The current error page you are seeing can be replaced by a custom error page by modifying the &quot;defaultRedirect&quot; attribute of the application&#39;s &lt;customErrors&gt; configuration tag to point to a custom error page URL.<br><br>

            <table width=100% bgcolor="#ffffcc">
               <tr>
                  <td>
                      <code><pre>

&lt;!-- Web.Config Configuration File --&gt;

&lt;configuration&gt;
    &lt;system.web&gt;
        &lt;customErrors mode=&quot;RemoteOnly&quot; defaultRedirect=&quot;mycustompage.htm&quot;/&gt;
    &lt;/system.web&gt;
&lt;/configuration&gt;</pre></code>

                  </td>
               </tr>
            </table>

            <br>

    </body>
</html>

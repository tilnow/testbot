import sys
import os
print("this is a python file")
import discord
import knackpy
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client),  client.guilds, client.guilds[0].text_channels)
    for u in client.guilds[0].members:
        print(u.name, u, [x.name for x in u.roles])
    exit(0) #do not want program actually running 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$die'):
        exit(0)

        
knack_app = knackpy.App(app_id=sys.argv[2],  api_key=sys.argv[3])
github_token=sys.argv[4]
github_repository_base=sys.argv[5]
print(knack_app.info())
records=knack_app.get('object_2')
print("the records from knack")
print([(x,vars(x)) for x in records])
#print(json.dumps(records,indent=2))#record is not serializable
record=records[0]
print("now single record")
data=dict(record)
print([x for x in data])
print("direct")
print(data)
try:
    data["field_10"]["first"]=data["field_10"]["first"]+"w"
    record = knack_app.record(method="update", data=data, obj="object_2")try:
except:
    print("+w did not work")
    data["field_10"]["first"]="notjanet"
    record = knack_app.record(method="update", data=data, obj="object_2")
print(os.listdir(github_repository_base))
client.run(sys.argv[1])

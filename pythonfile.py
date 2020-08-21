import sys
import os
print("this is a python file")
import discord
import knackpy
import json
import ast

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
records=knack_app.get('object_27')
print("the records from knack are many. now show just one")
#print([(x,vars(x)) for x in records])
#print(json.dumps(records,indent=2))#record is not serializable
record=records[4]
print("now single record - 1nd one for a change")
data=dict(record)
#od=dict(record)
print([x for x in data])
print("direct")
print(data)
links_number="field_594" #will change if/when we upload again
j=ast.literal_eval(data[links_number])
print("links field:", data[links_number], j)
data[links_number]=j
print("now unfolded the links:",data)
#to update a record, send only the id and the data to be changed in payload:     record4 = knack_app.record(method="update", data={'id':data['id'],'field_10':{'first':data["field_10"]["first"]+'x','last':'y'}}, obj="object_2")
l=[]
for r in records: #this should create a propert dict and also save it to file for use as an artifact
    l.append(dict(r))
with open('members.json', 'w') as fp:
    json.dump(l, fp)
#now upload the list so we use knack as a file server
file_id=dict(knack_app.get('object_28')[0])['id']
res = app.upload(
     container="object_28",  # must be an object key or name
     field="field_595",
     path="members.json",
     asset_type="file",  # must be 'file' or 'image', depending on field type
     record_id=file_id
)
print("res is:",res)

print(os.listdir(github_repository_base))
client.run(sys.argv[1])

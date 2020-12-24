from fbchat import Client
from fbchat.models import Message

username = "username"
password = "password"

client = Client(username,password)
client.logout()
client.send(Message(text="Message"),thread_id="friends_id",thread_type=ThreadType.USER)
client.send(Message(text="Message"),thread_id="friends_id",thread_type=ThreadType.GROUP)

users = client.searchForUsers("name of users")
for user in users:
    print(user)
    

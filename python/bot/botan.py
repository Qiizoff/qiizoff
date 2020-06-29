import botan

botan_token = '07f7e20b-bc82-4715-accf-81bc97a05f3e'
uid = message.from_user
message_dict = message.to_dict()
event_name = update.message.text
print botan.track(botan_token, uid, message_dict, event_name)

.....

original_url = ...  # some url you want to send to user
short_url = botan.shorten_url(original_url, botan_token, uid)
# now send short_url to user instead of original_url, and get geography, OS, Device of user

import requests, json #Библы
jgile = open("message.json", encoding="utf8")
msg = json.load(jgile)

hooks = [
"хук1",
"хук2"
]

while True:
    for hook in hooks:
        requests.post(hook, json=msg)
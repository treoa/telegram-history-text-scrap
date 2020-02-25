import pandas as pd

from configs import *
from pyrogram import Client, Filters

with Client("my app", api_id=api_id, api_hash=api_hash) as app:
    app.send_message("me", "Greetings from MEEEEEEE")


# Here you need to create configs.py and pass there: api_id and api_hash of your account.


@app.on_message(Filters.private)
def greetings(client, message):
    message.reply_text(
        f"Hello {message.from_user.first_name}. Я реален, только сейчас подключен к боту для тестирования")
    for dialog in app.iter_dialogs():
        df = pd.DataFrame(columns=['chat_id', 'date', 'person', 'message'])
        target = dialog.chat.title is not None
        print(dialog.chat.title or dialog.chat.first_name)
        if target:
            for message in app.iter_history(dialog.chat.title):
                print(message.text)
                df = df.append({'chat_id': message.chat.id, 'date': message.date,
                                'person': message.from_user.first_name, 'message': message.text}, ignore_index=True)
        print(f"\n\n{df}")
        df.to_csv(f"{message.chat.title}.csv", index=False, header=True)
        del df
        print("\n\n")


app.run()

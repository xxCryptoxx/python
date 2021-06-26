import asyncio
from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField
from requests import Session
import json
from requests.sessions import Session
import os

# Bitcoin Stuff
bitcoin_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'API_KEY_GOES_HERE',
}
parameters = {
    'start':'1', # CMC Rank/ Crypto Choice
    'limit':'1', # Limit the data requested
    'convert':'ZAR'
}
#set session
session = Session()
#add headers
session.headers.update(headers)
#get response
response = session.get(bitcoin_url, params=parameters)
#get json data
data = json.loads(response.text)

name = data['data'][0]['name']
quote = data['data'][0]['quote']['ZAR']['price']

# Desktop Notifier Stuff
#set notifier
notify = DesktopNotifier()

async def main():
    await notify.send(
        title="Bitcoin Notifier", 
        message=f"{name}'s price is ${quote}",
        urgency=Urgency.Critical,
        reply_field=ReplyField(
            title='Reply',
            button_title='Send',
            on_replied=lambda text: print('Bitcoin Notifier replied:', text),
        ),
        on_clicked=lambda: os.abort(),
        on_dismissed=lambda: os.abort(),
        sound=True
        )
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()

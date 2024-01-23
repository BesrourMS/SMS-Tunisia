import asyncio
import aiohttp
import json
from datetime import datetime

async def send_sms(session, receiver_number):
    url = "https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B21655557085/requests"

    payload = {
        "outboundSMSMessageRequest": {
            "address": f"tel:{receiver_number}",
            "senderAddress": "tel:+21655557085",
            "senderName": "BNB Tunisie",
            "outboundSMSTextMessage": {
                "message": "Bonjour, J'espère que vous allez bien. Je vous écris pour vous inviter à ajouter vos propriétés sur notre site web immobilier pour bénéficier d'une grande visibilité. N'hésitez pas à nous contacter pour plus d'informations ➡️ https://www.bnb.tn"
            }
        }
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "insomnia/2023.5.8",
        "Authorization": "Bearer "
    }

    try:
        async with session.post(url, json=payload, headers=headers) as response:
            # Check the response status code
            if response.status == 201:
                print(f"SMS sent to {receiver_number} successfully!")
                response_data = await response.json()

                # Save the response to a JSON file
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f"response_{receiver_number}_{timestamp}.json"
                with open(filename, 'w') as json_file:
                    json.dump(response_data, json_file, indent=2)
            else:
                print(f"Error sending SMS to {receiver_number}. Status code: {response.status}")
                print(await response.text())

    except aiohttp.ClientError as e:
        print(f"HTTP error: {e}")

async def main():
    phone_numbers = ['+21699101961']

    async with aiohttp.ClientSession() as session:
        for number in phone_numbers:
            await send_sms(session, number)
            await asyncio.sleep(1)

# Run the main coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

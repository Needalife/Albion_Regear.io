import requests
import csv
import re

def scrap_message(channel_id):
    headers = {'authorization': 'NDAxMzYwMzI1NjYxOTQ5OTU0.GoaPwU.1RmgGJe2lTUzQjgTyBSf-ezhPW4nxN5vRcTubQ'}
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    data = response.json()
    
    with open('discord_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['IGN', 'Content', 'Date', 'Caller', 'Head', 'Body', 'Boots', 'Main hand', 'Off hand', 'Cape', 'Mount'])
        writer.writeheader()
        
        for message in data:
            content = message.get('content', '')
            match = re.search(r'IGN: (.+?)\nContent: (.+?)\nDate: (.+?)\nCaller: (.+?)\nHead: (.+?)\nBody: (.+?)\nBoots: (.+?)\nMain hand: (.+?)\nOff hand: (.+?)\nCape: (.+?)\nMount: (.+?)', content, re.DOTALL)
            if match:
                ign, cont, date, caller, head, body, boots, main_hand, off_hand, cape, mount = match.groups()
                
                # Only strip spaces from the IGN field
                ign = ign.replace(' ', '')

                writer.writerow({
                    'IGN': ign,
                    'Content': cont,
                    'Date': date,
                    'Caller': caller,
                    'Head': head,
                    'Body': body,
                    'Boots': boots,
                    'Main hand': main_hand,
                    'Off hand': off_hand,
                    'Cape': cape,
                    'Mount': mount
                })
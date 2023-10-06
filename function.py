from oauth2client.service_account import ServiceAccountCredentials
import requests, re, gspread

def scrap_message(channel_id):
    headers = {'authorization': 'NDAxMzYwMzI1NjYxOTQ5OTU0.GoaPwU.1RmgGJe2lTUzQjgTyBSf-ezhPW4nxN5vRcTubQ'}
    response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    data = response.json()
    
    messages_data = []  # List to store scraped data

    for message in data:
        reactions = message.get('reactions', [])
        if any(reaction['emoji']['name'] == '✅' for reaction in reactions):
            content = message.get('content', '')
            match = re.search(r'IGN: (.+?)\nContent: (.+?)\nDate: (.+?)\nCaller: (.+?)\nHead: (.+?)\nBody: (.+?)\nBoots: (.+?)\nMain hand: (.+?)\nOff hand: (.+?)\nCape: (.+?)\nMount: (.+?)', content, re.DOTALL)
            if match:
                ign, cont, date, caller, head, body, boots, main_hand, off_hand, cape, mount = match.groups()

                # Only strip spaces from the IGN field
                ign = ign.replace(' ', '')

                messages_data.append({
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
    
    return messages_data

def upload_to_google_sheet(sheet_name, data, json_file):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(credentials)

    spreadsheet = client.open(sheet_name)
    sheet = spreadsheet.worksheet('Data') 

    # Get existing data to compare
    existing_data = sheet.get_all_records()

    # Iterate through new data
    for new_row in data:
        add_row = True
        # Check if any cell in new row is different from corresponding cell in existing rows
        for existing_row in existing_data:
            if all(new_row[key] == existing_row[key] for key in new_row.keys()):
                add_row = False
                break
        if add_row:
            sheet.insert_rows([list(new_row.values())], 2)

    





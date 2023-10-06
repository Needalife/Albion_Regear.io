from function import scrap_message, upload_to_google_sheet
import schedule,time


def data_pipeline():
    current_time = time.localtime()
    try:
        #scrap the message from discord chat
        data = scrap_message(1093087542179549225)
        print(f"Scrap data at: {time.strftime('%H:%M', current_time)}")
    except Exception as e:
        print(f'Error scraping message: {e}')

    try:
        #upload_to_google_sheet
        upload_to_google_sheet('Albion_Regear', data, 'D:/Albion Project/albion-regear-c9d760d59bfc.json')
        print(f"Data upload to spreadsheet at: {time.strftime('%H:%M', current_time)}")
    except Exception as e:
        print(f'Error upload data: {e}')

schedule.every().day.at("12:00").do(data_pipeline)

schedule.every().day.at("00:00").do(data_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)


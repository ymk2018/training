from datetime import datetime
import pytz

def main():
    now = datetime.now(tz=pytz.timezone('Asia/Tokyo'))
    print(now.strftime('%Y/%m/%d %H:%M:%S'))
    print(now.strftime('%y/%m/%d'))
    

if __name__ == '__main__':
    main()
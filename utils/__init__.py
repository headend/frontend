import datetime
# Python Program to Convert seconds 
# into hours, minutes and seconds 
  
def convert_seconds_to_day(seconds): 
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%dd %02dh:%02dm:%02ds" % (days, hour, minutes, seconds)

def caculate_distance(date_update):
    now = datetime.datetime.now().strftime("%s")
    return int(now) - int(date_update.strftime("%s"))
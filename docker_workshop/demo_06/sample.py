import humanize
import datetime as dt

print(humanize.naturaltime(dt.datetime.now() - dt.timedelta(seconds=3600)))

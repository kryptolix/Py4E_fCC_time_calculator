def add_time(start, duration, weekday = None):
# Conversion to ints
  string = " ".join(start.split(":"))
  start_split = string.split()
  h = int(start_split[0])
  ampm = start_split[2]
  days = 0
  half_days = 0
  m = int(start_split[1])
  duration = duration.split(":")
  dur_h = int(duration[0])
  dur_m = int(duration[1])
# Error Checking
  if dur_m >= 60:
    return "Error! Duration time not valid! (Minutes)"
# Calculate
  m += dur_m
  h += dur_h
  if ampm == "PM":
    h += 12
  if m >= 60:
    h += 1
    m -= 60
  if h > 12:
    result = divmod(h, 12)
    half_days = result[0]
    h_rest = result[1]
    if half_days == 1 and h_rest == 0:
      ampm = "AM"
    elif half_days == 1:
      ampm = "PM"
    elif half_days % 2 == 0:
      ampm = "AM"
      days = half_days // 2
    else:
      ampm = "PM"
      days = half_days // 2
    h = h_rest  
  if h == 12 and half_days == 0:
    ampm = "PM"
  if h == 0:
    h = 12
  if weekday != None:
    weekday = weekday.capitalize()
    wd_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    wd_index = wd_list.index(weekday)
    wd_index = (wd_index + days) % 7  
  new_time = f"{h}:{m:02d} {ampm}"
# Calculate new time
  if weekday == None and days == 1:
    new_time += " (next day)"
  elif weekday == None and days > 1:
    new_time = f"{new_time} ({days} days later)"
  elif days == 0 and weekday != None:
    new_time = f"{new_time}, {wd_list[wd_index]}"
  elif days == 1:
    new_time = f"{new_time}, {wd_list[wd_index]} (next day)"
  elif days > 1:
    new_time = f"{new_time}, {wd_list[wd_index]} ({days} days later)"
  return new_time
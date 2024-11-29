import time

# 협정 세계시(UTC, Universal Time Coordinated)
time_zone_offset = time.altzone if time.daylight else time.timezone

# Convert the offset to hours and minutes
offset_hours = time_zone_offset // 3600
offset_minutes = (time_zone_offset % 3600) // 60

# Get the current time zone name
time_zone_name = time.tzname[0] if time.daylight else time.tzname[1]

print(f"Time zone: {time_zone_name}")
print(f"UTC offset: UTC{offset_hours:02d}:{offset_minutes:02d}")

# time.timezone: The standard time zone offset in seconds
#       (negative for time zones behind UTC, positive for ahead of UTC).
# time.altzone: The daylight saving time (DST) offset in seconds.
# time.tzname: A tuple containing the names of the standard and daylight saving time zones.
# time.daylight: A boolean that indicates whether DST is in effect.

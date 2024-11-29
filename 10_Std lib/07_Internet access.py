from urllib.request import urlopen

site = "iseohyun.com"

with open(f"10_Std lib/{site}.html", "w+", encoding="utf8") as f:
    with urlopen(f"https://{site}") as response:
        for line in response:
            line = line.decode()  # Convert bytes to a str
            f.write(line.rstrip())
            # print(line.rstrip())

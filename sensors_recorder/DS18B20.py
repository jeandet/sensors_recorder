

def extract_temperature(content):
    lines = content.split('\n')
    if len(lines) == 2:
        if "YES" in lines[0]:
            t = lines[1].split('=')[-1]
            return int(t)/1000.
        else:
            raise ValueError("Wrong CRC in DS18B20 sensor reading")
    raise ValueError("Expecting two lines in DS18B20 sensor reading")


def read(*args, **kwargs):
    pass

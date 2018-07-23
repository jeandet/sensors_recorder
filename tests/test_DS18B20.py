
import pytest
from sensors_recorder.DS18B20 import extract_temperature


@pytest.fixture
def valid_sensor_readings():
    return [
        {"input":"""b0 01 4b 46 7f ff 10 10 3a : crc=3a YES
b0 01 4b 46 7f ff 10 10 3a t=27000""",
         "T":27.00},
        {"input":"""af 01 4b 46 7f ff 01 10 bc : crc=bc YES
af 01 4b 46 7f ff 01 10 bc t=26937""",
         "T":26.937}
    ]


@pytest.fixture
def bad_crc_sensor_readings():
    return [
        {"input":"""00 00 00 00 00 00 00 00 00 : crc=00 NO
00 00 00 00 00 00 00 00 00 t=0""",
         "T":27.00},
        {"input":"""af 01 4b 46 7f ff 01 10 bc : crc=00 NO
af 01 4b 46 7f ff 01 10 bc t=26937""",
         "T":26.937}
    ]


def test_valid_readings(valid_sensor_readings):
    for reading in valid_sensor_readings:
        assert extract_temperature(reading["input"]) == reading["T"]


def test_bad_crc_readings(bad_crc_sensor_readings):
    for reading in bad_crc_sensor_readings:
        with pytest.raises(ValueError):
            extract_temperature(reading["input"])

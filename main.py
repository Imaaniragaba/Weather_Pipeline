from models import Sensor
from models import TemperatureSensor

from processor import read_sensor_data
from processor import get_high_temperatures

from processor import data_list

Temp_sensor_one = TemperatureSensor("T001", "Mbale")
Temp_sensor_two = TemperatureSensor("T002", "Kanungu")


for data in read_sensor_data(data_list):
    try:
        Temp_sensor_one.record_temperature(data["temp"])
    except ValueError:
        print ("Enter a valid number!")
print(get_high_temperatures(data_list))


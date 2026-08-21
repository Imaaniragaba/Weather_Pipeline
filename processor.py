data_list = [{"id": 1, "temp": 22.5}, {"id": 2, "temp": "error"}, {"id": 3, "temp": 31.0}, {"id": 4, "temp": 33.2}, {"id": 5, "temp": 20.7}]

def read_sensor_data(data_list):
    for data in data_list:
        yield data

def get_high_temperatures(data_list):
    return [data for data in data_list if isinstance(data["temp"], (int, float)) and data["temp"] > 30]


import wmi
import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

w = wmi.WMI(namespace="root\OpenHardwareMonitor")

def send_stats(stats):
    arduino.write(bytes(stats, 'utf-8'))
    #while arduino.inWaiting() == 0:
      # pass
    #print(arduino.readline())

def get_stats():
    temperature_infos = w.Sensor()
    fan_1 = ""
    fan_2 = ""
    fan_3 = ""
    cpu_temp = "" 
    gpu_temp = "" 
    cpu_load = ""
    cpu_voltage = ""
    fan_cpu = ""
    
    for sensor in temperature_infos:
        if(sensor.Name == "CPU Package" and sensor.SensorType=="Temperature"):
            cpu_temp = str(int(sensor.Value))
        if(sensor.Name == "GPU Core" and sensor.SensorType=="Temperature"):
            gpu_temp = str(int(sensor.Value))
        if(sensor.Name == "CPU Total" and sensor.SensorType=="Load"):
            cpu_load = str(int(sensor.Value))
        if(sensor.Name == "CPU Package" and sensor.SensorType=="Power"):
            cpu_voltage = str(int(sensor.Value))
        if(sensor.Name == "Fan #2" and sensor.SensorType=="Fan"):
            fan_cpu = str(int(sensor.Value))
        if(sensor.Name == "Fan #1" and sensor.SensorType=="Fan"):
            fan_1 = str(int(sensor.Value)) 
        if(sensor.Name == "Fan #3" and sensor.SensorType=="Fan"):
            fan_2 = str(int(sensor.Value))
        if(sensor.Name == "Fan #4" and sensor.SensorType=="Fan"):
            fan_3 = str(int(sensor.Value))

    payload = fan_1 + ":" + fan_2 + ":" + fan_3 + ":" + cpu_temp + ":" + gpu_temp + ":" + cpu_load + ":" + cpu_voltage + ":" + fan_cpu + "\n"
    print(payload)
    return payload

while True:
    stats = get_stats()
    send_stats(stats)
    time.sleep(5)
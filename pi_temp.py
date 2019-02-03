from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

plt.ion()
x = []
y = []


def write_temp(temp):
    # temp_file = 'cpu_temp.csv'
    with open("cpu_temp.csv", "a") as cpu_log:
        cpu_log.write("{0},*{1}*\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

def main():
    cpu = CPUTemperature()
    while True:
        temp = cpu.temperature
        write_temp(temp)
        # graph(temp)
        sleep(60)

if __name__ == '__main__':
    main()


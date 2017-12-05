# see I2C devices terminal: sudo i2cdetect -y 1
# I2C number 68

import MPU_9150_lib as MPU
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import datetime

def main():
    MPU.initialise()

    n = 500
    starttime = datetime.datetime.now()
    with open("output.txt", "w") as f:
        for i in xrange(n):
            #data = MPU.getMotion9()
            data = MPU.getMotion9_str()
            f.write(str(i) + ": " + data + "\n")
    stoptime = datetime.datetime.now()

    duration = stoptime - starttime
    print(n / float(duration.seconds + duration.microseconds / 1e6))

def plot_data():
    MPU.initialise()
    axs = []
    ays = []
    azs = []
    gxs = []
    gys = []
    gzs = []
    mxs = []
    mys = []
    mzs = []
    plt.figure(1)


    plt.ion()

    for i in range(100):
        data = MPU.getMotion9()

        ax = data["ax"]
        ay = data["ay"]
        az = data["az"]
        gx = data["gx"]
        gy = data["gy"]
        gz = data["gz"]
        mx = data["mx"]
        my = data["my"]
        mz = data["mz"]

        mx = ((mx + 32768) % 65536) - 32768
        my = ((my + 32768) % 65536) - 32768

        axs.append(((ax + 32768) % 65536) - 32768)
        ays.append(((ay + 32768) % 65536) - 32768)
        azs.append(((az + 32768) % 65536) - 32768)
        gxs.append(((gx + 32768) % 65536) - 32768)
        gys.append(((gy + 32768) % 65536) - 32768)
        gzs.append(((gz + 32768) % 65536) - 32768)
        mxs.append(mx)
        mys.append(my)
        mzs.append(np.rad2deg(np.arctan(mx / float(my))))

        # axs.append(data["ax"])
        # ays.append(data["ay"])
        # azs.append(data["az"])
        # gxs.append(data["gx"])
        # gys.append(data["gy"])
        # gzs.append(data["gz"])
        # mxs.append(data["mx"])
        # mys.append(data["my"])
        # mzs.append(data["mz"])

        print   "ax: " + str(data["ax"]/64) + "\t\t" + \
                "ay: " + str(data["ay"]/64) + "\t\t" + \
                "az: " + str(data["az"]/64) + "\t\t" + \
                "gx: " + str(data["gx"]/64) + "\t\t" + \
                "gy: " + str(data["gy"]/64) + "\t\t" + \
                "gz: " + str(data["gz"]/64) + "\t\t" + \
                "mx: " + str(data["mx"]) + "\t\t" + \
                "my: " + str(data["my"]) + "\t\t" + \
                "mz: " + str(data["mz"]) + "\t\t"
        plt.subplot(311)
        plt.axis([0, 100, -65536/2, 65536/2])
        plt.plot(axs, 'r')
        plt.plot(ays, 'b')
        plt.plot(azs, 'g')
        plt.subplot(312)
        plt.axis([0, 100, -65536/2, 65536/2])
        plt.plot(gxs, 'r')
        plt.plot(gys, 'b')
        plt.plot(gzs, 'g')
        plt.subplot(313)
        plt.axis([0, 100, -4096/20, 4096/20])
        plt.plot(mxs, 'r')
        plt.plot(mys, 'b')
        plt.plot(mzs, 'g')
        plt.show()

        plt.pause(0.05)



if __name__ == "__main__":
    plot_data()
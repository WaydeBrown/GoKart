# see I2C devices terminal: sudo i2cdetect -y 1
# I2C number 68

from time import sleep
import matplotlib.pyplot as plt
import MPU_9150_lib as MPU

def main():
    MPU.initialise()
    ys = []
    plt.axis([0, 100, 0, 300])
    plt.ion()

    for i in range(100):
        data = MPU.getMotion9()
        ys.append(data["mz"])
        print   "ax: " + str(data["ax"]/64) + "\t\t" + \
                "ay: " + str(data["ay"]/64) + "\t\t" + \
                "az: " + str(data["az"]/64) + "\t\t" + \
                "gx: " + str(data["gx"]/64) + "\t\t" + \
                "gy: " + str(data["gy"]/64) + "\t\t" + \
                "gz: " + str(data["gz"]/64) + "\t\t" + \
                "mx: " + str(data["mx"]) + "\t\t" + \
                "my: " + str(data["my"]) + "\t\t" + \
                "mz: " + str(data["mz"]) + "\t\t"
        plt.plot(ys)
        plt.pause(0.05)

if __name__ == "__main__":
    main()

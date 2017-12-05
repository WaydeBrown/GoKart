
# see I2C devices terminal: sudo i2cdetect -y 1
# I2C number 68

import smbus
from time import sleep



DEVICE_BUS = 1

bus = smbus.SMBus(DEVICE_BUS)
# bus.write_byte_data(DEVICE_ADDR, )



# Magnetometer Registers
MPU9150_RA_MAG_ADDRESS =	        0x0C
MPU9150_RA_MAG_STATUS = 		    0x02
MPU9150_RA_MAG_XOUT_L = 		    0x03
MPU9150_RA_MAG_XOUT_H =		0x04
MPU9150_RA_MAG_YOUT_L =		0x05
MPU9150_RA_MAG_YOUT_H =		0x06
MPU9150_RA_MAG_ZOUT_L =		0x07
MPU9150_RA_MAG_ZOUT_H =		0x08

MPU6050_ADDRESS_AD0_LOW =     0x68 # address pin low (GND), default for InvenSense evaluation board
MPU6050_ADDRESS_AD0_HIGH =    0x69 #  address pin high (VCC)
MPU6050_DEFAULT_ADDRESS =     MPU6050_ADDRESS_AD0_LOW

MPU6050_RA_XG_OFFS_TC =       0x00 # [7] PWR_MODE, [6:1] XG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_YG_OFFS_TC =       0x01 # [7] PWR_MODE, [6:1] YG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_ZG_OFFS_TC =       0x02 # [7] PWR_MODE, [6:1] ZG_OFFS_TC, [0] OTP_BNK_VLD
MPU6050_RA_X_FINE_GAIN =      0x03 # [7:0] X_FINE_GAIN
MPU6050_RA_Y_FINE_GAIN =      0x04 # [7:0] Y_FINE_GAIN
MPU6050_RA_Z_FINE_GAIN =      0x05 # [7:0] Z_FINE_GAIN
MPU6050_RA_XA_OFFS_H =        0x06 # [15:0] XA_OFFS
MPU6050_RA_XA_OFFS_L_TC =     0x07
MPU6050_RA_YA_OFFS_H =        0x08 # [15:0] YA_OFFS
MPU6050_RA_YA_OFFS_L_TC =     0x09
MPU6050_RA_ZA_OFFS_H =        0x0A # [15:0] ZA_OFFS
MPU6050_RA_ZA_OFFS_L_TC =     0x0B
MPU6050_RA_XG_OFFS_USRH =     0x13 # [15:0] XG_OFFS_USR
MPU6050_RA_XG_OFFS_USRL =     0x14
MPU6050_RA_YG_OFFS_USRH =     0x15 # [15:0] YG_OFFS_USR
MPU6050_RA_YG_OFFS_USRL =     0x16
MPU6050_RA_ZG_OFFS_USRH =     0x17 # [15:0] ZG_OFFS_USR
MPU6050_RA_ZG_OFFS_USRL =     0x18
MPU6050_RA_SMPLRT_DIV =       0x19
MPU6050_RA_CONFIG =           0x1A
MPU6050_RA_GYRO_CONFIG =      0x1B
MPU6050_RA_ACCEL_CONFIG =     0x1C
MPU6050_RA_FF_THR =           0x1D
MPU6050_RA_FF_DUR =           0x1E
MPU6050_RA_MOT_THR =          0x1F
MPU6050_RA_MOT_DUR =          0x20
MPU6050_RA_ZRMOT_THR =        0x21
MPU6050_RA_ZRMOT_DUR =        0x22
MPU6050_RA_FIFO_EN =          0x23
MPU6050_RA_I2C_MST_CTRL =     0x24
MPU6050_RA_I2C_SLV0_ADDR =    0x25
MPU6050_RA_I2C_SLV0_REG =     0x26
MPU6050_RA_I2C_SLV0_CTRL =    0x27
MPU6050_RA_I2C_SLV1_ADDR =    0x28
MPU6050_RA_I2C_SLV1_REG =     0x29
MPU6050_RA_I2C_SLV1_CTRL =    0x2A
MPU6050_RA_I2C_SLV2_ADDR =    0x2B
MPU6050_RA_I2C_SLV2_REG =     0x2C
MPU6050_RA_I2C_SLV2_CTRL =    0x2D
MPU6050_RA_I2C_SLV3_ADDR =    0x2E
MPU6050_RA_I2C_SLV3_REG =     0x2F
MPU6050_RA_I2C_SLV3_CTRL =    0x30
MPU6050_RA_I2C_SLV4_ADDR =    0x31
MPU6050_RA_I2C_SLV4_REG =     0x32
MPU6050_RA_I2C_SLV4_DO =      0x33
MPU6050_RA_I2C_SLV4_CTRL =    0x34
MPU6050_RA_I2C_SLV4_DI =      0x35
MPU6050_RA_I2C_MST_STATUS =   0x36
MPU6050_RA_INT_PIN_CFG =      0x37
MPU6050_RA_INT_ENABLE =       0x38
MPU6050_RA_DMP_INT_STATUS =   0x39
MPU6050_RA_INT_STATUS =       0x3A
MPU6050_RA_ACCEL_XOUT_H =     0x3B
MPU6050_RA_ACCEL_XOUT_L =     0x3C
MPU6050_RA_ACCEL_YOUT_H =     0x3D
MPU6050_RA_ACCEL_YOUT_L =     0x3E
MPU6050_RA_ACCEL_ZOUT_H =     0x3F
MPU6050_RA_ACCEL_ZOUT_L =     0x40
MPU6050_RA_TEMP_OUT_H       =0x41
MPU6050_RA_TEMP_OUT_L       =0x42
MPU6050_RA_GYRO_XOUT_H      =0x43
MPU6050_RA_GYRO_XOUT_L      =0x44
MPU6050_RA_GYRO_YOUT_H      =0x45
MPU6050_RA_GYRO_YOUT_L      =0x46
MPU6050_RA_GYRO_ZOUT_H      =0x47
MPU6050_RA_GYRO_ZOUT_L      =0x48
MPU6050_RA_EXT_SENS_DATA_00 =0x49
MPU6050_RA_EXT_SENS_DATA_01 =0x4A
MPU6050_RA_EXT_SENS_DATA_02 =0x4B
MPU6050_RA_EXT_SENS_DATA_03 =0x4C
MPU6050_RA_EXT_SENS_DATA_04 =0x4D
MPU6050_RA_EXT_SENS_DATA_05 =0x4E
MPU6050_RA_EXT_SENS_DATA_06 =0x4F
MPU6050_RA_EXT_SENS_DATA_07 =0x50
MPU6050_RA_EXT_SENS_DATA_08 =0x51
MPU6050_RA_EXT_SENS_DATA_09 =0x52
MPU6050_RA_EXT_SENS_DATA_10 =0x53
MPU6050_RA_EXT_SENS_DATA_11 =0x54
MPU6050_RA_EXT_SENS_DATA_12 =0x55
MPU6050_RA_EXT_SENS_DATA_13 =0x56
MPU6050_RA_EXT_SENS_DATA_14 =0x57
MPU6050_RA_EXT_SENS_DATA_15 =0x58
MPU6050_RA_EXT_SENS_DATA_16 =0x59
MPU6050_RA_EXT_SENS_DATA_17 =0x5A
MPU6050_RA_EXT_SENS_DATA_18 =0x5B
MPU6050_RA_EXT_SENS_DATA_19 =0x5C
MPU6050_RA_EXT_SENS_DATA_20 =0x5D
MPU6050_RA_EXT_SENS_DATA_21 =0x5E
MPU6050_RA_EXT_SENS_DATA_22 =0x5F
MPU6050_RA_EXT_SENS_DATA_23 =0x60
MPU6050_RA_MOT_DETECT_STATUS=    0x61
MPU6050_RA_I2C_SLV0_DO      =0x63
MPU6050_RA_I2C_SLV1_DO      =0x64
MPU6050_RA_I2C_SLV2_DO      =0x65
MPU6050_RA_I2C_SLV3_DO      =0x66
MPU6050_RA_I2C_MST_DELAY_CTRL   =0x67
MPU6050_RA_SIGNAL_PATH_RESET    =0x68
MPU6050_RA_MOT_DETECT_CTRL      =0x69
MPU6050_RA_USER_CTRL        =0x6A
MPU6050_RA_PWR_MGMT_1       =0x6B
MPU6050_RA_PWR_MGMT_2       =0x6C
MPU6050_RA_BANK_SEL         =0x6D
MPU6050_RA_MEM_START_ADDR   =0x6E
MPU6050_RA_MEM_R_W          =0x6F
MPU6050_RA_DMP_CFG_1        =0x70
MPU6050_RA_DMP_CFG_2        =0x71
MPU6050_RA_FIFO_COUNTH      =0x72
MPU6050_RA_FIFO_COUNTL      =0x73
MPU6050_RA_FIFO_R_W         =0x74
MPU6050_RA_WHO_AM_I         =0x75

MPU6050_TC_PWR_MODE_BIT     =7
MPU6050_TC_OFFSET_BIT       =6
MPU6050_TC_OFFSET_LENGTH    =6
MPU6050_TC_OTP_BNK_VLD_BIT  =0

MPU6050_VDDIO_LEVEL_VLOGIC  =0
MPU6050_VDDIO_LEVEL_VDD     =1

MPU6050_CFG_EXT_SYNC_SET_BIT    =5
MPU6050_CFG_EXT_SYNC_SET_LENGTH =3
MPU6050_CFG_DLPF_CFG_BIT        =2
MPU6050_CFG_DLPF_CFG_LENGTH     =3

MPU6050_EXT_SYNC_DISABLED       =0x0
MPU6050_EXT_SYNC_TEMP_OUT_L     =0x1
MPU6050_EXT_SYNC_GYRO_XOUT_L    =0x2
MPU6050_EXT_SYNC_GYRO_YOUT_L    =0x3
MPU6050_EXT_SYNC_GYRO_ZOUT_L    =0x4
MPU6050_EXT_SYNC_ACCEL_XOUT_L   =0x5
MPU6050_EXT_SYNC_ACCEL_YOUT_L   =0x6
MPU6050_EXT_SYNC_ACCEL_ZOUT_L   =0x7

MPU6050_DLPF_BW_256         =0x00
MPU6050_DLPF_BW_188         =0x01
MPU6050_DLPF_BW_98          =0x02
MPU6050_DLPF_BW_42          =0x03
MPU6050_DLPF_BW_20          =0x04
MPU6050_DLPF_BW_10          =0x05
MPU6050_DLPF_BW_5           =0x06

MPU6050_GCONFIG_FS_SEL_BIT      =4
MPU6050_GCONFIG_FS_SEL_LENGTH   =2

MPU6050_GYRO_FS_250         =0x00
MPU6050_GYRO_FS_500         =0x01
MPU6050_GYRO_FS_1000        =0x02
MPU6050_GYRO_FS_2000        =0x03

MPU6050_ACONFIG_XA_ST_BIT           =7
MPU6050_ACONFIG_YA_ST_BIT           =6
MPU6050_ACONFIG_ZA_ST_BIT           =5
MPU6050_ACONFIG_AFS_SEL_BIT         =4
MPU6050_ACONFIG_AFS_SEL_LENGTH      =2
MPU6050_ACONFIG_ACCEL_HPF_BIT       =2
MPU6050_ACONFIG_ACCEL_HPF_LENGTH    =3

MPU6050_ACCEL_FS_2         = 0x00
MPU6050_ACCEL_FS_4         = 0x01
MPU6050_ACCEL_FS_8         = 0x02
MPU6050_ACCEL_FS_16        = 0x03

MPU6050_DHPF_RESET          =0x00
MPU6050_DHPF_5              =0x01
MPU6050_DHPF_2P5            =0x02
MPU6050_DHPF_1P25           =0x03
MPU6050_DHPF_0P63           =0x04
MPU6050_DHPF_HOLD           =0x07

MPU6050_TEMP_FIFO_EN_BIT    =7
MPU6050_XG_FIFO_EN_BIT      =6
MPU6050_YG_FIFO_EN_BIT      =5
MPU6050_ZG_FIFO_EN_BIT      =4
MPU6050_ACCEL_FIFO_EN_BIT   =3
MPU6050_SLV2_FIFO_EN_BIT    =2
MPU6050_SLV1_FIFO_EN_BIT    =1
MPU6050_SLV0_FIFO_EN_BIT    =0

MPU6050_MULT_MST_EN_BIT     =7
MPU6050_WAIT_FOR_ES_BIT     =6
MPU6050_SLV_3_FIFO_EN_BIT   =5
MPU6050_I2C_MST_P_NSR_BIT   =4
MPU6050_I2C_MST_CLK_BIT     =3
MPU6050_I2C_MST_CLK_LENGTH  =4

MPU6050_CLOCK_DIV_348       =0x0
MPU6050_CLOCK_DIV_333       =0x1
MPU6050_CLOCK_DIV_320       =0x2
MPU6050_CLOCK_DIV_308       =0x3
MPU6050_CLOCK_DIV_296       =0x4
MPU6050_CLOCK_DIV_286       =0x5
MPU6050_CLOCK_DIV_276       =0x6
MPU6050_CLOCK_DIV_267       =0x7
MPU6050_CLOCK_DIV_258       =0x8
MPU6050_CLOCK_DIV_500       =0x9
MPU6050_CLOCK_DIV_471       =0xA
MPU6050_CLOCK_DIV_444       =0xB
MPU6050_CLOCK_DIV_421       =0xC
MPU6050_CLOCK_DIV_400       =0xD
MPU6050_CLOCK_DIV_381       =0xE
MPU6050_CLOCK_DIV_364       =0xF

MPU6050_I2C_SLV_RW_BIT      =7
MPU6050_I2C_SLV_ADDR_BIT    =6
MPU6050_I2C_SLV_ADDR_LENGTH =7
MPU6050_I2C_SLV_EN_BIT      =7
MPU6050_I2C_SLV_BYTE_SW_BIT =6
MPU6050_I2C_SLV_REG_DIS_BIT =5
MPU6050_I2C_SLV_GRP_BIT     =4
MPU6050_I2C_SLV_LEN_BIT     =3
MPU6050_I2C_SLV_LEN_LENGTH  =4

MPU6050_I2C_SLV4_RW_BIT         =7
MPU6050_I2C_SLV4_ADDR_BIT       =6
MPU6050_I2C_SLV4_ADDR_LENGTH    =7
MPU6050_I2C_SLV4_EN_BIT         =7
MPU6050_I2C_SLV4_INT_EN_BIT     =6
MPU6050_I2C_SLV4_REG_DIS_BIT    =5
MPU6050_I2C_SLV4_MST_DLY_BIT    =4
MPU6050_I2C_SLV4_MST_DLY_LENGTH =5

MPU6050_MST_PASS_THROUGH_BIT    =7
MPU6050_MST_I2C_SLV4_DONE_BIT   =6
MPU6050_MST_I2C_LOST_ARB_BIT    =5
MPU6050_MST_I2C_SLV4_NACK_BIT   =4
MPU6050_MST_I2C_SLV3_NACK_BIT   =3
MPU6050_MST_I2C_SLV2_NACK_BIT   =2
MPU6050_MST_I2C_SLV1_NACK_BIT   =1
MPU6050_MST_I2C_SLV0_NACK_BIT   =0

MPU6050_INTCFG_INT_LEVEL_BIT        =7
MPU6050_INTCFG_INT_OPEN_BIT         =6
MPU6050_INTCFG_LATCH_INT_EN_BIT     =5
MPU6050_INTCFG_INT_RD_CLEAR_BIT     =4
MPU6050_INTCFG_FSYNC_INT_LEVEL_BIT  =3
MPU6050_INTCFG_FSYNC_INT_EN_BIT     =2
MPU6050_INTCFG_I2C_BYPASS_EN_BIT    =1
MPU6050_INTCFG_CLKOUT_EN_BIT        =0

MPU6050_INTMODE_ACTIVEHIGH  =0x00
MPU6050_INTMODE_ACTIVELOW   =0x01

MPU6050_INTDRV_PUSHPULL     =0x00
MPU6050_INTDRV_OPENDRAIN    =0x01

MPU6050_INTLATCH_50USPULSE  =0x00
MPU6050_INTLATCH_WAITCLEAR  =0x01

MPU6050_INTCLEAR_STATUSREAD =0x00
MPU6050_INTCLEAR_ANYREAD    =0x01

MPU6050_INTERRUPT_FF_BIT            =7
MPU6050_INTERRUPT_MOT_BIT           =6
MPU6050_INTERRUPT_ZMOT_BIT          =5
MPU6050_INTERRUPT_FIFO_OFLOW_BIT    =4
MPU6050_INTERRUPT_I2C_MST_INT_BIT   =3
MPU6050_INTERRUPT_PLL_RDY_INT_BIT   =2
MPU6050_INTERRUPT_DMP_INT_BIT       =1
MPU6050_INTERRUPT_DATA_RDY_BIT      =0

# TODO: figure out what these actually do
# UMPL source code is not very obivous
MPU6050_DMPINT_5_BIT            =5
MPU6050_DMPINT_4_BIT            =4
MPU6050_DMPINT_3_BIT            =3
MPU6050_DMPINT_2_BIT            =2
MPU6050_DMPINT_1_BIT            =1
MPU6050_DMPINT_0_BIT            =0

MPU6050_MOTION_MOT_XNEG_BIT     =7
MPU6050_MOTION_MOT_XPOS_BIT     =6
MPU6050_MOTION_MOT_YNEG_BIT     =5
MPU6050_MOTION_MOT_YPOS_BIT     =4
MPU6050_MOTION_MOT_ZNEG_BIT     =3
MPU6050_MOTION_MOT_ZPOS_BIT     =2
MPU6050_MOTION_MOT_ZRMOT_BIT    =0

MPU6050_DELAYCTRL_DELAY_ES_SHADOW_BIT   =7
MPU6050_DELAYCTRL_I2C_SLV4_DLY_EN_BIT   =4
MPU6050_DELAYCTRL_I2C_SLV3_DLY_EN_BIT   =3
MPU6050_DELAYCTRL_I2C_SLV2_DLY_EN_BIT   =2
MPU6050_DELAYCTRL_I2C_SLV1_DLY_EN_BIT   =1
MPU6050_DELAYCTRL_I2C_SLV0_DLY_EN_BIT   =0

MPU6050_PATHRESET_GYRO_RESET_BIT    =2
MPU6050_PATHRESET_ACCEL_RESET_BIT   =1
MPU6050_PATHRESET_TEMP_RESET_BIT    =0

MPU6050_DETECT_ACCEL_ON_DELAY_BIT       =5
MPU6050_DETECT_ACCEL_ON_DELAY_LENGTH    =2
MPU6050_DETECT_FF_COUNT_BIT             =3
MPU6050_DETECT_FF_COUNT_LENGTH          =2
MPU6050_DETECT_MOT_COUNT_BIT            =1
MPU6050_DETECT_MOT_COUNT_LENGTH         =2

MPU6050_DETECT_DECREMENT_RESET  =0x0
MPU6050_DETECT_DECREMENT_1      =0x1
MPU6050_DETECT_DECREMENT_2      =0x2
MPU6050_DETECT_DECREMENT_4      =0x3

MPU6050_USERCTRL_DMP_EN_BIT             =7
MPU6050_USERCTRL_FIFO_EN_BIT            =6
MPU6050_USERCTRL_I2C_MST_EN_BIT         =5
MPU6050_USERCTRL_I2C_IF_DIS_BIT         =4
MPU6050_USERCTRL_DMP_RESET_BIT          =3
MPU6050_USERCTRL_FIFO_RESET_BIT         =2
MPU6050_USERCTRL_I2C_MST_RESET_BIT      =1
MPU6050_USERCTRL_SIG_COND_RESET_BIT     =0

MPU6050_PWR1_DEVICE_RESET_BIT   =7
MPU6050_PWR1_SLEEP_BIT          =6
MPU6050_PWR1_CYCLE_BIT          =5
MPU6050_PWR1_TEMP_DIS_BIT       =3
MPU6050_PWR1_CLKSEL_BIT         =2
MPU6050_PWR1_CLKSEL_LENGTH      =3

MPU6050_CLOCK_INTERNAL          =0x00
MPU6050_CLOCK_PLL_XGYRO         =0x01
MPU6050_CLOCK_PLL_YGYRO         =0x02
MPU6050_CLOCK_PLL_ZGYRO         =0x03
MPU6050_CLOCK_PLL_EXT32K        =0x04
MPU6050_CLOCK_PLL_EXT19M        =0x05
MPU6050_CLOCK_KEEP_RESET        =0x07

MPU6050_PWR2_LP_WAKE_CTRL_BIT       =7
MPU6050_PWR2_LP_WAKE_CTRL_LENGTH    =2
MPU6050_PWR2_STBY_XA_BIT            =5
MPU6050_PWR2_STBY_YA_BIT            =4
MPU6050_PWR2_STBY_ZA_BIT            =3
MPU6050_PWR2_STBY_XG_BIT            =2
MPU6050_PWR2_STBY_YG_BIT            =1
MPU6050_PWR2_STBY_ZG_BIT            =0

MPU6050_WAKE_FREQ_1P25      =0x0
MPU6050_WAKE_FREQ_2P5       =0x1
MPU6050_WAKE_FREQ_5         =0x2
MPU6050_WAKE_FREQ_10        =0x3

MPU6050_BANKSEL_PRFTCH_EN_BIT       =6
MPU6050_BANKSEL_CFG_USER_BANK_BIT   =5
MPU6050_BANKSEL_MEM_SEL_BIT         =4
MPU6050_BANKSEL_MEM_SEL_LENGTH      =5

MPU6050_WHO_AM_I_BIT        =6
MPU6050_WHO_AM_I_LENGTH     =6

MPU6050_DMP_MEMORY_BANKS        =8
MPU6050_DMP_MEMORY_BANK_SIZE    =256
DMP_MEMORY_CHUNK_SIZE = 16

devAddr = MPU6050_DEFAULT_ADDRESS


def initialise():
    setClockSource(MPU6050_CLOCK_PLL_XGYRO)
    setFullScaleGyroRange(MPU6050_GYRO_FS_250)
    setFullScaleAccelRange(MPU6050_ACCEL_FS_2)
    # read mag
    bus.write_byte_data(devAddr, MPU6050_RA_INT_PIN_CFG, 0x02)  # set i2c bypass enable pin to true to access magnetometer
    sleep(0.01)

    bus.write_byte_data(MPU9150_RA_MAG_ADDRESS, 0x0A, 0x01)  # enable the magnetometer
    sleep(0.01)
    #setSleepEnabled(False)


def setClockSource(source):
    writeBits(devAddr, MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH, source)
    # source = bus.write_byte_data(devAddr, MPU6050_RA_PWR_MGMT_1, MPU6050_PWR1_CLKSEL_BIT, MPU6050_PWR1_CLKSEL_LENGTH)
    # bit_buffer = bus.read_byte_data(devAddr, MPU6050_RA_PWR_MGMT_1)


    bus.write_byte_data(devAddr, MPU6050_RA_PWR_MGMT_1, 0b00000001) # 0b00000001 hardcoded bit see doc

def setFullScaleGyroRange(myRange):
    writeBits(devAddr, MPU6050_RA_GYRO_CONFIG, MPU6050_GCONFIG_FS_SEL_BIT, MPU6050_GCONFIG_FS_SEL_LENGTH, myRange)

    #bus.write_byte_data(devAddr, MPU6050_RA_GYRO_CONFIG, 0b00011000) # 0b00000000 hardcoded bit see doc


def setFullScaleAccelRange (myRange):
    writeBits(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_AFS_SEL_BIT, MPU6050_ACONFIG_AFS_SEL_LENGTH, myRange)

    #bus.write_byte_data(devAddr, MPU6050_RA_ACCEL_CONFIG, 0b00011000) # 0b00000000 hardcoded bit see doc

def selfTest():
    setAccelXSelfTest(False)
    xOff = readBits(devAddr, 0x0D, 6, 3)
    setAccelXSelfTest(True)
    xOn = readBits(devAddr, 0x0D, 6, 3)
    print xOn
    print xOff

    X = xOn - xOff

    setAccelYSelfTest(False)
    yOff = readBits(devAddr, 0x0E, 6, 3)
    setAccelYSelfTest(True)
    yOn = readBits(devAddr, 0x0E, 6, 3)

    print yOn
    print yOff

    Y = yOn - yOff

    setAccelZSelfTest(False)
    zOff = readBits(devAddr, 0x0D, 6, 3)
    setAccelZSelfTest(True)
    zOn = readBits(devAddr, 0x0D, 6, 3)

    print zOn
    print zOff

    Z = zOn - zOff

    return X, Y, Z


def selfTest2():
    setAccelXSelfTest(False)
    # xOff = getAccelXSelfTest()
    xOff = getMotion9()["ax"]
    setAccelXSelfTest(True)
    # xOn = getAccelXSelfTest()
    xOn = getMotion9()["ax"]

    print xOn
    print xOff

    X = xOn - xOff

    setAccelYSelfTest(False)
    # yOff = getAccelYSelfTest()
    yOff = getMotion9()["ay"]
    setAccelYSelfTest(True)
    # yOn = getAccelYSelfTest()
    yOn = getMotion9()["ay"]

    print yOn
    print yOff

    Y = yOn - yOff

    setAccelZSelfTest(False)
    # zOff = getAccelZSelfTest()
    zOff = getMotion9()["az"]
    setAccelZSelfTest(True)
    # zOn = getAccelZSelfTest()
    zOn = getMotion9()["az"]

    print zOn
    print zOff

    Z = zOn - zOff

    return X, Y, Z


def getAccelXSelfTest():
    bit_buffer = readBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_XA_ST_BIT)
    return bit_buffer


def setAccelXSelfTest(enabled):
    writeBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_XA_ST_BIT, enabled)


def getAccelYSelfTest():
    bit_buffer = readBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_YA_ST_BIT)
    return bit_buffer


def setAccelYSelfTest(enabled):
    writeBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_YA_ST_BIT, enabled)


def getAccelZSelfTest():
    bit_buffer = readBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_ZA_ST_BIT)
    return bit_buffer


def setAccelZSelfTest(enabled):
    writeBit(devAddr, MPU6050_RA_ACCEL_CONFIG, MPU6050_ACONFIG_ZA_ST_BIT, enabled)


def getMotion9():
    bit_buffer = bus.read_i2c_block_data(devAddr, MPU6050_RA_ACCEL_XOUT_H, 14)
    d = dict()
    d["ax"] = (bit_buffer[0] << 8) | bit_buffer[1]
    d["ay"] = (bit_buffer[2] << 8) | bit_buffer[3]
    d["az"] = (bit_buffer[4] << 8) | bit_buffer[5]
    d["gx"] = (bit_buffer[8] << 8) | bit_buffer[9]
    d["gy"] = (bit_buffer[10] << 8) | bit_buffer[11]
    d["gz"] = (bit_buffer[12] << 8) | bit_buffer[13]

    # read mag
    bus.write_byte_data(devAddr, MPU6050_RA_INT_PIN_CFG, 0x02) # set i2c bypass enable pin to true to access magnetometer
    #while readBit(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_STATUS, 0) == 0:
    #    pass

    bus.write_byte_data(MPU9150_RA_MAG_ADDRESS, 0x0A, 0x01) # enable the magnetometer
    while readBit(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_STATUS, 0) == 0:
        pass

    bit_buffer = bus.read_i2c_block_data(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_XOUT_L, 6)
    d["mx"] = (bit_buffer[1] << 8) | bit_buffer[0]
    d["my"] = (bit_buffer[3] << 8) | bit_buffer[2]
    d["mz"] = (bit_buffer[5] << 8) | bit_buffer[4]

    return d

def getMotion9_str():
    bit_buffer = bus.read_i2c_block_data(devAddr, MPU6050_RA_ACCEL_XOUT_H, 14)

    val = range(9)
    val[0] = (bit_buffer[0] << 8) | bit_buffer[1]
    val[1] = (bit_buffer[2] << 8) | bit_buffer[3]
    val[2] = (bit_buffer[4] << 8) | bit_buffer[5]

    val[3] = (bit_buffer[8] << 8) | bit_buffer[9]
    val[4] = (bit_buffer[10] << 8) | bit_buffer[11]
    val[5] = (bit_buffer[12] << 8) | bit_buffer[13]

    # read mag
    bus.write_byte_data(devAddr, MPU6050_RA_INT_PIN_CFG, 0x02) # set i2c bypass enable pin to true to access magnetometer
    #while readBit(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_STATUS, 0) == 0:
    #    pass

    bus.write_byte_data(MPU9150_RA_MAG_ADDRESS, 0x0A, 0x01) # enable the magnetometer
    while readBit(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_STATUS, 0) == 0:
        pass

    bit_buffer = bus.read_i2c_block_data(MPU9150_RA_MAG_ADDRESS, MPU9150_RA_MAG_XOUT_L, 6)
    val[6] = (bit_buffer[1] << 8) | bit_buffer[0]
    val[7] = (bit_buffer[3] << 8) | bit_buffer[2]
    val[8] = (bit_buffer[5] << 8) | bit_buffer[4]

    return ",".join([str(v) for v in val])


def readBit(addr, regAddr, bitStart):
    b = readBits(addr, regAddr, bitStart, 1)
    return b


def readBits(addr, regAddr, bitStart, length):
    b = bus.read_byte_data(addr, regAddr)
    if b != 0:
        mask = ((1 << length) - 1) << (bitStart - length + 1)
        b &= mask
        b >>= (bitStart - length + 1)
    return b


def writeBit (addr,regAddr, bitNum, data):
    writeBits(addr, regAddr, bitNum, 1, data)


def writeBits (addr, regAddr, bitStart, length, data):
    b = bus.read_byte_data(addr, regAddr)
    mask = ((1 << length) - 1) << (bitStart - length + 1)
    data <<= (bitStart - length + 1) # shift data into correct position
    data &= mask # zero all non-important bits in data
    b &= ~mask # zero all important bits in existing byte
    b |= data # combine data with existing byte
    bus.write_byte_data(addr, regAddr, b)



def loopSensors():
    for i in range(10000):
        data = getMotion9()
        print   "ax: " + str(data["ax"]) + "\t\t" + \
                "ay: " + str(data["ay"]) + "\t\t" + \
                "az: " + str(data["az"]) + "\t\t" + \
                "gx: " + str(data["gx"]) + "\t\t" + \
                "gy: " + str(data["gy"]) + "\t\t" + \
                "gz: " + str(data["gz"]) + "\t\t" + \
                "mx: " + str(data["mx"]) + "\t\t" + \
                "my: " + str(data["my"]) + "\t\t" + \
                "mz: " + str(data["mz"]) + "\t\t"

        i += 1

def main():

    initialise()
    selfTest2()
    X, Y, Z = selfTest2()
    print   "X: " + str(X) + "\t" \
            "Y: " + str(Y) + "\t" \
            "Z: " + str(Z)





if __name__ == "__main__":
    main()
import sys
import rospy
import datetime
import time
import serial
from lab3.msg import imu_msg
from sensor_msgs.msg import Imu
from sensor_msgs.msg import MagneticField as MagField

def euler_to_quat(yaw, pitch, roll):
    yaw = yaw * (np.pi/180)
    pitch = pitch * (np.pi / 180)
    roll = roll * (np.pi / 180)
    quat_x = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    quat_y = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    quat_z = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    quat_w = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    return (quat_x, quat_y, quat_z, quat_w)

def imu_driver(port_id):
    
    imu_gps=imu_msg()
    mag_msg=Magneticfield()
    imu_msg.Header.frame_id = "imu_msg1_Frame"
    if line.startswith(b"$VNYMR"):
      data = line.split(b',')
      print(data)
      gyro_z = float(data[12].split('*')[0])
      yaw = float(data[1]) 
      pitch = float(data[2]) 
      roll = float(data[3]) 
      mag_x = float(data[4]) 
      mag_y = float(data[5])
      mag_z = float(data[6])
      acc_x = float(data[7])
      acc_y = float(data[8])
      acc_z = float(data[9])
      gyr_x = float(data[10])
      gyr_y = float(data[11])
      quat_x, quat_y, quat_z, quat_w = euler_to_quat(yaw, pitch, roll)
      imu_msg.header.stamp = rospy.Time.now()
      imu_msg.header.seq += 1
      imu_msg.IMU.orientation.x = quat_x
      imu_msg.IMU.orientation.y = quat_y
      imu_msg.IMU.orientation.z = quat_z
      imu_msg.IMU.orientation.w = quat_w

      imu_msg.IMU.angular_velocity.x = gyro_x
      imu_msg.IMU.angular_velocity.y = gyro_y
      imu_msg.IMU.angular_velocity.z = gyro_z

      imu_msg.IMU.linear_acceleration.x = acc_x
      imu_msg.IMU.linear_acceleration.y = acc_y
      imu_msg.IMU.linear_acceleration.z = acc_z

      imu_msg.MagField.magnetic_field.x = mag_x
      imu_msg.MagField.magnetic_field.y = mag_y
      imu_msg.MagField.magnetic_field.z = mag_z
      print(imu_msg)
      imu_pub.publish(imu_msg) 
    else:
   		print("Incorrect string formation")
if __name__ == "__main__":
	SENSOR_NAME = "IMU_SENSOR"
	rospy.init_node('driver', anonymous=True)
	serial_port = rospy.get_param('~port','/dev/ttyUSB1')
	serial_baud = rospy.get_param('~baudrate',115200)
	port = serial.Serial(serial_port, serial_baud, timeout=5.0)
	sampling_rate = rospy.get_param("~sampling_rate", 40.0) 
	imu_pub = rospy.Publisher("imu",Imu, queue_size=10)
	rate=rospy.Rate(40)
	line = port.readline()
	while not rospy.is_shutdown():

        	if line == '':
        	        rospy.logwarn("DEPTH: No data")

        	else:
             		imu_driver(line)

	try:
        	imu_driver(sys.argv[1])
	except rospy.ROSInterruptException:
        	port.close()

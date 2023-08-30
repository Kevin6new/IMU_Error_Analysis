import matplotlib.pyplot as plt
import quaternion
import pandas as pd
import numpy as np
import seaborn as sb

fixed_df = pd.read_csv(r'/home/kevin32/catkin_ws/src/rtk_lab/analysis/imu.csv')

grr_x=fixed_df[".IMU.orientation.x"].to_numpy()
grr_y=fixed_df[".IMU.orientation.y"].to_numpy()
grr_z=fixed_df[".IMU.orientation.z"].to_numpy()

def get_quaternion_from_euler(roll, pitch, yaw):
  qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
  qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
  qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
 
  return [qx, qy, qz]

orr_x,orr_y,orr_z=get_quaternion_from_euler(grr_x,grr_y,grr_z)

ang_x = fixed_df[".IMU.angular_velocity.x"].to_numpy()
ang_y = fixed_df[".IMU.angular_velocity.y"].to_numpy()
ang_z =fixed_df[".IMU.angular_velocity.z"].to_numpy()

lin_x = fixed_df[".IMU.linear_acceleration.x"].to_numpy()
lin_y = fixed_df[".IMU.linear_acceleration.y"].to_numpy()
lin_z =fixed_df[".IMU.linear_acceleration.z"].to_numpy()

mag_x = fixed_df[".MagField.magnetic_field.x"].to_numpy()
mag_y = fixed_df[".MagField.magnetic_field.y"].to_numpy()
mag_z =fixed_df[".MagField.magnetic_field.z"].to_numpy()


IMUtimes = fixed_df[".Header.stamp.secs"].to_numpy()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = orr_x,color='red')
plt.xlabel("Time(s)")
plt.ylabel("Orientation in X(rad)")
plt.title("Orientation vs Time")
plt.show()

print(np.mean(orr_x))
print(np.std(orr_x))


sb.scatterplot(data = fixed_df, x =IMUtimes, y = orr_y)
plt.xlabel("Time(s)")
plt.ylabel("Orientation in Y(rad)")
plt.title("Orientation vs Time")
plt.show()

print(np.mean(orr_y))
print(np.std(orr_y))

sb.scatterplot(data = fixed_df, x =IMUtimes, y = orr_z,color='green')
plt.xlabel("Time(s)")
plt.ylabel("Orientation in Z(rad)")
plt.title("Orientation vs Time")
plt.show()

print(np.mean(orr_z))
print(np.std(orr_z))

sb.scatterplot(data = fixed_df, x =IMUtimes, y = ang_x,color='red')
plt.xlabel("Time(s)")
plt.ylabel("Angular Velocity in X(rad/s)")
plt.title("Angular Velocity vs Time")
plt.show()


sb.scatterplot(data = fixed_df, x =IMUtimes, y = ang_y)
plt.xlabel("Time(s)")
plt.ylabel("Angular Velocity in Y(rad/s)")
plt.title("Angular Velocity vs Time")
plt.show()


sb.scatterplot(data = fixed_df, x =IMUtimes, y = ang_z,color='green')
plt.xlabel("Time(s)")
plt.ylabel("Angular Velocity in Z(rad/s)")
plt.title("Angular Velocity vs Time")
plt.show()


sb.scatterplot(data = fixed_df, x =IMUtimes, y = lin_x,color='red')
plt.xlabel("Time(s)")
plt.ylabel("Linear Acceleration in X(m/s2)")
plt.title("Linear Acceleration vs Time")
plt.show()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = lin_y)
plt.xlabel("Time(s)")
plt.ylabel("Linear Acceleration in Y(m/s2)")
plt.title("Linear Acceleration vs Time")
plt.show()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = lin_z,color='green')
plt.xlabel("Time(s)")
plt.ylabel("Linear Acceleration in Z(m/s2)")
plt.title("Linear Acceleration vs Time")
plt.show()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = mag_x,color='red')
plt.xlabel("Time(s)")
plt.ylabel("Magnetic Fluctuation in X(Teslas)")
plt.title("Magnetic Fluctuation vs Time")
plt.show()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = mag_y)
plt.xlabel("Time(s)")
plt.ylabel("Magnetic Fluctuation in Y(Teslas)")
plt.title("Magnetic Fluctuation vs Time")
plt.show()

sb.scatterplot(data = fixed_df, x =IMUtimes, y = mag_z,color='green')
plt.xlabel("Time(s)")
plt.ylabel("Magnetic Fluctuation in Z(Teslas)")
plt.title("Magnetic Fluctuation vs Time")
plt.show()



	 

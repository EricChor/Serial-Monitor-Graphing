import serial
import matplotlib.pyplot as plt
import sys
import threading

# serial_data = serial.Serial('COM1',115200)
# serial_data = serial.Serial('COM2',115200)
# serial_data = serial.Serial('COM3',115200)
# serial_data = serial.Serial('COM4',115200)
# serial_data = serial.Serial('COM5',115200)
# serial_data = serial.Serial('COM6',115200)
# serial_data = serial.Serial('COM7',115200)
# serial_data = serial.Serial('COM8',115200)
# serial_data = serial.Serial('COM9',115200)
# serial_data = serial.Serial('COM10',115200)
# serial_data = serial.Serial('COM11',115200)
serial_data = serial.Serial('COM12',115200)
# serial_data = serial.Serial('COM13',115200)
# serial_data = serial.Serial('COM14',115200)
# serial_data = serial.Serial('COM15',115200)
# serial_data = serial.Serial('COM16',115200)
# serial_data = serial.Serial('COM17',115200)
# serial_data = serial.Serial('COM18',115200)
# serial_data = serial.Serial('COM19',115200)
# serial_data = serial.Serial('COM20',115200)
# serial_data = serial.Serial('COM21',115200)
# serial_data = serial.Serial('COM22',115200)
# serial_data = serial.Serial('COM23',115200)
# serial_data = serial.Serial('COM24',115200)


float_data_array = [0.0] * 4
x_poses = []
y_poses = []

global continue_running
continue_running = True

goal_point_x = [0.0,0.0]
goal_point_y = [0.0,0.0]

#plt.ion()
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.xlim(-100,100)
plt.ylim(-100,100)

def draw_line(x1, y1, x2, y2):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the line between the two points
    ax.plot([x1, x2], [y1, y2], marker='o')

def exit_thread():
    input_string = input("press enter to exit")
    global continue_running
    continue_running = False
    print(continue_running)
    sys.exit()

Threaded_exit = threading.Thread(target=exit_thread)
Threaded_exit.start()

while True:
    if continue_running == False:
        print ("continue_running is false")
        sys.exit()
    try:
        serial_data.reset_input_buffer()
        data = serial_data.readline()
        data.decode("utf-8")[0:-2]
        data = str(data)
        string_data_array = data.split(":")
        string_data_array[0] = string_data_array[0][2:]
        string_data_array[3] = string_data_array[3].removesuffix("\\r\\n'")

        float_data_array[0] = float(string_data_array[0])
        float_data_array[1] = float(string_data_array[1])
        float_data_array[2] = float(string_data_array[2])
        float_data_array[3] = float(string_data_array[3])

        x_poses.append([float_data_array[0]])
        y_poses.append([float_data_array[1]])
        goal_point_x[0] = float_data_array[0]
        goal_point_x[1] = float_data_array[2]
        goal_point_y[0] = float_data_array[1]
        goal_point_y[1] = float_data_array[3]

        
        plt.clf()
        plt.xlabel('x - axis') 
        plt.ylabel('y - axis') 
        plt.xlim(-100,100)
        plt.ylim(-100,100)
        plt.plot(x_poses,y_poses, label = "current pose",linestyle = 'solid',color = 'blue')
        plt.plot(goal_point_x, goal_point_y, label = "target poses", linestyle = 'dashed',color = 'red')
        plt.pause(0.05)

        #print(float_data_array)
        #print (string_data_array)
        #print (float_data_array)
    except:
        print ("exception thrown")
        plt.pause(0.05)



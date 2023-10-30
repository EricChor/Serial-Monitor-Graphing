import serial                  
import matplotlib.pyplot as plt	
import pandas as pd

def two_list_len_same(a,b):
    len_min = min (len(a),len(b))
    result_a = a[0:len_min],b[0:len_min]

if __name__ == '__main':
    data_list = []
    cycle_mark = True
    plt.ion()
    plt.figure(1)
    data_array = pd.DataFrame(columns=["x_pos", "y_pos"])
    ser = serial.Serial('COM6', 115200)

    while True:
        while cycle_mark:
            data = ser.readline().decode("utf-8")
            data_list = data.strip().split(":")
            #checks x_pos
            if data_list[0] == "x_pos":
                data_array.loc[len(data_array.index)] = data_list[1]
            elif data_list[0] == "y_pos":
                data_array.loc[len(data_array.index)-1] = data_list[1]
            elif data_list[0] == "End":
                cycle_mark = False
        cycle_mark = True

        draw_from_list = two_list_len_same(data_array['x_pos'].to_numpy(), data_array['y_pos'].to_numpy())

        plt.clf()
        plt.title("Odometry Position")
        plt.plot(draw_from_list[0], draw_from_list[1])
        plt.draw()
        plt.pause(0.1)
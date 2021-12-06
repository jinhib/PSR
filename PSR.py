from scipy.io import wavfile
import matplotlib.pyplot as plt
import os
import numpy as np

base_dir = 'E:/Experiment/2021.03.LungSound/0.data'
ori_dir = base_dir + '/' + 'original/together'
psr_cnt = 0.05
save_dir = base_dir + '/' + 'PSR_' + str(psr_cnt) + '/together'
file_list = os.listdir(ori_dir)

for file_name in file_list:
    sr, data = wavfile.read(ori_dir + '/' + file_name)
    if len(np.shape(data)) == 2:
        data1 = data[:, 0]
    else:
        data1 = data
    abs_max = min(data1)
    for cmp in data1:
        if abs_max < abs(cmp):
            abs_max = abs(cmp)

    i = 0
    axle = []

    while i < len(data):
        axle.append(data1[int(i)]/abs_max)
        i += psr_cnt * sr

    x, y = axle[:-1], axle[1:]
    ax = plt.gca()
    plt.scatter(x, y)
    plt.axis([-1.2, 1.2, -1.2, 1.2])
    ax.set_aspect('equal')
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.tick_params('both', length=0)
    plt.savefig(save_dir + '/' + file_name[:-4] + '.jpg')
    plt.close()
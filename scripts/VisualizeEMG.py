import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from matplotlib import rcParams
config = {
    "font.family":'Times New Roman',  # 设置字体类型
}
rcParams.update(config)
bound_gaussian_sigma = 42

# * 配色方案一
# red = '#9C4084'
# blue = '#3F81B4'
# green = '6EBDB7'

# * 配色方案二
# green = '#479650'
# blue = '#345AA4'
# grey = '#919396'

# * 双色配色方案
green = '#428B69'
yellow = '#E4C671'


visualizeMode = 2 # 1代表三种模拟条件绘制在一幅子图上，2代表一种模拟条件的两种不同速度绘制在一幅子图上

if visualizeMode == 1:
    # * NOBMSEXO
    noBMSEXO_data = r'data\Experiment\sEMG\GASM_BMSEXOON_08.csv'

    # * BMSON
    BMSON_data = r'data\Experiment\sEMG\GASM_BMSON_08.csv' # GASM_08

    # * BMSEXOON
    BMSEXOON_data = r'data\Experiment\sEMG\GASM_BMSEXOON_08.csv' # GASM_08

    noBMSEXO_df = pd.read_csv(noBMSEXO_data)
    BMSON_df = pd.read_csv(BMSON_data)
    BMSEXOON_df = pd.read_csv(BMSEXOON_data)

    noBMSEXO_x = noBMSEXO_df['X']
    noBMSEXO_mean = noBMSEXO_df['Mean']
    noBMSEXO_mean_smooth = gaussian_filter1d(noBMSEXO_df['Mean'], sigma=9)
    noBMSEXO_upper_bound = noBMSEXO_df['Mean + Std Dev']
    noBMSEXO_upper_bound_smooth = gaussian_filter1d(noBMSEXO_df['Mean + Std Dev'], sigma=bound_gaussian_sigma)
    noBMSEXO_lower_bound = noBMSEXO_df['Mean - Std Dev']
    noBMSEXO_lower_bound_smooth = gaussian_filter1d(noBMSEXO_df['Mean - Std Dev'], sigma=bound_gaussian_sigma)

    BMSON_x = BMSON_df['X']
    BMSON_mean = BMSON_df['Mean']
    BMSON_mean_smooth = gaussian_filter1d(BMSON_df['Mean'], sigma=9)
    BMSON_upper_bound = BMSON_df['Mean + Std Dev']
    BMSON_upper_bound_smooth = gaussian_filter1d(BMSON_df['Mean + Std Dev'], sigma=bound_gaussian_sigma)
    BMSON_lower_bound = BMSON_df['Mean - Std Dev']
    BMSON_lower_bound_smooth = gaussian_filter1d(BMSON_df['Mean - Std Dev'], sigma=bound_gaussian_sigma)

    BMSEXOON_x = BMSEXOON_df['X']
    BMSEXOON_mean = BMSEXOON_df['Mean']
    BMSEXOON_mean_smooth = gaussian_filter1d(BMSEXOON_df['Mean'], sigma=9)
    BMSEXOON_upper_bound = BMSEXOON_df['Mean + Std Dev']
    BMSEXOON_upper_bound_smooth = gaussian_filter1d(BMSEXOON_df['Mean + Std Dev'], sigma=bound_gaussian_sigma)
    BMSEXOON_lower_bound = BMSEXOON_df['Mean - Std Dev']
    BMSEXOON_lower_bound_smooth = gaussian_filter1d(BMSEXOON_df['Mean - Std Dev'], sigma=bound_gaussian_sigma)

    fig, ax = plt.subplots(figsize=(6, 6))

    plt.plot(noBMSEXO_x, noBMSEXO_mean_smooth, color=grey, label='NOBMSEXO Mean', linewidth=3.0, linestyle='--')
    plt.plot(BMSON_x, BMSON_mean_smooth, color=green, label='BMSON Mean', linewidth=3.0, linestyle='--')
    plt.plot(BMSEXOON_x, BMSEXOON_mean_smooth, color=blue, label='BMSEXOON Mean', linewidth=3.0, linestyle='--')

    plt.fill_between(noBMSEXO_x, noBMSEXO_lower_bound_smooth, noBMSEXO_upper_bound_smooth, color=grey, alpha=0.2)
    plt.fill_between(BMSON_x, BMSON_lower_bound_smooth, BMSON_upper_bound_smooth, color=green, alpha=0.2)
    plt.fill_between(BMSEXOON_x, BMSEXOON_lower_bound_smooth, BMSEXOON_upper_bound_smooth, color=blue, alpha=0.2)

    plt.title("Muscle Activation ", fontsize=14)
    plt.xlabel("Gait Phase (%)", fontsize=12)
    plt.ylabel("RMS of GASM", fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.show()

if visualizeMode == 2:
    # * BMSEXOON
    lower_data = r'data\Experiment\sEMG\VASM_BMSEXOON_08.csv' # VASM_08
    faster_data = r'data\Experiment\sEMG\VASM_BMSEXOON_12.csv' # VASM_12

    lower_df = pd.read_csv(lower_data)
    faster_df = pd.read_csv(faster_data)

    lower_x = lower_df['X']
    lower_mean = lower_df['Mean']
    lower_mean_smooth = gaussian_filter1d(lower_df['Mean'], sigma=9)
    lower_upper_bound = lower_df['Mean + Std Dev']
    lower_upper_bound_smooth = gaussian_filter1d(lower_df['Mean + Std Dev'], sigma=bound_gaussian_sigma)
    lower_lower_bound = lower_df['Mean - Std Dev']
    lower_lower_bound_smooth = gaussian_filter1d(lower_df['Mean - Std Dev'], sigma=bound_gaussian_sigma)

    faster_x = faster_df['X']
    faster_mean = faster_df['Mean']
    faster_mean_smooth = gaussian_filter1d(faster_df['Mean'], sigma=9)
    faster_upper_bound = faster_df['Mean + Std Dev']
    faster_upper_bound_smooth = gaussian_filter1d(faster_df['Mean + Std Dev'], sigma=bound_gaussian_sigma)
    faster_lower_bound = faster_df['Mean - Std Dev']
    faster_lower_bound_smooth = gaussian_filter1d(faster_df['Mean - Std Dev'], sigma=bound_gaussian_sigma)

    fig, ax = plt.subplots(figsize=(6, 6))

    plt.plot(lower_x, lower_mean_smooth, color=green, label='0.8 m/s', linewidth=3.0, linestyle='--')
    plt.plot(faster_x, faster_mean_smooth, color=yellow, label='1.2 m/s', linewidth=3.0, linestyle='--')
    plt.fill_between(lower_x, lower_lower_bound_smooth, lower_upper_bound_smooth, color=green, alpha=0.2)
    plt.fill_between(faster_x, faster_lower_bound_smooth, faster_upper_bound_smooth, color=yellow, alpha=0.2)

    plt.title("Muscle Activation ", fontsize=14)
    plt.xlabel("Gait Phase (%)", fontsize=12)
    plt.ylabel("RMS of VASM", fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.show()
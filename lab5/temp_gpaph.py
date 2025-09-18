import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def plot_temperature(data:dict,location:str, filename='temperature_plot.png'):
    times = []
    temps = []

    for time_str, temp in data.items():
        time_obj = datetime.strptime(time_str, '%H:%M')
        times.append(time_obj)
        temps.append(temp)

    sorted_data = sorted(zip(times, temps))
    times_sorted, temps_sorted = zip(*sorted_data)

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(times_sorted, temps_sorted, marker='o', linestyle='-',
            color='red', linewidth=3, markersize=8, markerfacecolor='white', markeredgewidth=2)

    ax.fill_between(times_sorted, temps_sorted, alpha=0.3, color='red')

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))

    ax.set_title(f'Hourly air temperature in {location}', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)

    ax.grid(True, alpha=0.2)

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)

    for time, temp in zip(times_sorted, temps_sorted):
        ax.annotate(f'{temp}°C',
                    xy=(time, temp),
                    xytext=(0, 15),
                    textcoords='offset points',
                    ha='center',
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

    print(f'Saved to: {filename}')

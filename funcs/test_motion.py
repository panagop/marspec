import numpy as np
import matplotlib.pyplot as plt
from eqsig.single import AccSignal

from dataclasses import dataclass


@dataclass
class TestMotion:

    acc_signal: AccSignal
    periods: np.ndarray = np.linspace(0, 4.0, num=400)

    def __post_init__(self):
        self.acc_signal.response_times = self.periods
        self.acc_signal.generate_displacement_and_velocity_series()

    @classmethod
    def from_acc_file(cls,
                      pathfilename: str,
                      motion_step: float,
                      scale_factor: float = 1.0,
                      accel_column: int = 1,
                      skiprows: int = 2):

        rec = np.loadtxt(
            pathfilename, usecols=accel_column,
            skiprows=skiprows)*scale_factor

        acc_signal = AccSignal(
            rec, motion_step)

        return cls(acc_signal=acc_signal)
    
    @classmethod
    def from_csv_file(cls, pathfilename: str, motion_step: float, scale_factor: float = 1.0, accel_column: int = 1, skiprows: int = 0):
        pass

    
    def fig_time_histories(self):

        fig, ax = plt.subplots(3, figsize=(10, 10))
        ax[0].plot(self.acc_signal.time, self.acc_signal.values)
        ax[1].plot(self.acc_signal.time, self.acc_signal.velocity)
        ax[2].plot(self.acc_signal.time, self.acc_signal.displacement)

        ax[0].set_ylabel('Acceleration (m/s²)')
        ax[0].set_xlabel('Time (s)')
        ax[1].set_ylabel('Velocity (m/s)')
        ax[1].set_xlabel('Time (s)')
        ax[2].set_ylabel('Displacement (m)')
        ax[2].set_xlabel('Time (s)')

        fig.suptitle(
            'Χρονοϊστορίες επιταχύνσεων, ταχυτήτων και μετακινήσεων', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        return fig

    def fig_sa(self):

        s_a = self.acc_signal.s_a

        fig, ax = plt.subplots()
        ax.plot(self.periods, s_a, label="eqsig")
        ax.legend()
        ax.set_xlabel('Perios (s)')
        ax.set_ylabel('Spectral Acceleration m/s²')
        ax.set_title('Response Spectrum')

        return fig

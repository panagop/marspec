import numpy as np
import matplotlib.pyplot as plt
from eqsig.single import AccSignal

from dataclasses import dataclass

# ΣΥΝΑΡΤΗΣΕΙΣ ΓΙΑ ΑΡΧΕΙΑ ΤΧΤ
# ΧΡΟΝΟΪΣΤΟΡΙΕΣ ΕΠΙΤΑΧΥΝΣΗΣ, ΤΑΥΤΗΤΑΣ ΚΑΙ ΑΠΟΚΡΙΣΗΣ


def show_test_motion(pathfilename: str,
                     motion_step: float):

    rec = np.loadtxt(pathfilename, skiprows=2)
    acc_signal = AccSignal(rec, motion_step)
    acc_signal.generate_displacement_and_velocity_series()

    fig, ax = plt.subplots(3)
    ax[0].plot(acc_signal.time, acc_signal.values)
    ax[1].plot(acc_signal.time, acc_signal.velocity)
    ax[2].plot(acc_signal.time, acc_signal.displacement)

    return fig




# ΦΑΣΜΑΤΑ FOURIER
def show_fourier_spectra_stable_against_aliasing(pathfilename: str,
                                                 motion_step: float):

    rec = np.loadtxt(pathfilename, skiprows=2)
    rec2 = np.zeros(2 ** 13)
    rec2[:len(rec)] = rec
    org_signal = AccSignal(rec, motion_step)
    extended_signal = AccSignal(rec2, motion_step)

    rec_split = []
    for i in range(int(len(rec2) / 2)):
        rec_split.append(rec2[i * 2])

    acc_split = AccSignal(rec_split, motion_step * 2)

    fig, ax = plt.subplots(2)
    ax[0].plot(org_signal.time, org_signal.values)
    ax[0].plot(extended_signal.time, extended_signal.values)
    ax[0].plot(acc_split.time, acc_split.values)

    ax[1].plot(org_signal.fa_frequencies, abs(
        org_signal.fa_spectrum), lw=0.7, label="original")
    ax[1].plot(acc_split.fa_frequencies, abs(
        acc_split.fa_spectrum), lw=0.7, label="split")
    ax[1].plot(extended_signal.fa_frequencies, abs(
        extended_signal.fa_spectrum), lw=0.7, label="full")

    plt.legend()
    return fig

# ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ


def show_response_spectra_at_high_frequencies(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, skiprows=2)
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    s_a_in_g = s_a / 9.81

    fig, ax = plt.subplots()
    ax.plot(times, s_a_in_g, label="eqsig")
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Spectral Acceleration (g)')
    ax.set_title('Response Spectra at High Frequencies')

    return fig

# ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ


def show(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, skiprows=2)
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    fig, ax = plt.subplots()
    ax.plot(times, s_a, label="eqsig")
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Spectral Acceleration')
    ax.set_title('Response Spectra at High Frequencies')

    return fig


# ΣΥΝΑΡΤΗΣΕΙΣ ΓΙΑ ΑΡΧΕΙΑ ASC


def show_test_motion_L(pathfilename: str, motion_step: float):
    # Διαβάζουμε τη δεύτερη στήλη του αρχείου
    rec = np.loadtxt(pathfilename, usecols=1, skiprows=1)*0.01
    acc_signal = AccSignal(rec, motion_step)
    acc_signal.generate_displacement_and_velocity_series()

    fig, ax = plt.subplots(3, figsize=(10, 10))
    ax[0].plot(acc_signal.time, acc_signal.values)
    ax[1].plot(acc_signal.time, acc_signal.velocity)
    ax[2].plot(acc_signal.time, acc_signal.displacement)

    ax[0].set_ylabel('Acceleration (m/s²)')
    ax[0].set_xlabel('Period T (s)')
    ax[1].set_ylabel('Velocity (m/s)')
    ax[1].set_xlabel('Period T (s)')
    ax[2].set_ylabel('Displacement (m)')
    ax[2].set_xlabel('Period T (s)')

    fig.suptitle(
        'Φασματική ανάλυση σεισμού, σύμφωνα με την συνιστώσα L', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    return fig


def show_test_motion_T(pathfilename: str, motion_step: float):
    # Διαβάζουμε τη τέταρτη στήλη του αρχείου
    rec = np.loadtxt(pathfilename, usecols=3, skiprows=1)*0.01
    acc_signal = AccSignal(rec, motion_step)
    acc_signal.generate_displacement_and_velocity_series()

    fig, ax = plt.subplots(3, figsize=(10, 10))
    ax[0].plot(acc_signal.time, acc_signal.values)
    ax[1].plot(acc_signal.time, acc_signal.velocity)
    ax[2].plot(acc_signal.time, acc_signal.displacement)

    ax[0].set_ylabel('Acceleration (m/s²)')
    ax[0].set_xlabel('Period T (s)')
    ax[1].set_ylabel('Velocity (m/s)')
    ax[1].set_xlabel('Period T (s)')
    ax[2].set_ylabel('Displacement (m)')
    ax[2].set_xlabel('Period T (s)')

    fig.suptitle(
        'Φασματική ανάλυση σεισμού, σύμφωνα με την συνιστώσα T', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    return fig

# ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ


def show_response_spectra_at_high_frequencies_L(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, usecols=1, skiprows=1)
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    s_a_in_g = s_a / 9.81

    fig, ax = plt.subplots()
    ax.plot(times, s_a_in_g, label="eqsig")
    ax.legend()
    ax.set_xlabel('Period T (s)')
    ax.set_ylabel('Spectral Acceleration (g)')

    fig.suptitle('Ελαστικό Φάσμα Απόκρισης, σύμφωνα με την συνιστώσα L')
    plt.tight_layout(rect=[0, 0, 1, 1])

    return fig


def show_response_spectra_at_high_frequencies_T(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, usecols=3, skiprows=1)
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    s_a_in_g = s_a / 9.81

    fig, ax = plt.subplots()
    ax.plot(times, s_a_in_g, label="eqsig")
    ax.legend()
    ax.set_xlabel('Period T (s)')
    ax.set_ylabel('Spectral Acceleration (g)')

    fig.suptitle('Ελαστικό Φάσμα Απόκρισης, σύμφωνα με την συνιστώσα T')
    plt.tight_layout(rect=[0, 0, 1, 1])

    return fig

# ΦΑΣΜΑ ΑΠΟΚΡΙΣΗΣ (m/s2)


def show_L(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, usecols=1, skiprows=1)*0.01
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    fig, ax = plt.subplots()
    ax.plot(times, s_a, label="eqsig")
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Spectral Acceleration')
    ax.set_title('Response Spectra at High Frequencies')

    return fig


def show_T(pathfilename: str, motion_step: float):
    rec = np.loadtxt(pathfilename, usecols=3, skiprows=1)*0.01
    times = np.linspace(0, 4.0, num=400)
    acc_signal = AccSignal(rec, motion_step, response_times=times)
    s_a = acc_signal.s_a

    fig, ax = plt.subplots()
    ax.plot(times, s_a, label="eqsig")
    ax.legend()
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Spectral Acceleration')
    ax.set_title('Response Spectra at High Frequencies')

    return fig

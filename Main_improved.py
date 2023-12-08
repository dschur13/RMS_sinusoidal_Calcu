import math
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

def get_time_vars():
    user_input2 = input("Is frequency in hertz? y/n")
    if user_input2 == "y":
        frequency = (float(input("Enter frequency: ")) * 2*math.pi)
        user_input1 = input("Were you given end time? y/n?: ")
        if user_input1 == "y":
            end_time = (float(input("Enter end time: ")))
            return end_time, frequency
        elif user_input1 == "n":
            end_time = (float((1/frequency)*10))
            return end_time, frequency
        t = float(end_time - start_time)
        return t
    elif user_input2 == "n":
        frequency = (float(input("Enter frequency: ")) / 2*math.pi)
        user_input1 = input("Were you given end time? y/n?: ")
        if user_input1 == "y":
            end_time = (float(input("Enter end time: ")))
            return end_time, frequency
        elif user_input1 == "n":
            end_time = (float((1/frequency))*10 )   
            return end_time, frequency   
        t = float(end_time - start_time)
        return t

def get_ang_freq(frequency):
    angular_frequency = float(frequency*1000)
    return angular_frequency

def integrand(t, amplitude, frequency, phase_angle):
    angular_frequency = float(frequency*1000)
    instantaneous_value = float(amplitude * np.cos(angular_frequency * t + math.radians(phase_angle)))
    return float(instantaneous_value**2)

def calculate_rms(amplitude, frequency, phase_angle, end_time, start_time=0):
    result = quad(integrand, start_time,end_time, args=(amplitude, frequency, phase_angle))
    print(result)
    #rms = math.sqrt(result)
    #return rms

def plot_signal(amplitude, angular_frequency, phase_angle, end_time, start_time=0):
    time_values = np.linspace(start_time, end_time, num=1000)
    signal_values = amplitude * np.cos(angular_frequency * time_values + math.radians(phase_angle))

    plt.plot(time_values, signal_values, label='Sinusoidal Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Sinusoidal Signal')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    #Determine end time and frequency
    # Input values
 



  
    
    phase_angle = float(input("Enter phase angle (in degrees): "))

    # Convert phase angle to radians
    phase_angle_rad = math.radians(phase_angle)

    amplitude = float(input("what is the amplitude?: "))

    # Calculate RMS value
    rms_value = calculate_rms(amplitude, frequency, phase_angle_rad, end_time, start_time)

    print("\nInput Values:")
    print(f"Amplitude: {amplitude}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Frequency: {frequency} mHz")
    print(f"Phase Angle: {phase_angle} degrees")

    print("\nResults:")
    print(f"RMS Value: {rms_value}")

    # Plot the signal
    plot_signal(amplitude, frequency, phase_angle_rad, end_time, start_time=0)

if __name__ == "__main__":
    main()

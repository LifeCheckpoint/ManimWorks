from manimlib import UP, RIGHT
import numpy as np

class Effect:
    def wiggle(freq=2, amp: list=[1,1,1], octaves=3, amp_mult=0.5):
        def updater(mobject, dt):
            offset = np.zeros((3,))
            ts = 0
            
            for i in range(octaves):
                octave_freq = freq * (2 ** i)
                for dim in range(3):
                    octave_amp = amp[dim] * (amp_mult ** i)
                    offset[dim] += octave_amp * np.sin(2 * np.pi * octave_freq * ts)

            ts += dt
            print(offset)
            mobject.shift(offset)

        return updater
        
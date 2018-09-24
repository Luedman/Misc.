# Misc.
A collection of scripts related to quantitative Finance

### RandomNumber.py
This script is linear congruential pseudo random number generator that generates 100'000 random numbers. After normalizing them into an intervall between zero and one, pixels are with a value of less than 0.5 are drawn black, whereas all the other pixels are left white. That way you can easiliy detect patterns, which depend on the paramerts a and b.

### WienerProcess.py
This script produces vectors with the values that simulate a Wiener process in discretized form. You can define number of processes and and the number of steps per process.

import math
import sys
# Parameters for object A
m_a = float(input("Enter mass of object A (kg):"))
c_a = float(input("Enter the heat capacity of object A (J/kg°C):"))
t_a = float(input("Enter initial temperature of object A (°C):"))
# Parameters for object B
m_b = float(input("Enter mass of object B (kg):"))
c_b = float(input("Enter the heat capacity of object B (J/kg°C):"))
t_b = float(input("Enter initial temperature of object B (°C):"))
# Calculate final temperature:
final_temp = (m_a * c_a * t_a + m_b * c_b * t_b) / (m_a * c_a + m_b * c_b)
print(f"The final equilibrium temperature after mixing is: {final_temp:.2f} °C")
# Calculate heat lost or gained by each object
if t_a < t_b:
    print(f"Object A gains {final_temp - t_a:.2f} °C")
    print(f"Object B loses {t_b - final_temp:.2f} °C")
elif t_a > t_b:
    print(f"Object A loses {t_a - final_temp:.2f} °C")
    print(f"Object B gains {final_temp - t_b:.2f} °C")
else:
    print("Both objects have the same temperature. No heat transfer occurs.")
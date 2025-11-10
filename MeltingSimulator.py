import math
import sys
solids = {
    "ice": {"melting_point": 0, "fusion": 334000, "heat_capacity": 2.1*1000},
    "aluminum": {"melting_point": 660, "fusion": 397000, "heat_capacity": 0.9*1000},
    "copper": {"melting_point": 1085, "fusion": 205000, "heat_capacity": 0.39*1000},
    "iron": {"melting_point": 1538, "fusion": 247000, "heat_capacity": 0.45*1000},
    "gold": {"melting_point": 1064, "fusion": 64000, "heat_capacity": 0.13*1000},
    "silver": {"melting_point": 961, "fusion": 105000, "heat_capacity": 0.24*1000},
    "lead": {"melting_point": 327, "fusion": 23000, "heat_capacity": 0.13*1000},
    "tin": {"melting_point": 232, "fusion": 59000, "heat_capacity": 0.23*1000},
    "zinc": {"melting_point": 420, "fusion": 112000, "heat_capacity": 0.39*1000},
    "silicon": {"melting_point": 1414, "fusion": 1800000, "heat_capacity": 0.71*1000},
    "salt": {"melting_point": 801, "fusion": 492000, "heat_capacity": 0.86*1000}
}
print("Available solids for melting simulation:")
for solid in solids:
    print(f"- {solid.capitalize()}")
selected_solid = input("Enter the name of the solid:").lower()
if selected_solid not in solids:
    print("Not found")
    sys.exit(1)

melting_point = solids[selected_solid]["melting_point"]
fusion_heat = solids[selected_solid]["fusion"]
heat_capacity = solids[selected_solid]["heat_capacity"]

print(f"{selected_solid.capitalize()} melts at {melting_point} °C with a heat of fusion of {fusion_heat} J/kg and a specific heat capacity of {heat_capacity} J/kg°C.")

mass = float(input("Enter the mass of the solid (in kilograms)"))
initial_temp = float(input("Enter the initial temperature of the solid (in °C):"))
energy_efficiency = float(input("Enter the energy efficiency percentage (1-100):")) / 100.0
heat_for_melting_temperature = mass * heat_capacity * (melting_point - initial_temp)
energy_capacity = float(input("Enter the energy capacity of the heating source (in kilowatts): ")) * 1000
heat_for_phase_change = mass * fusion_heat
total_heat_required = (heat_for_melting_temperature + heat_for_phase_change) / energy_efficiency

if initial_temp >= melting_point:
    print(f"The solid is already above its melting point of {melting_point} °C.")
    sys.exit(0)
else:
    print(f"Total heat required to melt the solid: {total_heat_required:.2f} J")
    time_required = total_heat_required / energy_capacity
    print(f"Time required to melt the solid: {time_required:.2f} seconds")


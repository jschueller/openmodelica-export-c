import otfmi

path_fmu = 'deviation_c.fmu'
model_fmu = otfmi.FMUFunction(path_fmu, inputs_fmu=["E", "F", "L", "I"], outputs_fmu=["y"])

print(model_fmu)
x = [3.1e7, 3.1e4, 255.0, 420.0]
y = model_fmu(x)
print(y)


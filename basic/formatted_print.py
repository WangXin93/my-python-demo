name = "Neil"
times = [6, 12, 18]
temperatures = [11.13, 12.55, 10.98]

print("Hi %s:" % name)
for time, tp in zip(times, temperatures):
    print("Time: %-3d Temperature: %.1f C" % (time, tp))

print("Hi {name}:".format(name=name))
for time, tp in zip(times, temperatures):
    print("Time: {:<3d} Temperature: {:.1f} C".format(time, tp))

print(f"Hi {name}:")
for time, tp in zip(times, temperatures):
    print(f"Time: {time:<3d} Temperature: {tp:.1f} C")

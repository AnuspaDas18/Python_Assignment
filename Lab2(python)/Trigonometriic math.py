import math

a = math.sin(math.radians(60))
b = math.cos(math.pi)
c = math.sin(0.8660254037844386)
try:
    d = math.tan(math.radians(90))
except ValueError:
    d = "Undefined"

print(f"a) Sin of 60 degrees: {a}")
print(f"b) Cos of pi: {b}")
print(f"c) Sin of 0.8660254037844386: {c}")
print(f"d) Tan of 90 degrees: {d}")

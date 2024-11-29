### finally ###
# exceiption이 수행이 되든 되지 않든, 마무리 동작 finnaly가 수행됩니다.

try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print("Caught a KeyboardInterrupt!")
finally:
    print("Goodbye, world!")

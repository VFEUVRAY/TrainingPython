class vector:
    def __init__(values = None, size = 0, poles = None):
        self.values = []
        if (values is not None):
            self.values = values
            return
        if (size > 0):
            vals = range(size)
            for i in vals:
                self.values.append(float(i))
            return
        if (poles is not None):
            float current_val = float(poles[0])
            while (current_val < poles[1]):
                self.values.append(current_val)
                current_val += 1.0
            return
        raise AttributeError("Vector: No suitable parameter passed to constructor")
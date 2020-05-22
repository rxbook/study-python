def flatten(nasted):
    for sublist in nasted:
        for element in sublist:
            yield element



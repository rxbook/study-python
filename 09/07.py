def flatten(nested):
    try:
        #��Ҫ���������ַ����Ķ���
        try:nested + ''
        except TypeError:pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested



        


        



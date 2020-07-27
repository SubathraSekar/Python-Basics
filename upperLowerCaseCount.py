def calculateCount(stringVal):
        lst = []
        upper=0
        lower=0
        for i in stringVal:
            if i.isupper():
                upper=upper+1
            elif i.islower():
                lower=lower+1
        lst.append(upper)
        lst.append(lower)
        return lst
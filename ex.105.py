def notas(*n, situ = False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    return  r


resp = notas(5.5, 8, 9)
print(resp)

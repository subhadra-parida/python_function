def tri_recoursion(k):
    result=0
    if (k>0):
        result (k+tri_recoursion(k-1))
        print(result)
    else:
        result=0
    return result
print("output")
tri_recoursion(6)

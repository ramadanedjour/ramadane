note=[8,12,15,18,6,14,11,19,13,9,16]
moyenne=sum.element/11
if moyenne>=16:
    print("mention excellent")
elif moyenne<16 and moyenne>14:
    print("mention bien")
elif moyenne<14 and moyenne>12:
    print("mention assez bien")
    break
elif moyenne<12 and moyenne>10:
    print("la mention est passable")
else:
    print("moyenne raté")

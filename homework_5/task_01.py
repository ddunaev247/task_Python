# Генератор песенки «TEN green bottles hanging on the wall»
bottles = " green bottles hanging on the wall,"
numb = ["Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
for i in range(10):
    print(numb[i] + bottles)
    print(numb[i] + bottles)
    print("And if one green bottle should accidentally fall,")
    if i != 9:
        print("There‛ll be " + numb[i + 1] + bottles)
    else:
        print("NO green bottles hanging on the wall!")

try:
    with open("exemple1_base_type.py", 'r') as file:
        for ligne in file:
            #print ligne,
            print(ligne, end='') # python 3
except IOError as e:
    print(e)
def pojedynek(value1, value2):
    ciosPostaci1 = value1.atak()
    ciosPostaci2 = value2.atak()
    print(f'{value1.__class__.__name__} uderza z siłą {ciosPostaci1}!')
    print(f'{value2.__class__.__name__} uderza z siłą {ciosPostaci2}!')
    if ciosPostaci1 > ciosPostaci2:

        print(f'{value1.__class__.__name__} wygrał pojedynek z {value2.__class__.__name__}!')
    elif ciosPostaci1 == ciosPostaci2:
        print(f'Pojedynek pomiędzy {value1.__class__.__name__} oraz {value2.__class__.__name__}'
              f' zakończył się remisem!')
    else:
        print(f'{value2.__class__.__name__} wygrał pojedynek z {value1.__class__.__name__}!')
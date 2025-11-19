'''
write a function that accepts **kwargs to print out a formatted description of a person (e.g., name,age,city).
'''

def person_info(**kwargs):
    if not kwargs:
        print("No information provided!")
        return
    
    print("Person Details:")
    print("----------------")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Example call
person_info(name="Aesha", age=20, city="Surat")

# Puja Roy
# Practice Python Test for CUNY Upskilling
# May 2, 2022

print("Question: 1")
the_intensity = 125.11  # In Python's syntax there can be no space in variables
print(the_intensity)


print("Question: 2")
x = str(int(float('2')))
print(x)

print("Question: 3")
if not 1 in [10,20] and 1 < 2:
    print(1)
else: # No indentation for else or it will cause errors in the program to execute the output.
        print(2) 

print("Question: 4")
d = {
    "food": {
        "rice":
        {
            "weight": 30.01,
            "taste": "good",
            "forms": ["boiled"]
            },
        "banana":
        {
            "weight": 19,
            "taste": "excellent",
            }
        }
    }
print(d["food"]["banana"]["taste"])

print("Question: 5")
def foo(*args):
    return len(args)
print(foo(1,2,4))

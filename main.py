# write your code here
person=[
    {
        'name':"badriya",
        'age': 21,
        'hobbies': ["sleeping", "eating", "swimming"]


    }
]
name=person[0].get('name')
print(name)

age=person[0].get('age')
print(age)

person[0]['age']= 24
print(person)

person[0]['country']= 'kuwait'
print(person)

print(len(person[0]))

person[0]['hobbies'].append("reading")
print(person)

def check_hobbies(person):
    if len(person[0]['hobbies'])>=3:
        print(f"WOW YOU ARE AMAZING")
check_hobbies(person)
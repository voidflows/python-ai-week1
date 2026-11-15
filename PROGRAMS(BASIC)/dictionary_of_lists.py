skills = {
    "Rahul" : ["Java","Python"],
    "Ganesh" : ["SpringBoot","Batch Script"]
}

print(skills["Rahul"])
print(skills["Rahul"][1])

for k,v in skills.items():
    print(k,v)

for name,topics in skills.items():
    for topic in topics:
        print(f"{name} ->>> {topic}")

for name in skills:
    print(name,skills[name])
words = ["red","blue","red","green","blue","red"]

frequency ={} # Empty dictionary not an empty set[s=set(),this is empty set]

for i in words:
    if i in frequency:
        frequency[i]+=1 # dictionaries use square brackets to access a value using a key, not an index.
    else:
        frequency[i] = 1

print(frequency)
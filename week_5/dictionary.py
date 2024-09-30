# dictionary = a collection of {key:value} pairs 
#              ordered and changeable. No duplicates

capitals = {"USA" : "Washington D.C.", 
            "India" : "New Delhi", 
            "China" : "Beijing",
            "Russia" : "Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

 # if capitals.get("Russia"):
#    print("That capital  exist")

# else:
#    print("That capital doesn't exist")

    
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# removes item
# capitals.pop("China")
# remove last item
# capitals.popitem()
# print(capitals)

# capitals.clear()
 # returns all keys and NOT values
 keys = capitals.keys()
print(keys)

for key in capitals.keys():
 print(key)

 values = capitals.values()
 print(values)
 for value in capitals.values():
  print(value)

  items = capitals.items()
  for key, value in capitals.items():
   print(f"{key}:{value}")
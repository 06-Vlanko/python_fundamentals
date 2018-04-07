def dictionaryToTuple (dictionary):
    return dictionary.items()

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
tupleList = dictionaryToTuple (my_dict)

print tupleList
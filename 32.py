'''Write a Python script to sort (ascending and descending) a dictionary by
value.'''

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("desecding List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=False)
print("ascending List: ")
print(my_list)

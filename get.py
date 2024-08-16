my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Retrieve values
name = my_dict.get('name')  # Returns 'Alice'
print(name)

# Retrieve with default value
country = my_dict.get('country', 'USA')  # Returns 'USA' (default value) because 'country' key is not present
print(country)

# Retrieve non-existent key without default value
nickname = my_dict.get('nickname',None)  # Returns None because 'nickname' key is not present
print(nickname)

# Retrieve Value only since the key  value exists in dictionary
names = my_dict.get('name','YAshwanth')  # Returns 'Alice'
print(names)
# """ In this case, the get method retrieves the value for the key 'name' from my_dict. Since the key 'name' exists, it returns 'Alice'. If the key did not exist, it would return the default value 'YAshwanth' """

inp_str = "abcdefgabc"
 
# using set() + count() to get count 
# of each element in string 
out = {x : inp_str.count(x) for x in set(inp_str )} 
 
# printing result 
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(out))
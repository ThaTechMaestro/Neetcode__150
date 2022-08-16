''''
Name: Encode and Decode Strings

Link: https://leetcode.com/problems/encode-and-decode-strings/

Input -> List containing Strings
Output -> List Containing Strings

The initial Problem/Bruteforce:
    If you use any symbol to encode a string
    What happens when that symbol becomes part of the string?


Insightful Approach/Question:

    How do I encode a list of strings without using any character?
    What other property of a string in that list can I use for encoding?

    How do I know which words are complete for decoding?

    Approach1:
        Converting each string characters to its ASCII values
            encode: 
                converting each string into its equivalent ascii
                adding a unique identifier symbol for easy decoding

            decode:
                Picking each string with the help of unique identifier symbol
                Then use a decoding logic


There is an interesting curiosity in the last comment mentioned in the behaviour:  
    https://stackoverflow.com/questions/6886544/python-how-does-split-method-work
    Understand it and explain it

    Demo:
        s = "1 2 3 4 5 6 "
        print(s.split())
        print(s.split(' '))

Look into Approach 2:
    https://leetcode.com/problems/encode-and-decode-strings/discuss/1972902/2-Different-Approaches-Simple-and-Easy

'''

#-------Approach 1
def encode(strs):
  result = []

  for string in strs:
    for c in string:
      result.append(str(ord(c)))
      result.append(';')
    result.append(' ')

  return ''.join(result)

def decode(str):
  print("Decode S")
  print(str)

  result = str.split()
  print(result)
  chra = ""
  decode_list = []
  #return result


  for string in result:
    print(string)
    print(string.split(";"))
    for c in string.split(";"):
      if c:
        chra += chr(int(c))
        
    decode_list.append(chra)
    chra = ""

  print(decode_list)

  return decode_list

test = '72;101;108;108;111;'

print(test.split(";"))


answer = encode(["Hello","World", ";;;;"])
print(answer)

decoded = decode(answer)
print(decoded)

print(chr(int("7")))

"""
The idea of this solution is the use of a dictionary as hash table
Using the difference between the number and each element of the list we can
find the number which sum is num througth only an aditional iteration in the list
We can asumme that the construction of the dictionary has a complexity of O(n) 
And the searching into the elements has at most O(n/c) complexity
this solution has complexity of Ω(n) and under of O(n^2)
"""
import sys

def find_sum_pairs(lst,num):
  output = {}
  #O(n) length of the list
  for li in lst:
    diff = num - li
    if output.get(diff)==None:
      output[diff] = [li]
    else:
      output[diff].append(li)     
  #O(n)
  for li in lst:
    if output.get(li)!=None:
      value = output[li]
      if value[0]>li:
        value.append(li)
  return output

def sum_pairs(lst,num):
  message = ""
  find_pairs = find_sum_pairs(lst,num)
  for v in find_pairs.values():
    #Usually v is length 2, but sometimes there are more than 2 numbers that sum is num with the same difference
    if len(v)>=2:
      for i in range(0,len(v)):
        for j in range(i+1,len(v)):
          vi,vj = v[i],v[j]
          if vi+vj == num:
            message+="+ "+str(vi)+","+str(vj)+"\n"
  return message


#Testing area:
def test_sum_tuple():
  assert sum_pairs([1,9,5,0,20,-4,12,16,7],12).split() == ['+', '12,0', '+', '16,-4', '+', '7,5'], "Incorrect test #1"
  assert sum_pairs([1,9,5,0,20,-4,12,16,7,-4,6,6,6],12).split() == ['+', '12,0', '+', '16,-4', '+', '16,-4', '+', '7,5', '+', '6,6', '+', '6,6', '+', '6,6'], "Incorrect test #2"
  print("Testing app: Everything is passed")

if __name__ == "__main__":
  test_sum_tuple()
  args = sys.argv[1:]
  if(len(args))>1:
    lst = list(map(lambda x:int(x),args[0].split(",")))
    num = int(args[1])
    print(sum_pairs(lst,num))
  else:
    print("Bad use of the application")
    print("You need to call this file as follows:")
    print("python app.py <list> <number>")
    print("for example:")
    print("python app.py 1,2,3,4,5 12")


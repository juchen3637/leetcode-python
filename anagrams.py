#This is my original solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        print(s)
        if len(s) != len(t):
            return 0
        else:
            for i in range(len(s)):
                list1.append(s[i])
            list1.sort()
            for n in range(len(t)):
                list2.append(t[n])
            list2.sort()
            if list1 == list2:
                return 1
            else:
                return 0
            
#This looks like my solution but better, same idea but the built in sorted() function is able to sort the string first then compare
#them, my solution used the .sort() function for lists which needed me to add each individual character to a list first which is slower
#than just sorting the string itself
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return 1
        else:
            return 0
            
#Counting solution, fastest and optimal solution, it counts the number of times each character appears in each string by using 2 hashmaps/dictionaries,
#then compares the 2 hashmaps


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap_1 = {}
        hashmap_2 = {}

        if len(s) != len(t):
            return 0
        else:
            for i in range(len(s)):
                hashmap_1[s[i]] = 1 + hashmap_1.get(s[i], 0) #.get() returns the value of the key, if the key doesn't exist it returns 0, this also adds 1 to the value of the key
                hashmap_2[t[i]] = 1 + hashmap_2.get(t[i], 0)
            if hashmap_1 == hashmap_2:
                return 1
            else:
                return 0


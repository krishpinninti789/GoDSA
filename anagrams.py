from collections import defaultdict
def groupAnagrams(self, strs):
    """
     :type strs: List[str]
    :rtype: List[List[str]]
    """
    # Counter(i)
    #  { { e:1,a:1,t:1}:[tea,ate,eat],{t:1,a:1,n:1}:[tan,nat],{b:1,a:1,t:1}:[bat]}
    
    my_dict = defaultdict(list)
    for word in strs:
        # my_dict[tuple(Counter(word))].append(word)
        char_dict = [0]*26
        for char in word:
            char_dict[ord(char)-ord('a')] +=1
        my_dict[tuple(char_dict)].append(word)
    return list(my_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

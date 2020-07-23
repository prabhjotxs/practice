def longestPreSuf(s, l):
  left = 0
  rght = l-1
  nrght = l-1
  common = 0
  maxcommon = 0
  print(l)
  while rght >= 1:
    if rght < l and s[left] == s[rght]:
      common += 1
      rght += 1
      left += 1
    else:
      if common > maxcommon:
        maxcommon = common
        common = 0
      rght = nrght - 1
      nrght = rght
      left = 0
  print(maxcommon)

string = "abcdef"
length = len(string)
print(length)
longestPreSuf(string, length)

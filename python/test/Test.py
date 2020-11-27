import re
str =  'UMEPLAY逃脱<e class="address">\uf3e5</e><e class="address">\uf1b9</e>(徐<e class="address">\uf136</e><e class="address">\uee0a</e>) '
pattern = re.compile('.*?<e class="address">(.*?)</e>.*?', re.S)
arr = re.findall(pattern, str)
print(arr)
arr1 = ['unif3e5']
a = arr1[0].replace('uni', r'\u')
arr1.append(a)
print(len(arr[1]))
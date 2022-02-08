import re

reg1 = "{id}"
reg2 = "{id"
reg3 = "id}"
reg4 = "/test/{id}"
reg5 = "/test/{id}/{name}"


regex1 = "[{]"
regex2 = "[}]"
regex3 = "[{...}]"
regex4 = "[{][...][]}]"
regex5 = "{.*}"

regex = regex5

# print(re.match(regex, reg1))
# print(re.match(regex, reg2))
# print(re.match(regex, reg3))
# print(re.match(regex, reg4))
print(re.match(regex, reg4))


# print(re.search(regex, reg4).group(0))

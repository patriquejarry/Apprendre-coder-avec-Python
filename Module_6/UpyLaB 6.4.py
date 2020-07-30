def substitue(message, abreviation):

    for a in abreviation:
        message = message.replace(a, abreviation[a])
    return message

print(substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck', 'N.' : 'Norris', 'cpt' : 'counted', '2' : 'two times', 'inf' : 'infinity'}))
# 'Chuck Norris counted two times to infinity'

print(substitue('C. N. cpt 2 to inf', {'C.': 'Chuck', 'cpt': 'counted', 'N.': 'Norris', '2': '2 times', 'inf': 'infinity'}))
# 'Chuck Norris counted 2 times to infinity'
print(substitue('viva C. N. : C. N. cpt 2 to inf and even further', {'C.': 'Chuck', 'cpt': 'counted', 'N.': 'Norris', '2': '2 times', 'inf': 'infinity'}))
# 'viva Chuck Norris : Chuck Norris counted 2 times to infinity and even further'
print(substitue('A A A A is it good', {'inf': 'infinity', 'cpt': 'counted', 'N.': 'Norris', '2': '2 times', 'A': 'Ha'}))
# 'Ha Ha Ha Ha is it good'
print(substitue('mm les c', {'mm': 'messieurs', 'c': 'commissaires'}))
# 'messieurs les commissaires'

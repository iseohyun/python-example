'''
	 print Format
'''

print("{: >10}".format("*"))
print("{: >10}".format("**"))
print("{: >10}".format("***"))
print("{: >10}".format(500))
print("{: >+10}".format(500))
print("{: >+10}".format(-500))
print("{:_>+10}".format(-500))
print("{:,}".format(1234567890))
print("{:+,}".format(1234567890))
print("{:^<+30,}".format(1234567890))

print("{:f}".format(5/7))
print("{:.2f}".format(5/7))
print("{:.19f}".format(5/7))
print("{:*>+10.3f}".format(5/7))
# extract emails from given string
import re
s = """Hello from shubhamg199630@gmail.com
        to priya@yahoo.com about the meeting @2PM"""
output = re.findall("\S+@\S+", s)
print(output)



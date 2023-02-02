file = open("include.py", 'a+')
file.write("def test_for_bug1(version):\n    if version == 2.6 or version == 2.7:\n        print(\"This version: {} has the bug.\".format(version))\n        return True\n    else:\n        print(\"This version: {} does not have the bug.\".format(version))\n        return False\n\ndef test_for_bug2(version):\n    if version == 2.7 or version == 2.6 or version == 2.5:\n        print(\"This version: {} has the bug.\".format(version))\n        return True\n    else:\n        print(\"This version: {} does not have the bug.\".format(version))\n        return False\n\ndef test_for_bug3(version):\n    if version == 2.7 or version == 2.6 or version == 2.5 or version == 2.4 or version == 2.3 or version == 2.2:\n        print(\"This version: {} has the bug.\".format(version))\n        return True\n    else:\n        print(\"This version: {} does not have the bug.\".format(version))\n        return False\n\ndef test_for_bug4(version):\n    if version == 2.7 or version == 2.6 or version == 2.5 or version == 2.4 or version == 2.3 or version == 2.2 or version == 2.1:\n        print(\"This version: {} has the bug.\".format(version))\n        return True\n    else:\n        print(\"This version: {} does not have the bug.\".format(version))\n        return False\n\n")
file.close()

from include import *

# We have a list of firmware versions. A bug was introduced in some version, but we don't which version. We have the list of firmware versions in the order they were created. Your goal is to find the firmware version that first introduced a bug.

# Firmware list:
# 2.7: Known to contain the bug
# 2.6
# 2.5
# 2.4
# 2.3
# 2.2
# 2.1
# 2.0: Known not to contain the bug


# You have the method below to that returns whether or not a firmware version contains a bug regression

# test_for_bugX(firmware_version) where X can be {1,2,3,4} - tests if firmware_version contains a bug.
#    firmware: versions are: 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7
# Returns: true if firmware contains bug, else false.

firmware_versions = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7]

def find_bug(versions):
    min = []
    for version in versions:
        if test_for_bug1(version) == True:
            min.append(version)
            break
        if test_for_bug2(version) == True:
            min.append(version)
            break
        if test_for_bug3(version) == True:
            min.append(version)
            break
        if test_for_bug4(version) == True:
            min.append(version)
            break
    #min.sort()
    print(min)


#check if mid has bug
#if yes stop would be mid & start is 0
#go on till bug is found
#else
#if no start would be mid+1

find_bug(firmware_versions)
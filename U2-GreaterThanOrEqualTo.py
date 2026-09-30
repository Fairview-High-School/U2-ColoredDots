def greaterThanOrEqualTo(a, b):
     if a > b:
          return True
     else:
          if a == b:
               return True
          else:
               return False

# def greaterThanOrEqualTo(a, b):
#      if a > b:
#           return True
#      else:
#           return a == b

# def greaterThanOrEqualTo(a, b):
#      return not(a < b)

# def greaterThanOrEqualTo(a, b):
#      return a > b or a == b


#Main Script to test
#Uncomment out the version of greaterThanOrEqualTo(a,b) that you want to test.
#Then test this script
#Make sure only 1 version is un-commented at a time.

print("3 is greater than or equal to 4", greaterThanOrEqualTo(3,4))
print("3 is greater than or equal to 3", greaterThanOrEqualTo(3,3))
print("4 is greater than or equal to 3", greaterThanOrEqualTo(4,3))
print("4 is greater than or equal to 4", greaterThanOrEqualTo(4,4))

print("Should be False, True, True, True")
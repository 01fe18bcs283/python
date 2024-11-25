try: 
    print("statement-1") 
    #print("statement-2") 
    print(10/0) 
    print("statement-3") 
    
except : 
    print(10/0) 
    #print("statement-4") 
    
print("statement-5")


# Case1: if there is no exception then 1,2,3,5 and it is normal termination.
# Case2: if there is an exception at statement-2 then 1, 4, 5 and it is normal termination.
# Case3: if there is an exception at statement-2 but corresponding except block is not matched then 1, and it is abnormal termination.
# Case4: if there is an exception at statement-4 then it is always abnormal termination.
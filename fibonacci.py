# Software Maintenance
# Week 1 Assignment 1a
# Daniel Linna
# 0509355
# 19.1.2020
########################################################################################

def fib(length, startpoint):
    try:
        value1 = value2 = int(startpoint)
    except (ValueError):
        print("Incorrect startpoint.")
        return -1

    try:
        length = int(length)
    except (ValueError):
        length = 10
    
    

    # Opening file
    try:
        t1 = open("result.txt", "w", encoding="UTF-8")

        # Loop to calculate the Fibonacci sequence, using length and startingpoint inputs
        for i in range(1,length+1):
            sum = value1 + value2
            value1 = value2
            value2 = sum
            # Write result to file
            t1.write(str(sum)+"\n")
            
        # After loop, close file
        t1.close()
        
    except (IOError, FileNotFoundError):
        print("Something went wrong.")
        return -1

# Successful return
    return 0


######################################### EOF #########################################

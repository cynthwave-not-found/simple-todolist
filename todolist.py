work = [""]

def addtask(task, work):
    work.append(task)
    print("Successfully added task " + str(task) + " in to-do list!")
    addnewline()
    return work;

def reptask(work):
    try: 
        taskno = int(input("Replace task number "))
        if (taskno-1 <= len(work)):
            repinp = str(input("Which is the task " + str(work[taskno-1]) + ", with task "))
        else: 
            err()
        work[taskno-1] = repinp; 
        print("Successfully replaced task " + str(taskno) + " of to-do list with " + str(repinp))
    except ValueError: 
        print("Error: please enter a valid number")
    except IndexError: 
        print("Error: please enter a valid index")
    except: 
        generr()
    finally: 
        addnewline()

        

def deltask(taskno, work):
    try: 
        work.pop(taskno-1)
        print("Successfully deleted task " + str(taskno) + " of to-do list!")
    except ValueError: 
        print("Error: please enter a valid number")
    except IndexError: 
        print("Error: please enter a valid index")
    except: 
        generr()
    finally: 
        addnewline()

def viewtask(work): 
    print("")
    print("----------To-do list-----------")
    if len(work) != 0: 
        for x in range(len(work)): 
            print(str(x+1) + "  " + str(work[x]))
    else: 
        print("     To-do list empty!     ")
    addnewline();

def addnewline(): 
    print("--------------------------------")
    
def generr():
    iserr = 1; 
    print("Something went wrong, rebooting...")

iserr = 0; 
work.clear()
inp = 1
repinp = 0
print("-----To-do List Application-----")


while (inp != 0) and (iserr == 0): 
    print(" 1  Add item")
    print(" 2  Replace item")
    print(" 3  Delete item")
    print(" 4  View to-do list")
    print(" 0  Exit program")

    inp = int(input("Run program "))
    if (inp == 1): 
        addnewline()
        inp = str(input("Add task "))
        addtask(inp, work)
    elif (inp == 2): 
        addnewline()
        reptask(work)
    elif (inp == 3): 
        addnewline()
        inp = int(input("Delete task number "))
        deltask(inp, work)
    elif (inp == 4): 
        viewtask(work)
    elif (inp == 0):
        print("Exiting program...")
    else: 
        generr()
       
viewtask(work); 

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20220177 (w1953141)
 
# Date: 13/12/2022




progress=0
trailer=0
retriever=0
exclude=0
total=0

list_main=[]
marks_dict={}

def histogram():                                                 
    print('_'*50)
    print()
    print('Histogram')
    print('Progress  ',progress,':',progress * '*')
    print('Trailer   ',trailer, ':',trailer *'*' )
    print('Retriever ',retriever,':',retriever *'*' )
    print('Exclude   ',exclude, ':',exclude *'*' )
    print()
    print(total,'Outcomes in total')
    print('_'*50)
    
    


while True:
    
    try:

        uow_id=input('please enter your University of Westminster ID :')
        print()
        pass_credits=int(input("Enter your total PASS credits:"))

        while pass_credits not in range(0,121,20):
            print("Out of range,Please enter again")
            pass_credits=int(input("Enter your total PASS credits:"))

        else:
            defer_credits=int(input("Enter your total DEFER credits:"))

            while defer_credits not in range(0,121,20):
                print("Out of range,Please enter again")
                defer_credits=int(input("Enter your total DEFER credits:"))

            else:
                fail_credits=int(input("Enter your total FAIL credits:"))

                while fail_credits not in range(0,121,20):
                    print("Out of range,Please enter again")
                    fail_credits=int(input("Enter your total FAIL credits:"))
                tot_1=pass_credits + defer_credits + fail_credits

                if tot_1==120:
                    if pass_credits==120:
                      output_result="Progress"
                      print(output_result)
                      list_main.append(['Progress',pass_credits,defer_credits,fail_credits])
                      progress +=1
                      total +=1

                    elif pass_credits==100:
                        output_result="Progress (module trailer)"
                        print(output_result)
                        list_main.append(['Progress (module trailer)',pass_credits,defer_credits,fail_credits])
                        trailer+=1
                        total+=1

                    elif pass_credits<=80 and fail_credits<=60:
                        output_result="Do not progress – module retriever"
                        print(output_result)
                        list_main.append(['Module retriever',pass_credits,defer_credits,fail_credits])
                        retriever+=1
                        total+=1

                    elif pass_credits<=40 and defer_credits<=40 and fail_credits>=80:
                        output_result="Exclude"
                        print(output_result)
                        list_main.append(['Exclude',pass_credits,defer_credits,fail_credits])
                        exclude+=1
                        total+=1

                    print()
                    selection=input("Would you like to enter another set of data?\n Enter 'y' for yes or 'q' to quit and view results:")
                    print()
                    selection1=selection.lower()

                    str_marks=','.join((str(pass_credits),str(defer_credits),str(fail_credits)))   # I took join() method from https://www.w3schools.com/python/ref_string_join.asp
                    single_value=output_result+'-'+ str_marks
                    marks_dict[uow_id]=single_value

                    if selection1=='q':
                        histogram()               # calling the function
                        
                        break
                    
                    elif selection1=='y':
                        continue
                    
                    else:
                        print("Invalid selection")
                
                else:
                     print("Total incorrect")

    except ValueError:
        print("Integer required")



#Part 2 – List (extension)

print()
print('Part 2:\n')
for i in list_main:
    print(f'{i[0]} - {i[1]}, {i[2]}, {i[3]}')


    
    
#Part 3 - Text File (extension)

text_file = open("progression.txt","w")

text_file.write('Part 3: \n')

for c in list_main:
    text_file.write(f'{c[0]} - {c[1]}, {c[2]}, {c[3]} \n')
    
text_file.close()
print()

f = open("progression.txt","r")    #reading the text file

progression_data = f.read()
print(progression_data)

f.close()




#Part 4 – Dictionary (separate program) 

print("Part 4:\n")
for key,value in marks_dict.items():
    
    print(key,':',value,end=" ")













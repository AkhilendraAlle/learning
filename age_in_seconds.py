'''def age_in_seconds():
    age = input("Enter you age : ")
    age_in_seconds = int(age)*365*24*60*60
    print ("According to your age you have lived for {} seconds.".format(age_in_seconds))
    
age_in_seconds()    
exit()'''
def age_in():
    
   verify = input("Specify seconds (s) or years (y): ")
   print verify

   if str(verify) == "s":
       seconds = input("Enter the seconds: ")
       years = int(seconds)/60/60/24/365
       print("According to {} seconds you have completed {} years".format(seconds,years))
   elif str(verify) == "y":
        years = input ("Enter the years")
        seconds = int(years)*365*24*60*60
        print("According to {} years you have completed {} seconds".format(years,seconds))
   else: print("Kindly enter the vaid option as ""s"" for seconds or ""y"" for years ")
         
age_in()

     

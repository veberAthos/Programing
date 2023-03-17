#---------------------------------#
#           IF STATEMENT          #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/14/2023

# Building the following code:

# Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in.
# If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, 
# otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”.

itsRaining = input("Is it raining?: ").lower()


if itsRaining == "yes":
    itsWindy = input("Is it windy?: ").lower()
    if itsWindy == "yes":
        print("It is to windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
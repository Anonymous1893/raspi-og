print("Hello, my name is Eliza. What would you like to talk about?")
probe = input()
i = 0
youme = ""
while probe.count("go away") == 0:
    probe = probe.lower()
    probe = probe.strip(".")
    probe = probe.strip("?")
    if probe.count("feel") >= 1:
        print("Do you often feel that way?")
    elif probe.count("i am") == 1:
        probe = probe.split(" ")
        while len(probe) >= (i-1):
            if probe[i] == "am":
                print("How long have you been", probe[i+1]+"?")
                break
            i = i+1
        i = 0
    elif probe.count("you") and probe.count("me") == 1:
        probe = probe.split(" ")
        while len(probe) >= (i+1):
            if probe[i] == "you":
                i = i+1
                while probe[i] != "me":
                    youme = youme+ str(probe[i])+ " "
                    i = i+1
            i = i+1
        youme = youme.strip(" ")
        print("What makes you think I", youme,"you?")
    else:
        print("Please go on")
    probe = input()
    youme=""
print("I hope I have helped you!")

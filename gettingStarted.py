def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No"
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No"
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No"
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - "
        answer = "7d55c59a938072c4182c3730c597b9aa3b720c2469eb34f9c7ad1b6bc22df09c"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No"
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
        answer = "4"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
        answer = "2"
    else: 
            ### you should understand why this else case should be included
            ### what happens if there is a typo in one of the questions?
            ### maybe put something here to flag an issue and catch errors
            answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
        return(answer)
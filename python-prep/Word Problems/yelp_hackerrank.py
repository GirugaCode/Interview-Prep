# <-- EXPAND to see the data classes
import fileinput


class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id


"""
    Sample Input:
        biz_owner_id: 42
        all_messages: [
            {"sender": 1,  "recipient": 42, "conversation_id": 1},
            {"sender": 42, "recipient": 1,  "conversation_id": 1},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 3,  "recipient": 88, "conversation_id": 3},
            {"sender": 3,  "recipient": 42, "conversation_id": 4},
        ]

    Sample Output:
        33 (Business owner 42 received three conversations total (1, 2, and 4), but only
        responded to one conversation (conversation ID 1)).

    How is the sample output created:
        Number of conversations where the business owner wrote back = 1
        Number of total conversations = 3
        *
        100
        is equal to 33(rounded)
        
    Assumptions / Questions:
    - Can you calarify what the three total conversations in the example above would be?
        - I'm assuming its only three conversations because of the unique ids with "42" as the recipient
    - If the messages are empty we would return a response rate of 0
    
    Pseudocode:
    Find the # of conversations where the owner wrote back
        - If the sender value of biz_owner_id has a recipient value of the same
        - Then we know the owner wrote back
        - Increment a count
    
    Find Number of total conversations
        - Find the number of unique conversation_ids that has the biz_owner_id
        - If the recipient is the biz_owner_id
            - Add that conversation_id into a set
        - Then we increment a count depending on how many are in the set
    
    Find the total using formula
        (# of conversations where the owner wrote back) / (# of total conversations) * 100
    
    Return that total

"""
def business_responsiveness_rate(biz_owner_id, all_messages):
    num_owner_reply = 0
    convo_set = set()
    res_rate = 0

    for message in all_messages:
        if message.sender == biz_owner_id:
            num_owner_reply += 1
        
        if message.recipient == biz_owner_id:
            convo_set.add(message.conversation_id)

    res_rate = (num_owner_reply // len(convo_set)) * 100

    return res_rate


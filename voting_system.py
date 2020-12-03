

canditate_1 = input("Enter the candidate 1 name: ")
canditate_2 = input("Enter the candidate 2 name: ")

canditate_1_votes = 0
canditate_2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter = len(voter_id)

while True:

    if voter_id == []:
        print("Voting session over!!!")
        if canditate_1_votes > canditate_2_votes:
            percent = (canditate_1_votes/num_of_voter)*100
            print(canditate_1, "has won","with",percent,"%votes.")
            break
                        
        elif canditate_2_votes > canditate_1_votes:
            percent = (canditate_2_votes / num_of_voter)*100
            print(canditate_2, "has won","with",percent, "% votes.")
            break

    else:
        voter = int(input("Enter your Voter ID number: "))
        if voter in voter_id:
            print("You are a Valid Voter!!")
            voter_id.remove(voter)
            vote = int(input("Enter your vote 1 or 2: "))
            if vote == 1:
                canditate_1_votes+=1
                print("Thank you for casting your vote!!")

            elif vote == 2:
                canditate_2_votes+=1
                print("Thank you for casting your vote!!")

        else:
            print("You are not Elligible to vote or You have already voted!!")
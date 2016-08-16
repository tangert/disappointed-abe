

# have base response, header and footer
# have an array of all possible responses
# after each response to a new tweet, add a tweet to the array 
# cycle through the response array ?

#Want Disappointed Abe to tweet YOUR thoughts at Trump? Tweet with #DisappointedAbe and see your fame rise. 

if __name__ == '__main__':
	
	header = "Dear Mr. Trump,"
	footer = "Sincerely, a Dissapointed Abe Lincoln."
	
	responses = [
	"I died for THIS?!",
	"If I was alive today, I would shoot myself just because of you.",
	]


	# random generator 
	#create responses here. 
	for i in range(0, responses.__len__()):
		response = header + "\n" + responses[i] + "\n" + footer
		print "\n" + response
		print "\n Character count: " + str(len(response))
	
	

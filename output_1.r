#PayMo data coding challenge using R using the first type of constraint
#If two users have never sent or requested a payment to the other, then classify 
#the payment/request as unverfied

#Change directory to where the data is
setwd("/Users/glori/Documents/GitHub/digital-wallet/paymo_input")

#Import the batch payment data into R--this is the past data that we want to determine
#if there has been past payments
full_batch_data<-read.table("batch_payment.csv",header=TRUE,sep=",",fill=TRUE)

#First we want to find a unique list of the users (in either the id1 column or the id2 column)
#Using nice R functions
#First find the unique list of the id1's
unique_id1<-unique(full_batch_data$id1)
#Second find the unique list of the id2's
unique_id2<-unique(full_batch_data$id2)
#Then append the unique lists and find the unique ones from there
all_ids<-unique(as.numeric(c(unique_id1,unique_id2)))

#Want to create a dictionary using half of the ids as the key with the vector
#of the ids that they've ever had a payment with (received or paid) as the value
num_keys<-ceiling(length(all_ids)/2)

#Initialize the dictionary with the keys that we want (only half of the unique ids)
id_dictionary<-vector(mode="list",length=num_keys)
names(id_dictionary)<-all_ids[1:num_keys]

#iterate through the ids and add values to the vector of that id's "friends"
for (i in 1:num_keys){
	#Initialize the vector of friends ids
	temp_list_friends<-c()
	
	#For readability, define a new variable for the id who we want to add to the dictionary
	id_to_add<-all_ids[i]
	
	#Find all occurrences where the id is in the id1 column
	#Remember there could be zero rows if the person was also in the id2 column
	temp_list_friends<-append(temp_list_friends,full_batch_data[as.numeric(full_batch_data$id1)==all_ids[i],]$id2)
	
	#Find all occurrences where the id is in the id2 column
	
	
}

#Import the stream payment data into R for testing
full_stream_data<-read.table("stream_payment.csv",header=TRUE,sep=",",fill=TRUE)
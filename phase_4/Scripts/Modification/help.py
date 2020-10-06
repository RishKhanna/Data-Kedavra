temp1=[
"Creating an Issue",
"Adding Tags to Article",
"Adding Categories to the Article",
"Adding Tags to the Article",
"Add a Member",
"Add a Subscriber",
"Add a Sponsor"
]

temp2 = [
"Modify the contents of the Article",
"Change the issue of an Article",
"Change the tags in an Article",
"Change the categories in an Article",
"Modify Member details",
"Modify Subscriber details"
]

temp3 = [
"Remove a Member",
"Delete an Article",
"Unsubscribe",
"Remove a Sponsor"
]

for i in temp3 :
	i = "_".join(i.split())
	print("def", i.lower(),"() :")
	print("\tpass\n")

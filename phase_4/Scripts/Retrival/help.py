temp=["List_all_Issues",
"List_all_Articles",
"List_all_Authors",
"Articles_from_a_particular_Magazine_Issue",
"List_of_all_Articles_written_by_an_Author",
"List_all_Editors",
"List_of_all_Articles_edited_by_an_Editor",
"List_all_Designers",
"List_of_all_Articles_designed_by_a_Designer",
"Show_Cartoons_by_Designer",
"Show_Cartoons_from_a_particular_Issue",
"Show_Cartoons_from_a_particular_Volume",
"Subscribers_for_a_given_Volume",
"Subscribers_for_a_given_Issue"]

temp2=[
"Issues_in_a_Volume",
"Articles_with_a_particular_category",
"Sort_Articles_by_name",
"Show_Cartoons_with_a_particular_Tag",
"Subscribers_with_a_particular_subscription_type",
]

temp3=[
"Average_number_of_subscribers_for_a_Volume",
"Total_number_of_articles_in_a_Volume",
"Subscription_Change_between_two_given_dates"
]

temp4=[
"Search_Articles_by_name",
"Search_Members_by_name"
]

temp5=[
"Most_frequent_category_of_Articles_written_by_each_Author",
"List_of_subscribers_who_subscribed_between_two_consecutive_Volumes"
]

# for i in temp5:
# 	print("def",i.lower(),"():")
# 	print("    pass")
# 	print("\n")

for i in range(len(temp5)):
	print("elif ch2==",i+1,":")
	print("\tanalysis." + temp5[i].lower() + "()" )
	print("")

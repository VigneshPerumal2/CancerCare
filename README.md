# CancerCare

Teammates:  Amulya Murahari (murahari.a)
            Vignesh Perumal Samy (perumalsamy.v)
            Sunayana Shivanagi   (shivanagi.s)

Repository Link : https://github.com/VigneshPerumal2/CancerCare.git


Cancer is a disease of the genome, caused by genetic variations in genes. These mutations impact the processes that regulate how cells interact with their environment and grow.

The goal of this project is to develop a database tool that will allow us to examine patient information and get insightful knowledge about how frequently cancer occurs. Twitter database schema is also included in the cancer care system. The data is based on assessing the changing gene conditions in patients over time and will then be used to determine which type of treatment is most likely to save the patient because genes play a vital part in cancer detection.


Explanation on some of the design decisions:

•	The user table contains the details of the user such as the User_Name, Handle_Name, Description and other details of the User. Here, the User_Id is unique and hence it is a Primary Key.Each user is allowed an unlimited number of tweets. The details of the tweets are stored on the table.

•	A user can tweet about the condition of cancer or any related issues about cancer, in the hope of any help or medical assistance required from his end. Based on the hashtags, the tweet mentions and Url, the user can get potential help.

•	The ‘Tweets’ table has ‘Tweet_Id’ as its primary key which uniquely distinguishes the Tweet made by the User. The ‘Location’ table contains the ‘Location_Id’ as the primary key, giving us the location from where the User has posted the tweet.

•	‘Hashtag’, Tweet_Mention’, ‘Tweet_Url’ are the tables related to the tweets of the User, wherein Hashtag_Id, Mention_Id, Url_Id are the primary keys respectively. 

•	The User can tweet as many tweets as possible about Cancer, through which the treatment and the cancer type can be identified. This information is helpful as it gives us insights into the exact condition or situation of the User.

![image](https://user-images.githubusercontent.com/34863107/201505783-693d0562-5e2f-43f6-9ddd-f8e069bed37a.png)

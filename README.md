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

# Conceptual Diagram 

![image](https://user-images.githubusercontent.com/34863107/201505851-2fb48c5e-7df6-449e-8868-0953eb708829.png)

# UML Diagram

![image](https://user-images.githubusercontent.com/34863107/201505875-25483ff9-1fd1-4dab-bc9c-67374f7b4546.png)


# ERD Diagram

![image](https://user-images.githubusercontent.com/34863107/201505890-7e78f097-2b87-4736-900f-964647ceb9a1.png)

# Conceptual Diagram Queries:

Create table for USER –

CREATE TABLE IF NOT EXISTS USER
         (
         User_Id INTEGER PRIMARY KEY AUTOINCREMENT,
         User_Name     TEXT   NOT NULL,
         Handle_Name   TEXT   NOT NULL,
         Description   TEXT   NOT NULL,
         Followers_Count     INTEGER,
         Created_Date   TEXT  NOT NULL,
         Image_Url      TEXT  NOT NULL,
         Smoker      TEXT  NOT NULL,
         hasCancer      TEXT  NOT NULL,
         Cancer_Type      TEXT  NOT NULL
         );

Create table for CANCER_TYPE –

CREATE TABLE IF NOT EXISTS CANCER_TYPE
         (Hashtag_Id INTEGER NOT NULL,
         Cancer_Id INTEGER PRIMARY KEY AUTOINCREMENT,
         Cancer_Type      TEXT  NOT NULL,
         FOREIGN KEY(Hashtag_Id) REFERENCES HASHTAG(Hashtag_Id));


Create table for TREATMENT –

CREATE TABLE IF NOT EXISTS TREATMENT
         (Cancer_Id INTEGER NOT NULL,
          Treatment_Id INTEGER PRIMARY KEY AUTOINCREMENT,
          Treatment_Type      TEXT  NOT NULL,
          FOREIGN KEY(Cancer_Id) REFERENCES CANCER_TYPE(Cancer_Id));


Create table for LOCATION – 

CREATE TABLE IF NOT EXISTS LOCATION
         (User_Id INTEGER NOT NULL ,
          Location_Id INTEGER PRIMARY KEY AUTOINCREMENT,
          Location    TEXT  ,
          FOREIGN KEY(User_Id) REFERENCES USER(User_Id) );

Create table for TWEETS – 

CREATE TABLE IF NOT EXISTS TWEETS
         (Tweet_Id INTEGER PRIMARY KEY NOT NULL,
          Tweet_Handle TEXT NOT NULL,
          Tweet_Text TEXT NOT NULL,
          Posted_At TEXT,
          Alert TEXT,
          User_Id INTEGER NOT NULL,
          FOREIGN KEY(User_Id) REFERENCES USER(User_Id));



Create table for HASHTAG – 

CREATE TABLE IF NOT EXISTS HASHTAG
         (Hashtag_Id INTEGER PRIMARY KEY NOT NULL,
          Hashtag_Text TEXT NOT NULL,
          Tweet_Id  INTEGER NOT NULL,
          FOREIGN KEY(Tweet_Id) REFERENCES TWEETS(Tweet_Id));



Create table for TWEET_MENTION – 

CREATE TABLE IF NOT EXISTS TWEET_MENTION
         (Mention_Id INTEGER PRIMARY KEY NOT NULL,
          Source_User TEXT NOT NULL,
          Target_User TEXT NOT NULL,
          Tweet_Id  INTEGER NOT NULL,
          FOREIGN KEY(Tweet_Id) REFERENCES TWEETS(Tweet_Id));


Create table for TWEET_URL – 

CREATE TABLE IF NOT EXISTS TWEET_URL
         (Url_Id INTEGER PRIMARY KEY NOT NULL,
          Tweet_Url TEXT NOT NULL,
          Tweet_Id  INTEGER NOT NULL,
          FOREIGN KEY(Tweet_Id) REFERENCES TWEETS(Tweet_Id));

  # USE-CASE

1) Use Case: Most popular Cancer_Type Tweets
Description: The most popular cancer type tweets
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT cancer_type, COUNT (hashtag_id)FROM cancer_type 
GROUP BY cancer_type 
ORDER BY COUNT (hashtag_id)DESC;

Relational Algebra: 
τ COUNT (hashtag_id) ↓
  γ cancer_type, COUNT (hashtag_id) cancer_type

<img width="476" alt="image" src="https://user-images.githubusercontent.com/34863107/201505971-6d97f2ed-9fd2-4f17-820e-9cead5e7cc81.png">

 
2) Use Case: Most popular Treatment_Type Tweets
Description: The most popular treatment type tweets
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT treatment_type, COUNT (treatment_id)
FROM treatment GROUP BY treatment_type 
ORDER BY COUNT (treatment_id)DESC;

Relational Algebra: 
τ COUNT (treatment_id) ↓
  γ treatment_type, COUNT (treatment_id) treatment

<img width="469" alt="image" src="https://user-images.githubusercontent.com/34863107/201505985-358d18d9-1970-4043-a937-9997992050e6.png">

3) Use Case: Most popular Location for cancer tweets
Description: The most popular location for cancer tweets
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT location, COUNT (location_id)FROM location 
GROUP BY location 
ORDER BY COUNT (location_id)DESC;

Relational Algebra: 
τ COUNT (location_id) ↓
  γ location, COUNT (location_id) location

<img width="474" alt="image" src="https://user-images.githubusercontent.com/34863107/201506011-efdef150-c42e-40d0-9463-5889e860f28d.png">

4) Use Case: No. of tweets made on Lung Cancer Type
Description: The number of tweets made on Lung Cancer Type
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT COUNT (t . tweet_id)
FROM tweets AS t, hashtag AS h, cancer_type AS c 
WHERE t . tweet_id = h . tweet_id 
AND h . hashtag_id = c . hashtag_id 
AND c . cancer_type = 'lungcancer';

Relational Algebra: 
π COUNT (tweet_id)
  γ COUNT (tweet_id)
   σ t . tweet_id = h . tweet_id AND h . hashtag_id = c . hashtag_id AND c . cancer_type = "lung cancer"
    (ρ t tweets ×
     ρ h hashtag ×
      ρ c cancer_type)

<img width="477" alt="image" src="https://user-images.githubusercontent.com/34863107/201506028-42636fb8-17c5-480b-84b1-264b3021959f.png">

5) Use Case: No. of tweets made on Breast Cancer Type
Description: The number of tweets made on Breast Cancer Type
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT COUNT (t . tweet_id)
FROM tweets AS t, hashtag AS h, cancer_type AS c 
WHERE t . tweet_id = h . tweet_id 
AND h . hashtag_id = c . hashtag_id 
AND c . cancer_type = 'breastcancer'

Relational Algebra: 
π COUNT (tweet_id)
  γ COUNT (tweet_id)
   σ t . tweet_id = h . tweet_id AND h . hashtag_id = c . hashtag_id AND c . cancer_type = "breast cancer"
    (ρ t tweets ×
     ρ h hashtag ×
      ρ c cancer_type)
<img width="482" alt="image" src="https://user-images.githubusercontent.com/34863107/201506042-f1693729-8e4f-43fc-b5d9-43ad258a270f.png">

6) Use Case: No. of tweets made on Kidney Cancer Type
Description: The number of tweets made on Kidney Cancer Type
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT COUNT (t . tweet_id)
FROM tweets AS t, hashtag AS h, cancer_type AS c 
WHERE t . tweet_id = h . tweet_id 
AND h . hashtag_id = c . hashtag_id 
AND c . cancer_type = 'kidneycancer';


Relational Algebra: 
π COUNT (tweet_id)
  γ COUNT (tweet_id)
   σ t . tweet_id = h . tweet_id AND h . hashtag_id = c . hashtag_id AND c . cancer_type = "kidney cancer"
    (ρ t tweets ×
     ρ h hashtag ×
      ρ c cancer_type)

<img width="479" alt="image" src="https://user-images.githubusercontent.com/34863107/201506052-64289a4c-5589-4e93-a467-2b67caa9ef5e.png">

7) Use Case: Smokers got Cancer
Description: The number of smokers who got Cancer 
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT hascancer, COUNT (user_id)
FROM user 
WHERE hascancer = 'Yes' 
AND smoker = 'Yes' ORDER BY COUNT (user_id);

Relational Algebra: 
τ COUNT (user_id)
  π hascancer, COUNT (user_id)
   γ COUNT (user_id)
    σ hascancer = "Yes" AND smoker = "Yes" user

<img width="470" alt="image" src="https://user-images.githubusercontent.com/34863107/201506064-6dc3b9b5-624e-4821-b236-fa47defebc8c.png">

8) Use Case: Smokers haven't got Cancer
Description: The number of smokers who have not got Cancer 
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT hascancer, COUNT (user_id)
FROM user WHERE hascancer = 'No' 
AND smoker = 'Yes' 
ORDER BY COUNT (user_id);

Relational Algebra: 
τ COUNT (user_id)
  π hascancer, COUNT (user_id)
   γ COUNT (user_id)
    σ hascancer = "No" AND smoker = "Yes" user
<img width="478" alt="image" src="https://user-images.githubusercontent.com/34863107/201506078-deca2589-7efe-4967-ad7e-46a82145c14c.png">

9) Use Case: Non smokers got Cancer
Description: The number of non-smokers who have got Cancer 
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT hascancer, COUNT (user_id)
FROM user 
WHERE hascancer = 'Yes' 
AND smoker = 'No' ORDER BY COUNT (user_id);

Relational Algebra: 
τ COUNT (user_id)
  π hascancer, COUNT (user_id)
   γ COUNT (user_id)
    σ hascancer = "Yes" AND smoker = "No" user
<img width="475" alt="image" src="https://user-images.githubusercontent.com/34863107/201506088-4a651296-7b1a-465d-91bf-eb37bd48cdb5.png">

10) Use Case: Medical Emergency Alert
Description: The medical emergency Alert 
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT u . user_name, u . handle_name, u . smoker, u . hascancer, u . cancer_type 
FROM user AS u, tweets AS t 
WHERE u . user_id = t . user_id AND alert = 'Yes';

Relational Algebra: 
π u . user_name, u . handle_name, u . smoker, u . hascancer, u . cancer_type
  σ u . user_id = t . user_id AND alert = "Yes"
   (ρ u user ×
    ρ t tweets)
<img width="481" alt="image" src="https://user-images.githubusercontent.com/34863107/201506113-acbebfff-d410-457f-8da4-39fbb58a942d.png">

11) Use Case: Most popular Hashtag Cancer
Description: The most Popular Hashtag Cancer
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT hashtag_text, COUNT (hashtag_text)
FROM hashtag GROUP BY hashtag_text 
ORDER BY COUNT (hashtag_text)DESC;

Relational Algebra: 
τ COUNT (hashtag_text) ↓
  γ hashtag_text, COUNT (hashtag_text) hashtag
<img width="480" alt="image" src="https://user-images.githubusercontent.com/34863107/201506128-0848fa10-45a8-4e4d-95ed-8cdb4abe1af1.png">

12) Use Case: Rare Cancer Type
Description: The Rare Cancer Type
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT cancer_type, COUNT (cancer_type)
FROM cancer_type GROUP BY cancer_type 
ORDER BY COUNT (cancer_type);

Relational Algebra: 
τ COUNT (cancer_type)
  γ cancer_type, COUNT (cancer_type) cancer_type
<img width="485" alt="image" src="https://user-images.githubusercontent.com/34863107/201506148-ca8e6553-442b-40aa-9651-de33b46fe52f.png">

13) Use Case: Review the tweets made by the user
Description: Reviewing the tweets made by the user
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database
SQL Statement : 
SELECT * FROM tweets AS t, user AS u 
WHERE t . user_id = u . user_id;
Relational Algebra: 
σ t . user_id = u . user_id
  (ρ t tweets ×
   ρ u user)

<img width="480" alt="image" src="https://user-images.githubusercontent.com/34863107/201506163-7d5af980-c13e-46be-be1a-511daebe5b6f.png">

14) Use Case: No. of tweets made on Skin Cancer Type
Description: Number of tweets that is made by the user on Skin Cancer
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT COUNT (t . tweet_id)FROM tweets AS t, hashtag AS h, cancer_type AS c 
WHERE t . tweet_id = h . tweet_id 
AND h . hashtag_id = c . hashtag_id 
AND c . cancer_type = 'skincancer';

Relational Algebra: 
π COUNT (tweet_id)
 γ COUNT (tweet_id)
  σ t . tweet_id = h . tweet_id AND h . hashtag_id = c . hashtag_id AND c . cancer_type = "skincancer"
    (ρ t tweets ×
     ρ h hashtag ×
     ρ c cancer_type)
<img width="477" alt="image" src="https://user-images.githubusercontent.com/34863107/201506173-4cf4aabd-b6ed-4ef5-9af2-f7815c215b33.png">

15) Use Case: No. of tweets made on Prostate Cancer Type
Description: Number of tweets that is made by the user on Prostate Cancer
Actor: User
Precondition: User must have unique twitter handle to tweet
Actor action: User tweets about the cancer
System Responses: The tweets are stored in the database

SQL Statement : 
SELECT COUNT (t . tweet_id)FROM tweets AS t, hashtag AS h, cancer_type AS c 
WHERE t . tweet_id = h . tweet_id 
AND h . hashtag_id = c . hashtag_id 
AND c . cancer_type = 'prostatecancer'
Relational Algebra: 
π COUNT (tweet_id)
  γ COUNT (tweet_id)
   σ t . tweet_id = h . tweet_id AND h . hashtag_id = c . hashtag_id AND c . cancer_type = "prostatecancer"
    (ρ t tweets ×
    ρ h hashtag ×
    ρ c cancer_type)
<img width="478" alt="image" src="https://user-images.githubusercontent.com/34863107/201506185-c57f7395-a2e0-4275-a339-f5a1d35ee663.png">


# QUERIES


1. What user posted this tweet?

SELECT U.User_Name, U.Handle_Name
FROM USER U, TWEETS T
WHERE U.User_Id= T.User_Id
AND T.Tweet_Id='1591132276909559808';

 <img width="360" alt="image" src="https://user-images.githubusercontent.com/34863107/201506200-59cd2526-7d44-481b-af06-99ed15d7f2b9.png">


2. When did the user post this tweet?

SELECT Posted_At
FROM  TWEETS
WHERE Tweet_Id='1591132276909559808';

 <img width="360" alt="image" src="https://user-images.githubusercontent.com/34863107/201506204-f53772ec-fb8e-478c-bcf6-0e22ab5d12f6.png">

 3. What tweets have this user posted in the past 24 hours?

SELECT  Tweet_Text
FROM    Tweets
WHERE   TWEETS.Posted_At >= datetime('now','-1 day')
AND User_id = 1 ;
<img width="360" alt="image" src="https://user-images.githubusercontent.com/34863107/201506210-0973bbe1-a363-4f87-b3f7-8a10c138fcab.png">

4. How many tweets have this user posted in the past 24 hours?

SELECT  COUNT(Tweet_Id)
FROM    Tweets
WHERE   TWEETS.Posted_At >= datetime('now','-1 day') 
AND User_id = 1 ;
<img width="360" alt="image" src="https://user-images.githubusercontent.com/34863107/201506229-1821f236-d218-41d3-828a-ba62654e6481.png">

5. When did this user join Twitter?

SELECT Joined_At FROM USER WHERE User_Id=1;

6. What keywords/ hashtags are popular?

SELECT hashtag_text, COUNT (hashtag_text)FROM hashtag 
GROUP BY hashtag_text 
ORDER BY COUNT (hashtag_text)DESC;

7. What tweets are popular?

SELECT TWEEET_TEXT,RETWEETS, LIKES
FROM TWEETS
ORDER BY LIKES DESC;
















 








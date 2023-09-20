# book_recommender_system
frt:Future Ready Talent project by Yukta Rajkumar Gurnani

I have created a book recommender system that recommends similar books to the reader based on his/her interest.
The books recommendation system is used by online websites which provide ebooks like google play books, open library, good Read’s, etc.

About - Book Recommender System

For building up this system, I have used a dataset from kaggle.

Based on the dataset, I have done collaborative and content-based filtering.

Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users.
It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user.

Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.

The HOME page of this website shows the results of content-based filtering by recommending top 20 books of the dataset based on the number of votes.

Whereas, the RECOMMEND section of website asks user to enter a book name and recommends books related to that genre.

Home Page - (Content-based filtering results)
![Screenshot (1675)](https://github.com/Yukta026/book_recommender_system/assets/143731993/167e374b-95e3-4619-ba46-579598942a5a)

Recommend Page - (Collaborative filtering results)
![Screenshot (1676)](https://github.com/Yukta026/book_recommender_system/assets/143731993/6c7a7436-cffc-40e6-81a0-0d9ec1384bf6)

About Page -
![Screenshot (2142)](https://github.com/Yukta026/book_recommender_system/assets/143731993/d7651600-2ee2-4f3b-a5fe-1d9c608b6203)

Code - 
Initially, I had written this code in Jupyter notebook then exported the results in .pkl file and developed the website using flask
![Screenshot (2202)](https://github.com/Yukta026/book_recommender_system/assets/143731993/6b2d0cf5-634d-4dc6-b6fe-2cd6a1bca920)

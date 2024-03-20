# -*- coding:utf-8 _*-
english1={
    "we":"我们",
    "world":"世界",
    "company":"公司",  
    }
english2=english1
english3=english1.copy()
print("english",english1)
print("enlish2",english2)
print("english3",english3)
print("------------------------------")
print("change english2")
english2["city"]="城市"
print("english",english1)
print("enlish2",english2)
print("english3",english3)
print("------------------------------")
print("change english3")
english3["school"]="学校"
print("english",english1)
print("enlish2",english2)
print("english3",english3)
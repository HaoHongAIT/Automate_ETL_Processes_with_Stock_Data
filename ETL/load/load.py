import hashlib
import pandas as pd
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship


def add_Category(file_path):
    category = pd.read_csv(file_path)
    for i in range(0, len(category)):
        c = Category(name=category['name'][i])
        db.session.add(c)


def add_News(file_path):
    news = pd.read_csv(file_path)
    for i in range(0, len(news)):
        db.session.add(News(title=news['title'][i],
                            brief=news['brief'][i],
                            date=news['date'][i],
                            category_id=news['category'][i],
                            content=news['content'][i], ))


def add_User(file_path):
    user_data = pd.read_csv(file_path)
    for i in range(0, len(user_data)):
        db.session.add(User(username=user_data['username'][i],
                            password=str(hashlib.md5(
                                user_data['password'][i].encode('utf8')).hexdigest()),
                            user_role=str(user_data['role'][i]),
                            email=str(user_data['email'][i]), )
                       )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_Category(r'./csv/categories.csv')
        add_News(r'./csv/rice.csv')
        add_News(r'./csv/coffee.csv')
        add_User(r'./csv/user.csv')
        db.session.commit()
    print('Add data successfully')

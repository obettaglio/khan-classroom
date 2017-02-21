"""Generator of users, students, exam results, and Khan Academy activities."""

import random
from model import (User, Student, Subject, Classroom, Exam, ExamResult, Exercise,
                   ExerciseResult, Video, VideoResult)
from model import db, connect_to_db
from server import app

f_names = ["Meggie", "Leslie", "Kiko", "Stephanie", "Lindsey", "Anne",
           "Erica", "Gina", "Ryan", "Dennis", "Ethan", "Todd", "Mark", "Jack",
           "Joel", "Henry", "Ronan", "Sam", "Gansey", "Kyle"]

l_names = ["Smith", "Johnson", "Inge", "Glassman", "Weinberg", "Carroll",
           "Mahnken", "Yeh", "Goodman", "Winchester", "Burton", "Conrad",
           "Chen", "Boyette", "Lonne", "Fischbach", "Wickham", "Horvatic",
           "Yoder", "Hardin"]

# genders = ["f", "m", "tw", "tm", "nb_gf", "pref"]

lorems = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce " +
          "auctor ex vitae nulla tempor, fermentum.", "Lorem ipsum dolor sit " +
          "amet, consectetur adipiscing elit. Morbi euismod congue tellus eget " +
          "dapibus. Suspendisse eu sapien pretium, sollicitudin lacus in, " +
          "facilisis erat. Duis quam purus, dictum id dictum in.", "Lorem " +
          "ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor " +
          "neque augue, eget viverra augue porttitor ut. Proin facilisis varius " +
          "urna, elementum pulvinar ex. Class aptent taciti sociosqu ad litora " +
          "torquent per conubia nostra, per inceptos himenaeos. Proin iaculis, " +
          "metus sed placerat viverra, libero risus fermentum felis, sit amet " +
          "tincidunt."
          ]


def mock_users():

    file = open("static/data/user_data.txt", "r+")
    for f_name in f_names:
        for l_name in l_names:
            khan_username = f_name[:2].lower() + l_name[:5]
            user_email = khan_username + "@mockuser.com"
            password = khan_username + str(123)
            # age = random.randrange(15, 50)
            # gender = random.choice(genders)

            line = "|".join([user_email, password, f_name, l_name, khan_username])

            file.write(line + "\n")

    file.close()


# def fake_reviews():

#     connect_to_db(app)

#     review_list = Game.query.filter(Game.release_date < '2017-02-28 00:00:00').order_by(Game.release_date.desc()).limit(200)

#     file = open("static/data/review_data.txt", "r+")
#     user_id = 1

#     while user_id <= 400:
#         for game in review_list:
#             game_id = game.game_id
#             score = random.randrange(60, 100)
#             comment = random.choice(lorems)

#             line = "|".join([str(game_id), str(user_id), str(score), comment])
#             file.write(line + "\n")

#         user_id += 1

#     file.close()

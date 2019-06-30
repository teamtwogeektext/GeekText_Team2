# from geek_text import db, User, Book, Publisher, Author
#
# db.create_all()
#
# ######## DUMMY USERS #########
#
# test_user1 = User('Lui', 'lui@woof.com', 'treat123')
# test_user2 = User('Rick', 'ricksanchez@gmail.com', 'pickle')
#
# db.session.add(test_user1)
# db.session.add(test_user2)
#
# ####### DUMMY PUBLISHERS #######
#
# pub1 = Publisher('The Publishing Co.', '123 Pubcrawl St')
# db.session.add(pub1)
#
# ####### DUMMY AUTHORS #######
#
# auth1 = Author('Lebron James')
# auth2 = Author('Andy Weir')
# db.session.add(auth1)
# db.session.add(auth2)
#
# ####### DUMMY TITLES #########
#
# book1 = Book(ISBN='123456789012', title='The Martian', genre='Sci-Fi', pubYear='2014', price=10.99, stock=12,
#      pub_id=1, auth_id=2)
# book2 = Book(ISBN='210987654321', title='Python For Dummies', genre='Educational', pubYear='2019', price=5.99, stock=17,
#      pub_id=1, auth_id=1)
# db.session.add(book1)
# db.session.add(book2)
#
# db.session.commit()



# <main role="main" class="container">
#       <div class="row">
#         <div class="col-md-8">
#           {% block content %}{% endblock %}
#         </div>
#         <div class="col-md-4">
#           <div class="content-section">
#             <h3>Our Sidebar</h3>
#             <p class='text-muted'>You can put any information here you'd like.
#               <ul class="list-group">
#                 <li class="list-group-item list-group-item-light">Latest Posts</li>
#                 <li class="list-group-item list-group-item-light">Announcements</li>
#                 <li class="list-group-item list-group-item-light">Calendars</li>
#                 <li class="list-group-item list-group-item-light">etc</li>
#               </ul>
#             </p>
#           </div>
#         </div>
#       </div>
#     </main>
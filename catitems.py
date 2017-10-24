from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbtables import Base, Category, Item, User

engine = create_engine('sqlite:///data.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# adding categories
Category1 = Category(name='Soccer', user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name='Basketball', user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name='Baseball', user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name='Frisbee', user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name='Snowboarding', user_id=1)
session.add(Category5)
session.commit()

Category2 = Category(name='Rock Climbing', user_id=1)
session.add(Category2)
session.commit()

Category6 = Category(name='Foosball', user_id=1)
session.add(Category6)
session.commit()

Category7 = Category(name='Skating', user_id=1)
session.add(Category7)
session.commit()

Category8 = Category(name='Hockey', user_id=1)
session.add(Category8)
session.commit()

Category9 = Category(name='Cricket', user_id=1)
session.add(Category9)
session.commit()

Category10 = Category(name='Throwball', user_id=1)
session.add(Category10)
session.commit()


# adding items
item1 = Item(name="Soccer Ball", user_id=1,
             description="an inflated ball used in playing soccer",
             categories=Category1)
session.add(item1)
session.commit()

item2 = Item(name="Snowboard", user_id=1,
             description="""Snowboards are boards that are usually /
             the width of one's foot longways, with the ability to /
             glide on snow.[1]Snowboards are differentiated from /
             monoskis by the stance of the user. In monoskiing, the user
             stands with feet inline with direction of travel /
             (facing tip of monoski/downhill) /
             (parallel to long axis of board), /
             whereas in snowboarding, users stand with feet /
             transverse(more or less) /
             to the longitude of the board. Users of such equipment may be /
             referred to as snowboarders. Commercial snowboards generally /
             require extra equipment such as bindings and /
             special boots which help /
             secure both feet of a snowboarder, who generally rides in an /
             upright position.[1] These types of boards are /
             commonly used by people /
             at ski hills or resorts for leisure, entertainment, and /
             competitive purposes in the activity called snowboarding.""",
             categories=Category5)
session.add(item2)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category:" + category.name

print('items added')
# fetching all the categories

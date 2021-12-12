from sqlalchemy import create_engine
from os import environ
from sqlalchemy.orm import backref, relationship, session, sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }
"""
classes = [State, City, User, Place, Review, Amenity]


class DBStorage:
    """this is the creation of our storage object"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes an storage object"""
        HBNB_MYSQL_USER = environ.get('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = environ.get('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = environ.get('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = environ.get('HBNB_MYSQL_DB')
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                          .format(HBNB_MYSQL_USER,
                                                  HBNB_MYSQL_PWD,
                                                  HBNB_MYSQL_HOST,
                                                  HBNB_MYSQL_DB),
                                          pool_pre_ping=True)
        except KeyError:
            print("user, password, host, or database not set correctly")
            return
        if environ.get('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns all items or all items of a specific class"""
        # return dict {cls.ID: <object>}
        newDict = {}
        if cls is None:
            for class_list in classes:
                for object in self.__session.query(class_list):
                    newDict.update({type(object).__name__ + "." +
                                    object.id: object})
        else:
            for object in self.__session.query(cls):
                newDict.update({type(object).__name__ + "." +
                                object.id: object})
        return newDict

    def new(self, obj):
        """Creates new item"""
        self.__session.add(obj)

    def save(self):
        """saves item"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an item"""
        if obj:
            self.__session.query.filter_by(id=obj.id).delete()

    def reload(self):
        """reloads the storage object"""
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        SessionObj = scoped_session(sessionFactory)
        self.__session = SessionObj()

    def close(self):
        """closing SQLAlchemy session"""
        self.__session.close()

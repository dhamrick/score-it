from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import asc, desc
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Players (Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key = True)
    user_name = Column(String(15), nullable = False, unique = True)
    name = Column(String(25), nullable = False)
    email = Column(String(25), nullable = False, unique = True)
    address = Column(String(80), nullable = True)

class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key = True)
    name = Column(String(25), nullable = False, unique = True)
    game_type = Column(String(10), nullable = True)
    players_max = Column(Integer, nullable = False)
    player_min = Column(Integer, nullable = False)
    difficulty = Column(String(15), nullable = True)

class GameOwnership (Base):
    __tablename__ = 'game_ownership'
    id_player = Column(Integer, ForeignKey('players.id'), primary_key = True)
    id_game = Column(Integer, ForeignKey('games.id'), primary_key = True)

class GameNights (Base):
    __tablename__ = 'game_nights'
    id = Column(Integer, primary_key = True)
    date = Column(Date, nullable = False)
    host = Column(Integer, ForeignKey('players.id'))

class GameStats (Base):
    __tablename__ = 'game_stats'
    id = Column(Integer, primary_key = True)
    game_night = Column(Integer, ForeignKey('game_nights.id'))
    id_game = Column(Integer, ForeignKey('games.id'))
    player = Column(Integer, ForeignKey('players.id'))
    score = Column(Integer, nullable = False)

engine = create_engine('postgres://vagrant@/scoreit')

Base.metadata.create_all(engine)




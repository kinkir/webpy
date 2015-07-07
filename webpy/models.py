from sqlalchemy import Column, Integer, String
from webpy.database import Base


class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    cpu_time = Column(Integer)
    cpu_quota = Column(Integer)

    def __init__(self, name, time, quota):
        self.name = name
        self.cpu_time = time
        self.cpu_quota = quota

    def __repr__(self):
        return '<Plan: %r:%d:%d>' % (self.name, self.cpu_time, self.cpu_quota)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    plan_id = Column(Integer)  # 0 plan is anon user

    def __init__(self, username, email, plan=0):
        self.username = username
        self.email = email
        self.plan = plan

    def __repr__(self):
        return "<User: %r:%r>" % self.username, self.plan
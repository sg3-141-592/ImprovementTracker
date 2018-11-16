from sqlalchemy import create_engine, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date

# DevDB, to be replaced with a production DB in future
engine = create_engine('sqlite:///improvementData.db', connect_args={'check_same_thread': False}, echo=False)

# Create the table structure
Base = declarative_base()

# List of objectives
class ObjectivesType(Base):
    __tablename__ = 'objectives'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Session used to update the database
Session = sessionmaker()
Session.configure(bind=engine)
dbSession = Session()

# Create some test data to get it started
if __name__ == "__main__":
    # Create some dummy objectives
    testObjectives = [ObjectivesType(name="Great Place to Work",
                                     description="Improve the business for the employees"),
                      ObjectivesType(name="Lead Time Reduction",
                                     description="Get out products out the door quicker"),
                      ObjectivesType(name="Reduce Cost",
                                     description="Bring down the cost of our products"),]
    dbSession.add_all(testObjectives)
    dbSession.commit()
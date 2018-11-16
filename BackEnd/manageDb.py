from sqlalchemy import create_engine, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date

# DevDB, to be replaced with a production DB in future
engine = create_engine('sqlite:///improvementData.db', connect_args={'check_same_thread': False}, echo=False)

# Create the table structure
Base = declarative_base()

# Convert an SQLite row as a table
def as_dict(row):
       return {c.name: getattr(row, c.name) for c in row.__table__.columns}

## -------------------------------------------------
## Objectives
## -------------------------------------------------
# List of objectives
class Objectives(Base):
    __tablename__ = 'objectives'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)


def getObjectives():
    return dbSession.query(Objectives).all()

## -------------------------------------------------
## BenefitTypes
## -------------------------------------------------
# List of benefits types
class BenefitTypes(Base):
    __tablename__ = 'benefitTypes'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

def getBenefitTypes():
    return dbSession.query(BenefitTypes).all()

## -------------------------------------------------
## Improvement
## -------------------------------------------------
class Improvement(Base):
    __tablename__ = 'improvements'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    benefits = relationship("Benefit")

## -------------------------------------------------
## Benefit
## -------------------------------------------------
class Benefit(Base):
    __tablename__ = 'benefits'    

    id = Column(Integer, primary_key=True)

    description = Column(String, nullable=False)

    # Link to the BenefitType category
    benefit_type = Column(Integer, ForeignKey('benefitTypes.id'))

    # Improvement ID is used to build a relationship between improvements
    # and episodes
    parent_improvement = Column(Integer, ForeignKey('improvements.id'))
    improvement = relationship("Improvement", back_populates="benefits")

Base.metadata.create_all(engine)

# Session used to update the database
Session = sessionmaker()
Session.configure(bind=engine)
dbSession = Session()

# Create some test data to get it started
if __name__ == "__main__":
    # Create some dummy objectives
    testObjectives = [Objectives(name="Great Place to Work",
                                 description="Improve the business for the employees"),
                      Objectives(name="Lead Time Reduction",
                                 description="Get out products out the door quicker"),
                      Objectives(name="Reduce Cost",
                                 description="Bring down the cost of our products"),]
    dbSession.add_all(testObjectives)
    dbSession.commit()

    # Create some dummy benefit types
    testBenefits = [BenefitTypes(name="Time",
                             description="Users reduce the amount of time they need to spend reviewing work"),
                    BenefitTypes(name="Great Place to Work",
                             description="Users have access to best in class tooling, and feel listened to"),
                    BenefitTypes(name="Automation",
                             description="Increase quality through automation, and reduce effort")]
    dbSession.add_all(testBenefits)
    dbSession.commit()

    # Create some dummy improvements
    testImprovements = Improvement(name="BeyondCompare",
                                    description="Buying BeyondCompare and deploying through SE-Desktop")
    improvementBenefits = Benefit(description="Faster reviews by being able to get accurate differentials",
                                 benefit_type=testBenefits[0].id,
                                 parent_improvement=testImprovements.id)
    dbSession.add(testImprovements)
    dbSession.commit()
    dbSession.add(improvementBenefits)
    dbSession.commit()
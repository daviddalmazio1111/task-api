from sqlalchemy import create_engine
from models import Base
from models import Task
from sqlalchemy.orm import sessionmaker

db_user="postgres"
db_password="dalmada2"
db_host="db"
db_port="5432"
db_name="tasks_db"

db_url=f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine=create_engine(db_url)
try:
    conn= engine.connect()
    print("Success")
    #Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    
    """
    modify_button=Task(id=1,task="modify button",owner="pierre")
    
    session.add(modify_button)
    session.commit()
    """


except Exception as ex:
    print(ex)
Session=sessionmaker(bind=engine)
session=Session()

from sqlalchemy import create_engine,NVARCHAR,Integer,DateTime,Column
from sqlalchemy.orm import sessionmaker,declarative_base
from datetime import datetime


engine=create_engine("sqlite:///DB/todo.db",echo=True)
base=declarative_base()
sestion=sessionmaker(bind=engine)()

class ToDo(base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True)
    task=Column(NVARCHAR)
    time=Column(DateTime,default=datetime.now, nullable=False)

    def __init__(self,task=None,time=None):
        self.task=task
        self.time=time

base.metadata.create_all(engine)


obj=ToDo()

def read():
    return sestion.query(ToDo).order_by(ToDo.time.asc()).all()
def add_task(obj):
    try:
        sestion.add(obj)
        sestion.commit()
        return True
    except Exception as e:
        return(str(e))

def delete_all_tasks():
    sestion.query(ToDo).delete()
    sestion.commit()
    

def delete_task(task_id):
    task = sestion.query(ToDo).get(task_id)
    if task:
        sestion.delete(task)
        sestion.commit()


from sqlalchemy import CheckConstraint, Column, Integer

from orm.database import Base
from orm.mixins import RecordTimestamps


class GlobalSetting(Base, RecordTimestamps):
    __tablename__ = "global_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_annonce_index_on_chain = Column(Integer, nullable=False)
    __table_args__ = (CheckConstraint("id = 1", name="single_row_check"),)

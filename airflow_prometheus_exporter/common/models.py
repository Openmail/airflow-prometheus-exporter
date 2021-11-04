from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import synonym
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utcdatetime import UTCDateTime

Base = declarative_base()


class DelayAlertMetadata(Base):
    __tablename__ = "delay_alert_metadata"
    __table_args__ = {"schema": "ddns"}
    dag_id = Column(String(250), primary_key=True)
    task_id = Column(String(250), primary_key=True, nullable=True)
    sla_interval = Column(String(64), primary_key=True)
    sla_time = Column(String(5), primary_key=True, nullable=True)
    affected_pipeline = Column(Text, nullable=True)
    alert_name = Column(String(250), nullable=True)
    alert_target = Column(String(250), nullable=True)
    group_title = Column(Text, nullable=True)
    inhibit_rule = Column(Text, nullable=True)
    link = Column(Text, nullable=True)
    note = Column(Text, nullable=True)
    ready = Column(Boolean, nullable=True)
    enabled = synonym("ready")


class DelayAlertAuxiliaryInfo(Base):
    __tablename__ = "delay_alert_auxiliary_info"
    __table_args__ = {"schema": "ddns"}
    dag_id = Column(String(250), primary_key=True)
    task_id = Column(String(250), primary_key=True, nullable=True)
    sla_interval = Column(String(64), primary_key=True)
    sla_time = Column(String(5), primary_key=True, nullable=True)
    latest_successful_run = Column(UTCDateTime)
    latest_sla_miss_state = Column(Boolean)


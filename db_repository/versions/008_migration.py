from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('image', String(length=120)),
    Column('link1', String(length=120)),
    Column('link2', String(length=120)),
    Column('link3', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['link1'].create()
    post_meta.tables['post'].columns['link2'].create()
    post_meta.tables['post'].columns['link3'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['link1'].drop()
    post_meta.tables['post'].columns['link2'].drop()
    post_meta.tables['post'].columns['link3'].drop()

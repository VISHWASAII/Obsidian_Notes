- The data Migration Happening using the Alembic Data Migration
- It is lightweight database migration tool
- Sql alchemy only add new table. but using Alembic we can change the database structure
```
Using this We can modify the data for the database

1 -- pip install alembic 

2 -- alembic init <Name>

3 -- alembic revision -m <m>

4 -- alembic upgrade <rev#>

5 -- alembic downgrade
```

- The alembic ini file will be created we need to add the db configuration there
```
sqlalchemy.url = driver://user:pass@localhost/dbname
```

- Alembic Revision
```
alembic revision -m ''create phone number col on user table"

Then 'Like github'
alembic upgrade <revision id> 
```
- Lets setup migration
```
we need to import our Model and we are change the config little bit

from sqlalchemy import engine_from_config

from sqlalchemy import pool

  

from alembic import context

  

import models

# this is the Alembic Config object, which provides

# access to the values within the .ini file in use.

config = context.config

  

# Interpret the config file for Python logging.

# This line sets up loggers basically.

  

fileConfig(config.config_file_name)

  

# add your model's MetaData object here

# for 'autogenerate' support

# from myapp import mymodel

# target_metadata = mymodel.Base.metadata

target_metadata = models.Base.metadata
```

- Now creating alembic revision
```
revision -m "Create phone num for user col"

[Inside versions -> revision id ]
"""Create phone num for user col

  

Revision ID: 3dde7b839e07

Revises:

Create Date: 2025-04-30 13:19:40.046003

  

"""

from typing import Sequence, Union

  

from alembic import op

import sqlalchemy as sa

  
  

# revision identifiers, used by Alembic.

revision: str = '3dde7b839e07'

down_revision: Union[str, None] = None

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None

  
  

def upgrade() -> None:

    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))

  
  

def downgrade() -> None:

    pass
  

"""


command

alembic upgrade revision id
```
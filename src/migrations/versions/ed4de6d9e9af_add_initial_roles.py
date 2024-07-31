"""add initial roles

Revision ID: ed4de6d9e9af
Revises: a97a51510331
Create Date: 2024-07-30 21:58:11.075083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed4de6d9e9af'
down_revision: Union[str, None] = 'a97a51510331'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    INSERT INTO role (id, name, permissions) VALUES
    (1, 'admin', '{"1": "admin"}'),
    (2, 'user', '{"2": "user"}');
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

"""Add note field to User table

Revision ID: 31dbefab6a9c
Revises: 079f4604893e
Create Date: 2025-04-07 19:53:54.994291

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31dbefab6a9c'
down_revision: Union[str, None] = '079f4604893e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('note', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'note')
    # ### end Alembic commands ###

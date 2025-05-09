"""Add buyer_id field to Annonce table

Revision ID: 3bbfccff7654
Revises: c89b1ab60d42
Create Date: 2025-04-11 13:04:28.877169

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3bbfccff7654"
down_revision: Union[str, None] = "c89b1ab60d42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("annonces", sa.Column("buyer_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "annonces", "users", ["buyer_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "annonces", type_="foreignkey")
    op.drop_column("annonces", "buyer_id")
    # ### end Alembic commands ###

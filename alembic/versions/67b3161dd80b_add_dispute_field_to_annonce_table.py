"""Add dispute field to Annonce table

Revision ID: 67b3161dd80b
Revises: 4a0c8d007287
Create Date: 2025-04-16 15:02:38.461683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67b3161dd80b'
down_revision: Union[str, None] = '4a0c8d007287'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('annonces', sa.Column('shipment_confirmation', sa.JSON(), nullable=True))
    op.add_column('annonces', sa.Column('dispute', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('annonces', 'dispute')
    op.drop_column('annonces', 'shipment_confirmation')
    # ### end Alembic commands ###

"""Add_annonce_table

Revision ID: 8d02ebc7755d
Revises: b63598a42449
Create Date: 2025-03-21 19:46:55.414251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d02ebc7755d'
down_revision: Union[str, None] = 'b63598a42449'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('annonces',
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titre', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('prix', sa.Float(), nullable=False),
    sa.Column('categorie', sa.String(length=100), nullable=False),
    sa.Column('photos', sa.Text(), nullable=True),
    sa.Column('date_publication', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('hash_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_url')
    )
    op.add_column('users', sa.Column('solana_address', sa.String(length=255), nullable=False))
    op.create_unique_constraint(None, 'users', ['solana_address'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'solana_address')
    op.drop_table('annonces')
    # ### end Alembic commands ###

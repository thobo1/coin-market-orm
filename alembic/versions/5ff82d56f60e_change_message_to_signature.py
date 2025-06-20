"""Change message to signature

Revision ID: 5ff82d56f60e
Revises: 726ba107830f
Create Date: 2025-06-20 20:29:31.076199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ff82d56f60e'
down_revision: Union[str, None] = '726ba107830f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('price_requests', sa.Column('buyer_id', sa.Integer(), nullable=True))
    op.add_column('price_requests', sa.Column('seller_id', sa.Integer(), nullable=True))
    op.add_column('price_requests', sa.Column('last_offer_by', sa.String(), nullable=True))
    op.add_column('price_requests', sa.Column('offer_price', sa.Float(), nullable=True))
    op.alter_column('price_requests', 'annonce_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('price_requests', 'message',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               nullable=True)
    op.alter_column('price_requests', 'status',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.create_index(op.f('ix_price_requests_id'), 'price_requests', ['id'], unique=False)
    op.drop_constraint(op.f('price_requests_user_id_fkey'), 'price_requests', type_='foreignkey')
    op.create_foreign_key(None, 'price_requests', 'users', ['seller_id'], ['id'])
    op.create_foreign_key(None, 'price_requests', 'users', ['buyer_id'], ['id'])
    op.drop_column('price_requests', 'offered_price')
    op.drop_column('price_requests', 'user_id')


def downgrade() -> None:
    op.add_column('price_requests', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('price_requests', sa.Column('offered_price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'price_requests', type_='foreignkey')
    op.drop_constraint(None, 'price_requests', type_='foreignkey')
    op.create_foreign_key(op.f('price_requests_user_id_fkey'), 'price_requests', 'users', ['user_id'], ['id'])
    op.drop_index(op.f('ix_price_requests_id'), table_name='price_requests')
    op.alter_column('price_requests', 'status',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('price_requests', 'message',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               nullable=False)
    op.alter_column('price_requests', 'annonce_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('price_requests', 'offer_price')
    op.drop_column('price_requests', 'last_offer_by')
    op.drop_column('price_requests', 'seller_id')
    op.drop_column('price_requests', 'buyer_id')
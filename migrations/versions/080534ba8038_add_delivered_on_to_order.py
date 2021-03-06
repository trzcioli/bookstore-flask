"""add delivered_on to order

Revision ID: 080534ba8038
Revises: 4e8c2eb9ae96
Create Date: 2019-01-14 23:07:47.734911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080534ba8038'
down_revision = '4e8c2eb9ae96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('delivered_on', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_order_delivered_on'), 'order', ['delivered_on'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_delivered_on'), table_name='order')
    op.drop_column('order', 'delivered_on')
    # ### end Alembic commands ###

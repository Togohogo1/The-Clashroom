"""nobadges

Revision ID: 4d998c6ec630
Revises: 7950a35f5dbd
Create Date: 2020-05-04 11:55:22.475532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d998c6ec630'
down_revision = '7950a35f5dbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account') as batch_op:
        batch_op.drop_column('badges')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account') as batch_op:
        batch_op.add_column(sa.Column('badges', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
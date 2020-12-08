"""empty message

Revision ID: 9164a17f11a2
Revises: f7a794904ff2
Create Date: 2020-12-03 08:07:26.747959

"""
from alembic import op
import sqlalchemy as sa

# Add the show model and columns

# revision identifiers, used by Alembic.
revision = '9164a17f11a2'
down_revision = 'f7a794904ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    # ### end Alembic commands ###
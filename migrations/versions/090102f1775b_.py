"""empty message

Revision ID: 090102f1775b
Revises: f50ea5cd3306
Create Date: 2018-10-19 16:07:18.134717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090102f1775b'
down_revision = 'f50ea5cd3306'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Reporter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Reporter')
    # ### end Alembic commands ###

"""empty message

Revision ID: 0339ecb01100
Revises: 
Create Date: 2018-08-11 13:56:21.141491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0339ecb01100'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('submission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('card_id', sa.String(length=255), nullable=False),
    sa.Column('card_url', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('hook', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card_id'),
    sa.UniqueConstraint('card_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('submission')
    # ### end Alembic commands ###

"""Added account and image

Revision ID: 71253aff1a15
Revises: 
Create Date: 2019-06-25 18:55:38.293407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71253aff1a15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('publisher',
    sa.Column('publisher_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('publisher_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_image', sa.String(length=50), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('books',
    sa.Column('ISBN', sa.String(length=13), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('genre', sa.Text(), nullable=True),
    sa.Column('pubYear', sa.String(length=4), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('pub_id', sa.Integer(), nullable=False),
    sa.Column('auth_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['auth_id'], ['author.author_id'], ),
    sa.ForeignKeyConstraint(['pub_id'], ['publisher.publisher_id'], ),
    sa.PrimaryKeyConstraint('ISBN'),
    sa.UniqueConstraint('ISBN')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('publisher')
    op.drop_table('author')
    # ### end Alembic commands ###

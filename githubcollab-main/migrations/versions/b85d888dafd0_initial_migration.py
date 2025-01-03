"""Initial migration.

Revision ID: b85d888dafd0
Revises: 
Create Date: 2024-11-12 19:19:45.461645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b85d888dafd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    with op.batch_alter_table('experience', schema=None) as batch_op:
        batch_op.add_column(sa.Column('monthstart', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('yearstart', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('monthend', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('yearend', sa.Integer(), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.drop_column('year')
        batch_op.drop_column('month')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('experience', schema=None) as batch_op:
        batch_op.add_column(sa.Column('month', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('year', sa.INTEGER(), nullable=True))
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
        batch_op.drop_column('yearend')
        batch_op.drop_column('monthend')
        batch_op.drop_column('yearstart')
        batch_op.drop_column('monthstart')

    op.create_table('item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=30), nullable=False),
    sa.Column('price', sa.INTEGER(), nullable=False),
    sa.Column('barcode', sa.VARCHAR(length=4), nullable=False),
    sa.Column('desc', sa.VARCHAR(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('barcode'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###

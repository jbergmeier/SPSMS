"""empty message

Revision ID: fca07e491165
Revises: 4c76b5bff4e6
Create Date: 2020-05-24 14:25:06.721931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca07e491165'
down_revision = '4c76b5bff4e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prebooking', sa.Column('ad_date', sa.DateTime(), nullable=False))
    op.add_column('prebooking', sa.Column('id_area_category', sa.Integer(), nullable=False))
    op.add_column('prebooking', sa.Column('id_customer', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'prebooking', 'ad_category_area', ['id_area_category'], ['id'])
    op.create_foreign_key(None, 'prebooking', 'app_user', ['id_customer'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'prebooking', type_='foreignkey')
    op.drop_constraint(None, 'prebooking', type_='foreignkey')
    op.drop_column('prebooking', 'id_customer')
    op.drop_column('prebooking', 'id_area_category')
    op.drop_column('prebooking', 'ad_date')
    # ### end Alembic commands ###

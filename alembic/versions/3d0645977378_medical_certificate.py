"""medical_certificate

Revision ID: 3d0645977378
Revises: 14d5e28d3626
Create Date: 2012-06-29 11:33:20.282837

"""

# revision identifiers, used by Alembic.
revision = '3d0645977378'
down_revision = '14d5e28d3626'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exam_admissions', sa.Column('medical_certificate', sa.Boolean(), nullable=True))
    op.add_column('exams', sa.Column('medical_certificate', sa.Boolean(), nullable=True))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exams', 'medical_certificate')
    op.drop_column('exam_admissions', 'medical_certificate')
    ### end Alembic commands ###

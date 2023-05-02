"""init

Revision ID: 05df19fb81b9
Revises: 
Create Date: 2023-04-28 17:11:20.029241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05df19fb81b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'questionss',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('questionText', sa.String),
        sa.Column('questionAnswers', sa.ARRAY()),
        sa.Column('correct', sa.String),


    )


def downgrade():
    op.drop_table('questions')

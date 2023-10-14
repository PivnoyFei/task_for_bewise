"""Initial

Revision ID: 282d2176c10b
Revises: 
Create Date: 2023-10-13 16:52:17.816005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282d2176c10b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_question_id'), 'question', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_question_id'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###
"""Translation for achievments

Revision ID: 63a4828c15a6
Revises: 39d74eef735b
Create Date: 2024-03-27 15:19:39.139115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63a4828c15a6'
down_revision: Union[str, None] = '39d74eef735b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievments', sa.Column('name_ru', sa.String(), nullable=False))
    op.add_column('achievments', sa.Column('name_en', sa.String(), nullable=False))
    op.add_column('achievments', sa.Column('ru_description', sa.String(), nullable=False))
    op.add_column('achievments', sa.Column('en_description', sa.String(), nullable=False))
    op.drop_column('achievments', 'description')
    op.drop_column('achievments', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievments', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('achievments', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('achievments', 'en_description')
    op.drop_column('achievments', 'ru_description')
    op.drop_column('achievments', 'name_en')
    op.drop_column('achievments', 'name_ru')
    # ### end Alembic commands ###

"""ндачальная миграция

Revision ID: 025cfc656151
Revises: 
Create Date: 2023-03-10 20:54:34.452068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025cfc656151'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'crpterror',
        sa.Column('_id', sa.Integer,
                  primary_key=True, nullable=False),
        sa.Column('report_date', sa.String),
        sa.Column('report_period', sa.String),
        sa.Column('inn', sa.String),
        sa.Column('doc', sa.String),
    )


def downgrade() -> None:
    op.drop_table("crpterror")

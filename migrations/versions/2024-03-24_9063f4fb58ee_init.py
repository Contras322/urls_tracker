"""Init migration. Added table visited_urls.

Revision ID: 9063f4fb58ee
Revises: 
Create Date: 2024-03-24 11:38:30.097609

"""
# pylint: skip-file; noqa

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9063f4fb58ee"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "visited_urls",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("link", sa.String(length=512), nullable=False),
        sa.Column("domain", sa.String(length=256), nullable=False),
        sa.Column("visit_dttm", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("visited_urls")
    # ### end Alembic commands ###

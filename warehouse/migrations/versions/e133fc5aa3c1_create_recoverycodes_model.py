# SPDX-License-Identifier: Apache-2.0
"""
create recoverycodes model

Revision ID: e133fc5aa3c1
Revises: b5bb5d08543d
Create Date: 2020-01-17 22:53:33.012851
"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects import postgresql

revision = "e133fc5aa3c1"
down_revision = "f47d2f06c13e"


def upgrade():
    op.create_table(
        "user_recovery_codes",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("code", sa.String(length=128), nullable=False),
        sa.Column(
            "generated", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], initially="DEFERRED", deferrable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("user_recovery_codes")

"""
I really should document this script!
"""
# ---------------------------------------------------------------------------------------------------------------------
__author__ = "William Hamilton"
__python__ = ""
__created__ = "16/04/2025"
__copyright__ = "Copyright © 2025~"
__license__ = ""
__ToDo__ = """
- nothing to add just yet
"""

from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


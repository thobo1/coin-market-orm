from sqlalchemy import DECIMAL
from sqlalchemy.dialects.mysql import BIGINT, FLOAT, INTEGER

DEFAULT_LENGTH = 255
UnsignedInt = INTEGER(unsigned=True)
UnsignedBigInt = BIGINT(unsigned=True)
UnsignedFloat = FLOAT(unsigned=True)

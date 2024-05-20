# UTC - Coordinated Universal Time

import datetime
from datetime import timezone

utc_now = datetime.datetime.now(timezone.utc)
print(utc_now)

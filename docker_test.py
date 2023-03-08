from time import sleep
from logging import getLogger

logger = getLogger(__name__)

print("Container starteds")
for i in range(3):
    logger.warning(i)
    print(i)
    sleep(1)
print("bye bye")
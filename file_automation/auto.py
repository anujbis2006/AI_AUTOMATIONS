import os
source_dir = "/Users/anujbiswas/AI_AUTOMATIONS/first_automation/socks"
with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
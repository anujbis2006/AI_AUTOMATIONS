import camelot
tables = camelot.read_pdf('/Users/anujbiswas/AI_AUTOMATIONS/extarction_automation/extract.pdf',pages = '1')
tables.export('/Users/anujbiswas/AI_AUTOMATIONS/extarction_automation/tables.csv',f = 'csv',compress=True)
tables[0].to_csv('/Users/anujbiswas/AI_AUTOMATIONS/extarction_automation/tables.csv')
import frappe
from frappe.utils import (date_diff,add_to_date)

def get_additional_half_day(doc,method):
    working_days= date_diff(doc.end_date, doc.start_date) + 1
    STANDARD_TIME = 1.90 # 2Hour after work day
    additional_half_day = 0
    for single_date in (add_to_date(doc.start_date,days=n) for n in range(working_days)):
        exists = frappe.db.exists("Attendance",{"employee":doc.employee,"attendance_date":single_date,"docstatus":1,"status":"Present"})
        if exists:
            attendance_record = frappe.get_doc("Attendance",{"employee":doc.employee,"attendance_date":single_date,"docstatus":1,"status":"Present"})
            if attendance_record.working_hours > 7:
                diff_hours = attendance_record.working_hours - 7
                if diff_hours >= STANDARD_TIME:
                    additional_half_day += 1
    doc.additional_half_day = additional_half_day
    doc.add_tax_components()
    doc.validate()
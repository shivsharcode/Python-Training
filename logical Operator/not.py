"""
if applicant has high income OR good credit AND doesn't have a criminal record => Eligible for loan
"""

has_high_income = True
has_good_credit = True
has_criminal_record = False

if (has_high_income or has_good_credit) and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")


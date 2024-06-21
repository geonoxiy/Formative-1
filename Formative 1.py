def savings(gross_pay, tax_rate, expenses):
    centavos_remaining = gross_pay - (float(tax_rate)*gross_pay) - expenses
    return int(centavos_remaining)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    waste = str(int(total_material) - int(num_jobs) * int(job_consumption)) + str(material_units)
    return waste

def interest(principal, rate, periods):
    simple_interest = int(principal) * float(rate) * int(periods)
    principal += simple_interest
    return int(principal)

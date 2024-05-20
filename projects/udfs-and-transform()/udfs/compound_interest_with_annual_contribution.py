class CompoundInterestUDF:
    def calculate_compound_interest(self, principal, rate, periods, annual_contribution):
        if principal is not None and rate is not None and periods is not None and annual_contribution is not None:
            total_amount = principal
            for _ in range(periods):
                total_amount = (total_amount + annual_contribution) * (1 + rate)
            return total_amount
        return None
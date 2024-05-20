class CompoundInterestUDF:
    def calculate_compound_interest(self, principal, rate, periods):
        if principal is not None and rate is not None and periods is not None:
            return principal * (1 + rate) ** periods
        return None

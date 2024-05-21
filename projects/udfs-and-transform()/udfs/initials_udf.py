class InitialsUDF:
    def get_initials(self, name, surname):
        if name and surname:
            initials = f"{name[0].upper()}{surname[0].upper()}"
            return initials
        return None

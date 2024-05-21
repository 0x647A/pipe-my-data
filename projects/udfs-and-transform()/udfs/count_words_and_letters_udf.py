class DescriptionUDFs:
    @staticmethod
    def count_words(description):
        if description:
            return len(description.split())
        else:
            return 0

    @staticmethod
    def count_chars(description):
        if description:
            return len(description)
        else:
            return 0

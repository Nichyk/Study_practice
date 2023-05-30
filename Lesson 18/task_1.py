# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter
# is a valid email string.
# Email validations:
# Valid email address format
# Email address
class SomeClass:
    def __init__(self, email):
        self.email = self.validate(email)

    @staticmethod
    def validate(email):
        if email.count('@') == 0 or email.count('@') > 1:
            raise ValueError('Not an email format')
        else:
            email_name_list = email.split('@')
            local = email_name_list[0]
            domain = email_name_list[1]
            local_check = '!#$%&\'*+-/=?^_`{|}~.'
            for index, value in enumerate(local):
                if not value.isalpha() and not value.isdigit() and value not in local_check:
                    raise ValueError(f'{value} is not allowed in local name')
                if value == '.' and (index == 0 or index == (len(local) - 1)):
                    raise ValueError(f'{value} can\'t be first or last value in local name')
                if (value == '-' or value == '_') and index == len(local) - 1:
                    raise ValueError(f'{value} can\'t be last value in local name')
                if local[index] == '.' and local[index + 1] == '.':
                    raise ValueError(f'You can\'t use {value} more than 1 time in a row')
            if len(domain) < 3:
                raise ValueError('Domain name can\'t be shorter than 2 signs')
            else:
                domain_check = '-.'
                if domain.count('.') >= 1:
                    domain_name_list = domain.split('.')
                    if len(domain_name_list[-1]) < 2:
                        raise ValueError('Last portion of domain name can\'t be shorter than 2 signs')
                for index, value in enumerate(domain):
                    if not value.isalpha() and not value.isdigit() and value not in domain_check:
                        raise ValueError(f'{value} is not allowed in domain name')
                    if value == '-' and (index == 0 or index == (len(domain) - 1)):
                        raise ValueError(f'{value} can\'t be first or last value in domain name')
            return email


s = SomeClass('nichyk.sergey@gmail.com')
print(s.email)

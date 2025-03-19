class NullBalance:
    def check_null_balance(description):
        if description is None:
            return False
        return "NullBalance" in description

description1 = "Bu hisobda NullBalance muammosi mavjud."
description2 = "Bu hisobda hech qanday muammo yo‘q."


print(NullBalance.check_null_balance(description1))  
print(NullBalance.check_null_balance(description2))  
print(NullBalance.check_null_balance(None))  
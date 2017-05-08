from zomato import Zomato

# Provide ZOMATO-API-KEY
z = Zomato("ZOMATO-API-KEY")

# Provide restaurant ID here in place of 12345
z.parse("res_id=12345")

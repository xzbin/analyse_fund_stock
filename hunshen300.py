import akshare as ak

# 沪深300 6%
# fund_codes = '110020'

# 上证50
fund_codes = '110003'

fund_history = ak.fund_em_open_fund_info(fund_codes)
print(fund_history)

# 1 * (1 + x) ** 10 = 1.7974

# import math
#
# print(math.pow(2.4335, 1 / 15) - 1)
# print((1 + 0.10) ** 10)

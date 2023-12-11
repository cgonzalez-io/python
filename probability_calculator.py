# Calculating the number of different committees with strictly more women than men

# Total number of ways to form committees of 6 members with more women than men
# Possible combinations: 4 women and 2 men, 5 women and 1 man, all 6 women

# 4 women (out of 16) and 2 men (out of 13)
committees_4w_2m = (16, 4) * (13, 2)

# 5 women (out of 16) and 1 man (out of 13)
committees_5w_1m = (16, 5) * (13, 1)

# All 6 women (out of 16)
committees_6w = (16, 6)

# Total number of committees
total_committees = committees_4w_2m + committees_5w_1m + committees_6w
print(total_committees)

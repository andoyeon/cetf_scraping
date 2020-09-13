# from dateutil.relativedelta import relativedelta
from datetime import datetime


def Add_years(d, years):
    # d 값의 하이픈 -> , 변경
    # d.replace('-', ',')
    # expr_dt = regs_dt =
    # count+1, regs_nm, regs_num, regs_dt
    dt = datetime.strptime(d, '%Y-%m-%d')

    output = datetime(dt.year + years)

    # output = d - relativedelta(years=5)
    print(d, '5년 후:', output)



if __name__ == '__main__':
    # Add_years('2016-09-09', 5)
    d = '2016-09-09'
    dt = datetime.strptime(d, '%Y-%m-%d')
    print(dt)
    # print(dt.year + 5)
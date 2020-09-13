import pandas as pd
import csv


def read_file(path):
    # 인증번호 파일 불러오기
    regs_num = pd.read_csv(path, encoding='CP949')    # CodeError해결
    regs_nm = list(pd.DataFrame(regs_num).iloc[:, 1])
    regs_num = list(pd.DataFrame(regs_num).iloc[:, 2])

    print(type(regs_nm))
    print(regs_nm)
    return list(regs_nm), list(regs_num)


def save_file(regs_nm, regs_num, regs_dt):
    # 세 요소로 데이터 프레임 생성하기
    # df3 = pd.DataFrame(regs_nm, regs_num, regs_dt)
    # print(regs_nm)
    df = pd.DataFrame({"regs_nm": regs_nm})
    df["reg_num"] = regs_num
    df["regs_dt"] = regs_dt

    # 데이터 프레임을 csv파일로 저장
    df.to_csv('output_02.csv', mode='a', header=True)



if __name__ == '__main__':
    pass
    # read_file('product_list.csv')
    # regs_nm = ['A', 'B', 'C']
    # regs_num = ['HH-AA', 'AA-GG', 'BB-BNN']
    # regs_dt = ['0000-00-00', '1111-09-09', '3939-99-99']
    # result = make_file(regs_nm, regs_num, regs_dt)
    # print(result)
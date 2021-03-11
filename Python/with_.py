# import pickle

with open('study.txt', 'w', encoding='utf-8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

with open('study.txt', "r", encoding='utf-8') as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i) + '주간보고서.txt', 'w', encoding='utf-8') as report_file:
        report_file.write('- {0} 주차 주간보고 -\n'.format(i))
        report_file.write('부서 : \n')
        report_file.write('이름 : \n')
        report_file.write('업무 요약 : \n')
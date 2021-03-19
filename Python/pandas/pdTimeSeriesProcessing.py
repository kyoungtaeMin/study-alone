# %%
import numpy as np
import pandas as pd
from pandas.core.indexes import period
from pandas.tseries import offsets

# %%
# 시계열 처리

# %%
idx = pd.DatetimeIndex(['2020-03-01', '2020-03-02', '2021-03-03',
                        '2021-03-04', '2021-03-05'])
s = pd.Series([0, 1, 2, 3, 4], index=idx)
s

# %%
s['2021-03-03': ]

# %%
s[: '2021-03-04']

# %%
s['2020']

# %%
# 시계열 데이터 구조

# %%
from datetime import datetime

# %%
dates = pd.to_datetime(['12-12-2019', datetime(2020, 1, 1), '3rd of Jun, 2021',
                       '2021-Mar-1', '20210714'])
dates

# %%
dates.to_period('D')

# %%
dates- dates[0]

# %%
pd.date_range('2021-01-01', '2021-03-15')

# %%
pd.date_range('2021-03-19', periods=7)

# %%
pd.date_range('2021-03-19', periods=7, freq='M')

# %%
pd.date_range('2021-03-19', periods=7, freq='H')

# %%
idx = pd.to_datetime(['2020-01-01 12:00:00', '2020-01-02 00:00:00']+ [None])
idx

# %%
idx[2]

# %%
pd.isnull(idx)

# %%
# 시계열 기본

# %%
dates = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 4),
         datetime(2020, 1, 7), datetime(2020, 1, 10), datetime(2020, 1, 11),
         datetime(2020, 1, 15)]
dates

# %%
ts = pd.Series(np.random.randn(7), index=dates)
ts

# %%
ts.index

# %%
ts.index[0]

# %%
ts[ts.index[2]]

# %%
ts['2020-01-04']

# %%
ts['1/4/2020']

# %%
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2018-01-01', periods=1000))
ts

# %%
ts['2020']

# %%
ts['2020-06']

# %%
ts[datetime(2020, 9, 1): ]

# %%
ts['2020-06-01': '2020-07-14']

# %%
tdf = pd.DataFrame(np.random.randn(1000, 4),
                   index=pd.date_range('2018-04-01', periods=1000),
                   columns=['A', 'B', 'C', 'D'])
tdf

# %%
tdf['2020']

# %%
tdf['2020-06']

# %%
tdf['2020-07-14': ]

# %%
tdf['C']

# %%
ts = pd.Series(np.random.randn(10),
               index=pd.DatetimeIndex(['2020-01-01', '2020-01-01',
                                       '2020-01-02', '2020-01-02', 
                                       '2020-01-03', '2020-01-04', 
                                       '2020-01-05', '2020-01-05', 
                                       '2020-01-06', '2020-01-07']))
ts

# %%
ts.index.is_unique

# %%
ts['2020-01-01']

# %%
ts.groupby(level=0).mean()

# %%
pd.date_range('2020-01-01', '2020-07-01')

# %%
pd.date_range(start='2020-01-01', periods=10)

# %%
pd.date_range(end='2020-07-14', periods=10)

# %%
pd.date_range('2020-07-01', '2020-07-14', freq='B')
# B는 Business의 B라서 영업일만 표시

# %%
# 주기와 오프셋

# %%
pd.timedelta_range(0, periods=12, freq='H')
# H는 Hour

# %%
pd.timedelta_range(0, periods=60, freq='T')
# T는 Minute

# %%
pd.timedelta_range(0, periods=10, freq='1H30T')

# %%
pd.date_range('2021-01-01', periods=20, freq='B')

# %%
pd.date_range('2021-01-01', periods=30, freq='2H')

# %%
pd.date_range('2021-01-01', periods=20, freq='S')

# %%
# 시프트 (Shift)

# %%
ts = pd.Series(np.random.randn(5),
               index=pd.date_range('2021-01-01', periods=5,
                                   freq='B'))
ts

# %%
ts.shift(1)

# %%
ts.shift(3)
# 위에서 부터 순차적으로 밀려서 3까지 Nan값으로 바뀐다
# 4번째에 1의 값이 온다

# %%
ts.shift(-2)
# 음수로 주면 아래에서 부터 위로 민다

# %%
ts.shift(3, freq='B')
# freq를 적용하면 3부터 다시 freq를 계산해서 값을 입력한다

# %%
ts.shift(2, freq='W')

# %%
# 시간대 처리
# - 국제표준시(Coordinated Universal Time, UTC)를 기준으로 떨어진 거리만큼
#   오프셋으로 시간대 처리
# - 전 세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리인 pytz(pyTimeZone) 사용


# %%
import pytz
pytz.common_timezones

# %%
tz = pytz.timezone('Asia/Seoul')

# %%
dinx = pd.date_range('2021-01-01 09:00', periods=7, freq='B')
ts = pd.Series(np.random.randn(len(dinx)), index=dinx)
ts

# %%
pd.date_range('2021-01-01 09:00', periods=7, freq='B', tz='UTC')

# %%
ts_utc = ts.tz_localize('UTC')
ts_utc

# %%
ts_utc.index

# %%
ts_utc.tz_convert('Asia/Seoul')

# %%
ts_seoul = ts.tz_localize('Asia/Seoul')
ts_seoul

# %%
ts_seoul.tz_convert('UTC')

# %%
ts_seoul.tz_convert('Europe/Berlin')

# %%
ts.index.tz_localize('America/New_York')

# %%
stamp = pd.Timestamp('2021-01-01 00:00')
stamp_utc = stamp.tz_localize('UTC')
stamp_utc

# %%
stamp_utc.value

# %%
stamp_utc.tz_convert('Asia/Seoul')

# %%
stamp_utc.tz_convert('Asia/Seoul').value

# %%
stamp_ny = pd.Timestamp('2021-01-01 00:00', tz='America/New_York')
stamp_ny

# %%
stamp_utc.value

# %%
stamp_ny.value

# %%
stamp_utc.tz_convert('Asia/Shanghai')

# %%
stamp = pd.Timestamp('2021-01-01 00:00', tz='Asia/Seoul')
stamp

# %%
from pandas.tseries.offsets import Hour
stamp+ Hour()

# %%
stamp+ 3* Hour()

# %%
ts_utc

# %%
ts1 = ts_utc[: 5].tz_convert('Europe/Berlin')
ts2 = ts_utc[2: ].tz_convert('America/New_York')
ts = ts1+ ts2

# %%
ts.index

# %%
# 기간과 기간 연산


# %%
p = pd.Period(2021, freq='A-JAN')
p
# 'A'는 년도 단위

# %%
p+ 2

# %%
p- 3

# %%
p1 = pd.Period(2011, freq='A-JAN')
p2 = pd.Period(2021, freq='A-JAN')
p2- p1

# %%
pr = pd.period_range('2021-01-01', '2021-06-30', freq='M')
pr

# %%
pd.Series(np.random.randn(6), index=pr)

# %%
pidx = pd.PeriodIndex(['2021-01', '2021-02', '2021-03'], freq='M')
pidx

# %%
p = pd.Period('2021', freq='A-FEB')
p

# %%
p.asfreq('M', how='start')

# %%
p.asfreq('M', how='end')

# %%
p = pd.Period('2021', freq='A-OCT')
p

# %%
p.asfreq('M', how='start')

# %%
p.asfreq('M', how='end')

# %%
pr = pd.period_range('2011', '2021', freq='A-JUL')
ts = pd.Series(np.random.randn(len(pr)), index=pr)
ts

# %%
ts.asfreq('M', how='start')

# %%
ts.asfreq('M', how='end')

# %%
ts.asfreq('B', how='end')

# %%
p = pd.Period('2021Q1', freq='Q-JUL')
p

# %%
p.asfreq('D', how='start')
# how 생략가능

# %%
p.asfreq('D', 'end')

# %%
pr = pd.period_range('2020Q3', '2021Q3', freq='Q-JAN')
ts = pd.Series(np.arange(len(pr)), index=pr)
ts

# %%
pr = pd.date_range('2020-01-01', periods=5, freq='Q-JAN')
ts = pd.Series(np.random.randn(5), index=pr)
ts

# %%
ts.to_period()

# %%
pr = pd.date_range('2021-01-01', periods=5, freq='D')
ts = pd.Series(np.random.randn(5), index=pr)
ts

# %%
p = ts.to_period('M')
p

# %%
p.to_timestamp(how='start')


# %%
# 리샘플링 (Resampling)
# - 리샘플링(Resampling) : 시계열의 빈도 변환
# - 다운샘플링(Down sampling) : 상위 빈도 데이터를 하위 빈도 데이터로 집계
# - 업샘플링(Up sampling) : 하위 빈도 데이터를 상위 빈도 데이터로 집계
# - resample() 메소드


# %%
dr = pd.date_range('2021-01-01', periods=200, freq='D')
ts = pd.Series(np.random.randn(len(dr)), index=dr)
ts

# %%
ts.resample('M').mean()

# %%
ts.resample('M', kind='period').mean()

# %%
dr = pd.date_range('2021-01-01', periods=10, freq='T')
ts = pd.Series(np.arange(10), index=dr)
ts

# %%
ts.resample('2T', closed='left').sum()
# left는 기준을 잡아주는 시간이 시작시간 그대로 시작

# %%
ts.resample('2T', closed='right').sum()
# right는 기준을 잡아주는 시간이 시작시간 - 지정한 시간단위로 시작

# %%
ts.resample('2T', closed='right', label='right').sum()

# %%
ts.resample('2T', closed='right', label='right', loffset='-1s').sum()

# %%
ts.resample('2T').ohlc()
# 시가, 고가, 저가, 종가, 표현 함수

# %%
df = pd.DataFrame(np.random.randn(10, 4),
                  index=pd.date_range('2020-07-01', periods=10, freq='M'),
                  columns=['c1', 'c2', 'c3', 'c4'])
df

# %%
df.resample('Y').asfreq()

# %%
df.resample('W-FRI').asfreq()

# %%
df.resample('H').asfreq()

# %%
df.resample('H').ffill()

# %%
df.resample('H').ffill(limit=2)

# %%
df.resample('Q-DEC').mean()

# %%
df.resample('Y').mean()

# %%
df.resample('A').mean()


# %%
# 무빙 윈도우 (Moving Window)


# %%
df = pd.DataFrame(np.random.randn(300, 4),
                  index=pd.date_range('2020-01-01', periods=300, freq='D'),
                  columns=['c1', 'c2', 'c3', 'c4'])
df

# %%
df.rolling(30).mean().plot()
# 이동평균

# %%
df.rolling(60).mean().plot()

# %%
df.c1.rolling(60, min_periods=10).std().plot()

# %%
df.rolling(60, min_periods=10).std()[10: 50].plot()

# %%
df.rolling(60, min_periods=10).std().expanding().mean().plot()
# expanding()을 사용하면 고정 window에서 확장 window로 변경
# 중간에 결측치가 있어도 해당 값을 누적해서 더해감.

# %%
df.rolling(60).mean().plot(logy=True)

# %%
df.rolling('20D').mean().plot()

# %%
df.c1.rolling(30, min_periods=20).mean().plot(style='--', label='Simple MA')
df.c1.ewm(span=30).mean().plot(style='-', label='EWMA')
# ewm은 rolling과 expanding을 같이 사용하는 효과

# %%
df.c1.rolling(100, min_periods=50).corr(df.c3).plot()

# %%
df.c2.rolling(100, min_periods=50).corr(df.c4).plot()


# 4h 12m 53s
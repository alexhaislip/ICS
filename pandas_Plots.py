import pandas

pd.Series(np.random.randn(1000),
    index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()
<matplotlib.axes._subplots.AxesSubplot at 0x7f536b017ed0>


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
    columns=['A', 'B', 'C', 'D'])

df = df.cumsum()

plt.figure()
<Figure size 640x480 with 0 Axes>

df.plot()
<matplotlib.axes._subplots.AxesSubplot at 0x7f53723daa10>

plt.legend(loc='best')
<matplotlib.legend.Legend at 0x7f5369d93dd0>
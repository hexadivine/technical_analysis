# Technical Analysis

A pure python library to perform technical analysis in a very efficient way without installing any dependencies other than numpy.


## Installation

```
pip install -U git+https://github.com/h3x4d1v1n3/technical_analysis
```

## Why to use this library
- Does not require any other dependencies or packages to be installed on the system to perform technical analysis like ta-lib.
- Easy to install and it is a cross platform library.
- Works flawlessly with below parameter as a datatype
  - Numpy Arrays
  - Pandas Dataframes
  - Python Lists
- This library uses numpy library to perform arithmetic operations 
- Library's structure and code is easy to understand as compared to ta-lib or any other library.
- This library will support 139+ indicators (currently supports 5)

  
## Supported Functions

- Momentum indicator (momentum)
  - Directional Movement (PLUS_DM/MINUS_DM)
  - Moving Average Convergence/Divergence (MACD)
  - Relative Strength Index (RSI)

- Moving Average Indicator (moving_average)
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Rolling/Smooth Moving Average(RMA/SMMA - both functions are same)
  - Moving Average Cross (MA_CROSS)

- Trend Indicator (trend)
  - Directional Index (PLUS_DI/MINUS_DI)
  - Directional Movement Index (DMI)
  - Average Directional Movement Index (ADX)

- Volatility Indicator (trend)
  - Average True Range (ATR)
  - True Range (TRANGE)

- Other
  - Average Gain & Loss (AVG_GAIN, AVG_LOSS)
  - Cross (CROSSOVER & CROSSUNDER)

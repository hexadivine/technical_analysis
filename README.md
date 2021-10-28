# Technical Analysis

A pure python library to perform technical analysis in a very efficient way without installing any dependencies other than numpy.


## Why to use this library
- Does not require any other dependencies or packages to be installed on the system to perform technical analysis like ta-lib.
- Library's structure and code is easy to understand as compared to ta-lib or any other library.
- Works flawlessly with below parameter as a datatype
  - Numpy Arrays
  - Pandas Dataframes
  - Python Lists
- This library uses numpy library to perform arithmetic operations 
- This library will support 139+ indicators (currently supports 5)
- Easy to install and it is a cross platform library.


## Installation

```
pip install -U git+https://github.com/h3x4d1v1n3/technical_analysis
```
  
## Supported Functions

| Sr. No. | Function Name |           Indicator name           |
|:-------:|:-------------:|:----------------------------------:|
|    1    |      ADX      | Average Directional Movement Index |
|    2    |      ATR      |         Average True Range         |
|    3    |      SMA      |        Simple Moving Average       |
|  ***4***   |      ***SMMA***     |       ***Smoothed Moving Average***      |
|    5    |       TRANGE      |             True Range             |



## Functions To Add

| Sr. No. |    Function Name    |                        Indicator name                        |
|:-------:|:-------------------:|:------------------------------------------------------------:|
|    1    |          AD         |                       Chaikin A/D Line                       |
|    2    |        ADOSC        |                    Chaikin A/D Oscillator                    |
|    3    |         ADXR        |           Average Directional Movement Index Rating          |
|    4    |         APO         |                   Absolute Price Oscillator                  |
|    5    |        AROON        |                             Aroon                            |
|    6    |       AROONOSC      |                       Aroon Oscillator                       |
|    7    |       AVGPRICE      |                         Average Price                        |
|    8    |        BBANDS       |                        Bollinger Bands                       |
|    9    |         BETA        |                             Beta                             |
|    10   |         BOP         |                       Balance Of Power                       |
|    11   |         CCI         |                    Commodity Channel Index                   |
|    12   |      CDL2CROWS      |                           Two Crows                          |
|    13   |    CDL3BLACKCROWS   |                       Three Black Crows                      |
|    14   |      CDL3INSIDE     |                     Three Inside Up/Down                     |
|    15   |    CDL3LINESTRIKE   |                       Three-Line Strike                      |
|    16   |     CDL3OUTSIDE     |                     Three Outside Up/Down                    |
|    17   |   CDL3STARSINSOUTH  |                   Three Stars In The South                   |
|    18   |  CDL3WHITESOLDIERS  |                Three Advancing White Soldiers                |
|    19   |   CDLABANDONEDBABY  |                        Abandoned Baby                        |
|    20   |   CDLADVANCEBLOCK   |                         Advance Block                        |
|    21   |     CDLBELTHOLD     |                           Belt-hold                          |
|    22   |     CDLBREAKAWAY    |                           Breakaway                          |
|    23   |  CDLCLOSINGMARUBOZU |                       Closing Marubozu                       |
|    24   | CDLCONCEALBABYSWALL |                    Concealing Baby Swallow                   |
|    25   |   CDLCOUNTERATTACK  |                         Counterattack                        |
|    26   |  CDLDARKCLOUDCOVER  |                       Dark Cloud Cover                       |
|    27   |       CDLDOJI       |                             Doji                             |
|    28   |     CDLDOJISTAR     |                           Doji Star                          |
|    29   |   CDLDRAGONFLYDOJI  |                        Dragonfly Doji                        |
|    30   |     CDLENGULFING    |                       Engulfing Pattern                      |
|    31   |  CDLEVENINGDOJISTAR |                       Evening Doji Star                      |
|    32   |    CDLEVENINGSTAR   |                         Evening Star                         |
|    33   | CDLGAPSIDESIDEWHITE |             Up/Down-gap side-by-side white lines             |
|    34   |  CDLGRAVESTONEDOJI  |                        Gravestone Doji                       |
|    35   |      CDLHAMMER      |                            Hammer                            |
|    36   |    CDLHANGINGMAN    |                          Hanging Man                         |
|    37   |      CDLHARAMI      |                        Harami Pattern                        |
|    38   |    CDLHARAMICROSS   |                     Harami Cross Pattern                     |
|    39   |     CDLHIGHWAVE     |                       High-Wave Candle                       |
|    40   |      CDLHIKKAKE     |                        Hikkake Pattern                       |
|    41   |    CDLHIKKAKEMOD    |                   Modified Hikkake Pattern                   |
|    42   |   CDLHOMINGPIGEON   |                         Homing Pigeon                        |
|    43   |  CDLIDENTICAL3CROWS |                     Identical Three Crows                    |
|    44   |      CDLINNECK      |                        In-Neck Pattern                       |
|    45   |  CDLINVERTEDHAMMER  |                        Inverted Hammer                       |
|    46   |      CDLKICKING     |                            Kicking                           |
|    47   |  CDLKICKINGBYLENGTH |     Kicking - bull/bear determined by the longer marubozu    |
|    48   |   CDLLADDERBOTTOM   |                         Ladder Bottom                        |
|    49   |  CDLLONGLEGGEDDOJI  |                       Long Legged Doji                       |
|    50   |     CDLLONGLINE     |                       Long Line Candle                       |
|    51   |     CDLMARUBOZU     |                           Marubozu                           |
|    52   |    CDLMATCHINGLOW   |                         Matching Low                         |
|    53   |      CDLMATHOLD     |                           Mat Hold                           |
|    54   |  CDLMORNINGDOJISTAR |                       Morning Doji Star                      |
|    55   |    CDLMORNINGSTAR   |                         Morning Star                         |
|    56   |      CDLONNECK      |                        On-Neck Pattern                       |
|    57   |     CDLPIERCING     |                       Piercing Pattern                       |
|    58   |    CDLRICKSHAWMAN   |                         Rickshaw Man                         |
|    59   | CDLRISEFALL3METHODS |                 Rising/Falling Three Methods                 |
|    60   |  CDLSEPARATINGLINES |                       Separating Lines                       |
|    61   |   CDLSHOOTINGSTAR   |                         Shooting Star                        |
|    62   |     CDLSHORTLINE    |                       Short Line Candle                      |
|    63   |    CDLSPINNINGTOP   |                         Spinning Top                         |
|    64   |  CDLSTALLEDPATTERN  |                        Stalled Pattern                       |
|    65   |   CDLSTICKSANDWICH  |                        Stick Sandwich                        |
|    66   |      CDLTAKURI      |      Takuri (Dragonfly Doji with very long lower shadow)     |
|    67   |     CDLTASUKIGAP    |                          Tasuki Gap                          |
|    68   |     CDLTHRUSTING    |                       Thrusting Pattern                      |
|    69   |      CDLTRISTAR     |                        Tristar Pattern                       |
|    70   |   CDLUNIQUE3RIVER   |                        Unique 3 River                        |
|    71   |  CDLUPSIDEGAP2CROWS |                     Upside Gap Two Crows                     |
|    72   | CDLXSIDEGAP3METHODS |               Upside/Downside Gap Three Methods              |
|    73   |         CMO         |                  Chande Momentum Oscillator                  |
|    74   |        CORREL       |             Pearson's Correlation Coefficient (r)            |
|    75   |         DEMA        |               Double Exponential Moving Average              |
|    76   |          DX         |                  Directional Movement Index                  |
|    77   |         EMA         |                  Exponential Moving Average                  |
|    78   |     HT_DCPERIOD     |           Hilbert Transform - Dominant Cycle Period          |
|    79   |      HT_DCPHASE     |           Hilbert Transform - Dominant Cycle Phase           |
|    80   |      HT_PHASOR      |             Hilbert Transform - Phasor Components            |
|    81   |       HT_SINE       |                 Hilbert Transform - SineWave                 |
|    82   |     HT_TRENDLINE    |          Hilbert Transform - Instantaneous Trendline         |
|    83   |     HT_TRENDMODE    |            Hilbert Transform - Trend vs Cycle Mode           |
|    84   |         KAMA        |                Kaufman Adaptive Moving Average               |
|    85   |      LINEARREG      |                       Linear Regression                      |
|    86   |   LINEARREG_ANGLE   |                    Linear Regression Angle                   |
|    87   | LINEARREG_INTERCEPT |                  Linear Regression Intercept                 |
|    88   |   LINEARREG_SLOPE   |                    Linear Regression Slope                   |
|    89   |          MA         |                      All Moving Average                      |
|    90   |         MACD        |             Moving Average Convergence/Divergence            |
|    91   |       MACDEXT       |                MACD with controllable MA type                |
|    92   |       MACDFIX       |        Moving Average Convergence/Divergence Fix 12/26       |
|    93   |         MAMA        |                 MESA Adaptive Moving Average                 |
|    94   |         MAX         |             Highest value over a specified period            |
|    95   |       MAXINDEX      |        Index of highest value over a specified period        |
|    96   |       MEDPRICE      |                         Median Price                         |
|    97   |         MFI         |                       Money Flow Index                       |
|    98   |       MIDPOINT      |                     MidPoint over period                     |
|    99   |       MIDPRICE      |                  Midpoint Price over period                  |
|   100   |         MIN         |             Lowest value over a specified period             |
|   101   |       MININDEX      |         Index of lowest value over a specified period        |
|   102   |        MINMAX       |       Lowest and highest values over a specified period      |
|   103   |     MINMAXINDEX     | Indexes of lowest and highest values over a specified period |
|   104   |       MINUS_DI      |                  Minus Directional Indicator                 |
|   105   |       MINUS_DM      |                  Minus Directional Movement                  |
|   106   |         MOM         |                           Momentum                           |
|   107   |         NATR        |                 Normalized Average True Range                |
|   108   |         OBV         |                       On Balance Volume                      |
|   109   |       PLUS_DI       |                  Plus Directional Indicator                  |
|   110   |       PLUS_DM       |                   Plus Directional Movement                  |
|   111   |         PPO         |                  Percentage Price Oscillator                 |
|   112   |         ROC         |          Rate of change : ((price/prevPrice)-1)*100          |
|   113   |         ROCP        |    Rate of change Percentage: (price-prevPrice)/prevPrice    |
|   114   |         ROCR        |            Rate of change ratio: (price/prevPrice)           |
|   115   |       ROCR100       |     Rate of change ratio 100 scale: (price/prevPrice)*100    |
|   116   |         RSI         |                    Relative Strength Index                   |
|   117   |         SAR         |                         Parabolic SAR                        |
|   118   |        SAREXT       |                   Parabolic SAR - Extended                   |
|   119   |        STDDEV       |                      Standard Deviation                      |
|   120   |        STOCH        |                          Stochastic                          |
|   121   |        STOCHF       |                        Stochastic Fast                       |
|   122   |       STOCHRSI      |              Stochastic Relative Strength Index              |
|   123   |         SUM         |                           Summation                          |
|   124   |          T3         |            Triple Exponential Moving Average (T3)            |
|   125   |         TEMA        |               Triple Exponential Moving Average              |
|   126   |        TRIMA        |                   Triangular Moving Average                  |
|   127   |         TRIX        |       1-day Rate-Of-Change (ROC) of a Triple Smooth EMA      |
|   128   |         TSF         |                     Time Series Forecast                     |
|   129   |       TYPPRICE      |                         Typical Price                        |
|   130   |        ULTOSC       |                      Ultimate Oscillator                     |
|   131   |         VAR         |                           Variance                           |
|   132   |       WCLPRICE      |                     Weighted Close Price                     |
|   133   |        WILLR        |                         Williams' %R                         |
|   134   |         WMA         |                    Weighted Moving Average                   |

> bold styling denotes functions that are not supported by ta-lib  

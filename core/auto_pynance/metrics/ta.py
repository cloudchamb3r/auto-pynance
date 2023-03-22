import talib

def bbands(close, timeperiod : int=5, nbdevup : int=2, nbdevdn : int=2, matype : int=0):
    return talib.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)

def dema(close, timeperiod : int=30):
    return talib.DEMA(close, timeperiod)

def ema(close, timeperiod : int=30):
    return talib.EMA(close, timeperiod)

def ht_trendline(close):
    return talib.HT_TRENDLINE(close)

def kama(close, timeperiod: int = 30):
    return talib.KAMA(close, timeperiod)

def ma(close, timeperiod: int = 30, matype : int= 0):
    return talib.MA(close, timeperiod, matype)

def mama(close, fastlimit: int=0, slowlimit: int=0):
    return talib.MAMA(close, fastlimit, slowlimit)

def mavp(close, periods, minperiod: int = 2, maxperiod : int = 30, matype : int = 0):
    return talib.MABVP(close, periods, minperiod, maxperiod, matype)

def midpoint(close, timeperiod : int = 14):
    return talib.MIDPOINT(close, timeperiod)

def midprice(low, high, timeperiod : int = 14):
    return talib.MIDPRICE(low, high, timeperiod)

def sar(high, low, acceleration :int= 0, maximum :int= 0):
    return talib.SAR(high, low, acceleration, maximum)

def sarext(high, low, startvalue:int=0, offsetonreverse:int=0, accelerationinitlong:int=0, accelerationlong:int=0, accelerationmaxlong:int=0, accelerationinitshort:int=0, accelerationshort:int=0, accelerationmaxshort:int=0):
    return talib.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)

def sma(close, timeperiod : int=30):
    return talib.SMA(close, timeperiod)

def t3(close, timeperiod : int=5, vfactor :int=0):
    return talib.T3(close, timeperiod, vfactor)

def tema(close, timeperiod : int=30):
    return talib.TEMA(close, timeperiod)

def trima(close, timeperiod:int=30):
    return talib.TRIMA(close, timeperiod)

def wma(close, timeperiod: int=30):
    return talib.WMA(close, timeperiod)

### Momentum Indicator Functions

def adx(high, low, close, timeperiod : int= 14):
    return talib.ADX(high, low, close, timeperiod)

def adxr(high, low, close, timeperiod : int = 14):
    return talib.ADXR(high, low, close, timeperiod)

def apo(close, fastperiod : int = 12, slowperiod :int = 26 , matype: int = 0):
    return talib.APO(close, fastperiod, slowperiod, matype)

def aproon(high, low, timeperiod: int = 14):
    return talib.APROON(high, low, timeperiod)

def aroonosc(high, low, timeperiod: int = 14):
    return talib.AROONOSC(high, low, timeperiod)

def bop(open, high, low, close):
    return talib.BOP(open, high, low, close)

def cci(high, low, close, timeperiod: int = 14):
    return talib.CCI(high, low, close, timeperiod)

def cmo(close, timeperiod: int = 14):
    return talib.CMO(close, timeperiod)

def dx(high, low, close, timeperiod: int = 14):
    return talib.DX(high, low, close, timeperiod)

def macd(close, fastperiod: int = 12, slowperiod: int = 26, signalperiod: int = 9):
    return talib.MACD(close, fastperiod, slowperiod, signalperiod)

def macdext(close, fastperiod:int=12, fastmatype:int=0, slowperiod:int=26, slowmatype:int=0, signalperiod:int=9, signalmatype :int=0):
    return talib.MACDEXT(close, fastperiod, fastmatype , slowperiod, slowmatype, signalperiod, signalmatype)

def macdfix(close, signalperiod: int=9):
    return talib.MACDFIX(close, signalperiod)

def mfi(high, low, close, volume, timeperiod: int=14):
    return talib.MFI(high, low, close, volume, timeperiod)

def minus_di(high, low, close, timeperiod: int=14):
    return talib.MINUS_DI(high, low, close, timeperiod)

def minus_dm(high, low, timeperiod: int=14):
    return talib.MINUS_DM(high, low, timeperiod)

def mom(close, timeperiod: int=10):
    return talib.MOM(close, timeperiod)

def plus_di(high, low, close, timeperiod: int=14):
    return talib.PLUS_DI(high, low, close, timeperiod)

def plus_dm(high, low, timeperiod: int=14):
    return talib.PLUS_DM(high, low, timeperiod)

def ppo(close, fastperiod: int=12, slowperiod: int=26, matype: int=0):
    return talib.PPO(close, fastperiod, slowperiod, matype)

def roc(close, timeperiod: int=10):
    return talib.ROC(close, timeperiod)

def rocp(close, timeperiod: int=10):
    return talib.ROCP(close, timeperiod)

def rocr(close, timeperiod: int=10):
    return talib.ROCR(close, timeperiod)

def rocr100(close, timeperiod: int=10):
    return talib.ROCR100(close, timeperiod)

def rsi(close, timeperiod: int=14):
    return talib.RSI(close, timeperiod)

def stoch(high, low, close, fastk_period:int=5, slowk_period:int=3, slowk_matype:int=0, slowd_period:int=3, slowd_matype:int=0):
    return talib.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)

def stochf(high, low, close, fastk_period: int=5, fastd_period: int=3, fastd_matype: int=0):
    return talib.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)

def stochrsi(close, timeperiod: int=14, fastk_period: int=5, fastd_period: int=3, fastd_matype: int=0):
    return talib.STOCHRSI(close, timeperiod, fastk_period, fastd_period, fastd_matype)

def trix(close, timeperiod: int=30):
    return talib.TRIX(close, timeperiod)

def ultosc(high, low, close, timeperiod1: int=7, timeperiod2: int=14, timeperiod3: int=28):
    return talib.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)

def willr(high, low, close, timeperiod: int=14):
    return talib.WILLR(high, low, close, timeperiod)

# Volume Indicator Functions

def ad(high, low, close, volume):
    return talib.AD(high, low, close, volume)

def adosc(high, low, close, volume, fastperiod: int = 3, slowperiod: int = 10):
    return talib.ADOSC(high, low, close, volume, fastperiod, slowperiod)

def obv(close, volume):
    return talib.OBV(close, volume)

# Cycle Indicator Functions

def ht_dcperiod(close):
    return talib.HT_DCPERIOD(close)

def ht_dcphase(close):
    return talib.HT_DCPHASE(close)

def ht_phasor(close):
    return talib.HT_PHASOR(close)

def ht_sine(close):
    return talib.HT_SINE(close)

def ht_trendmode(close):
    return talib.HT_TRENDMODE(close)


# Price Transform

def avgprice(open, high, low, close):
    return talib.AVGPRICE(open, high, low, close)

def medprice(high, low):
    return talib.MEDPRICE(high, low)

def typprice(high, low, close):
    return talib.TYPPRICE(high, low, close)

def wclprice(high, low, close):
    return talib.WCLPRICE(high, low, close)


# Volatility Indicator Functions

def atr(high, low, close, timeperiod: int = 14):
    return talib.ATR(high, low, close, timeperiod)

def natr(high, low, close, timeperiod: int = 14):
    return talib.NATR(high, low, close, timeperiod)

def trange(high, low, close):
    return talib.TRANGE(high, low, close)


# Pattern Recognition Functions
def cdl2crows(open, high, low, close):
    return talib.CDL2CROWS(open, high, low, close)

def cdl3blackrows(open, high, low, close):
    return talib.CDL3BLACKCROWS(open, high, low, close)

def cdl3inside(open, high, low, close):
    return talib.CDL3INSIDE(open, high, low, close)

def cdl3linestrike(open, high, low, close):
    return talib.CDL3LINESTRIKE(open, high, low, close)

def cdl3outside(open, high, low, close):
    return talib.CDL3OUTSIDE(open, high, low, close)

def cdl3starsinsouth(open, high, low, close):
    return talib.CDL3STARSINSOUTH(open, high, low, close)

def cdl3whitesoldiers(open, high, low, close):
    return talib.CDL3WHITESOLDIERS(open, high, low, close)

def cdlabandonedbaby(open, high, low, close, penetration: int = 0):
    return talib.CDLABANDONEDBABY(open, high, low, close, penetration)

def cdladvanceblock(open, high, low, close):
    return talib.CDLADVANCEBLOCK(open, high, low, close)

def cdlbelthold(open, high, low, close):
    return talib.CDLBELTHOLD(open, high, low, close)

def cdlbreakaway(open, high, low, close):
    return talib.CDLBREAKAWAY(open, high, low, close)

def cdlclosingmarubozu(open, high, low, close):
    return talib.CDLCLOSINGMARUBOZU(open, high, low, close)

def cdlconcealbabyswall(open, high, low, close):
    return talib.CDLCONCEALBABYSWALL(open, high, low, close)

def cdlcounterattack(open, high, low, close):
    return talib.CDLCOUNTERATTACK(open, high, low, close)

def cdldarkcloudcover(open, high, low, close, penetration: int = 0):
    return talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration)

def cdldoji(open, high, low, close):
    return talib.CDLDOJI(open, high, low, close)

def cdldojistar(open, high, low, close):
    return talib.CDLDOJISTAR(open, high, low, close)

def cdldragonflydoji(open, high, low, close):
    return talib.CDLDRAGONFLYDOJI(open, high, low, close)

def cdlengulfing(open, high, low, close):
    return talib.CDLENGULFING(open, high, low, close)

def cdleveningdojistar(open, high, low, close, penetration: int = 0):
    return talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration)

def cdleveningstar(open, high, low, close, penetration: int = 0):
    return talib.CDLEVENINGSTAR(open, high, low, close, penetration)

def cdlgapsidesidwhite(open, high, low, close):
    return talib.CDLGAPSIDESIDEWHITE(open, high, low, close)

def cdlgravestonedoji(open, high, low, close):
    return talib.CDLGRAVESTONEDOJI(open, high, low, close)

def cdlhammer(open, high, low, close):
    return talib.CDLHAMMER(open, high, low, close)

def cdlhangingman(open, high, low, close):
    return talib.CDLHANGINGMAN(open, high, low, close)

def cdlharami(open, high, low, close):
    return talib.CDLHARAMI(open, high, low, close)

def cdlharamicross(open, high, low, close):
    return talib.CDLHARAMICROSS(open, high, low, close)

def cdlhighwave(open, high, low, close):
    return talib.CDLHIGHWAVE(open, high, low, close)

def cdlhikkake(open, high, low, close):
    return talib.CDLHIKKAKE(open, high, low, close)

def cdlhikkakemod(open, high, low, close):
    return talib.CDLHIKKAKEMOD(open, high, low, close)

def cdlhomingpigeon(open, high, low, close):
    return talib.CDLHOMINGPIGEON(open, high, low, close)

def cdlidentical3cros(open, high, low, close):
    return talib.CDLIDENTICAL3CROWS(open, high, low, close)

def cdlinneck(open, high, low, close):
    return talib.CDLINNECK(open, high, low, close)

def cdlinvertedhammer(open, high, low, close):
    return talib.CDLINVERTEDHAMMER(open, high, low, close)

def cdlkicking(open, high, low, close):
    return talib.CDLKICKING(open, high, low, close)

def cdlkickingbylength(open, high, low, close):
    return talib.CDLKICKINGBYLENGTH(open, high, low, close)

def cdlladderbottom(open, high, low, close):
    return talib.CDLLADDERBOTTOM(open, high, low, close)

def cdllongleggeddoji(open, high, low, close):
    return talib.CDLLONGLEGGEDDOJI(open, high, low, close)

def cdllongline(open, high, low, close):
    return talib.CDLLONGLINE(open, high, low, close)

def cdlmarubozu(open, high, low, close):
    return talib.CDLMARUBOZU(open, high, low, close)

def cdlmatchinglow(open, high, low, close):
    return talib.CDLMATCHINGLOW(open, high, low, close)

def cdlmathold(open, high, low, close, penetration: int = 0):
    return talib.CDLMATHOLD(open, high, low, close, penetration)

def cdlmorningdojistar(open, high, low, close, penetration: int = 0):
    return talib.bCDLMORNINGDOJISTAR(open, high, low, close, penetration)

def cdlmorningstar(open, high, low, close, penetration: int = 0):
    return talib.CDLMORNINGSTAR(open, high, low, close, penetration)

def cdlonneck(open, high, low, close):
    return talib.CDLONNECK(open, high, low, close)

def cdlpiercing(open, high, low, close):
    return talib.CDLPIERCING(open, high, low, close)

def cdlrickshawman(open, high, low, close):
    return talib.CDLRICKSHAWMAN(open, high, low, close)

def cdlrisefall3methods(open, high, low, close):
    return talib.CDLRISEFALL3METHODS(open, high, low, close)

def cdlseparatinglines(open, high, low, close):
    return talib.CDLSEPARATINGLINES(open, high, low, close)

def cdlshootingstar(open, high, low, close):
    return talib.CDLSHOOTINGSTAR(open, high, low, close)

def cdlshortline(open, high, low, close):
    return talib.CDLSHORTLINE(open, high, low, close)

def cdlspinningtop(open, high, low, close):
    return talib.CDLSPINNINGTOP(open, high, low, close)

def cdlstalledpattern(open, high, low, close):
    return talib.CDLSTALLEDPATTERN(open, high, low, close)

def cdlsticksandwich(open, high, low, close):
    return talib.CDLSTICKSANDWICH(open, high, low, close)

def cdltakuri(open, high, low, close):
    return talib.CDLTAKURI(open, high, low, close)

def cdltasukigap(open, high, low, close):
    return talib.CDLTASUKIGAP(open, high, low, close)

def cdlthrusting(open, high, low, close):
    return talib.CDLTHRUSTING(open, high, low, close)

def cdltristar(open, high, low, close):
    return talib.CDLTRISTAR(open, high, low, close)

def cdlunique3river(open, high, low, close):
    return talib.CDLUNIQUE3RIVER(open, high, low, close)

def cdlupsidegap2crows(open, high, low, close):
    return talib.CDLUPSIDEGAP2CROWS(open, high, low, close)

def cdlxsidegap3methods(open, high, low, close):
    return talib.CDLXSIDEGAP3METHODS(open, high, low, close)

# Statistic Functions

def beta(high, low, timeperiod: int = 5):
    return talib.BETA(high, low, timeperiod)

def correl(high, low, timeperiod: int = 30):
    return talib.CORREL(high, low, timeperiod)

def linearreg(close, timeperiod: int = 14):
    return talib.LINEARREG(close, timeperiod)

def linearreg_angle(close, timeperiod: int = 14):
    return talib.LINEARREG_ANGLE(close, timeperiod)

def linearreg_intercept(close, timeperiod: int = 14):
    return talib.LINEARREG_INTERCEPT(close, timeperiod)

def linearreg_slope(close, timeperiod: int = 14):
    return talib.LINEARREG_SLOPE(close, timeperiod)

def stddev(close, timeperiod: int = 5, nbdev: int = 1):
    return talib.STDDEV(close, timeperiod, nbdev)

def tsf(close, timeperiod: int = 14):
    return talib.TSF(close, timeperiod)

def var(close, timeperiod: int = 5, nbdev: int = 1):
    return talib.VAR(close, timeperiod, nbdev)


# Math Transform Functions

def acos(close):
    return talib.ACOS(close)

def asin(close):
    return talib.ASIN(close)

def atan(close):
    return talib.ATAN(close)

def ceil(close):
    return talib.CEIL(close)

def cos(close):
    return talib.COS(close)

def cosh(close):
    return talib.COSH(close)

def exp(close):
    return talib.EXP(close)

def floor(close):
    return talib.FLOOR(close)

def ln(close):
    return talib.LN(close)

def log10(close):
    return talib.LOG10(close)

def sin(close):
    return talib.SIN(close)

def sinh(close):
    return talib.SINH(close)

def sqrt(close):
    return talib.SQRT(close)

def tan(close):
    return talib.TAN(close)

def tanh(close):
    return talib.TANH(close)

def add(high, low):
    return talib.ADD(high, low)

def div(high, low):
    return talib.DIV(high, low)

def max(close, timeperiod: int = 30):
    return talib.MAX(close, timeperiod)

def maxindex(close, timeperiod: int = 30):
    return talib.MAXINDEX(close, timeperiod)

def min(close, timeperiod: int = 30):
    return talib.MIN(close, timeperiod)

def minindex(close, timeperiod: int = 30):
    return talib.MININDEX(close, timeperiod)

def minmax(close, timeperiod: int = 30):
    return talib.MINMAX(close, timeperiod)

def minmaxindex(close, timeperiod: int = 30):
    return talib.MINMAXINDEX(close, timeperiod)

def mult(high, low):
    return talib.MULT(high, low)

def sub(high , low):
    return talib.SUB(high, low)

def sum(close, timeperiod: int = 30):
    return talib.SUM(close, timeperiod)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#-*- coding: utf-8 -*-\n",
    "import sys\n",
    "reload(sys)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 그래프를 노트북 안에 그리기 위해 설정\n",
    "%matplotlib inline\n",
    "\n",
    "# 필요한 패키지와 라이브러리를 가져옴\n",
    "import matplotlib as mpl\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.font_manager as fm\n",
    "\n",
    "# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처\n",
    "mpl.rcParams['axes.unicode_minus'] = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>시간대</th>\n",
       "      <th>업종</th>\n",
       "      <th>통화건수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>3789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>9054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>치킨</td>\n",
       "      <td>21605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>피자</td>\n",
       "      <td>2170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>2410</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>8471</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1</td>\n",
       "      <td>치킨</td>\n",
       "      <td>11358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1</td>\n",
       "      <td>피자</td>\n",
       "      <td>1162</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>1652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>7499</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2</td>\n",
       "      <td>치킨</td>\n",
       "      <td>5870</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2</td>\n",
       "      <td>피자</td>\n",
       "      <td>830</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>3</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>1072</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>3</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>6416</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>3</td>\n",
       "      <td>치킨</td>\n",
       "      <td>3037</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>3</td>\n",
       "      <td>피자</td>\n",
       "      <td>531</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>4</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>775</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>4</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>5640</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>4</td>\n",
       "      <td>치킨</td>\n",
       "      <td>1603</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>4</td>\n",
       "      <td>피자</td>\n",
       "      <td>295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>5</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>796</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>5</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>4550</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>5</td>\n",
       "      <td>치킨</td>\n",
       "      <td>980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>5</td>\n",
       "      <td>피자</td>\n",
       "      <td>245</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>6</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>558</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>6</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>4142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>6</td>\n",
       "      <td>치킨</td>\n",
       "      <td>735</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>6</td>\n",
       "      <td>피자</td>\n",
       "      <td>240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>7</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>715</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>7</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>4838</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>66</th>\n",
       "      <td>16</td>\n",
       "      <td>치킨</td>\n",
       "      <td>52385</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>16</td>\n",
       "      <td>피자</td>\n",
       "      <td>32268</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>68</th>\n",
       "      <td>17</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>24561</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>17</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>86328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>17</td>\n",
       "      <td>치킨</td>\n",
       "      <td>95094</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>71</th>\n",
       "      <td>17</td>\n",
       "      <td>피자</td>\n",
       "      <td>44218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>72</th>\n",
       "      <td>18</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>30991</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>18</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>116342</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>18</td>\n",
       "      <td>치킨</td>\n",
       "      <td>145929</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>18</td>\n",
       "      <td>피자</td>\n",
       "      <td>59663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76</th>\n",
       "      <td>19</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>28240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>77</th>\n",
       "      <td>19</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>98778</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>19</td>\n",
       "      <td>치킨</td>\n",
       "      <td>146077</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>19</td>\n",
       "      <td>피자</td>\n",
       "      <td>56709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>20</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>20686</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>20</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>49628</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>20</td>\n",
       "      <td>치킨</td>\n",
       "      <td>118330</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>20</td>\n",
       "      <td>피자</td>\n",
       "      <td>44705</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84</th>\n",
       "      <td>21</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>15629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>85</th>\n",
       "      <td>21</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>18660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>86</th>\n",
       "      <td>21</td>\n",
       "      <td>치킨</td>\n",
       "      <td>102228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>87</th>\n",
       "      <td>21</td>\n",
       "      <td>피자</td>\n",
       "      <td>36124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>88</th>\n",
       "      <td>22</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>11567</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>89</th>\n",
       "      <td>22</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>11965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>22</td>\n",
       "      <td>치킨</td>\n",
       "      <td>84819</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>91</th>\n",
       "      <td>22</td>\n",
       "      <td>피자</td>\n",
       "      <td>22477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>92</th>\n",
       "      <td>23</td>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>7468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>23</td>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>9967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>23</td>\n",
       "      <td>치킨</td>\n",
       "      <td>47173</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>23</td>\n",
       "      <td>피자</td>\n",
       "      <td>6723</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>96 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    시간대           업종    통화건수\n",
       "0     0  음식점-족발/보쌈전문    3789\n",
       "1     0     음식점-중국음식    9054\n",
       "2     0           치킨   21605\n",
       "3     0           피자    2170\n",
       "4     1  음식점-족발/보쌈전문    2410\n",
       "5     1     음식점-중국음식    8471\n",
       "6     1           치킨   11358\n",
       "7     1           피자    1162\n",
       "8     2  음식점-족발/보쌈전문    1652\n",
       "9     2     음식점-중국음식    7499\n",
       "10    2           치킨    5870\n",
       "11    2           피자     830\n",
       "12    3  음식점-족발/보쌈전문    1072\n",
       "13    3     음식점-중국음식    6416\n",
       "14    3           치킨    3037\n",
       "15    3           피자     531\n",
       "16    4  음식점-족발/보쌈전문     775\n",
       "17    4     음식점-중국음식    5640\n",
       "18    4           치킨    1603\n",
       "19    4           피자     295\n",
       "20    5  음식점-족발/보쌈전문     796\n",
       "21    5     음식점-중국음식    4550\n",
       "22    5           치킨     980\n",
       "23    5           피자     245\n",
       "24    6  음식점-족발/보쌈전문     558\n",
       "25    6     음식점-중국음식    4142\n",
       "26    6           치킨     735\n",
       "27    6           피자     240\n",
       "28    7  음식점-족발/보쌈전문     715\n",
       "29    7     음식점-중국음식    4838\n",
       "..  ...          ...     ...\n",
       "66   16           치킨   52385\n",
       "67   16           피자   32268\n",
       "68   17  음식점-족발/보쌈전문   24561\n",
       "69   17     음식점-중국음식   86328\n",
       "70   17           치킨   95094\n",
       "71   17           피자   44218\n",
       "72   18  음식점-족발/보쌈전문   30991\n",
       "73   18     음식점-중국음식  116342\n",
       "74   18           치킨  145929\n",
       "75   18           피자   59663\n",
       "76   19  음식점-족발/보쌈전문   28240\n",
       "77   19     음식점-중국음식   98778\n",
       "78   19           치킨  146077\n",
       "79   19           피자   56709\n",
       "80   20  음식점-족발/보쌈전문   20686\n",
       "81   20     음식점-중국음식   49628\n",
       "82   20           치킨  118330\n",
       "83   20           피자   44705\n",
       "84   21  음식점-족발/보쌈전문   15629\n",
       "85   21     음식점-중국음식   18660\n",
       "86   21           치킨  102228\n",
       "87   21           피자   36124\n",
       "88   22  음식점-족발/보쌈전문   11567\n",
       "89   22     음식점-중국음식   11965\n",
       "90   22           치킨   84819\n",
       "91   22           피자   22477\n",
       "92   23  음식점-족발/보쌈전문    7468\n",
       "93   23     음식점-중국음식    9967\n",
       "94   23           치킨   47173\n",
       "95   23           피자    6723\n",
       "\n",
       "[96 rows x 3 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "d1 = pd.read_csv(\"../../static/statistics/del.csv\", names=['시간대', '업종', '통화건수'], header=None)\n",
    "d1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>업종</th>\n",
       "      <th>통화건수 합</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>음식점-족발/보쌈전문</td>\n",
       "      <td>240778</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>음식점-중국음식</td>\n",
       "      <td>1107161</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>치킨</td>\n",
       "      <td>981587</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>피자</td>\n",
       "      <td>450595</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            업종   통화건수 합\n",
       "0  음식점-족발/보쌈전문   240778\n",
       "1     음식점-중국음식  1107161\n",
       "2           치킨   981587\n",
       "3           피자   450595"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2 = pd.read_csv(\"../../static/statistics/del_food.csv\", names=['업종', '통화건수 합'], header=None)\n",
    "d2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>시간대</th>\n",
       "      <th>통화건수 합</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>36618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>23401</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>15851</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>11056</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>8313</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5</td>\n",
       "      <td>6571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6</td>\n",
       "      <td>5675</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7</td>\n",
       "      <td>6583</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8</td>\n",
       "      <td>9856</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>9</td>\n",
       "      <td>23539</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>10</td>\n",
       "      <td>66669</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>11</td>\n",
       "      <td>190701</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>12</td>\n",
       "      <td>227835</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>13</td>\n",
       "      <td>179271</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>14</td>\n",
       "      <td>137515</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>15</td>\n",
       "      <td>129367</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>16</td>\n",
       "      <td>160221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>17</td>\n",
       "      <td>250201</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>18</td>\n",
       "      <td>352925</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>19</td>\n",
       "      <td>329804</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>20</td>\n",
       "      <td>233349</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>21</td>\n",
       "      <td>172641</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>22</td>\n",
       "      <td>130828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>23</td>\n",
       "      <td>71331</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    시간대  통화건수 합\n",
       "0     0   36618\n",
       "1     1   23401\n",
       "2     2   15851\n",
       "3     3   11056\n",
       "4     4    8313\n",
       "5     5    6571\n",
       "6     6    5675\n",
       "7     7    6583\n",
       "8     8    9856\n",
       "9     9   23539\n",
       "10   10   66669\n",
       "11   11  190701\n",
       "12   12  227835\n",
       "13   13  179271\n",
       "14   14  137515\n",
       "15   15  129367\n",
       "16   16  160221\n",
       "17   17  250201\n",
       "18   18  352925\n",
       "19   19  329804\n",
       "20   20  233349\n",
       "21   21  172641\n",
       "22   22  130828\n",
       "23   23   71331"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3 = pd.read_csv(\"../../static/statistics/del_time.csv\", names=['시간대', '통화건수 합'], header=None)\n",
    "d3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import datetime\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# make up some data\n",
    "x = list(d3['시간대'])\n",
    "y = list(d3['통화건수 합'])\n",
    "\n",
    "# plot\n",
    "plt.plot(x,y)\n",
    "# beautify the x-labels\n",
    "plt.gcf().autofmt_xdate()\n",
    "plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.subplots as tls\n",
    "from plotly.subplots import make_subplots\n",
    "import cufflinks as cf\n",
    "import pandas as pd\n",
    "import plotly.graph_objects as go\n",
    "cf.go_offline()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0.875,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "0",
         "textinfo": "label",
         "title": {
          "text": "0시"
         },
         "type": "pie",
         "values": [
          3789,
          9054,
          21605,
          2170
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0.875,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "1",
         "textinfo": "label",
         "title": {
          "text": "1시"
         },
         "type": "pie",
         "values": [
          2410,
          8471,
          11358,
          1162
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0.875,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "2",
         "textinfo": "label",
         "title": {
          "text": "2시"
         },
         "type": "pie",
         "values": [
          1652,
          7499,
          5870,
          830
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0.875,
           1
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "3",
         "textinfo": "label",
         "title": {
          "text": "3시"
         },
         "type": "pie",
         "values": [
          1072,
          6416,
          3037,
          531
         ]
        },
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0.7,
           0.825
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "4",
         "textinfo": "label",
         "title": {
          "text": "4시"
         },
         "type": "pie",
         "values": [
          775,
          5640,
          1603,
          295
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0.7,
           0.825
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "5",
         "textinfo": "label",
         "title": {
          "text": "5시"
         },
         "type": "pie",
         "values": [
          796,
          4550,
          980,
          245
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0.7,
           0.825
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "6",
         "textinfo": "label",
         "title": {
          "text": "6시"
         },
         "type": "pie",
         "values": [
          558,
          4142,
          735,
          240
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0.7,
           0.825
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "7",
         "textinfo": "label",
         "title": {
          "text": "7시"
         },
         "type": "pie",
         "values": [
          715,
          4838,
          850,
          180
         ]
        },
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0.525,
           0.65
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "8",
         "textinfo": "label",
         "title": {
          "text": "8시"
         },
         "type": "pie",
         "values": [
          1214,
          7031,
          1231,
          380
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0.525,
           0.65
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "9",
         "textinfo": "label",
         "title": {
          "text": "9시"
         },
         "type": "pie",
         "values": [
          2915,
          16346,
          2633,
          1645
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0.525,
           0.65
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "10",
         "textinfo": "label",
         "title": {
          "text": "10시"
         },
         "type": "pie",
         "values": [
          7294,
          43201,
          7585,
          8589
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0.525,
           0.65
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "11",
         "textinfo": "label",
         "title": {
          "text": "11시"
         },
         "type": "pie",
         "values": [
          12652,
          137366,
          16956,
          23727
         ]
        },
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0.35,
           0.475
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "12",
         "textinfo": "label",
         "title": {
          "text": "12시"
         },
         "type": "pie",
         "values": [
          12525,
          159498,
          26471,
          29341
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0.35,
           0.475
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "13",
         "textinfo": "label",
         "title": {
          "text": "13시"
         },
         "type": "pie",
         "values": [
          11642,
          114199,
          26664,
          26766
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0.35,
           0.475
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "14",
         "textinfo": "label",
         "title": {
          "text": "14시"
         },
         "type": "pie",
         "values": [
          11371,
          73482,
          27736,
          24926
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0.35,
           0.475
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "15",
         "textinfo": "label",
         "title": {
          "text": "15시"
         },
         "type": "pie",
         "values": [
          12836,
          55612,
          34238,
          26681
         ]
        },
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0.175,
           0.3
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "16",
         "textinfo": "label",
         "title": {
          "text": "16시"
         },
         "type": "pie",
         "values": [
          17420,
          58148,
          52385,
          32268
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0.175,
           0.3
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "17",
         "textinfo": "label",
         "title": {
          "text": "17시"
         },
         "type": "pie",
         "values": [
          24561,
          86328,
          95094,
          44218
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0.175,
           0.3
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "18",
         "textinfo": "label",
         "title": {
          "text": "18시"
         },
         "type": "pie",
         "values": [
          30991,
          116342,
          145929,
          59663
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0.175,
           0.3
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "19",
         "textinfo": "label",
         "title": {
          "text": "19시"
         },
         "type": "pie",
         "values": [
          28240,
          98778,
          146077,
          56709
         ]
        },
        {
         "domain": {
          "x": [
           0,
           0.2125
          ],
          "y": [
           0,
           0.125
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "20",
         "textinfo": "label",
         "title": {
          "text": "20시"
         },
         "type": "pie",
         "values": [
          20686,
          49628,
          118330,
          44705
         ]
        },
        {
         "domain": {
          "x": [
           0.2625,
           0.475
          ],
          "y": [
           0,
           0.125
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "21",
         "textinfo": "label",
         "title": {
          "text": "21시"
         },
         "type": "pie",
         "values": [
          15629,
          18660,
          102228,
          36124
         ]
        },
        {
         "domain": {
          "x": [
           0.525,
           0.7375
          ],
          "y": [
           0,
           0.125
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "22",
         "textinfo": "label",
         "title": {
          "text": "22시"
         },
         "type": "pie",
         "values": [
          11567,
          11965,
          84819,
          22477
         ]
        },
        {
         "domain": {
          "x": [
           0.7875,
           1
          ],
          "y": [
           0,
           0.125
          ]
         },
         "hole": 0.4,
         "hoverinfo": "percent",
         "labels": [
          "음식점-족발/보쌈전문",
          "음식점-중국음식",
          "치킨",
          "피자"
         ],
         "name": "23",
         "textinfo": "label",
         "title": {
          "text": "23시"
         },
         "type": "pie",
         "values": [
          7468,
          9967,
          47173,
          6723
         ]
        }
       ],
       "layout": {
        "autosize": false,
        "height": 2000,
        "showlegend": false,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "시간대별 업종 배달량"
        },
        "width": 1200
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"53bddaa2-5f39-4c96-9d8b-4a3629af02f0\" class=\"plotly-graph-div\" style=\"height:2000px; width:1200px;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"53bddaa2-5f39-4c96-9d8b-4a3629af02f0\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        '53bddaa2-5f39-4c96-9d8b-4a3629af02f0',\n",
       "                        [{\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.875, 1.0]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"0\", \"textinfo\": \"label\", \"title\": {\"text\": \"0\\uc2dc\"}, \"type\": \"pie\", \"values\": [3789, 9054, 21605, 2170]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.875, 1.0]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"1\", \"textinfo\": \"label\", \"title\": {\"text\": \"1\\uc2dc\"}, \"type\": \"pie\", \"values\": [2410, 8471, 11358, 1162]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.875, 1.0]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"2\", \"textinfo\": \"label\", \"title\": {\"text\": \"2\\uc2dc\"}, \"type\": \"pie\", \"values\": [1652, 7499, 5870, 830]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.875, 1.0]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"3\", \"textinfo\": \"label\", \"title\": {\"text\": \"3\\uc2dc\"}, \"type\": \"pie\", \"values\": [1072, 6416, 3037, 531]}, {\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.7, 0.825]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"4\", \"textinfo\": \"label\", \"title\": {\"text\": \"4\\uc2dc\"}, \"type\": \"pie\", \"values\": [775, 5640, 1603, 295]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.7, 0.825]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"5\", \"textinfo\": \"label\", \"title\": {\"text\": \"5\\uc2dc\"}, \"type\": \"pie\", \"values\": [796, 4550, 980, 245]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.7, 0.825]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"6\", \"textinfo\": \"label\", \"title\": {\"text\": \"6\\uc2dc\"}, \"type\": \"pie\", \"values\": [558, 4142, 735, 240]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.7, 0.825]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"7\", \"textinfo\": \"label\", \"title\": {\"text\": \"7\\uc2dc\"}, \"type\": \"pie\", \"values\": [715, 4838, 850, 180]}, {\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.525, 0.65]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"8\", \"textinfo\": \"label\", \"title\": {\"text\": \"8\\uc2dc\"}, \"type\": \"pie\", \"values\": [1214, 7031, 1231, 380]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.525, 0.65]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"9\", \"textinfo\": \"label\", \"title\": {\"text\": \"9\\uc2dc\"}, \"type\": \"pie\", \"values\": [2915, 16346, 2633, 1645]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.525, 0.65]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"10\", \"textinfo\": \"label\", \"title\": {\"text\": \"10\\uc2dc\"}, \"type\": \"pie\", \"values\": [7294, 43201, 7585, 8589]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.525, 0.65]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"11\", \"textinfo\": \"label\", \"title\": {\"text\": \"11\\uc2dc\"}, \"type\": \"pie\", \"values\": [12652, 137366, 16956, 23727]}, {\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.35, 0.475]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"12\", \"textinfo\": \"label\", \"title\": {\"text\": \"12\\uc2dc\"}, \"type\": \"pie\", \"values\": [12525, 159498, 26471, 29341]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.35, 0.475]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"13\", \"textinfo\": \"label\", \"title\": {\"text\": \"13\\uc2dc\"}, \"type\": \"pie\", \"values\": [11642, 114199, 26664, 26766]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.35, 0.475]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"14\", \"textinfo\": \"label\", \"title\": {\"text\": \"14\\uc2dc\"}, \"type\": \"pie\", \"values\": [11371, 73482, 27736, 24926]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.35, 0.475]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"15\", \"textinfo\": \"label\", \"title\": {\"text\": \"15\\uc2dc\"}, \"type\": \"pie\", \"values\": [12836, 55612, 34238, 26681]}, {\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.175, 0.3]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"16\", \"textinfo\": \"label\", \"title\": {\"text\": \"16\\uc2dc\"}, \"type\": \"pie\", \"values\": [17420, 58148, 52385, 32268]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.175, 0.3]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"17\", \"textinfo\": \"label\", \"title\": {\"text\": \"17\\uc2dc\"}, \"type\": \"pie\", \"values\": [24561, 86328, 95094, 44218]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.175, 0.3]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"18\", \"textinfo\": \"label\", \"title\": {\"text\": \"18\\uc2dc\"}, \"type\": \"pie\", \"values\": [30991, 116342, 145929, 59663]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.175, 0.3]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"19\", \"textinfo\": \"label\", \"title\": {\"text\": \"19\\uc2dc\"}, \"type\": \"pie\", \"values\": [28240, 98778, 146077, 56709]}, {\"domain\": {\"x\": [0.0, 0.2125], \"y\": [0.0, 0.125]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"20\", \"textinfo\": \"label\", \"title\": {\"text\": \"20\\uc2dc\"}, \"type\": \"pie\", \"values\": [20686, 49628, 118330, 44705]}, {\"domain\": {\"x\": [0.2625, 0.475], \"y\": [0.0, 0.125]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"21\", \"textinfo\": \"label\", \"title\": {\"text\": \"21\\uc2dc\"}, \"type\": \"pie\", \"values\": [15629, 18660, 102228, 36124]}, {\"domain\": {\"x\": [0.525, 0.7375], \"y\": [0.0, 0.125]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"22\", \"textinfo\": \"label\", \"title\": {\"text\": \"22\\uc2dc\"}, \"type\": \"pie\", \"values\": [11567, 11965, 84819, 22477]}, {\"domain\": {\"x\": [0.7875, 1.0], \"y\": [0.0, 0.125]}, \"hole\": 0.4, \"hoverinfo\": \"percent\", \"labels\": [\"\\uc74c\\uc2dd\\uc810-\\uc871\\ubc1c/\\ubcf4\\uc308\\uc804\\ubb38\", \"\\uc74c\\uc2dd\\uc810-\\uc911\\uad6d\\uc74c\\uc2dd\", \"\\uce58\\ud0a8\", \"\\ud53c\\uc790\"], \"name\": \"23\", \"textinfo\": \"label\", \"title\": {\"text\": \"23\\uc2dc\"}, \"type\": \"pie\", \"values\": [7468, 9967, 47173, 6723]}],\n",
       "                        {\"autosize\": false, \"height\": 2000, \"showlegend\": false, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"\\uc2dc\\uac04\\ub300\\ubcc4 \\uc5c5\\uc885 \\ubc30\\ub2ec\\ub7c9\"}, \"width\": 1200},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('53bddaa2-5f39-4c96-9d8b-4a3629af02f0');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = tls.make_subplots(\n",
    "    rows=6, cols=4,\n",
    "    specs=[[{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}],\n",
    "           [{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}],\n",
    "           [{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}],\n",
    "           [{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}],\n",
    "           [{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}],\n",
    "           [{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"},{\"type\": \"pie\"}]]\n",
    ")\n",
    "\n",
    "v= d1.groupby('시간대').size().reset_index(name=\"통화건수\")\n",
    "time = list(v['시간대'])\n",
    "\n",
    "\n",
    "row = 1\n",
    "col = 1\n",
    "for i in time:\n",
    "    pie_data = d1[d1['시간대'] == i]\n",
    "\n",
    "    fig.append_trace(go.Pie(name=i, title=str(i)+\"시\", textinfo=\"label\", labels=pie_data['업종'], values=pie_data['통화건수']), row=row, col=col)\n",
    "\n",
    "    col += 1\n",
    "\n",
    "    if( col % 5 == 0):\n",
    "        col = 1\n",
    "        row += 1\n",
    "        \n",
    "fig.update_traces(hole=.4, hoverinfo=\"percent\")\n",
    "fig.update_layout(\n",
    "    title=\"시간대별 업종 배달량\",\n",
    "    autosize=False, \n",
    "    showlegend=False,\n",
    "    width=1200,\n",
    "    height=2000\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "mode": "lines+markers",
         "name": "lines+markers",
         "type": "scatter",
         "x": [
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23
         ],
         "y": [
          36618,
          23401,
          15851,
          11056,
          8313,
          6571,
          5675,
          6583,
          9856,
          23539,
          66669,
          190701,
          227835,
          179271,
          137515,
          129367,
          160221,
          250201,
          352925,
          329804,
          233349,
          172641,
          130828,
          71331
         ]
        }
       ],
       "layout": {
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "시간대별 배달량"
        },
        "xaxis": {
         "title": {
          "text": "시간대"
         }
        },
        "yaxis": {
         "title": {
          "text": "배달량"
         }
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"b584f9d0-d874-4bdb-9e0f-9d2ccd7c9df5\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"b584f9d0-d874-4bdb-9e0f-9d2ccd7c9df5\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        'b584f9d0-d874-4bdb-9e0f-9d2ccd7c9df5',\n",
       "                        [{\"mode\": \"lines+markers\", \"name\": \"lines+markers\", \"type\": \"scatter\", \"x\": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], \"y\": [36618, 23401, 15851, 11056, 8313, 6571, 5675, 6583, 9856, 23539, 66669, 190701, 227835, 179271, 137515, 129367, 160221, 250201, 352925, 329804, 233349, 172641, 130828, 71331]}],\n",
       "                        {\"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"\\uc2dc\\uac04\\ub300\\ubcc4 \\ubc30\\ub2ec\\ub7c9\"}, \"xaxis\": {\"title\": {\"text\": \"\\uc2dc\\uac04\\ub300\"}}, \"yaxis\": {\"title\": {\"text\": \"\\ubc30\\ub2ec\\ub7c9\"}}},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('b584f9d0-d874-4bdb-9e0f-9d2ccd7c9df5');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = d3['시간대']\n",
    "y = d3['통화건수 합']\n",
    "fig = go.Figure()\n",
    "fig.add_trace(go.Scatter(x=x, y=y,mode='lines+markers', name='lines+markers'))\n",
    "fig.update_layout(title='시간대별 배달량',\n",
    "                   xaxis_title='시간대',\n",
    "                   yaxis_title='배달량')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}



```python
# Import Dependencies
import json
import pandas as pd
import numpy as np
```


```python
#Change json into dataframe
data_df = pd.read_json('purchase_data.json')
```


```python
#Make dataframe easier to type by dropping df 
data = data_df
```


```python
#Find out what kind of data and memory this dataset has
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 780 entries, 0 to 779
    Data columns (total 6 columns):
    Age          780 non-null int64
    Gender       780 non-null object
    Item ID      780 non-null int64
    Item Name    780 non-null object
    Price        780 non-null float64
    SN           780 non-null object
    dtypes: float64(1), int64(2), object(3)
    memory usage: 42.7+ KB



```python
#Remember how to use columns
data.columns
```




    Index(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN'], dtype='object')




```python
data.isnull().values.any()
```




    False




```python
#Find some basic stats about the data
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>780.000000</td>
      <td>780.000000</td>
      <td>780.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>22.729487</td>
      <td>91.293590</td>
      <td>2.931192</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.930604</td>
      <td>52.707537</td>
      <td>1.115780</td>
    </tr>
    <tr>
      <th>min</th>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>1.030000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.000000</td>
      <td>44.000000</td>
      <td>1.960000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>22.000000</td>
      <td>91.000000</td>
      <td>2.880000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000000</td>
      <td>135.000000</td>
      <td>3.910000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>45.000000</td>
      <td>183.000000</td>
      <td>4.950000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Find total revenue
data['Price'].sum()
```




    2286.33




```python
#Look at the top of ten entries
data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Show all duplicate Screen Names
pd.concat(g for _, g in data.groupby("SN") if len(g) > 1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>308</th>
      <td>37</td>
      <td>Male</td>
      <td>79</td>
      <td>Alpha, Oath of Zeal</td>
      <td>2.88</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>377</th>
      <td>37</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>431</th>
      <td>37</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>224</th>
      <td>26</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>647</th>
      <td>26</td>
      <td>Male</td>
      <td>156</td>
      <td>Soul-Forged Steel Shortsword</td>
      <td>1.16</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>721</th>
      <td>26</td>
      <td>Male</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>529</th>
      <td>38</td>
      <td>Male</td>
      <td>172</td>
      <td>Blade of the Grave</td>
      <td>1.69</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>359</th>
      <td>20</td>
      <td>Male</td>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>Aeliriam77</td>
    </tr>
    <tr>
      <th>637</th>
      <td>20</td>
      <td>Male</td>
      <td>18</td>
      <td>Torchlight, Bond of Storms</td>
      <td>1.77</td>
      <td>Aeliriam77</td>
    </tr>
    <tr>
      <th>317</th>
      <td>22</td>
      <td>Male</td>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
      <td>Aeliru63</td>
    </tr>
    <tr>
      <th>333</th>
      <td>22</td>
      <td>Male</td>
      <td>30</td>
      <td>Stormcaller</td>
      <td>4.15</td>
      <td>Aeliru63</td>
    </tr>
    <tr>
      <th>62</th>
      <td>19</td>
      <td>Female</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeri84</td>
    </tr>
    <tr>
      <th>251</th>
      <td>19</td>
      <td>Female</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Aeri84</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>312</th>
      <td>29</td>
      <td>Male</td>
      <td>68</td>
      <td>Storm-Weaver, Slayer of Inception</td>
      <td>2.49</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>760</th>
      <td>29</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>661</th>
      <td>15</td>
      <td>Male</td>
      <td>172</td>
      <td>Blade of the Grave</td>
      <td>1.69</td>
      <td>Aerithnucal56</td>
    </tr>
    <tr>
      <th>765</th>
      <td>15</td>
      <td>Male</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Aerithnucal56</td>
    </tr>
    <tr>
      <th>307</th>
      <td>26</td>
      <td>Male</td>
      <td>180</td>
      <td>Stormcaller</td>
      <td>2.78</td>
      <td>Aidain51</td>
    </tr>
    <tr>
      <th>690</th>
      <td>26</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Aidain51</td>
    </tr>
    <tr>
      <th>82</th>
      <td>23</td>
      <td>Male</td>
      <td>46</td>
      <td>Hopeless Ebon Dualblade</td>
      <td>4.75</td>
      <td>Airi27</td>
    </tr>
    <tr>
      <th>607</th>
      <td>23</td>
      <td>Male</td>
      <td>38</td>
      <td>The Void, Vengeance of Dark Magic</td>
      <td>2.82</td>
      <td>Airi27</td>
    </tr>
    <tr>
      <th>43</th>
      <td>22</td>
      <td>Male</td>
      <td>68</td>
      <td>Storm-Weaver, Slayer of Inception</td>
      <td>2.49</td>
      <td>Alaephos75</td>
    </tr>
    <tr>
      <th>380</th>
      <td>22</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Alaephos75</td>
    </tr>
    <tr>
      <th>177</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>155</td>
      <td>War-Forged Gold Deflector</td>
      <td>3.73</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>709</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>97</th>
      <td>17</td>
      <td>Female</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Assassasta79</td>
    </tr>
    <tr>
      <th>532</th>
      <td>17</td>
      <td>Female</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assassasta79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>728</th>
      <td>22</td>
      <td>Male</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Tyananurgue44</td>
    </tr>
    <tr>
      <th>643</th>
      <td>31</td>
      <td>Male</td>
      <td>182</td>
      <td>Toothpick</td>
      <td>3.48</td>
      <td>Tyeosri53</td>
    </tr>
    <tr>
      <th>655</th>
      <td>31</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tyeosri53</td>
    </tr>
    <tr>
      <th>111</th>
      <td>19</td>
      <td>Male</td>
      <td>160</td>
      <td>Azurewrath</td>
      <td>2.22</td>
      <td>Tyirithnu40</td>
    </tr>
    <tr>
      <th>512</th>
      <td>19</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.39</td>
      <td>Tyirithnu40</td>
    </tr>
    <tr>
      <th>508</th>
      <td>38</td>
      <td>Male</td>
      <td>181</td>
      <td>Reaper's Toll</td>
      <td>4.56</td>
      <td>Tyisriphos58</td>
    </tr>
    <tr>
      <th>663</th>
      <td>38</td>
      <td>Male</td>
      <td>101</td>
      <td>Final Critic</td>
      <td>4.62</td>
      <td>Tyisriphos58</td>
    </tr>
    <tr>
      <th>79</th>
      <td>29</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Undirrala66</td>
    </tr>
    <tr>
      <th>107</th>
      <td>29</td>
      <td>Male</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Undirrala66</td>
    </tr>
    <tr>
      <th>131</th>
      <td>29</td>
      <td>Male</td>
      <td>62</td>
      <td>Piece Maker</td>
      <td>4.36</td>
      <td>Undirrala66</td>
    </tr>
    <tr>
      <th>537</th>
      <td>29</td>
      <td>Male</td>
      <td>18</td>
      <td>Torchlight, Bond of Storms</td>
      <td>1.77</td>
      <td>Undirrala66</td>
    </tr>
    <tr>
      <th>596</th>
      <td>29</td>
      <td>Male</td>
      <td>133</td>
      <td>Faith's Scimitar</td>
      <td>3.82</td>
      <td>Undirrala66</td>
    </tr>
    <tr>
      <th>375</th>
      <td>22</td>
      <td>Male</td>
      <td>42</td>
      <td>The Decapitator</td>
      <td>4.82</td>
      <td>Yadaisuir65</td>
    </tr>
    <tr>
      <th>660</th>
      <td>22</td>
      <td>Male</td>
      <td>73</td>
      <td>Ritual Mace</td>
      <td>3.74</td>
      <td>Yadaisuir65</td>
    </tr>
    <tr>
      <th>160</th>
      <td>25</td>
      <td>Male</td>
      <td>112</td>
      <td>Worldbreaker</td>
      <td>3.29</td>
      <td>Yadanun74</td>
    </tr>
    <tr>
      <th>207</th>
      <td>25</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>2.19</td>
      <td>Yadanun74</td>
    </tr>
    <tr>
      <th>275</th>
      <td>25</td>
      <td>Male</td>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>Yadanun74</td>
    </tr>
    <tr>
      <th>281</th>
      <td>40</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Yaralnura48</td>
    </tr>
    <tr>
      <th>478</th>
      <td>40</td>
      <td>Male</td>
      <td>168</td>
      <td>Sun Strike, Jaws of Twisted Visions</td>
      <td>2.64</td>
      <td>Yaralnura48</td>
    </tr>
    <tr>
      <th>291</th>
      <td>7</td>
      <td>Male</td>
      <td>53</td>
      <td>Vengeance Cleaver</td>
      <td>3.70</td>
      <td>Yarithsurgue62</td>
    </tr>
    <tr>
      <th>720</th>
      <td>7</td>
      <td>Male</td>
      <td>82</td>
      <td>Nirvana</td>
      <td>1.11</td>
      <td>Yarithsurgue62</td>
    </tr>
    <tr>
      <th>297</th>
      <td>24</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Yarolwen77</td>
    </tr>
    <tr>
      <th>686</th>
      <td>24</td>
      <td>Male</td>
      <td>46</td>
      <td>Hopeless Ebon Dualblade</td>
      <td>4.75</td>
      <td>Yarolwen77</td>
    </tr>
    <tr>
      <th>515</th>
      <td>40</td>
      <td>Male</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Yasriphos60</td>
    </tr>
    <tr>
      <th>527</th>
      <td>40</td>
      <td>Male</td>
      <td>55</td>
      <td>Vindictive Glass Edge</td>
      <td>4.26</td>
      <td>Yasriphos60</td>
    </tr>
    <tr>
      <th>545</th>
      <td>40</td>
      <td>Male</td>
      <td>171</td>
      <td>Scalpel</td>
      <td>3.62</td>
      <td>Yasriphos60</td>
    </tr>
    <tr>
      <th>241</th>
      <td>32</td>
      <td>Male</td>
      <td>135</td>
      <td>Warped Diamond Crusader</td>
      <td>4.66</td>
      <td>Yathecal72</td>
    </tr>
    <tr>
      <th>363</th>
      <td>32</td>
      <td>Male</td>
      <td>16</td>
      <td>Restored Bauble</td>
      <td>3.11</td>
      <td>Yathecal72</td>
    </tr>
    <tr>
      <th>376</th>
      <td>17</td>
      <td>Male</td>
      <td>33</td>
      <td>Curved Axe</td>
      <td>1.35</td>
      <td>Zhisrisu83</td>
    </tr>
    <tr>
      <th>437</th>
      <td>17</td>
      <td>Male</td>
      <td>82</td>
      <td>Nirvana</td>
      <td>1.11</td>
      <td>Zhisrisu83</td>
    </tr>
  </tbody>
</table>
<p>375 rows × 6 columns</p>
</div>




```python
#Remember how to use loc and look at the first row, all columns
data.loc[0, :]
```




    Age                                   38
    Gender                              Male
    Item ID                              165
    Item Name    Bone Crushing Silver Skewer
    Price                               3.37
    SN                             Aelalis34
    Name: 0, dtype: object




```python
#Remember how to use columns
data_df.columns
```




    Index(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN'], dtype='object')




```python
#Look for duplicates in the SN column
data.SN.duplicated().sum()
```




    207




```python
data.loc[data.SN.duplicated(keep=False), :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
    </tr>
    <tr>
      <th>13</th>
      <td>23</td>
      <td>Male</td>
      <td>77</td>
      <td>Piety, Guardian of Riddles</td>
      <td>3.68</td>
      <td>Seorithstilis90</td>
    </tr>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
    </tr>
    <tr>
      <th>15</th>
      <td>21</td>
      <td>Male</td>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>4.77</td>
      <td>Haellysu29</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Idai61</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>32</th>
      <td>19</td>
      <td>Male</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Malunil62</td>
    </tr>
    <tr>
      <th>33</th>
      <td>24</td>
      <td>Male</td>
      <td>90</td>
      <td>Betrayer</td>
      <td>1.67</td>
      <td>Iskimnya76</td>
    </tr>
    <tr>
      <th>38</th>
      <td>20</td>
      <td>Male</td>
      <td>25</td>
      <td>Hero Cane</td>
      <td>1.03</td>
      <td>Chamjasknya65</td>
    </tr>
    <tr>
      <th>43</th>
      <td>22</td>
      <td>Male</td>
      <td>68</td>
      <td>Storm-Weaver, Slayer of Inception</td>
      <td>2.49</td>
      <td>Alaephos75</td>
    </tr>
    <tr>
      <th>45</th>
      <td>20</td>
      <td>Male</td>
      <td>120</td>
      <td>Agatha</td>
      <td>1.91</td>
      <td>Eusur90</td>
    </tr>
    <tr>
      <th>47</th>
      <td>24</td>
      <td>Male</td>
      <td>141</td>
      <td>Persuasion</td>
      <td>3.27</td>
      <td>Saellyra72</td>
    </tr>
    <tr>
      <th>48</th>
      <td>20</td>
      <td>Male</td>
      <td>73</td>
      <td>Ritual Mace</td>
      <td>3.74</td>
      <td>Ililsa62</td>
    </tr>
    <tr>
      <th>49</th>
      <td>22</td>
      <td>Male</td>
      <td>151</td>
      <td>Severance</td>
      <td>1.85</td>
      <td>Eosur70</td>
    </tr>
    <tr>
      <th>50</th>
      <td>32</td>
      <td>Female</td>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>Saistyphos30</td>
    </tr>
    <tr>
      <th>51</th>
      <td>16</td>
      <td>Male</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Reula64</td>
    </tr>
    <tr>
      <th>52</th>
      <td>24</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Chanirrala39</td>
    </tr>
    <tr>
      <th>53</th>
      <td>22</td>
      <td>Male</td>
      <td>51</td>
      <td>Endbringer</td>
      <td>2.67</td>
      <td>Chadanto83</td>
    </tr>
    <tr>
      <th>58</th>
      <td>24</td>
      <td>Female</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Tyaeristi78</td>
    </tr>
    <tr>
      <th>59</th>
      <td>15</td>
      <td>Male</td>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>Ila44</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>709</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>711</th>
      <td>22</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Tyananurgue44</td>
    </tr>
    <tr>
      <th>715</th>
      <td>15</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Ila44</td>
    </tr>
    <tr>
      <th>720</th>
      <td>7</td>
      <td>Male</td>
      <td>82</td>
      <td>Nirvana</td>
      <td>1.11</td>
      <td>Yarithsurgue62</td>
    </tr>
    <tr>
      <th>721</th>
      <td>26</td>
      <td>Male</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>723</th>
      <td>20</td>
      <td>Male</td>
      <td>69</td>
      <td>Frenzy, Defender of the Harvest</td>
      <td>1.06</td>
      <td>Tillyrin30</td>
    </tr>
    <tr>
      <th>724</th>
      <td>13</td>
      <td>Female</td>
      <td>117</td>
      <td>Heartstriker, Legacy of the Light</td>
      <td>4.15</td>
      <td>Chanosiast43</td>
    </tr>
    <tr>
      <th>725</th>
      <td>15</td>
      <td>Male</td>
      <td>14</td>
      <td>Possessed Core</td>
      <td>1.59</td>
      <td>Quarusrion32</td>
    </tr>
    <tr>
      <th>728</th>
      <td>22</td>
      <td>Male</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Tyananurgue44</td>
    </tr>
    <tr>
      <th>735</th>
      <td>10</td>
      <td>Male</td>
      <td>16</td>
      <td>Restored Bauble</td>
      <td>3.11</td>
      <td>Ethrusuard41</td>
    </tr>
    <tr>
      <th>738</th>
      <td>25</td>
      <td>Male</td>
      <td>56</td>
      <td>Foul Titanium Battle Axe</td>
      <td>4.33</td>
      <td>Tyadaru49</td>
    </tr>
    <tr>
      <th>740</th>
      <td>19</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>2.19</td>
      <td>Farusrian86</td>
    </tr>
    <tr>
      <th>743</th>
      <td>20</td>
      <td>Male</td>
      <td>134</td>
      <td>Undead Crusader</td>
      <td>4.67</td>
      <td>Haedasu65</td>
    </tr>
    <tr>
      <th>744</th>
      <td>21</td>
      <td>Male</td>
      <td>130</td>
      <td>Alpha</td>
      <td>1.56</td>
      <td>Ialistidru50</td>
    </tr>
    <tr>
      <th>745</th>
      <td>20</td>
      <td>Male</td>
      <td>79</td>
      <td>Alpha, Oath of Zeal</td>
      <td>2.88</td>
      <td>Sweecossa42</td>
    </tr>
    <tr>
      <th>749</th>
      <td>21</td>
      <td>Male</td>
      <td>114</td>
      <td>Yearning Mageblade</td>
      <td>1.79</td>
      <td>Frichassala85</td>
    </tr>
    <tr>
      <th>751</th>
      <td>26</td>
      <td>Female</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Lisjasksda68</td>
    </tr>
    <tr>
      <th>753</th>
      <td>20</td>
      <td>Male</td>
      <td>4</td>
      <td>Bloodlord's Fetish</td>
      <td>2.28</td>
      <td>Thryallym62</td>
    </tr>
    <tr>
      <th>754</th>
      <td>31</td>
      <td>Male</td>
      <td>104</td>
      <td>Gladiator's Glaive</td>
      <td>1.36</td>
      <td>Sondastan54</td>
    </tr>
    <tr>
      <th>757</th>
      <td>35</td>
      <td>Male</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Seosri62</td>
    </tr>
    <tr>
      <th>759</th>
      <td>19</td>
      <td>Male</td>
      <td>87</td>
      <td>Deluge, Edge of the West</td>
      <td>2.20</td>
      <td>Chanirrasta87</td>
    </tr>
    <tr>
      <th>760</th>
      <td>29</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>762</th>
      <td>36</td>
      <td>Male</td>
      <td>52</td>
      <td>Hatred</td>
      <td>4.39</td>
      <td>Lisosiast26</td>
    </tr>
    <tr>
      <th>763</th>
      <td>27</td>
      <td>Other / Non-Disclosed</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Eurisuru25</td>
    </tr>
    <tr>
      <th>765</th>
      <td>15</td>
      <td>Male</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Aerithnucal56</td>
    </tr>
    <tr>
      <th>767</th>
      <td>20</td>
      <td>Male</td>
      <td>122</td>
      <td>Unending Tyranny</td>
      <td>1.21</td>
      <td>Hailaphos89</td>
    </tr>
    <tr>
      <th>774</th>
      <td>24</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>1.14</td>
      <td>Lassassast73</td>
    </tr>
    <tr>
      <th>775</th>
      <td>22</td>
      <td>Male</td>
      <td>98</td>
      <td>Deadline, Voice Of Subtlety</td>
      <td>3.62</td>
      <td>Eural50</td>
    </tr>
    <tr>
      <th>776</th>
      <td>14</td>
      <td>Male</td>
      <td>104</td>
      <td>Gladiator's Glaive</td>
      <td>1.36</td>
      <td>Lirtossa78</td>
    </tr>
    <tr>
      <th>777</th>
      <td>20</td>
      <td>Male</td>
      <td>117</td>
      <td>Heartstriker, Legacy of the Light</td>
      <td>4.15</td>
      <td>Tillyrin30</td>
    </tr>
  </tbody>
</table>
<p>375 rows × 6 columns</p>
</div>




```python
# Find total revenue
data.Price.sum()
```




    2286.33




```python
new_df= data.loc[data.SN.duplicated(keep=False), :]
```


```python
new = new_df
```


```python
new.SN.count()
```




    375




```python
#Find counts for Gender column
new.Gender.value_counts()
```




    Male                     302
    Female                    67
    Other / Non-Disclosed      6
    Name: Gender, dtype: int64




```python
#Count number of gender types
gc = new.Gender.value_counts()
```


```python
tot_g = new.Gender.count()
```


```python
#Find percentages of gender 
g_pct = (gc/tot_g)*100
print(g_pct)
```

    Male                     80.533333
    Female                   17.866667
    Other / Non-Disclosed     1.600000
    Name: Gender, dtype: float64



```python
#Average Price for Females
data[data.Gender=='Female'].Price.mean()
```




    2.815514705882352




```python
#Total Revenue Females
data[data.Gender=='Female'].Price.sum()
```




    382.90999999999997




```python
#Total Count Females
data[data.Gender=='Female'].Gender.count()
```




    136




```python
#Average Price for Males
data[data.Gender=='Male'].Price.mean()
```




    2.9505213270142154




```python
#Total Count Males
data[data.Gender=='Male'].Gender.count()
```




    633




```python
#Total Revenue Males
data[data.Gender=='Male'].Price.sum()
```




    1867.68




```python
#Average Price for Neither Female or Male
data[data.Gender == 'Other / Non-Disclosed'].Price.mean()
```




    3.2490909090909086




```python
#Total Revenue Neither Female or Male
data[data.Gender == 'Other / Non-Disclosed'].Price.sum()
```




    35.739999999999995




```python
#Total Counts Gender
data.Gender.value_counts()
```




    Male                     633
    Female                   136
    Other / Non-Disclosed     11
    Name: Gender, dtype: int64




```python
data.groupby('Gender').Price.agg(['count','sum', 'mean'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>sum</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Define age bins
bins = [0, 10, 14, 19, 24, 29, 34, 39, 100]
```


```python
#Name age bins
age_group= ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+' ]
```


```python
data['AgeGroup'] = pd.cut(data['Age'], bins, labels=age_group)
```


```python
data.groupby('AgeGroup').Price.agg(['count','sum', 'mean'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>sum</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>AgeGroup</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>96.62</td>
      <td>3.019375</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>83.79</td>
      <td>2.702903</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>386.42</td>
      <td>2.905414</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>978.77</td>
      <td>2.913006</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>370.33</td>
      <td>2.962640</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>197.25</td>
      <td>3.082031</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>119.40</td>
      <td>2.842857</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>53.75</td>
      <td>3.161765</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Big Spenders
bs = data.groupby(['SN']).sum().sort_values("Price", ascending=False)
bs= bs.head(5)

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-90-6677e01b9106> in <module>()
          1 #Big Spenders
    ----> 2 bs = data.groupby(['SN']).sum().sort_values("Price", ascending=False)
          3 bs= bs.head(5)


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in groupby(self, by, axis, level, as_index, sort, group_keys, squeeze, **kwargs)
       5160         return groupby(self, by=by, axis=axis, level=level, as_index=as_index,
       5161                        sort=sort, group_keys=group_keys, squeeze=squeeze,
    -> 5162                        **kwargs)
       5163 
       5164     def asfreq(self, freq, method=None, how=None, normalize=False,


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in groupby(obj, by, **kwds)
       1846         raise TypeError('invalid type: %s' % type(obj))
       1847 
    -> 1848     return klass(obj, by, **kwds)
       1849 
       1850 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in __init__(self, obj, keys, axis, level, grouper, exclusions, selection, as_index, sort, group_keys, squeeze, **kwargs)
        514                                                     level=level,
        515                                                     sort=sort,
    --> 516                                                     mutated=self.mutated)
        517 
        518         self.obj = obj


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/groupby.py in _get_grouper(obj, key, axis, level, sort, mutated, validate)
       2932                 in_axis, name, level, gpr = False, None, gpr, None
       2933             else:
    -> 2934                 raise KeyError(gpr)
       2935         elif isinstance(gpr, Grouper) and gpr.key is not None:
       2936             # Add key to exclusions


    KeyError: 'SN'



```python
bs.groupby(["Item ID"]).count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>233</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>284</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>353</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>472</th>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>609</th>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['SN']==('Undirrala66')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>79</th>
      <td>29</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>107</th>
      <td>29</td>
      <td>Male</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>131</th>
      <td>29</td>
      <td>Male</td>
      <td>62</td>
      <td>Piece Maker</td>
      <td>4.36</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>537</th>
      <td>29</td>
      <td>Male</td>
      <td>18</td>
      <td>Torchlight, Bond of Storms</td>
      <td>1.77</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>596</th>
      <td>29</td>
      <td>Male</td>
      <td>133</td>
      <td>Faith's Scimitar</td>
      <td>3.82</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['SN']==('Saedue76')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>259</th>
      <td>25</td>
      <td>Male</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Saedue76</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>337</th>
      <td>25</td>
      <td>Male</td>
      <td>140</td>
      <td>Striker</td>
      <td>3.82</td>
      <td>Saedue76</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>411</th>
      <td>25</td>
      <td>Male</td>
      <td>7</td>
      <td>Thorn, Satchel of Dark Souls</td>
      <td>4.51</td>
      <td>Saedue76</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>708</th>
      <td>25</td>
      <td>Male</td>
      <td>73</td>
      <td>Ritual Mace</td>
      <td>3.74</td>
      <td>Saedue76</td>
      <td>25-29</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['SN']==('Mindimnya67')] 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>450</th>
      <td>39</td>
      <td>Female</td>
      <td>140</td>
      <td>Striker</td>
      <td>3.82</td>
      <td>Mindimnya67</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>464</th>
      <td>39</td>
      <td>Female</td>
      <td>163</td>
      <td>Thunderfury Scimitar</td>
      <td>3.02</td>
      <td>Mindimnya67</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>592</th>
      <td>39</td>
      <td>Female</td>
      <td>145</td>
      <td>Fiery Glass Crusader</td>
      <td>4.45</td>
      <td>Mindimnya67</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>623</th>
      <td>39</td>
      <td>Female</td>
      <td>161</td>
      <td>Devine</td>
      <td>1.45</td>
      <td>Mindimnya67</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['SN']==('Haellysu29')] 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>15</th>
      <td>21</td>
      <td>Male</td>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>4.77</td>
      <td>Haellysu29</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>381</th>
      <td>21</td>
      <td>Male</td>
      <td>166</td>
      <td>Thirsty Iron Reaver</td>
      <td>4.25</td>
      <td>Haellysu29</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>659</th>
      <td>21</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Haellysu29</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data['SN']==('Eoda93')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>AgeGroup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>108</th>
      <td>22</td>
      <td>Male</td>
      <td>35</td>
      <td>Heartless Bone Dualblade</td>
      <td>2.63</td>
      <td>Eoda93</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>166</th>
      <td>22</td>
      <td>Male</td>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
      <td>Eoda93</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>488</th>
      <td>22</td>
      <td>Male</td>
      <td>76</td>
      <td>Haunted Bronzed Bludgeon</td>
      <td>4.12</td>
      <td>Eoda93</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
bs.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>106.000000</td>
      <td>390.200000</td>
      <td>13.534000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>43.318587</td>
      <td>151.607058</td>
      <td>2.093342</td>
    </tr>
    <tr>
      <th>min</th>
      <td>63.000000</td>
      <td>233.000000</td>
      <td>11.580000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>66.000000</td>
      <td>284.000000</td>
      <td>12.730000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>100.000000</td>
      <td>353.000000</td>
      <td>12.740000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>145.000000</td>
      <td>472.000000</td>
      <td>13.560000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>156.000000</td>
      <td>609.000000</td>
      <td>17.060000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns
```




    Index(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN', 'AgeGroup'], dtype='object')




```python
pop_items = data['Item Name'].value_counts()
pop_items.head(5)
```




    Final Critic                            14
    Arcane Gem                              11
    Betrayal, Whisper of Grieving Widows    11
    Stormcaller                             10
    Retribution Axe                          9
    Name: Item Name, dtype: int64




```python
data.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns = ['ID', 'Name', 'Price']
```


```python
pop_item1= data[data['Name']==('Final Critic')]
pop_item1.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_item2= data[data['Name']==('Retribution Axe')]
pop_item2.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_item3= data[data['Name']==('Betrayal, Whisper of Grieving Widows')] 
pop_item3.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>61</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_item4= data[data['Name']==('Arcane Gem')]    
pop_item4.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>116</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_item5= data[data['Name']==('Stormcaller')]
pop_item5.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>30</td>
      <td>Stormcaller</td>
      <td>4.15</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_item1.Price.agg(['count','sum', 'mean'])
```




    count    14.000000
    sum      38.600000
    mean      2.757143
    Name: Price, dtype: float64




```python
P= data.sort_values(by= 'Price', ascending= False)
```


```python
P.head(25)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>83</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>50</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>657</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>388</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>227</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>359</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>532</th>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
    </tr>
    <tr>
      <th>19</th>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
    </tr>
    <tr>
      <th>670</th>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
    </tr>
    <tr>
      <th>348</th>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
    </tr>
    <tr>
      <th>471</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>468</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>716</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>100</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>645</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>487</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>104</th>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>304</th>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>336</th>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>317</th>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>166</th>
      <td>173</td>
      <td>Stormfury Longsword</td>
      <td>4.83</td>
    </tr>
    <tr>
      <th>419</th>
      <td>42</td>
      <td>The Decapitator</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>222</th>
      <td>131</td>
      <td>Fury</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>427</th>
      <td>131</td>
      <td>Fury</td>
      <td>4.82</td>
    </tr>
    <tr>
      <th>375</th>
      <td>42</td>
      <td>The Decapitator</td>
      <td>4.82</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Three Observable Trends
#Males outnumber females about 5 to 1
#People between 20-24 are largest age group
#The big spenders didn't buy any of the top 5 of most popular games
```

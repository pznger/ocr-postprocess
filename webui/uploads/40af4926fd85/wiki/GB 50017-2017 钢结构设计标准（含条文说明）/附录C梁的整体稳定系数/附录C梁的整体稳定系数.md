# 附录 C 梁的整体稳定系数

C.0.1 等截面焊接工字形和轧制H型钢（图C.0.1）简支梁的整体稳定系数 $\varphi _{\mathrm {b}}$ 应按下列公式计算：

$$\varphi _{b}=\beta _{b}\frac {4320}{\lambda _{y}^{2}}\cdot \frac {Ah}{W_{x}}[\sqrt {1+(\frac {\lambda _{y}t_{1}}{4.4h})^{2}}+\eta _{b}]\epsilon _{k}\tag{C.0.1-1}$$ $$\lambda _{y}=\frac {l_{1}}{i_{y}}\tag{C.0.1-2}$$

<!-- y b1 $b_{1}$ $L_{1}$ 1 x $x$ $L_{1}$ $b_{1}$ y $y$ -->
![](https://web-api.textin.com/ocr_image/external/419d731c1301e9fb.jpg) （a）双轴对称焊接工字形截面（b）加强受压翼缘的单轴对称焊接工字形截面

<!-- y $b_{1}$ $1$ A $y$ x x 4 $t_{2}$ b2 $b_{2}$ $y$ -->
![](https://web-api.textin.com/ocr_image/external/34cee08e0db427e1.jpg)

<!-- $y$ $b_{1}$ $L_{1}$ 1 x x b2l $b_{2}$ $L_{2}$ $y|$ -->
![](https://web-api.textin.com/ocr_image/external/d7eed9fe046526ec.jpg) （c）加强受拉翼缘的单轴对称焊接工字形截面（d）轧制H型钢截面

<!-- y b1 $b_{1}$ ~ 4 x x $L_{1}$ b1 $b_{1}$ y -->
![](https://web-api.textin.com/ocr_image/external/3affa1fbd994a8e1.jpg) 图C.0.1 焊接工字形和轧制H型钢截面不对称影响系数 $\eta _{b}$ 应按下列公式计算：

对双轴对称截面［图C.0.1(a）、图C.0.1(d)]：

$$\eta _{b}=0\tag{C.0.1-3}$$ 对单轴对称工字形截面［图C.0.1(b）、图C.0.1(c)]：

加强受压翼缘 $\eta _{b}=0.8(2\alpha _{b}-1)$  (C.0.1-4) 加强受拉翼缘 $\eta _{b}=2\alpha _{b}-1$  (C.0.1-5) $$\alpha _{b}=\frac {I_{1}}{I_{1}+I_{2}}\tag{C.0.1-6}$$ 当按公式（C.0.1-1）算得的 $\varphi _{\mathrm {b}}$ 值大于0.6时，应用下式计算的 $\varphi _{b}^{\prime }$ 代替 $\varphi _{\mathrm {b}}$ 值：

$$\varphi _{b}^{\prime }=1.07-\frac {0.282}{\varphi _{b}}\leq 1.0\tag{C.0.1-7}$$

式中： $\beta _{b}$ b-梁整体稳定的等效弯矩系数，应按表C.0.1采用；

$\lambda _{y}$ y-梁在侧向支承点间对截面弱轴 $y-y$ 的长细比；

A-梁的毛截面面积（ $mm^{2}$  ）；

$h$ 、 $t_{1}-$ -梁截面的全高和受压翼缘厚度，等截面铆接（或高强度螺栓连接）简支梁，其受压翼缘厚度 $t_{1}$ 包括翼缘角钢厚度在内（mm)；

$l_{1}$ 1-梁受压翼缘侧向支承点之间的距离（mm)；

$i_{y}$ y-梁毛截面对 $y$ 轴的回转半径（mm)；

$I_{1}$ 、 $I_{2}-$  一分别为受压翼缘和受拉翼缘对y轴的惯性矩( $mm^{3}$ 3)。

**表C.0.1 H型钢和等截面工字形简支梁的系数** $\beta _{b}$

<table border="1" ><tr>
<td>项次</td> <td>侧向支承</td> <td colspan="2">荷载</td> <td>$ξ\leq 2.0$</td> <td>$ξ>2.0$</td> <td>适用范围</td> </tr><tr> <td>1</td> <td rowspan="4">跨中无侧向支承</td> <td rowspan="2">均布荷载作用在</td> <td>上翼缘</td> <td>$0.69+0.13ξ$</td> <td>0.95</td> <td rowspan="4">图C.0.1(a）、（b）和（d）的截面</td> </tr><tr> <td>2</td> <td>下翼缘</td> <td>1.73-0.20ξ</td> <td>1.33</td> </tr><tr> <td>3</td> <td rowspan="2">集中荷载作用在</td> <td>上翼缘</td> <td>$0.73+0.18ξ$</td> <td>1.09</td> </tr><tr> <td>4</td> <td>下翼缘</td> <td>2.23-0.28</td> <td>1.67</td> </tr><tr> <td>5</td> <td rowspan="3">跨度中点有一个侧向支承点</td> <td rowspan="2">均布荷载作用在</td> <td>上翼缘</td> <td colspan="2">1.15</td> <td rowspan="6">图C.0.1<br>中的所<br>有截面</td> </tr><tr> <td>6</td> <td>下翼缘</td> <td colspan="2">1.40</td> </tr><tr> <td>7</td> <td colspan="2">集中荷载作用在截面高度的任意位置</td> <td colspan="2">1.75</td> </tr><tr> <td>8</td> <td rowspan="2">跨中有不少于两个等距离侧向支承点</td> <td rowspan="2">任意荷载作用在</td> <td>上翼缘</td> <td colspan="2">1.20</td> </tr><tr> <td>9</td> <td>下翼缘</td> <td colspan="2">1.40</td> </tr><tr> <td>10</td> <td colspan="3">梁端有弯矩，但跨中无荷载作用</td> <td colspan="2">$1.75-1.05(\frac {M_{2}}{M_{1}})+$0.3$(\frac {M_{2}}{M_{1}})^{2}$但$\leq 2.3$</td> </tr></table>

续表C.0.1 注：1 $ξ$ 为参数， $\xi =\frac {l_{1}t_{1}}{b_{1}h}$ ，其中 $b_{1}$ **为受压翼缘的宽度；** 2 $M_{1}$ 和 $M_{2}$ 为梁的端弯矩，使梁产生同向曲率时 $M_{1}$ 和 $M_{2}$ 取同号，产生反向曲率时取异号， $\vert M_{1}\vert \geq \vert M_{2}\vert ;$

3 表中项次3、4和7的集中荷载是指一个或少数几个集中荷载位于跨中央附近的情况，对其他情况的集中荷载，应按表中项次1、2、5、6内的数值采用；

4 表中项次8、9的 $\beta _{b}$ ，当集中荷载作用在侧向支承点处时，取 $\beta _{b}=1.20;$

5 荷载作用在上翼缘系指荷载作用点在翼缘表面，方向指向截面形心；荷载作用在下翼缘系指荷载作用点在翼缘表面，方向背向截面形心；

6对 $\alpha _{b}>0.$ .8的加强受压翼缘工字形截面，下列情况的 $\beta _{b}$ 值应乘以相应的系数：

项次1：当 $ξ\leq 1.0$ 0时，乘以0.95；

项次3：当 $ξ\leq 0.5$ 时，乘以0.90；当 $0$ $5<ξ\leq 1.0$时，乘以0.95。

**C.0.2** 轧制普通工字形简支梁的整体稳定系数 $\varphi _{b}$ 应按表C.0.2采用，当所得的 $\varphi _{b}$ 值大于0.6时，应取本标准式（C.0.1-7）算得的代替值。

**表C.0.2 轧制普通工字钢简支梁的** $\varphi _{b}$ **b**

<table border="1" ><tr>
<td rowspan="2">项次</td> <td colspan="3" rowspan="2">荷载情况</td> <td rowspan="2">工字钢型号</td> <td colspan="9">自由长度$l_{1}$(mm)</td> </tr><tr> <td>2</td> <td>3</td> <td>4</td> <td>5</td> <td>6</td> <td>7</td> <td>8</td> <td>9</td> <td>10</td> </tr><tr> <td rowspan="3">1</td> <td rowspan="11">跨中无侧向支承点的梁</td> <td rowspan="6">集中荷载作用于</td> <td rowspan="3">上翼缘</td> <td>10~20</td> <td>2.00</td> <td>1.30</td> <td>0.99</td> <td>0.80</td> <td>0.68</td> <td>0.58</td> <td>0.53</td> <td>0.48</td> <td>0.43</td> </tr><tr> <td rowspan="2">22~32<br>36~63</td> <td rowspan="2">2.40<br>2.80</td> <td rowspan="2">1.48<br>1.60</td> <td rowspan="2">1.09<br>1.07</td> <td rowspan="2">0.86<br>0.83</td> <td rowspan="2">0.72<br>0.68</td> <td rowspan="2">0.62<br>0.56</td> <td rowspan="2">0.54<br>0.50</td> <td>0.49</td> <td>0.45</td> </tr><tr> <td>0.45</td> <td>0.40</td> </tr><tr> <td rowspan="3">2</td> <td rowspan="3">下翼缘</td> <td>10~20</td> <td>3.10</td> <td>1.95</td> <td>1.34</td> <td>1.01</td> <td>0.82</td> <td>0.69</td> <td>0.63</td> <td>0.57</td> <td>0.52</td> </tr><tr> <td>22~40</td> <td rowspan="2">5.50<br>7.30</td> <td rowspan="2">2.80<br>3.60</td> <td>1.84</td> <td>1.37</td> <td>1.07</td> <td>0.86</td> <td>0.73</td> <td>0.64</td> <td>0.56</td> </tr><tr> <td>45~63</td> <td>2.30</td> <td>1.62</td> <td>1.20</td> <td>0.96</td> <td>0.80</td> <td>0.69</td> <td>0.60</td> </tr><tr> <td rowspan="3">3</td> <td rowspan="5">均布荷载作用于</td> <td rowspan="3">上翼缘</td> <td>10~20</td> <td>1.70</td> <td>1.12</td> <td>0.84</td> <td>0.68</td> <td>0.57</td> <td>0.50</td> <td>0.45</td> <td>0.41</td> <td>0.37</td> </tr><tr> <td rowspan="2">22~40<br>45~63</td> <td rowspan="2">2.10<br>2.60</td> <td rowspan="2">1.30<br>1.45</td> <td rowspan="2">0.93<br>0.97</td> <td rowspan="2">0.73<br>0.73</td> <td rowspan="2">0.60<br>0.59</td> <td rowspan="2">0.51<br>0.50</td> <td rowspan="2">0.45<br>0.44</td> <td>0.40</td> <td>0.36</td> </tr><tr> <td>0.38</td> <td>0.35</td> </tr><tr> <td rowspan="2">4</td> <td rowspan="2">下翼缘</td> <td rowspan="2">10~20<br>22~40<br>45~63</td> <td rowspan="2">2.50<br>4.00<br>5.60</td> <td>1.55</td> <td>1.08</td> <td>0.83</td> <td>0.68</td> <td>0.56</td> <td>0.52</td> <td>0.47</td> <td>0.42</td> </tr><tr> <td>2.20<br>2.80</td> <td>1.45<br>1.80</td> <td>1.10<br>1.25</td> <td>0.85<br>0.95</td> <td>0.70<br>0.78</td> <td>0.60<br>0.65</td> <td>0.52<br>0.55</td> <td>0.46<br>0.49</td> </tr><tr> <td>5</td> <td colspan="3">跨中有侧向支承点的梁（不论荷载作用点在截面高度上的位置）</td> <td>10~20<br>22~40<br>45~63</td> <td>2.20<br>3.00<br>4.00</td> <td>1.39<br>1.80<br>2.20</td> <td>1.01<br>1.24<br>1.38</td> <td>0.79<br>0.96<br>1.01</td> <td>-0.66<br>0.76<br>0.80</td> <td>0.57<br>0.65<br>0.66</td> <td>0.52<br>0.56<br>0.56</td> <td>0.47<br>0.49<br>0.49</td> <td>0.42<br>0.43<br>0.43</td> </tr></table> 注：1 同表C.0.1的注3、注5；

2 表中的 $\varphi _{\mathrm {b}}$ b适用于Q235钢。对其他钢号，表中数值应乘以 $\varepsilon _{\mathrm {k}}^{2}$  。

C.0.3 轧制槽钢简支梁的整体稳定系数，不论荷载的形式和荷载作用点在截面高度上的位置，均可按下式计算：

$$\varphi _{b}=\frac {570bt}{l_{1}h}\cdot \varepsilon _{k}^{2}\tag{C.0.3}$$

式中： $h$ 、 $b$ b、t-槽钢截面的高度、翼缘宽度和平均厚度。

当按公式（C.0.3）算得的 $\varphi _{\mathrm {b}}$ 值大于0.6时，应按本标准式（C.0.1-7）算得相应的 $\varphi _{b}^{\prime }$ 代替 $\varphi _{\mathrm {b}}$ 值。

![](https://web-api.textin.com/ocr_image/external/a9976b67635fb4f3.jpg) C.0.4 双轴对称工字形等截面悬臂梁的整体稳定系数，可按本标准式（C.0.1-1）计算，但式中系数 $\beta _{b}$ b应按表C.0.4查得，当按本标准式（C.0.1-2）计算长细比 $\lambda _{y}$ 时， $l_{1}$ 为悬臂梁的悬伸长度。当求得的 $\varphi _{b}$ b值大于0.6时，应按本标准式（C.0.1-7）算得的 $\varphi _{b}^{\prime }$ 代替 $\varphi _{b}$ b值。

**表C.0.4 双轴对称工字形等截面悬臂梁的系数** $\beta _{b}$

<table border="1" ><tr>
<td>项次</td> <td colspan="2">荷载形式</td> <td>$0.60\leq \xi \leq 1.24$</td> <td>$1.24<ξ\leq 1.9$6</td> <td>$1.96<ξ\leq 3.$.10</td> </tr><tr> <td>1</td> <td rowspan="2">自由端一个集中荷载作用在</td> <td>上翼缘</td> <td>$0.21+0.67ξ$</td> <td>$0.72+0.26ξ$</td> <td>$1.17+0.03ξ$</td> </tr><tr> <td>2</td> <td>下翼缘</td> <td>$2.94-0.65ξ$</td> <td>$2.64-0.40ξ$</td> <td>$2.15-0.15ξ$</td> </tr><tr> <td>3</td> <td colspan="2">均布荷载作用在上翼缘</td> <td>$0.62+0.82ξ$</td> <td>$1.25+0.31ξ$</td> <td>$1.66+0.10ξ$</td> </tr></table> 注：1 本表是按支承端为固定的情况确定的，当用于由邻跨延伸出来的伸臂梁时，应在构造上采取措施加强支承处的抗扭能力；

2 表中 $ξ$ 见表C.0.1注1。

**C.0.5** 均匀弯曲的受弯构件，当 $\lambda _{y}\leq 120\varepsilon _{k}$ 时，其整体稳定系**数** $\varphi _{\mathrm {b}}$ 可按下列近似公式计算：

1 工字形截面：

双轴对称单轴对称 $$\varphi _{b}=1.07-\frac {\lambda _{y}^{2}}{44000\varepsilon _{k}^{2}}\tag{C.0.5-1}$$ $$\varphi _{b}=1.07-\frac {W_{x}}{(2\alpha _{b}+0.1)Ah}\cdot \frac {\lambda _{y}^{2}}{14000\epsilon _{k}^{2}}\tag{C.0.5-2}$$

2 弯矩作用在对称轴平面，绕 x 轴的T形截面：

1）弯矩使翼缘受压时：

双角钢T形截面 $$\varphi _{b}=1-0.0017\lambda _{y}/\varepsilon _{k}\tag{C.0.5-3}$$ 剖分T型钢和两板组合T形截面 $$\varphi _{b}=1-0.0022\lambda _{y}/\varepsilon _{k}\tag{C.0.5-4}$$ 2）弯矩使翼缘受拉且腹板宽厚比不大于 $18\varepsilon _{k}$ k时：

$$\varphi _{b}=1-0.0005\lambda _{y}/\varepsilon _{k}\tag{C.0.5-5}$$ 当按公式（C.0.5-1）和公式（C.0.5-2）算得的 $\varphi _{b}$  b值大于1.0时，取 $\varphi _{b}=1.0。$

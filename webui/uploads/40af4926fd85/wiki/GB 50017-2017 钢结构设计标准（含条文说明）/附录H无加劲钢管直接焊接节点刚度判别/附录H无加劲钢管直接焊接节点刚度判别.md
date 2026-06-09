# 附录 H 无加劲钢管直接焊接节点刚度判别

**H.0.1** 本条为新增条文。近年来的研究表明，在工程常见的几何尺寸范围内，无加劲钢管直接焊接节点受荷载作用后，其相邻杆件的连接面会发生局部变形，从而引起相对位移或转动，表现出不同于铰接或完全刚接的非刚性性能。因此，相比原规范，本次修订增加了平面T形、Y形和平面或微曲面X形节点的刚度计算公式，与节点的刚度判别原则配套使用，可以确定结构计算时节点的合理约束模型。

本次修订列入的平面T形、Y形和平面或微曲面X形节点的刚度计算公式是在比较、分析国外有关规范和国内外有关资料的基础上，根据国内大学近十年来进行的试验、有限元分析和数值计算结果，通过回归分析归纳得出的。同时，将这些刚度公式的计算结果与23个管节点刚度试验数据进行了对比验证（表25～表29)，吻合良好。

**表25 T、Y形节点轴向刚度公式计算值与试验结果的比较**

<table border="1" ><tr>
<td>试件</td> <td>$\beta$</td> <td>y</td> <td>τ</td> <td>$\theta$</td> <td>$K_{\mathrm {NT}}$ （试验）(kN/mm)</td> <td>$K_{NT}^{j}$ （公式）(kN/mm)</td> <td>$K_{NT}/K_{NT}{}^{j}$</td> </tr><tr> <td>TC-12</td> <td>0.44</td> <td>35.4</td> <td>0.98</td> <td>$90^{\circ }$</td> <td>24.5</td> <td>23.0</td> <td>1.07</td> </tr><tr> <td>TC-13</td> <td>0.20</td> <td>46.7</td> <td>0.61</td> <td>$90^{\circ }$</td> <td>12.7</td> <td>11.4</td> <td>1.11</td> </tr><tr> <td>TC-14</td> <td>0.36</td> <td>46.7</td> <td>0.96</td> <td>$90^{\circ }$</td> <td>19.6</td> <td>16.2</td> <td>1.21</td> </tr><tr> <td>TC-17</td> <td>0.36</td> <td>46.9</td> <td>0.97</td> <td>$90^{\circ }$</td> <td>16.7</td> <td>16.0</td> <td>1.04</td> </tr><tr> <td>TC-115</td> <td>1.00</td> <td>23.8</td> <td>1.00</td> <td>$90^{\circ }$</td> <td>86.1</td> <td>101.0</td> <td>0.85</td> </tr></table>

**表26 T、Y形节点平面内弯曲刚度公式计算值与试验结果的比较**

<table border="1" ><tr>
<td>试件</td> <td>$\beta$</td> <td>y</td> <td>τ</td> <td>$\theta$</td> <td>$K_{\mathrm {MiT}}$ （试验）( $kN\cdot m$)</td> <td>$K_{\mathrm {MiT}}{}^{\mathrm {j}}$ （公式）( $kN\cdot m$)</td> <td>$K_{\mathrm {MiT}}/K_{\mathrm {MiT}}{}^{\mathrm {j}}$</td> </tr><tr> <td>TM-33</td> <td>0.36</td> <td>14.6</td> <td>0.97</td> <td>$90^{\circ }$</td> <td>279</td> <td>284</td> <td>0.98</td> </tr><tr> <td>TM-35</td> <td>1.00</td> <td>14.8</td> <td>1.0</td> <td>$90^{\circ }$</td> <td>2680</td> <td>2852</td> <td>0.94</td> </tr><tr> <td>TM-36</td> <td>0.36</td> <td>24.4</td> <td>1.0</td> <td>$90^{\circ }$</td> <td>115</td> <td>112</td> <td>1.02</td> </tr><tr> <td>TM-38</td> <td>1.00</td> <td>23.8</td> <td>1.0</td> <td>$90^{\circ }$</td> <td>1430</td> <td>1234</td> <td>1.16</td> </tr><tr> <td>SXN</td> <td>0.76</td> <td>7.0</td> <td>0.67</td> <td>$90^{\circ }$</td> <td>5003</td> <td>5910</td> <td>0.85</td> </tr><tr> <td>JB-1</td> <td>0.80</td> <td>14.4</td> <td>0.86</td> <td>$90^{\circ }$</td> <td>27000</td> <td>25234</td> <td>1.07</td> </tr></table>

**表27 X形节点轴向刚度公式计算值和试验结果的比较**

<table border="1" ><tr>
<td>试件</td> <td>D(mm)</td> <td>$\beta$</td> <td>y</td> <td>τ</td> <td>$\theta$</td> <td>$φ$</td> <td>$K_{NX}^{j}$（公式）(kN/m)</td> <td>$K_{NX}$ （试验）(kN/m)</td> <td>$K_{NX}/$ $K_{NX}^{j}$</td> </tr><tr> <td>XC-67</td> <td>318.50</td> <td>0.52</td> <td>36.19</td> <td>1.07</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$</td> <td>16.01</td> <td>16.18</td> <td>1.01</td> </tr><tr> <td>XC-74</td> <td>140.05</td> <td>0.36</td> <td>7.78</td> <td>1.03</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$</td> <td>210.95</td> <td>152.00</td> <td>0.72</td> </tr><tr> <td>XC-77</td> <td>165.23</td> <td>1.00</td> <td>19.35</td> <td>1.05</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$</td> <td>712.21</td> <td>774.73</td> <td>1.09</td> </tr><tr> <td>XC-78</td> <td>114.41</td> <td>1.00</td> <td>13.40</td> <td>1.05</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$</td> <td>913.69</td> <td>637.43</td> <td>0.70</td> </tr></table>

**表28 X形节点平面内抗弯刚度公式计算值和试验结果的比较**

<table border="1" ><tr>
<td>试件</td> <td>D (mm)</td> <td>$\beta$</td> <td>y</td> <td>τ</td> <td>$\theta$</td> <td>$φ$</td> <td>$K_{\mathrm {MiX}}{}^{\mathrm {j}}$ $(kN\cdot m)$</td> <td>$K_{\mathrm {MiX}}$ $(kN\cdot m)$</td> <td>$K_{\mathrm {MiX}}/$ $K_{MiX}^{j}$</td> </tr><tr> <td>XM-18</td> <td>408.5</td> <td>0.60</td> <td>20.43</td> <td>1.04</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$°</td> <td>6542</td> <td>7519</td> <td>1.15</td> </tr><tr> <td>SXN3</td> <td>168</td> <td>0.76</td> <td>7.00</td> <td>0.67</td> <td>$90^{\circ }$</td> <td>$0^{\circ }$</td> <td>5236</td> <td>5288.46</td> <td>1.01</td> </tr></table>

**表29 X形节点平面外弯曲刚度公式计算值与试验结果的比较**

<table border="1" ><tr>
<td rowspan="2">试件</td> <td rowspan="2">$\beta$</td> <td rowspan="2">γ</td> <td rowspan="2">$\theta$</td> <td rowspan="2">$φ$</td> <td rowspan="2">$K_{\mathrm {MoX}}$ $(kN\cdot m)$</td> <td colspan="2">$K_{\mathrm {MoX}}/K_{\mathrm {MoX}}{}^{\mathrm {j}}$</td> </tr><tr> <td>日本AIJ 公式</td> <td>本标准公式</td> </tr><tr> <td>B1-1</td> <td>0.9</td> <td>8.53</td> <td>$91^{\circ }$</td> <td>$6.5^{\circ }$</td> <td>67507</td> <td>7.05</td> <td>2.08</td> </tr><tr> <td>B1-2</td> <td>0.9</td> <td>8.53</td> <td>$88^{\circ }$</td> <td>$6.5^{\circ }$°</td> <td>85216</td> <td>8.90</td> <td>2.63</td> </tr><tr> <td>B2-1</td> <td>0.9</td> <td>8.53</td> <td>$78^{\circ }$</td> <td>$0^{\circ }$</td> <td>76895</td> <td>8.03</td> <td>2.21</td> </tr><tr> <td>B2-2</td> <td>0.9</td> <td>8.53</td> <td>$78^{\circ }$</td> <td>$0^{\circ }$</td> <td>95578</td> <td>9.98</td> <td>2.74</td> </tr><tr> <td>B3-1</td> <td>0.7</td> <td>10.97</td> <td>$86^{\circ }$</td> <td>$12^{\circ }$</td> <td>18926</td> <td>3.19</td> <td>1.00</td> </tr><tr> <td>B3-2</td> <td>0.7</td> <td>10.97</td> <td>$94^{\circ }$</td> <td>$12^{\circ }$</td> <td>22032</td> <td>3.71</td> <td>1.16</td> </tr></table> H.0.2 本条为新增条文。

**H.0.3** 本条为新增条文。空腹桁架的主管与支管以 $90^{\circ }$ 夹角相互连接，因此支管与主管连接节点不能作为铰接处理，需承担弯矩，否则体系几何可变。

采用若干子结构模型来近似表达图52中的多跨空腹“桁架”的不同节点位置。这些子结构的选取原则是能够反映空腹“桁架”不同节点部位如图53所示的变形模式。所采用的子结构模型见图54。

（a）偶数跨

<!-- P/2 P $2$ P P/2 P/2 $P$ P P P/2 $I_{c}$ 。 I。 $I_{c}$ I。 $I_{\mathrm {c}}$ 。 $I_{\mathrm {c}}$ $I_{c}$ $I_{c}$ 。 1 $I_{c}$ $I_{c}$ $I_{\mathrm {c}}$ 10 $L_{b}$ $I_{b}$ $I_{\mathrm {b}}$ $I_{\mathrm {b}}$ $I_{b}$ $I_{b}$ $L_{b}$ $I_{b}$ Ib $I_{b}$ 1b $I_{b}$ $I_{\mathrm {b}}$ $I_{\mathrm {b}}$ Ib $I_{b}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ $I_{c}$ l。 $l_{c}$ 1} $l_{c}$ $l_{c}$ $l_{c}$ lc $l_{c}$ 1。 $l_{c}$ 1。 $l_{c}$ l。 $l_{c}$ l。 $l_{c}$ （b）奇数跨 -->
![](https://web-api.textin.com/ocr_image/external/29bcc215fe86879d.jpg) 图52多跨空腹桁架

<!-- A B -->
![](https://web-api.textin.com/ocr_image/external/f64b3bbc2f592aa0.jpg)

<!-- B A C 本 -->
![](https://web-api.textin.com/ocr_image/external/3be4dab4335eb7e1.jpg) 图53 空腹格构梁的变形模式

<!-- 2 $L_{b}/2$ δ $δ$ V 1/2 $l_{c}/2$ $l_{c}/2$ -->
![](https://web-api.textin.com/ocr_image/external/00f6958f056608da.jpg)

<!-- $\downarrow δ$ $l_{c}/2$ V -->
![](https://web-api.textin.com/ocr_image/external/18d61d715ca88f4e.jpg)

<!-- $l_{b}/2$ $δ$ δ V 1/2 $l_{c}/2$ $l_{c}/2$ -->
![](https://web-api.textin.com/ocr_image/external/1e66ffe5b2535162.jpg) A B C 图54子结构模型节点刚度对格构梁在正常使用极限状态的行为有较大的影响。因此采用以下通过位移定义的标准来区分节点的刚性与半刚性：

$$\Delta =(\delta _{s}-\delta _{r})/\delta _{r}\tag{87}$$ 其中， $δ_{\mathrm {s}}$ s为具有半刚性连接的格构梁的位移； $δ_{\mathrm {r}}$ ，为具有刚性连接的格构梁的位移。

用于计算位移的荷载条件如图54所示。下文基于格构梁的变形行为推导节点刚度介于刚性与半刚性之间的分界线。在位移 $\delta _{s}$ s和 $\delta _{r}$ 的计算中由于基于格构梁正常使用极限状态，所以采用小位移理论，且半刚性连接的刚度假定为线弹性。

对于具有半刚性连接的子结构A，竖向位移 $δ_{\mathrm {s}}$ 经理论推导得：

$$\delta _{s}=\frac {Vl_{c}^{2}}{12K_{c}K_{b}}(K_{b}+K_{c})+\frac {Vl_{c}^{2}}{4K_{M}}\quad =\frac {Vl_{c}^{2}}{12K_{c}K_{b}K_{M}}\left(K_{M}K_{b}+K_{M}K_{c}+3K_{c}K_{b}\right)\tag{88}$$ $$K_{b}=\frac {EI_{b}}{l_{b}}\tag{89}$$ $$K_{c}=\frac {EI_{c}}{l_{c}}\tag{90}$$ 同理，对于具有刚性连接的子结构A，竖向位移 $δ_{\mathrm {s}}$ 经理论推导得：

$$\delta _{s}=\frac {Vl_{c}^{2}}{12K_{c}K_{b}}(K_{b}+K_{c})\tag{91}$$ $$\frac {K_{M}}{K_{b}}=\frac {3}{(1+G)\cdot \Delta }\tag{92}$$ $$G=\frac {K_{b}}{K_{c}}\tag{93}$$ 对于子结构B，格构梁的竖向位移与节点弯曲刚度无关，所以无需进行分界值的推导。对于具有半刚性连接的子结构C，竖向位移 $δ_{\mathrm {s}}$ 经理论推导得：

$$\delta _{s}=\frac {Vl_{c}^{2}}{24K_{c}(3K_{b}+K_{c})}\cdot (3K_{b}+4K_{c})+\frac {9Vl_{c}^{2}\cdot K_{b}^{2}}{4K_{M}(3K_{b}+K_{c})^{2}}\quad =\delta _{r}+\frac {9Vl_{c}^{2}\cdot K_{b}^{2}}{4K_{M}(3K_{b}+K_{c})^{2}}\tag{94}$$ 同理，对于具有刚性连接的子结构C，竖向位移 $δ_{\mathrm {s}}$ 经理论推导得：

$$\frac {K_{\mathrm {M}}}{K_{\mathrm {b}}}=\frac {54K_{\mathrm {b}}K_{\mathrm {c}}}{\Delta \cdot \left(3K_{\mathrm {b}}+K_{\mathrm {c}}\right)\left(3K_{\mathrm {b}}+4K_{\mathrm {c}}\right)}=\frac {54G}{\Delta \cdot (3G+1)(3G+4)}$$ (95) $$\delta _{s}=\frac {Vl_{c}^{2}}{24K_{c}(3K_{b}+K_{c})}\cdot (3K_{b}+4K_{c})\tag{96}$$ 若取 $\Delta =0.05$ ，则得到本标准条文中所述的节点弯曲刚度分界值。

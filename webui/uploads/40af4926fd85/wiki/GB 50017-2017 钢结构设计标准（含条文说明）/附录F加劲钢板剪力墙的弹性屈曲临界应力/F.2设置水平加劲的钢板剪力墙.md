## F.2 设置水平加劲的钢板剪力墙

**F.2.1** 仅设置水平加劲的钢板剪力墙，其弹性剪切屈曲临界应力 $\tau _{cr}$ 计算应符合下列规定：

1 参数 $\eta _{x}$  $\eta _{\tau th,h}$ 应按下列公式计算：

$$\eta _{x}=\frac {EI_{sx}}{Dh_{1}}\tag{F.2.1-1}$$ $$\eta _{\tau th,h}=6\eta _{h}(7\beta _{h}^{2}-4)\geq 5\tag{F.2.1-2}$$ $$\eta _{h}=0.42+\frac {0.58}{[1+5.42(I_{t,sx}/I_{sx})^{2.6}]^{0.77}}\tag{F.2.1-3}$$ $$0.8\leq \beta _{h}=\frac {L_{n}}{h_{1}}\leq 5\tag{F.2.1-4}$$

式中： $I_{sx}-$  一水平方向加劲肋的惯性矩（mm4），可考虑加劲肋与钢板剪力墙有效宽度组合截面，单侧钢板剪力墙的有效宽度取15倍的钢板厚度；

$h_{1}-$ $\searrow$ -剪力墙板区格高度（mm)；

$I_{t,sx}$  -水平加劲肋自由扭转常数（ $mm^{4}$ 4）。

2当 $\eta _{x}\geq \eta _{\tau th,h}$ 时，弹性剪切屈曲临界应力 $τ_{\mathrm {cr}}$ 应按下列公式计算：

$$\tau _{cr}=\tau _{crp}=k_{\tau p}\frac {\pi ^{2}D}{L_{n}^{2}t_{w}}\tag{F.2.1-5}$$ 当 $\frac {h_{1}}{L_{n}}\geq 1$ 时：

$$k_{\tau p}=\chi [5.34+\frac {4}{(h_{1}/L_{n})^{2}}]\tag{F.2.1-6}$$ 当 $\frac {h_{1}}{L_{n}}<1$ 时：

$$k_{\tau p}=\chi [4+\frac {5.34}{(h_{1}/L_{n})^{2}}]\tag{F.2.1-7}$$ 3当 $\eta _{x}<\eta _{\tau th,h}$ 时，弹性剪切屈曲临界应力 $τ_{\mathrm {cr}}$ 应按下列公式计算：

$$\tau _{cr}=k_{ss}\frac {\pi ^{2}D}{L_{n}^{2}t_{w}}\tag{F.2.1-8}$$ $$k_{ss}=k_{ss0}+[k_{\tau p}-k_{ss0}](\frac {\eta _{x}}{\eta _{\tau th,h}})^{0.6}\quad (F.2.1-9)$$

式中： $k_{\mathrm {ss}0}-$ -参数，根据本标准式（F.1.1-10）、式（F.1.1-11）计算。

F.2.2 仅设置水平加劲肋的钢板剪力墙，其竖向受压弹性屈曲临界应力 $\sigma _{cr}$ 的计算应符合下列规定：

1参数 $\eta _{x0}$ 应按下式计算：

$$\eta _{x0}=0.3(1+\cos \frac {\pi }{n_{h}+1})[1+(\frac {L_{n}}{h_{1}})^{2}]^{2}\tag{F.2.2-1}$$

式中： $n_{\mathrm {h}}$ -水平加劲肋的道数。

2 竖向受压弹性屈曲临界应力 $\sigma _{cr}$ 应按下列公式计算：

当 $\eta _{x}\geq \eta _{x0}$ 时 $$\sigma _{cr}=\sigma _{crp}=k_{pan}\frac {\pi ^{2}D}{L_{n}^{2}t_{w}}\tag{F.2.2-2}$$ $$k_{pan}=(\frac {L_{n}}{h_{1}}+\frac {h_{1}}{L_{n}})^{2}\tag{F.2.2-3}$$ 当 $\eta _{x}<\eta _{x0}$ 时：

$$\sigma _{cr}=\sigma _{cr0}+(\sigma _{crp}-\sigma _{cr0})(\frac {\eta _{y}}{\eta _{cth}})^{0.6}\tag{F.2.2-4}$$

式中： $σ_{\mathrm {cr}0}$  -未加劲钢板剪力墙的竖向弯曲屈曲应力（N／ $mm^{2})$ ，按本标准式（F.1.2-5）计算。

**F.2.3** 仅设置水平加劲肋的钢板剪力墙，其竖向抗弯弹性屈曲临界应力 $\sigma _{bcr}$ 应按下列公式计算：

当 $\eta _{x}\geq \eta _{x0}$ 时：

$$\sigma _{bcr}=\sigma _{bcrp}=k_{bpan}\frac {\pi ^{2}D}{L_{n}^{2}t_{w}}\tag{F.2.3-1}$$ $$k_{\mathrm {bpan}}=14+11\left(\frac {h_{1}}{L_{\mathrm {n}}}\right)^{2}+2.2\left(\frac {L_{\mathrm {n}}}{h_{1}}\right)^{2}\tag{F.2.3-2}$$ 当 $\eta _{x}<\eta _{x0}$ 时：

$$\sigma _{bcr}=\sigma _{bcr0}+(\sigma _{bcrp}-\sigma _{bcr0})(\frac {\eta _{y}}{\eta _{oth}})^{0.6}\quad (F.2.3-3)$$

式中： $σ_{\mathrm {bcr}0}$  -未加劲钢板剪力墙的竖向弯曲屈曲应力（N／ $mm^{2})$ ，按本标准式（F.1.3-4）计算。

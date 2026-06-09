## F.1 仅设置竖向加劲的钢板剪力墙

F.1.1 仅设置竖向加劲的钢板剪力墙，其弹性剪切屈曲临界应力 $τ_{\mathrm {cr}}$ r计算应符合下列规定：

1参数 $\eta _{y}$ 、 $\eta _{\tau th}$ h)应按下列公式计算：

$$\eta _{y}=\frac {EI_{sy}}{Da_{1}}\tag{F.1.1-1}$$ $$\eta _{\tau th}=6\eta _{k}(7\beta ^{2}-5)\geq 10\tag{F.1.1-2}$$ $$\eta _{k}=0.42+\frac {0.58}{[1+5.42(I_{t,sy}/I_{sy})^{2.6}]^{0.77}}\tag{F.1.1-3}$$ $$0.8\leq \beta =\frac {H_{n}}{a_{1}}\leq 5\tag{F.1.1-4}$$

式中：E-加劲肋的弹性模量 $N/mm^{2}$ ）；

$I_{sy}-$  -竖向加劲肋的惯性矩（ $mm^{4}$ 4)，可考虑加劲肋与钢板剪力墙有效宽度组合截面，单侧钢板剪力墙的有效宽度取15倍的钢板厚度；

D-单位宽度的弯曲刚度（ $N\cdot mm$ )，根据本标准式（9.2.4-3）计算；

$a_{1}$ 1-剪力墙板区格宽度（mm)；

$H_{n}$  -钢板剪力墙的净高度（mm)；

$I_{\mathrm {t},\mathrm {sy}}$  -竖向加劲肋自由扭转常数（ $mm^{4}$ ）。

2当 $\eta _{y}\geq \eta _{\tau th}$ 时，弹性剪切屈曲临界应力 $τ_{\mathrm {cr}}$ 应按下列公式计算：

$$\tau _{cr}=\tau _{crp}=k_{\tau p}\frac {\pi ^{2}D}{a_{1}^{2}t_{w}}\tag{F.1.1-5}$$ 当 $\frac {H_{n}}{a_{1}}\geq 1$ 时 $$k_{\tau p}=\chi [5.34+\frac {4}{(H_{n}/a_{1})^{2}}]\tag{F.1.1-6}$$ 当 $\frac {H_{n}}{a_{1}}<1$ 时：

$$k_{\tau p}=\chi [4+\frac {5.34}{(H_{n}/a_{1})^{2}}]\tag{F.1.1-7}$$

式中： $t_{\mathrm {w}}$ $-$ -剪力墙板的厚度（mm)；

$x$ -采用闭口加劲肋时取1.23，开口加劲肋时取1.0。

3当 $\eta _{y}<\eta _{\tau th}$ 时，弹性剪切屈曲临界应力 $τ_{\mathrm {cr}}$ 应按下列公式计算：

$$\tau _{cr}=k_{ss}\frac {\pi ^{2}D}{a_{1}^{2}t_{w}}\tag{F.1.1-8}$$ $$k_{\mathrm {ss}}=k_{\mathrm {ss}0}\left(\frac {a_{1}}{L_{\mathrm {n}}}\right)^{2}+\left[k_{\mathrm {rp}}-k_{\mathrm {ss}0}\left(\frac {a_{1}}{L_{\mathrm {n}}}\right)^{2}\right]\left(\frac {n_{\mathrm {y}}}{\eta _{\mathrm {rth}}}\right)^{0.6}$$ (F.1.1-9) 当 $\frac {H_{n}}{L_{n}}\geq 1$ 时：

$$k_{ss0}=6.5+\frac {5}{(H_{n}/L_{n})^{2}}\tag{F.1.1-10}$$ 当 $\frac {H_{n}}{L_{n}}<1$ 时：

$$k_{ss0}=5+\frac {6.5}{(H_{n}/L_{n})^{2}}\tag{F.1.1-11}$$

式中： $L_{n}-$  -钢板剪力墙的净宽度（mm）。

**F.1.2** 仅设置竖向加劲肋的钢板剪力墙，其竖向受压弹性屈曲临界应力 $\sigma _{cr}$ 的计算应符合下列规定：

1 参数 $\eta _{\sigma th}$ 应按下列公式计算：

$$\eta _{oth}=1.5(1+\frac {1}{n_{v}})[k_{pan}(n_{v}+1)^{2}-k_{oo}](\frac {H_{n}}{L_{n}})^{2}$$ (F.1.2-1) $$k_{\infty }=\chi (\frac {L_{n}}{H_{n}}+\frac {H_{n}}{L_{n}})^{2}\tag{F.1.2-2}$$

式中： $k_{\text {pan}}$  一小区格竖向受压屈曲系数，可以取 $k_{pan}=4\chi ,\chi$ 是嵌固系数，闭口加劲肋时取1.23，开口加劲肋时取1；

$n_{\mathrm {v}}-$ -竖向加劲肋的道数。

2 竖向受压弹性屈曲临界应力 $\sigma _{cr}$ 应按下列公式计算：

当 $\eta _{y}\geq \eta _{\sigma th}$ 时：

$$\sigma _{cr}=\sigma _{crp}=k_{pan}\frac {\pi ^{2}D}{a_{1}^{2}t_{w}}\tag{F.1.2-3}$$ 当 $\eta _{y}<\eta _{\sigma th}$ 时：

$$\sigma _{cr}=\sigma _{cr0}+(\sigma _{crp}-\sigma _{cr0})\frac {\eta _{y}}{\eta _{\sigma th}}\tag{F.1.2-4}$$ $$\sigma _{\mathrm {cr}0}=\frac {\pi ^{2}k_{\sigma 0}D}{L_{\mathrm {n}}^{2}t_{\mathrm {w}}}\tag{F.1.2-5}$$

式中： $k_{σ0}$ /-参数，按本标准式（F.1.2-2）计算。

F.1.3 仅设置竖向加劲肋的钢板剪力墙，其竖向抗弯弹性屈曲临界应力 $σ_{\mathrm {bcr}}$ 应按下列公式计算：

当 $\eta _{y}\geq \eta _{\sigma th}$ 时：

$$\sigma _{bcr}=\sigma _{bcrp}=k_{bpan}\frac {\pi ^{2}D}{a_{1}^{2}t_{w}}\tag{F.1.3-1}$$ $$k_{bpan}=4+2\beta _{\sigma }+2\beta _{\sigma }^{3}\tag{F.1.3-2}$$ 当 $\eta _{y}<\eta _{\sigma th}$ 时：

$$\sigma _{bcr}=\sigma _{bcr0}+(\sigma _{bcrp}-\sigma _{bcr0})\frac {\eta _{y}}{\eta _{\sigma th}}\tag{F.1.3-3}$$ $$\sigma _{bcr0}=\frac {\pi ^{2}k_{b0}D}{L_{n}^{2}t_{w}}\tag{F.1.3-4}$$ $$k_{b0}=14+11(\frac {H_{n}}{L_{n}})^{2}+2.2(\frac {L_{n}}{H_{n}})^{2}\tag{F.1.3-5}$$

式中： $k_{bpan}$ n-小区格竖向不均匀受压屈曲系数；

$\beta _{\sigma }$ 。-区格两边的应力差除以较大的压应力。

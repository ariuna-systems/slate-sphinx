# MathJax Support (Markdown)

Inline math with single dollars: $\sin(x) + \cos(x) = \sqrt{2}\,\sin\!\left(x + \tfrac{\pi}{4}\right)$.

Display math with double dollars:

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

A matrix using `amsmath`:

$$
A = \begin{pmatrix}
  a_{11} & a_{12} \\
  a_{21} & a_{22}
\end{pmatrix}
$$

Using the explicit `{math}` role: {math}`E = mc^2`.

Using a fenced math directive:

```{math}
\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
```

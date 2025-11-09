# Лабораторная работа №1

## 1.1 Вероятностное пространство, формула Байеса

### 1. Определить (с обоснованием), зависимы или независимы следующие события:
- Несовметсные события;

    **Решение:**

    По определению **несовместные** событий: $P(AB) = 0$.

    По определению **независимые** событий: $P(AB) = P(A)P(B)$.

    Таким образом: $P(A)P(B) = 0 \Rightarrow  P(A) = 0 \text{ или } P(B) = 0$.

    **Ответ:** несовместные события могут быть независимыми, если одно из них имеет нулевую вероятность, иначе - зависимые.

- Cобытия, образующие $\sigma$-алгебру $\Sigma$ в пространстве $(\Omega, \Sigma, \mathbb{P})$;

    **Решение:**

    По определению $\sigma$-алгебра:
    - если $A \in \sigma$, то $\overline{A} \in \sigma$;
    - если $A_1, \dots, A_n, \dots \in \sigma$, то $A_1 + \dots + A_n + \dots \in \sigma$.

    *Пример:* $\Omega = \left\lbrace1, 2, 3, 4\right\rbrace, \newline \sigma = \left\lbrace\left\lbrace1\right\rbrace, \left\lbrace2\right\rbrace, \left\lbrace3\right\rbrace, \left\lbrace4\right\rbrace,\left\lbrace1, 2\right\rbrace, \left\lbrace1, 3\right\rbrace, \left\lbrace1, 4\right\rbrace, \left\lbrace2, 3\right\rbrace, \left\lbrace2, 4\right\rbrace, \left\lbrace3, 4\right\rbrace, \left\lbrace1, 2, 3\right\rbrace, \left\lbrace1, 2, 4\right\rbrace, \left\lbrace2, 4, 3\right\rbrace\right\rbrace$ 

- События, имеющие одинаковую вероятность.
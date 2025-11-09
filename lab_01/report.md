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
    
    - $A = \left\lbrace1, 2\right\rbrace, B = \left\lbrace1, 3\right\rbrace$
  
        $P(A) = \frac{1}{2}, \ P(B) = \frac{1}{2}$

        $P(AB) = P({1}) = \frac{1}{4}, \ P(A)P(B) = \frac{1}{4} \Rightarrow A, B - \text{независимые}$  
    - $A = \left\lbrace1, 2, 3\right\rbrace, B = \left\lbrace1, 2\right\rbrace$
        
        $P(A) = \frac{3}{4}, \ P(B) = \frac{1}{2}$

        $P(AB) = P({1, 2}) = \frac{1}{2}, \ P(A)P(B) = \frac{3}{8} \Rightarrow A, B - \text{зависимые}$
    
    **Ответ:** события, образующие $\sigma$-алгебру могут быть как зависимые, так и независимые.

- События, имеющие одинаковую вероятность.

    ToDO


### 2. Опыт заключается в независимом подбрасывании двух симметричных монет. Рассматриваются следующие события:
- $A$ - появление герба на первой монете;
- $B$ - появление решки на первой монете;
- $C$ - появление герба на второй монете;
- $D$ - появление решки на второй монете;
- $E$ - появление хотя бы одного герба;
- $F$ - появление хотя бы одной решки;
- $G$ - появление одного герба и одной решки;
- $H$ - непоявление ни одного герба;
- $K$ - появление двух гербов.

    **Решение:**
    
    $\Omega = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)}, \text{(Г, Г)}, \text{(Р, Р)}, \right\rbrace$
    - $A$ - появление герба на первой монете $\left\lbrace \text{(Г, Р)}, \text{(Г, Г)}\right\rbrace$;
    - $B$ - появление решки на первой монете $\left\lbrace \text{(Р, Р)}, \text{(Р, Г)}\right\rbrace$;
    - $C$ - появление герба на второй монете $\left\lbrace \text{(Г, Г)}, \text{(Р, Г)}\right\rbrace$;
    - $D$ - появление решки на второй монете $\left\lbrace \text{(Г, Р)}, \text{(Р, Р)}\right\rbrace$;
    - $E$ - появление хотя бы одного герба $\left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace$;
    - $F$ - появление хотя бы одной решки $\left\lbrace \text{(Р, Р)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace$;
    - $G$ - появление одного герба и одной решки $\left\lbrace \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace$;
    - $H$ - непоявление ни одного герба $\left\lbrace \text{(Р, Р)}\right\rbrace$;
    - $K$ - появление двух гербов $\left\lbrace \text{(Г, Г)}\right\rbrace$.

    Определим, каким событиям этого списка равносильны следующие события:

    - $A + C = \left\lbrace \text{(Г, Р)}, \text{(Г, Г)}\right\rbrace \cup \left\lbrace \text{(Г, Г)}, \text{(Р, Г)}\right\rbrace = \left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)} \right\rbrace = E \ \text{(появление хотя бы одного орла)}$

        **Ответ**: $A + C = E$ 
    - $AC = \left\lbrace \text{(Г, Р)}, \text{(Г, Г)}\right\rbrace \cap \left\lbrace \text{(Г, Г)}, \text{(Р, Г)}\right\rbrace = \left\lbrace \text{(Г, Г)} \right\rbrace = K \ \text{(появление двух гербов)}$
  
        **Ответ**: $AC = K$  
    - $EF = \left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace \cap \left\lbrace \text{(Р, Р)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)} \right\rbrace = G \ \text{(появление одного герба и одной решки)}$
     
        **Ответ**: $EF = G$  
    - $G + E = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace \cup \left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)}, \text{(Г, Г)} \right\rbrace = E \ \text{(появление хотя бы одного герба)}$
     
        **Ответ**: $G + E = E$ 
    - $GE = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace \cup \left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace = \left\lbrace \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace = G \ \text{(появление одного герба и одной решки)}$

        **Ответ**: $GE = G$  
    - $BD = \left\lbrace \text{(Р, Р)}, \text{(Р, Г)}\right\rbrace \cap \left\lbrace \text{(Г, Р)}, \text{(Р, Р)}\right\rbrace = \left\lbrace \text{(Р, Р)}\right\rbrace = H \ \text{(непоявление ни одного герба)}$

        **Ответ**: $GE = H$   
    - $E + K =\left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)}\right\rbrace \cup \left\lbrace \text{(Г, Г)}\right\rbrace = \left\lbrace \text{(Г, Г)}, \text{(Г, Р)}, \text{(Р, Г)} \right\rbrace = G \ \text{(появление хотя бы одного герба)}$
     
        **Ответ**: $E + K = E$

### 3. Производится выстрел по вращающейся круговой мишени, в которой закрашены два непересекающихся сектора с углом 20◦. Какова вероятность попадания в закрашенную область?

**Решение:**

1. Полный круг - $360\degree$;
2. Два непересекающихся сектора с углом $20\degree \Rightarrow \ \text{общая закрашенная площадь} = 40\degree$
3. Вероятность попадания в закрашенную область: $P = \frac{40\degree}{360\degree} = \frac{1}{9}$
  
**Ответ:** $\frac{1}{9}$

### 4. Два парохода должны подойти к одному и тому же причалу независимо друг от друга и равновозможно в течение суток. Определить вероятность того, что одному из них придется ожидать освобождения причала, если время стоянки первого парохода - 1 час, а второго - 2 часа.

**Решение:**

**Ответ:** $\frac{139}{1152}$

### 5. Самолет, по которому ведется стрельба, состоит из трех различных по уязвимости частей:
1. Кабина летчика и двигатель
2. Топливные баки
3. Планер

Для поражения самолета достаточно либо одного попадания в первую часть, либо двух попаданий во вторую, либо трех в третью. При попадании в самолет одного снаряда, снаряд с вероятностью p1 попадает в первую часть, с вероятностью p2 — во вторую, с вероятностью p3 — в третью. Попавшие снаряды распределяются по частям независимо друг от друга. Известно, что в самолет попало m снарядов. Найти условную вероятность P(A|m) события A – «Самолет поражен» – при m = 1, 2, 3, 4

**Решение:**
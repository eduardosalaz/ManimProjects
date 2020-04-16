#Code is a mess, will refactor it when I know proper Manim
from manimlib.imports import *


class TitleCard(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        titulo1 = TextMobject("{\\fontsize{30}{30}\\selectfont Números}").to_edge(UP)
        titulo2 = TextMobject("{\\fontsize{30}{30}\\selectfont Cuadrados}").next_to(titulo1, DOWN, buff=0.5)
        titulo3 = TextMobject("{\\fontsize{30}{30}\\selectfont Triangulares}").next_to(titulo2, DOWN, buff=0.5)
        self.play(Write(titulo1), Write(titulo2), Write(titulo3))
        self.wait(2)
        self.play(FadeOutAndShiftDown(titulo1, UP), FadeOutAndShiftDown(titulo2, LEFT),
                  FadeOutAndShiftDown(titulo3, DOWN))
        self.wait(1)


class NumCuadrado1(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        primero = TextMobject("{\\Huge Primero\\ }").to_edge(UP)
        self.play(Write(primero))
        segundo = TextMobject("{\\huge ¿Qué es un número cuadrado?\\ }")
        num = TextMobject("{\\huge 25 \\ }").to_edge(DOWN).set_color(BLUE)
        cuadrado = Square().set_color(RED).to_edge(DOWN).scale(0.75)
        self.play(ReplacementTransform(primero, segundo))
        self.play(Write(num))
        self.wait(0.6)
        self.play(ReplacementTransform(num, cuadrado))
        self.wait(1)
        self.play(FadeOutAndShiftDown(segundo, RIGHT), FadeOutAndShiftDown(cuadrado, DOWN))
        self.wait(1)


class NumCuadrado2(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject(
            "Cualquier número que sea elemento de $\mathbb{Z}$ \\\\ multiplicado por si mismo \\\\ forma un número",
            " cuadrado")
        self.play(Write(text1))
        self.play(text1[1].set_color, BLUE)
        text3 = TextMobject("La fórmula para obtener un número cuadrado es")
        teX1 = TexMobject("S_k = n^2").set_color(BLUE).next_to(text3, DOWN, buff=0.5).scale(1.5)
        text5 = TextMobject("{\\small Siendo $k$ el elemento de la sucesión actual\\ }").to_edge(DOWN)
        self.play(ReplacementTransform(text1[0], text3), ReplacementTransform(text1[1], teX1))
        self.play(text3.shift, UP, teX1.shift, UP)
        self.wait(1)
        self.play(Write(text5))
        self.wait(2)
        self.play(FadeOutAndShiftDown(text3, UP), FadeOutAndShiftDown(teX1, RIGHT), FadeOutAndShiftDown(text5, DOWN))
        self.wait(1)


class DemoCuadrado(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("Los primeros elementos de la sucesión son: ")
        text1.to_edge(UP)
        self.play(Write(text1))
        sk1 = TexMobject("S_1 = ").move_to(UP * 2.3 + LEFT * 1.5)
        num1 = TexMobject("1^2 = ").move_to(UP * 2.4)
        res1 = TexMobject("1").move_to(UP * 2.4 + RIGHT * 1)
        self.play(GrowFromCenter(sk1))
        self.play(FadeInFromPoint(num1, sk1.get_center()))
        self.play(ReplacementTransform(num1.copy(), res1))
        self.play(res1.set_color, RED, run_time=1)
        cuad_1 = Square().scale(0.3).set_color(RED).next_to(res1, RIGHT, buff=1)
        self.play(ReplacementTransform(res1.copy(), cuad_1), run_time=1.5)
        self.wait(1)
        sk2 = TexMobject("S_2 = ").move_to(UP * 0.3 + LEFT * 1.5)
        num2 = TexMobject("2^2 = ").move_to(UP * 0.4)
        res2 = TexMobject("4").move_to(UP * 0.4 + RIGHT * 1)
        self.play(GrowFromCenter(sk2))
        self.play(FadeInFromPoint(num2, sk2.get_center()))
        self.play(
            ReplacementTransform(num2.copy(), res2))
        self.play(res2.set_color, BLUE, run_time=1)
        cuad_21 = Square().scale(0.15).set_color(BLUE).next_to(res2, RIGHT, buff=1)
        cuad_22 = Square().scale(0.15).set_color(BLUE).next_to(cuad_21, RIGHT, buff=0)
        cuad_23 = Square().scale(0.15).set_color(BLUE).next_to(cuad_22, UP, buff=0)
        cuad_24 = Square().scale(0.15).set_color(BLUE).next_to(cuad_21, UP, buff=0)
        self.play(ReplacementTransform(res2.copy(), cuad_21),
                  run_time=1)
        self.play(ReplacementTransform(res2.copy(), cuad_22),
                  run_time=1)
        self.play(ReplacementTransform(res2.copy(), cuad_23),
                  run_time=1)
        self.play(ReplacementTransform(res2.copy(), cuad_24),
                  run_time=1)
        self.wait(1)
        sk3 = TexMobject("S_3 = ").move_to(UP * -1.7 + LEFT * 1.5)
        num3 = TexMobject("3^2 = ").move_to(UP * -1.6)
        res3 = TexMobject("9").move_to(UP * -1.6 + RIGHT * 1)
        self.play(GrowFromCenter(sk3))
        self.play(FadeInFromPoint(num3, sk3.get_center()))
        self.play(ReplacementTransform(num3.copy(), res3))
        self.play(res3.set_color, GREEN, run_time=1)
        cuad_31 = Square().scale(0.1).set_color(GREEN).next_to(res3, RIGHT, buff=1)
        cuad_32 = Square().scale(0.1).set_color(GREEN).next_to(cuad_31, RIGHT, buff=0)
        cuad_33 = Square().scale(0.1).set_color(GREEN).next_to(cuad_32, RIGHT, buff=0)
        cuad_34 = Square().scale(0.1).set_color(GREEN).next_to(cuad_31, UP, buff=0)
        cuad_35 = Square().scale(0.1).set_color(GREEN).next_to(cuad_32, UP, buff=0)
        cuad_36 = Square().scale(0.1).set_color(GREEN).next_to(cuad_33, UP, buff=0)
        cuad_37 = Square().scale(0.1).set_color(GREEN).next_to(cuad_34, UP, buff=0)
        cuad_38 = Square().scale(0.1).set_color(GREEN).next_to(cuad_35, UP, buff=0)
        cuad_39 = Square().scale(0.1).set_color(GREEN).next_to(cuad_36, UP, buff=0)
        self.play(ReplacementTransform(res3.copy(), cuad_31), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_32), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_33), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_36), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_35), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_34), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_37), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_38), run_time=0.5)
        self.play(ReplacementTransform(res3.copy(), cuad_39), run_time=0.5)
        self.wait(2)
        self.play(FadeOutAndShiftDown(text1, UP), FadeOutAndShiftDown(sk1, UP), FadeOutAndShiftDown(num1, UP),
                  FadeOutAndShiftDown(res1, UP), FadeOutAndShiftDown(cuad_1, UP),
                  FadeOutAndShiftDown(sk2, UP), FadeOutAndShiftDown(num2, UP), FadeOutAndShiftDown(res2, UP),
                  FadeOutAndShiftDown(cuad_21, UP),
                  FadeOutAndShiftDown(cuad_22, UP), FadeOutAndShiftDown(cuad_23, UP), FadeOutAndShiftDown(cuad_24, UP),
                  FadeOutAndShiftDown(sk3, DOWN), FadeOutAndShiftDown(num3, DOWN), FadeOutAndShiftDown(res3, DOWN),
                  FadeOutAndShiftDown(cuad_31, DOWN), FadeOutAndShiftDown(cuad_32, DOWN),
                  FadeOutAndShiftDown(cuad_33, DOWN),
                  FadeOutAndShiftDown(cuad_36, DOWN), FadeOutAndShiftDown(cuad_35, DOWN),
                  FadeOutAndShiftDown(cuad_34, DOWN),
                  FadeOutAndShiftDown(cuad_37, DOWN), FadeOutAndShiftDown(cuad_38, DOWN),
                  FadeOutAndShiftDown(cuad_39, DOWN), run_time=1)
        self.wait(1)


class NumTri1(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        texto = TextMobject("{\\Large Y,\\ }", "{\\Large ¿Qué\\ }", "{\\Large es\\ }", "{\\Large un\\ }",
                            "{\\Large número\\ }", "{\\Large triangular\\ }", "{\\Large?\\ }")
        texto.to_edge(UP)
        self.play(Write(texto), run_time=2)
        self.play(texto[5].set_color, YELLOW, run_time=0.5)
        tri = Triangle()
        tri.next_to(texto, DOWN, buff=1).set_color(YELLOW).scale(1.5)
        self.play(ReplacementTransform(texto[5], tri), run_time=0.75)
        self.wait(1)
        self.play(FadeOutAndShiftDown(tri, UP), FadeOutAndShiftDown(texto, UP))
        self.wait(1)


class NumTri2(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject(
            "{\\Large Un número triangular es aquel que\\\\ puede recomponerse en la forma de un \\\\ \\ }",
            "{\\Large triángulo,\\ }", "{\\Large equilátero\\ }", "{\\Large o\\ }", "{\\Large isósceles\\ }")
        text1.to_edge(UP)
        self.play(Write(text1))
        self.play(text1[2].set_color, BLUE, text1[4].set_color, PURPLE, run_time=1)
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0])).set_color(PURPLE).move_to(
            UP * 0.7 + RIGHT * 3.2)
        triangle2 = Triangle().move_to(UP)
        self.play(ReplacementTransform(text1[2], triangle2), ReplacementTransform(text1[4], triangle))
        self.play(triangle2.set_color, BLUE, Rotate(triangle, PI / 4))
        self.wait(2)
        grupo = VGroup(text1[0], text1[1], text1[2], text1[3], triangle2)
        self.play(FadeOutAndShiftDown(grupo, UP), FadeOutAndShiftDown(triangle, UP))
        self.wait(1)


class NumTri3(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("{\\Large La fórmula para obtener un \\\\número triangular es: \\ }").to_edge(UP)
        elemento = TexMobject("T_k =").move_to(LEFT * 1).scale(1.2)
        formula = TexMobject("n(n+1)\over 2").move_to(RIGHT * 1).scale(1.2)
        self.play(Write(text1))
        self.play(Write(elemento), Write(formula))
        self.wait(3)
        text2 = TextMobject("{\\Large También se puede expresar con el\\\\ coeficiente binomial: }").to_edge(UP)
        coef = TexMobject("{n+1\choose 2}").move_to(RIGHT * 1).scale(1.2)
        self.play(ReplacementTransform(text1, text2))
        self.play(ReplacementTransform(formula, coef))
        self.wait(2)
        grupo = VGroup(text1, text2, elemento, coef)
        self.play(FadeOutAndShiftDown(grupo, UP))
        self.wait(1)


class DemoTri(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("Los primeros elementos de la sucesión son: ").to_edge(UP)
        self.play(Write(text1))
        tk1 = TexMobject("T_1 = ").move_to(UP * 2.3 + LEFT * 2)
        num1 = TexMobject("{1(1+1)\over2} = ").move_to(UP * 2.4)
        res1 = TexMobject("1").move_to(UP * 2.4 + RIGHT * 2)
        self.play(GrowFromCenter(tk1))
        self.play(FadeInFromPoint(num1, tk1.get_center()))
        self.wait(1)
        self.play(ReplacementTransform(num1.copy(), res1))
        self.play(res1.set_color, YELLOW, run_time=0.5)
        cuad_1 = Square().scale(0.3).set_color(YELLOW).next_to(res1, RIGHT, buff=1)
        self.play(ReplacementTransform(res1.copy(), cuad_1)
                  , run_time=2)
        tri1 = Polygon(np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 0, 0])).scale(1).set_color(
            YELLOW).next_to(res1, RIGHT, buff=1)
        self.play(ClockwiseTransform(cuad_1, tri1))
        self.wait(1)
        tk2 = TexMobject("T_2 = ")
        tk2.move_to(LEFT * 2)
        num2 = TexMobject("{2(2+1)\over2} = ")
        res2 = TexMobject("3")
        res2.move_to(RIGHT * 2)
        self.play(GrowFromCenter(tk2))
        self.play(FadeInFromPoint(num2, tk2.get_center()))
        self.wait(1)
        self.play(ReplacementTransform(num2.copy(), res2))
        self.play(res2.set_color, MAROON_A, run_time=0.5)
        cuad_21 = Square().scale(0.25).set_color(MAROON_A).next_to(res2, RIGHT, buff=1)
        cuad_22 = Square().scale(0.25).set_color(MAROON_A).next_to(cuad_21, RIGHT, buff=0)
        cuad_23 = Square().scale(0.25).set_color(MAROON_A).next_to(cuad_21, UP, buff=0)
        grupo1 = VGroup(cuad_21, cuad_22, cuad_23)
        self.play(ReplacementTransform(res2.copy(), grupo1)
                  , run_time=2)
        self.wait(1)
        tri2 = Polygon(np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 0, 0])).scale(1).set_color(
            MAROON_A).next_to(res2, RIGHT, buff=1)
        self.play(ClockwiseTransform(grupo1, tri2))
        self.wait(2)
        tk3 = TexMobject("T_3 = ")
        tk3.move_to(UP * -2.3 + LEFT * 2)
        num3 = TexMobject("{3(3+1)\over2} = ")
        num3.move_to(UP * -2.4)
        res3 = TexMobject("6")
        res3.move_to(UP * -2.4 + RIGHT * 2)
        self.play(GrowFromCenter(tk3))
        self.play(FadeInFromPoint(num3, tk3.get_center()))
        self.wait(1)
        self.play(ReplacementTransform(num3.copy(), res3))
        self.play(res3.set_color, ORANGE, run_time=0.5)
        cuad_31 = Square().scale(0.166).set_color(ORANGE).next_to(res3, RIGHT, buff=1)
        cuad_32 = Square().scale(0.166).set_color(ORANGE).next_to(cuad_31, RIGHT, buff=0)
        cuad_33 = Square().scale(0.166).set_color(ORANGE).next_to(cuad_32, RIGHT, buff=0)
        cuad_34 = Square().scale(0.166).set_color(ORANGE).next_to(cuad_31, UP, buff=0)
        cuad_35 = Square().scale(0.166).set_color(ORANGE).next_to(cuad_32, UP, buff=0)
        cuad_36 = Square().scale(0.166).set_color(ORANGE).next_to(cuad_34, UP, buff=0)
        grupo2 = VGroup(cuad_31, cuad_32, cuad_33, cuad_34, cuad_35, cuad_36)
        self.play(ReplacementTransform(res3.copy(), grupo2)
                  , run_time=2)
        self.wait(1)
        tri3 = Polygon(np.array([0, 0, 0]), np.array([0, 1, 0]), np.array([1, 0, 0])).scale(1).set_color(
            ORANGE).next_to(res3, RIGHT, buff=1)
        self.play(ClockwiseTransform(grupo2, tri3))
        self.wait(2)
        grupo0 = VGroup(grupo1, grupo2)
        grupoOff = VGroup(text1, tk1, tk2, tk3, res1, res2, res3, num1, num2, num3, cuad_1)
        self.play(FadeOutAndShiftDown(grupo0, DOWN), FadeOutAndShiftDown(grupoOff, DOWN))
        self.wait(1)


class TriConsec(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("{\\large La\\ }", "{\\large suma\\ }", "{\\large de\\ }", "{\\large dos\\ }",
                            "{\\large números\\ }",
                            "{\\large triangulares\\ }", "{\\large consecutivos\\\\ \\ }",
                            "{\\large es un número\\ }", "{\\large cuadrado,\\ }", "{\\large siendo esta\\ }",
                            "{\\large suma\\\\ \\ }", "{\\large el cuadrado de la diferencia \\ }",
                            "{\\large entre ambos números.\\ }").to_edge(UP)
        self.play(Write(text1))
        self.play(text1[3].set_color_by_gradient, GREEN_E, GREEN_A, text1[5].set_color_by_gradient, RED_E, RED_A,
                  text1[8].set_color_by_gradient, BLUE_E, BLUE_A)
        self.wait(2)
        cuad_1 = Square().set_color(GREEN_E).scale(0.4).move_to(UP * 0.1)
        cuad_21 = Square().set_color(RED_E).scale(0.4).next_to(cuad_1, RIGHT, buff=0)
        cuad_22 = Square().set_color(RED_E).scale(0.4).next_to(cuad_21, UP, buff=0)
        cuad_23 = Square().set_color(RED_E).scale(0.4).next_to(cuad_22, LEFT, buff=0)
        grupoCuad = VGroup(cuad_21, cuad_22, cuad_23)
        self.play(TransformFromCopy(text1[3], cuad_1), TransformFromCopy(text1[5], grupoCuad))
        self.wait(1)
        cuad_final = Square().set_color(BLUE_E).scale(0.8).move_to(cuad_1.get_corner(UP + RIGHT))
        self.play(FadeOut(cuad_1), FadeOut(grupoCuad), TransformFromCopy(text1[8], cuad_final))
        self.wait(1)
        text2 = TextMobject("{\\large Comprobado de manera algebraica\\ }")
        self.play(ReplacementTransform(cuad_final, text2))
        self.play(text2.shift, UP * 1)
        sumCons = TexMobject("T_n", "+", "T_{n-1}", "=").move_to(LEFT * 3).scale(0.8)
        self.play(TransformFromCopy(text1[1], sumCons))
        self.wait(1)
        arg1_1 = TexMobject("\\left(", "{{n^2}\over{2}}", "+", "{{n}\over{2}}", "\\right)").next_to(sumCons,
                                                                                                    RIGHT * 0.5,
                                                                                                    buff=0.3).scale(0.8)
        sum1 = TexMobject("+").next_to(arg1_1, RIGHT * 0.5, buff=0.3).scale(0.8)
        arg1_2 = TexMobject("\\left(", "{{(n-1)^2}\over{2}}", "+", "{{n-1}\over{2}}", "\\right)").move_to(
            RIGHT * 2.6).scale(0.8)
        self.play(TransformFromCopy(sumCons[0], arg1_1), TransformFromCopy(sumCons[1], sum1),
                  TransformFromCopy(sumCons[2], arg1_2))
        sumConscc = sumCons.copy().move_to(DOWN * 1.5 + LEFT * 2)
        arg2_1 = arg1_1.copy().next_to(sumConscc, RIGHT * 0.5, buff=0.3)
        arg2_2 = TexMobject("\\left(", "{{n^2}\over{2}}", "-", "{{n}\over{2}}", "\\right)").move_to(
            RIGHT * 2.5 + DOWN * 1.5).scale(0.8)
        sum2 = TexMobject("+").next_to(arg2_1, RIGHT * 0.5, buff=0.3).scale(0.8)
        textoATachar1 = VGroup(arg2_1[2], arg2_1[3])
        textonoTachado1 = VGroup(arg2_1[0], arg2_1[1], arg2_1[4])
        textoATachar2 = VGroup(arg2_2[2], arg2_2[3])
        textonoTachado2 = VGroup(arg2_2[0], arg2_2[1], arg2_2[4])
        tacha1 = Cross(textoATachar1)
        tacha2 = Cross(textoATachar2)
        tacha1.set_stroke(RED, 6)
        tacha2.set_stroke(RED, 6)
        self.wait(2)
        self.play(TransformFromCopy(sumCons, sumConscc), TransformFromCopy(sum1, sum2),
                  TransformFromCopy(arg1_1, arg2_1),
                  TransformFromCopy(arg1_2, arg2_2))
        self.wait(2)
        self.play(ShowCreation(tacha1), ShowCreation(tacha2), FadeOut(textoATachar1), FadeOut(textoATachar2), )
        self.play(FadeOut(tacha1), FadeOut(tacha2),
                  arg2_1[1].shift, RIGHT * 0.4, arg2_2[1].shift, RIGHT * 0.4)
        self.wait(2)
        textoABracket = VGroup(arg2_1, sum2, arg2_2)
        llave = Brace(textoABracket, DOWN, buff=SMALL_BUFF)
        textoLlave = llave.get_text("$n^2$")
        self.play(
            GrowFromCenter(llave),
            FadeIn(textoLlave),
            text1[11].set_color, GOLD_A,
            textoLlave.set_color, GOLD_A,
            run_time=1)
        self.wait(3)
        text3 = TextMobject("{\\large Otra representación visual\\ }").move_to(UP * 1)
        Todo = VGroup(sumCons, sumConscc, arg1_1, sum1, arg1_2, textonoTachado1, sum2, textonoTachado2, llave)
        self.play(ReplacementTransform(text2, text3), FadeOutAndShiftDown(Todo, DOWN), textoLlave.shift, LEFT * 5,
                  UP * 3.1)
        sumaVis = TexMobject("3", "+", "6", "=", "9").move_to(UP * 0.2)
        restaVis = TexMobject("6", "-", "3", "=", "3").move_to(DOWN * 0.5)
        restaVis[0].set_color(RED_D)
        restaVis[2].set_color(DARK_BLUE)

        cuadrado6_1 = Square().scale(0.2).set_color(RED_D).move_to(RIGHT * 3)
        cuadrado6_2 = Square().scale(0.2).set_color(RED_D).next_to(cuadrado6_1, LEFT, buff=0)
        cuadrado6_3 = Square().scale(0.2).set_color(RED_D).next_to(cuadrado6_2, LEFT, buff=0)
        cuadrado6_4 = Square().scale(0.2).set_color(RED_D).next_to(cuadrado6_1, DOWN, buff=0)
        cuadrado6_5 = Square().scale(0.2).set_color(RED_D).next_to(cuadrado6_4, LEFT, buff=0)
        cuadrado6_6 = Square().scale(0.2).set_color(RED_D).next_to(cuadrado6_4, DOWN, buff=0)
        cuadrados6 = VGroup(cuadrado6_1, cuadrado6_2, cuadrado6_3, cuadrado6_4, cuadrado6_5, cuadrado6_6)

        cuadrado3_1 = Square().scale(0.2).set_color(DARK_BLUE).move_to(LEFT * 3)
        cuadrado3_2 = Square().scale(0.2).set_color(DARK_BLUE).next_to(cuadrado3_1, RIGHT, buff=0)
        cuadrado3_3 = Square().scale(0.2).set_color(DARK_BLUE).next_to(cuadrado3_1, UP, buff=0)
        cuadrados3 = VGroup(cuadrado3_1, cuadrado3_2, cuadrado3_3)

        cuadrado9 = Square().scale(0.6).set_color(PINK).move_to(DOWN * 2)

        self.play(FadeIn(sumaVis))
        self.play(sumaVis[0].set_color, DARK_BLUE, sumaVis[2].set_color, RED_D,
                  TransformFromCopy(sumaVis[0], cuadrados3)
                  , TransformFromCopy(sumaVis[2], cuadrados6), cuadrados6.shift, DOWN * 1.6, cuadrados3.shift,
                  DOWN * 2.4)
        self.play(cuadrados6.shift, LEFT * 2.6, cuadrados3.shift, RIGHT * 2.6)
        self.wait(1)
        CuadradosJuntos = VGroup(cuadrados3, cuadrados6)
        self.play(sumaVis[4].set_color, PINK, TransformFromCopy(sumaVis[4], cuadrado9), FadeOut(CuadradosJuntos))
        self.play(TransformFromCopy(sumaVis, restaVis))
        self.play(textoLlave.move_to, restaVis[4], FadeOut(restaVis[4]))
        self.play(textoLlave.shift, UP * 0.1 + RIGHT * 0.1, textoLlave.set_color, PINK)
        restaFade = VGroup(restaVis[0], restaVis[1], restaVis[2], restaVis[3])
        todo = VGroup(text1, text3, sumaVis, restaFade, cuadrado9, textoLlave)
        self.wait(2)
        self.play(FadeOutAndShiftDown(todo, DOWN))
        self.wait(1)


class CuadTri1(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("{\\large Un número cuadrado triangular es\\\\ aquel que sea triangular y cuadrado \\ }"). \
            to_edge(UP)
        self.play(Write(text1))
        self.wait(1)
        text2 = TextMobject("{\\large ¿Con qué fórmula obtenemos dicha sucesión? \\ }").to_edge(UP)
        self.play(ReplacementTransform(text1, text2))
        self.wait(2)
        text3 = TextMobject("{\\large Se habían definido previamente\\\\ a las sucesiones como: \\\ }").to_edge(UP)
        self.play(ReplacementTransform(text2, text3))
        formulas = TexMobject("= N_k =", "S_k = n^2")
        forTK1_1 = TexMobject("T_k =")
        forTK1_2 = TexMobject("n(n+1)\over 2")
        formulas[0].move_to(RIGHT * 0.1)
        formulas[1].move_to(LEFT * 3)
        forTK1_1.move_to(RIGHT * 2.5 + DOWN * 0.05)
        forTK1_2.move_to(RIGHT * 4 + DOWN * 0.15)
        self.play(Write(formulas[1]), Write(forTK1_1), Write(forTK1_2))
        text4 = TextMobject("{\\large Si queremos números de ambas sucesiones, se establece: ").move_to(UP * 1.5)
        self.play(Write(text4))
        self.play(Write(formulas[0]))
        self.wait(2)
        text5 = TextMobject("{\\large Se define a $n$ como la raíz de un número triangular $N$\\ }").to_edge(UP)
        formulas1 = VGroup(formulas, forTK1_1, forTK1_2)
        self.play(FadeOut(formulas1), ReplacementTransform(text4, text5), FadeOut(text3))
        self.wait(2)
        forTK2_1 = TexMobject("N =").move_to(LEFT)
        forTK2_2 = TexMobject("n(n+1)\over 2").next_to(forTK2_1, RIGHT, buff=0.2)
        formulas2 = VGroup(forTK2_1, forTK2_2)
        self.play(Write(forTK2_1), Write(forTK2_2))
        self.wait(2)
        presupuesto = TextMobject("{\\footnotesize No había presupuesto para animar todo el desarrollo "
                                  "\\frownie \\ }").to_corner(DL).set_color(DARK_GRAY)
        text6 = TextMobject("{\\large Con esta definición y la fórmula general cuadrática,\\\\ se obtiene\\ }").to_edge(
            UP)
        self.add(presupuesto)
        self.play(ReplacementTransform(text5, text6))
        resultado1_1 = TexMobject("{n} =").move_to(LEFT * 1.3)
        resultado1_2 = TexMobject("{\sqrt{8N +1} -1}\over{2}").next_to(resultado1_1, RIGHT, buff=0.2)
        resultado1 = VGroup(resultado1_1, resultado1_2)
        self.play(ReplacementTransform(formulas2, resultado1))
        self.wait(2)
        text7 = TextMobject("Por lo tanto, $N$ es triangular $\Leftrightarrow 8N+1 $ es cuadrado.").to_edge(UP)
        self.play(ReplacementTransform(text6, text7))
        self.wait(2)
        text8 = TextMobject("Consecuentemente, un número cuadrado $M^2$ también es \\\\ triangular $\Leftrightarrow"
                            "8M^2+1$ es cuadrado. De tal manera,\\\\ hay números $x$ y $y$ que satisfacen a "
                            "$x^{2} -8y^{2} = 1$.").to_edge(UP)
        text9 = TextMobject("Esta es una Ecuación de Pell$^1$ con $n=8$ \\\\Al resolverla ignorando las ",
                            "soluciones triviales para ese \\\\valor de $n$ obtenemos la sucesión de ",
                            "\\\\números", " cuadrados", " triangulares.")
        presupuesto2 = TextMobject("{\\footnotesize Tampoco había presupuesto para la Ecuación de Pell\\ }") \
            .to_corner(DL).set_color(DARK_GRAY)
        self.play(ReplacementTransform(text7, text8), ReplacementTransform(resultado1, text9), ReplacementTransform(
            presupuesto, presupuesto2
        ))
        self.play(text9[3].set_color, RED, text9[4].set_color, BLUE)
        self.wait(3)
        Todo = VGroup(text8, text9, presupuesto2)
        self.play(FadeOutAndShiftDown(Todo, DOWN))
        self.wait(1)


class CuadTri2(Scene):
    def construct(self):
        credito = TextMobject("{\\fontsize{5}{10}\\selectfont @eduardosalaz}").to_corner(DR).set_color(GRAY)
        self.add(credito)
        text1 = TextMobject("Ilustrando con la solución trivial de 1").to_edge(UP)
        formula = TexMobject("M^{2} \Leftrightarrow 8M^2+1").next_to(text1, DOWN, buff=0.5)
        self.play(Write(text1))
        self.wait(3)
        text2 = TextMobject("Se comprueba con la fórmula que acabamos de ver").to_edge(UP)
        self.play(ReplacementTransform(text1, text2))
        prueba1 = TexMobject("1^2 =", "1", "\Leftrightarrow", "8*1^2 +1 =", "9")
        self.play(Write(prueba1), Write(formula))
        self.wait(2)
        textoABracket1 = VGroup(prueba1[0], prueba1[1])
        llave1 = Brace(textoABracket1, DOWN, buff=SMALL_BUFF)
        textoLlave1 = llave1.get_text("Triangular").set_color(YELLOW_D)
        self.play(
            GrowFromCenter(llave1),
            FadeIn(textoLlave1),
            run_time=1)
        textoABracket2 = VGroup(prueba1[3], prueba1[4])
        llave2 = Brace(textoABracket2, UP, buff=SMALL_BUFF)
        self.wait(1)
        textoLlave2 = llave2.get_text("Cuadrado").set_color(PURPLE_D)
        self.play(
            GrowFromCenter(llave2),
            FadeIn(textoLlave2)
        )
        self.wait(3)
        text3 = TextMobject("¿Qué tal otro ejemplo?, esta vez con el 36").to_edge(UP)
        prueba36 = TexMobject("6^2 =", "36", "\Leftrightarrow", "8*36^2 +1=", "289")
        self.play(ReplacementTransform(text2, text3), ReplacementTransform(prueba1, prueba36), FadeOut(llave1), FadeOut(llave2)
                  , FadeOut(textoLlave1), FadeOut(textoLlave2))
        self.wait(2)
        sqrt = TexMobject("\sqrt{289} =17").next_to(prueba36, RIGHT, buff=1).set_color(PURPLE_D)
        textoABracket3 = VGroup(prueba36[0], prueba1[1])
        llave3 = Brace(textoABracket3, DOWN, buff=SMALL_BUFF)
        textoLlave3 = llave3.get_text("Triangular").set_color(YELLOW_D)
        self.play(
            GrowFromCenter(llave3),
            FadeIn(textoLlave3),
            run_time=1)
        textoABracket4 = VGroup(prueba1[3], prueba1[4])
        llave4 = Brace(textoABracket4, UP, buff=SMALL_BUFF)
        textoLlave4 = llave4.get_text("Cuadrado").set_color(PURPLE_D)
        self.play(
            GrowFromCenter(llave4),
            FadeIn(textoLlave4),
            FadeIn(sqrt)
        )
        self.wait(2)
        numero = TexMobject("36").scale(2.5).move_to(UP*2.5)
        text4 = TextMobject("De manera visual:").to_edge(UP)
        self.play(ReplacementTransform(text3, text4), FadeOut(formula), FadeOut(prueba36), FadeOut(llave3), FadeOut(llave4), FadeOut(textoLlave3), FadeOut(textoLlave4),
                  FadeOut(sqrt))
        self.play(Write(numero))
        self.wait(2)
        cuadrado36_1 = Square().scale(0.2).set_color(RED).move_to(DOWN*0.5)
        cuadrado36_2 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_1, RIGHT, buff=0)
        cuadrado36_3 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_2, RIGHT, buff=0)
        cuadrado36_4 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_3, RIGHT, buff=0)
        cuadrado36_5 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_4, RIGHT, buff=0)
        cuadrado36_6 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_5, RIGHT, buff=0)
        cuadrado36_7 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_1, UP, buff=0)
        cuadrado36_8 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_2, UP, buff=0)
        cuadrado36_9 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_3, UP, buff=0)
        cuadrado36_10 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_4, UP, buff=0)
        cuadrado36_11 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_5, UP, buff=0)
        cuadrado36_12 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_6, UP, buff=0)
        cuadrado36_13 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_7, UP, buff=0)
        cuadrado36_14 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_8, UP, buff=0)
        cuadrado36_15 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_9, UP, buff=0)
        cuadrado36_16 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_10, UP, buff=0)
        cuadrado36_17 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_11, UP, buff=0)
        cuadrado36_18 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_12, UP, buff=0)
        cuadrado36_19 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_13, UP, buff=0)
        cuadrado36_20 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_14, UP, buff=0)
        cuadrado36_21 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_15, UP, buff=0)
        cuadrado36_22 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_16, UP, buff=0)
        cuadrado36_23 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_17, UP, buff=0)
        cuadrado36_24 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_18, UP, buff=0)
        cuadrado36_25 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_19, UP, buff=0)
        cuadrado36_26 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_20, UP, buff=0)
        cuadrado36_27 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_21, UP, buff=0)
        cuadrado36_28 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_22, UP, buff=0)
        cuadrado36_29 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_23, UP, buff=0)
        cuadrado36_30 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_24, UP, buff=0)
        cuadrado36_31 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_25, UP, buff=0)
        cuadrado36_32 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_26, UP, buff=0)
        cuadrado36_33 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_27, UP, buff=0)
        cuadrado36_34 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_28, UP, buff=0)
        cuadrado36_35 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_29, UP, buff=0)
        cuadrado36_36 = Square().scale(0.2).set_color(RED).next_to(cuadrado36_30, UP, buff=0)
        Cuadrado36 = VGroup(cuadrado36_1, cuadrado36_2, cuadrado36_3, cuadrado36_4, cuadrado36_5, cuadrado36_6,
            cuadrado36_7, cuadrado36_8, cuadrado36_9, cuadrado36_10, cuadrado36_11, cuadrado36_12, cuadrado36_13,
            cuadrado36_14, cuadrado36_15, cuadrado36_16, cuadrado36_17, cuadrado36_18, cuadrado36_19, cuadrado36_20,
            cuadrado36_21, cuadrado36_22, cuadrado36_23, cuadrado36_24, cuadrado36_25, cuadrado36_26, cuadrado36_27,
            cuadrado36_28, cuadrado36_29, cuadrado36_30, cuadrado36_31, cuadrado36_32, cuadrado36_33, cuadrado36_34,
            cuadrado36_35, cuadrado36_36).move_to(LEFT*0.0001)
        self.play(numero.set_color, RED, TransformFromCopy(numero, Cuadrado36), run_time=1)
        textoABracket5 = VGroup(cuadrado36_1, cuadrado36_2, cuadrado36_3, cuadrado36_4, cuadrado36_5, cuadrado36_6)
        llave5 = Brace(textoABracket5, DOWN, buff=SMALL_BUFF)
        textoLlave5 = llave5.get_text("$6$").set_color(RED)
        self.wait(1)
        textoABracket6 = VGroup(cuadrado36_1, cuadrado36_7, cuadrado36_13, cuadrado36_19, cuadrado36_25, cuadrado36_31)
        llave6 = Brace(textoABracket6, LEFT, buff=SMALL_BUFF)
        textoLlave6 = llave6.get_text("$6$").set_color(RED)
        self.play(
            GrowFromCenter(llave5),
            FadeIn(textoLlave5),
            GrowFromCenter(llave6),
            FadeIn(textoLlave6),
        )
        self.wait(3)
        self.play(FadeOut(Cuadrado36), FadeOut(llave5), FadeOut(llave6), FadeOut(textoLlave5), FadeOut(textoLlave6))
        self.wait(2)
        cuadrado36_1 = Square().scale(0.2).set_color(BLUE).move_to(DOWN*0.9)
        cuadrado36_2 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_1, RIGHT, buff=0)
        cuadrado36_3 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_2, RIGHT, buff=0)
        cuadrado36_4 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_3, RIGHT, buff=0)
        cuadrado36_5 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_4, RIGHT, buff=0)
        cuadrado36_6 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_5, RIGHT, buff=0)
        cuadrado36_7 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_6, RIGHT, buff=0)
        cuadrado36_8 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_7, RIGHT, buff=0)
        cuadrado36_9 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_1, UP, buff=0)
        cuadrado36_10 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_2, UP, buff=0)
        cuadrado36_11 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_3, UP, buff=0)
        cuadrado36_12 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_4, UP, buff=0)
        cuadrado36_13 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_5, UP, buff=0)
        cuadrado36_14 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_6, UP, buff=0)
        cuadrado36_15 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_7, UP, buff=0)
        cuadrado36_16 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_9, UP, buff=0)
        cuadrado36_17 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_10, UP, buff=0)
        cuadrado36_18 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_11, UP, buff=0)
        cuadrado36_19 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_12, UP, buff=0)
        cuadrado36_20 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_13, UP, buff=0)
        cuadrado36_21 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_14, UP, buff=0)
        cuadrado36_22 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_16, UP, buff=0)
        cuadrado36_23 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_17, UP, buff=0)
        cuadrado36_24 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_18, UP, buff=0)
        cuadrado36_25 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_19, UP, buff=0)
        cuadrado36_26 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_20, UP, buff=0)
        cuadrado36_27 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_22, UP, buff=0)
        cuadrado36_28 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_23, UP, buff=0)
        cuadrado36_29 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_24, UP, buff=0)
        cuadrado36_30 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_25, UP, buff=0)
        cuadrado36_31 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_27, UP, buff=0)
        cuadrado36_32 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_28, UP, buff=0)
        cuadrado36_33 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_29, UP, buff=0)
        cuadrado36_34 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_31, UP, buff=0)
        cuadrado36_35 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_32, UP, buff=0)
        cuadrado36_36 = Square().scale(0.2).set_color(BLUE).next_to(cuadrado36_34, UP, buff=0)
        Triangulo36 = VGroup(cuadrado36_1, cuadrado36_2, cuadrado36_3, cuadrado36_4, cuadrado36_5, cuadrado36_6,
            cuadrado36_7, cuadrado36_8, cuadrado36_9, cuadrado36_10, cuadrado36_11, cuadrado36_12, cuadrado36_13,
            cuadrado36_14, cuadrado36_15, cuadrado36_16, cuadrado36_17, cuadrado36_18, cuadrado36_19, cuadrado36_20,
            cuadrado36_21, cuadrado36_22, cuadrado36_23, cuadrado36_24, cuadrado36_25, cuadrado36_26, cuadrado36_27,
            cuadrado36_28, cuadrado36_29, cuadrado36_30, cuadrado36_31, cuadrado36_32, cuadrado36_33, cuadrado36_34,
            cuadrado36_35, cuadrado36_36).move_to(RIGHT*0.1+DOWN*0.5)
        self.play(numero.set_color, BLUE, TransformFromCopy(numero, Triangulo36), run_time=1)
        self.wait(3)
        self.play(FadeOut(text4), FadeOut(Triangulo36), FadeOut(numero))
        final = TextMobject("{\\Large ¿Preguntas? \\ }")
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(final))
        self.wait(1)




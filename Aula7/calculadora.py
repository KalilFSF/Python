import math


from flask import render_template, request
import math as mt



def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]


    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe log real de {num1}."
        else:
            resultado = math.log(num1)
            etapas = f"log({num1}) = {resultado}"

    elif operacao == "basc":

        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        num3_valor = request.form.get("num3", "").strip()
        if not num3_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num3 = float(num3_valor)

        if num1 == 0:
            resultado = "Erro: número igual a 0"
            etapas = f"Não existe bascara real de {num1}."
        else:

            delta = (num2 ** 2) - (4 * num1 * num3)

            if delta < 0:
                resultado = "Erro: Sem raízes reais"
                etapas = f"Delta é negativo ({delta})."
            
            else:
                # Cálculo das duas raízes
                x1 = (-num2 + (delta ** 0.5)) / (2 * num1)
                x2 = (-num2 - (delta ** 0.5)) / (2 * num1)
        
                resultado = f"x1 = {x1:.2f}, x2 = {x2:.2f}"
                etapas = f"Δ = {num2}² - 4*({num1})*({num3}) = {delta}."

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)


        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"

        elif operacao == "/":
            if num2 <= 0:
                resultado = "Erro: número negativo"
                etapas = f"Não existe divisão real de {num2}."
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ** {num2} = {resultado}"

        else:
            resultado = "Operação invalida!"
            etapas= "A operação selecionada é invalida"

    return render_template(
    "calculadora.html",
    etapas=etapas,
    resultado=resultado)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Kalil Felipe</title>
    <style>
        /* Estilização Base */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background-color: #f4f7f6;
            color: #333333;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }

        /* Container do Currículo */
        .cv-container {
            background-color: #ffffff;
            max-width: 700px;
            width: 100%;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }

        /* Títulos Principais (Azul Escuro) */
        h1 {
            color: #0b2545;
            font-size: 2.2rem;
            margin-top: 0;
            border-bottom: 3px solid #134074;
            padding-bottom: 10px;
        }

        h2 {
            color: #134074;
            font-size: 1.4rem;
            margin-top: 30px;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Listas */
        ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        li {
            margin-bottom: 12px;
            font-size: 1.05rem;
        }

        strong {
            color: #0b2545;
            display: inline-block;
            width: 120px;
        }

        /* Links de Texto */
        a.email-link {
            color: #134074;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
        }

        a.email-link:hover {
            color: #0b2545;
            text-decoration: underline;
        }

        /* Botão do WhatsApp Integrado ao Design */
        .btn-whatsapp {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #134074; /* Mudado de verde para o Azul Escuro do Tema */
            color: #ffffff !important;
            font-size: 0.95rem;
            font-weight: 600;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 6px;
            margin-top: 5px;
            transition: background-color 0.2s ease-in-out, transform 0.1s ease;
        }

        .btn-whatsapp:hover {
            background-color: #0b2545;
            transform: translateY(-1px);
        }

        .btn-whatsapp:active {
            transform: translateY(0);
        }

        ::selection {
            background-color: #134074; /* Cor do fundo (Azul Escuro) */
            color: #ffffff;            /* Cor do texto (Branco) */
        }
        
        ::-moz-selection {
           background-color: #134074;
           color: #ffffff;
        }

    </style>
</head>
<body>

    <div class="cv-container">
        <h1>Currículo | Kalil</h1>

        <h2>Informações Pessoais</h2>
        <ul>
            <li><strong>Nome:</strong> Kalil Felipe Silva Fernandes</li>  
            <!-- CORREÇÃO: O link 'mailto' agora coincide exatamente com o e-mail exibido em tela -->
            <li><strong>Email:</strong> <a class="email-link" href="mailto:kalil.fsf@cotemig.com.br">kalil.fsf@cotemig.com.br</a></li>
            <!-- CORREÇÃO: Estrutura do link wa.me arrumada. Substitua os números abaixo pelo seu telefone real -->
            <li><strong>Telefone:</strong> 
                <a href="https://wa.me" target="_blank" class="btn-whatsapp">
                    Contatar via WhatsApp
                </a>
            </td>
        </ul>

        <h2>Experiência Profissional</h2>
        <ul>
            <li><strong>Empresa:</strong> Cotemig</li>
            <li><strong>Cargo:</strong> Desenvolvedor de Software</li>
            <li><strong>Período:</strong> Jan 2024 | Dez 2026</li>
        </ul>
    </div>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

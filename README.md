# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Meio Ambiente](https://img.shields.io/badge/Meio%20Ambiente-Consciente-2EA44F?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 📌 Sobre o projeto

Script em **Python** criado para uma campanha de conscientização ambiental da companhia de saneamento da cidade. O programa recebe o tipo de imóvel e o consumo mensal de água, classifica o perfil de consumo e exibe um **alerta educativo** ao morador. 🌱

## 🎯 Objetivo

Ajudar os moradores a entender o próprio consumo de água e incentivar o uso consciente, evitando desperdícios e ajudando a identificar possíveis vazamentos.

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3**
- 💻 **Visual Studio Code**
- 🐙 **Git e GitHub**

## 📋 Regras de classificação

| Tipo de imóvel | Consumo mensal | Mensagem exibida |
|---|---|---|
| 🏢 Comercial | qualquer valor | Tarifa comercial aplicada – consulte o plano corporativo. |
| 🏬 Apartamento | menor que 10 m³ | Consumo econômico – excelente controle de água! |
| 🏠 Casa ou 🏬 apartamento | até 25 m³ | Consumo moderado – dentro do padrão residencial. |
| ⚠️ Qualquer outro caso | acima do limite residencial | Consumo excessivo – adote medidas de economia e verifique vazamentos. |

> 💡 A mensagem de consumo econômico vale apenas para apartamentos. Uma casa com menos de 10 m³ recebe a mensagem de consumo moderado.

## ▶️ Como executar

1. Instale o [Python](https://www.python.org/downloads/) no computador.
2. Clone este repositório:
```bash
   git clone https://github.com/thiagosantista1989-dev/consumo_agua.git
```
3. Entre na pasta do projeto:
```bash
   cd consumo_agua/consumo_agua
```
4. Execute o programa:
```bash
   python app.py
```
5. Informe o tipo de imóvel (`comercial`, `casa` ou `apartamento`) e o consumo mensal em m³.

## 💻 Exemplo de uso

```
O imovel do senhor é comercial, casa ou apartamento? apartamento
Qual o consumo em mensal em metros cubicos? 8
Consumo econômico – excelente controle de água!
```

## ✅ Testes realizados

| Tipo | Consumo (m³) | Resultado |
|---|---|---|
| apartamento | 9.9 | Consumo econômico |
| apartamento | 10 | Consumo moderado |
| casa | 5 | Consumo moderado |
| casa | 25 | Consumo moderado |
| casa | 30 | Consumo excessivo |
| apartamento | 40 | Consumo excessivo |
| comercial | 50 | Tarifa comercial |

## 📁 Estrutura do projeto

```
consumo_agua/
├── README.md
└── consumo_agua/
    └── app.py
```

## 👨‍💻 Autor

Feito por **Thiago Souza** 💙

📚 Atividade da Agenda 7 – Desenvolvimento de Sistemas

# ⚄ Gerador de Personagem RPG

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.x-092E20?style=flat-square&logo=django&logoColor=white)
![License](https://img.shields.io/badge/Licença-MIT-gold?style=flat-square)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-blueviolet?style=flat-square)

> Gerador aleatório de fichas de personagem para RPG de mesa, construído com Django. Cria personagens completos com raça, classe, atributos, origem, traços de personalidade e características sensoriais — tudo em um clique.

---

## 📸 Preview

<img width="1920" height="1080" alt="Captura de tela 2026-04-02 215053" src="https://github.com/user-attachments/assets/5b0a0308-a1d5-4d06-b745-a29765edaffb" />
<img width="1920" height="1080" alt="Captura de tela 2026-04-02 215751" src="https://github.com/user-attachments/assets/495185a2-eb13-4a2d-a218-1f3b02ec42d7" />

---

## ✨ Funcionalidades

- 🎲 **Geração completa** de fichas com um único clique
- 🧬 **16 raças** disponíveis (Humano, Elfo, Draconato, Tiefling, Autômato e mais)
- ⚔️ **14 classes** com subclasses únicas (Mago, Ladino, Bárbaro, Paladino, Bardo e mais)
- 📊 **Sistema de atributos numéricos** — 75 pontos distribuídos por camadas de prioridade, garantindo que os atributos primários da subclasse sejam sempre os mais altos
- 🗺️ **60 reinos de origem** com descrições temáticas
- 🎭 **Personalidade em 4 dimensões**: Arquétipo, Traço Sombra, Virtude e Vício
- 👁️ **Características sensoriais**: odor, voz, expressão e marcas de pele
- ⚡ **Geração via AJAX** — novo personagem sem recarregar a página
- 🌑 **Interface dark fantasy** com tema visual imersivo

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.12 | Linguagem principal |
| Django 6.x | Framework web |
| HTML/CSS/JS | Interface do usuário |
| Google Fonts (Cinzel + Crimson Pro) | Tipografia |

---

## 📁 Estrutura do Projeto

```
DjangoProject-gerador/
├── DjangoProject_gerador/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── geradordepersonagem/
│   ├── views.py        # lógica do gerador + views Django
│   ├── urls.py         # rotas do app
│   ├── models.py
│   └── apps.py
│
├── templates/
│   └── geradordepersonagem/
│       ├── index.html  # template principal
│       └── _ficha.html # partial do personagem (SSR)
│
└── manage.py
```

---

## 🚀 Como rodar localmente

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/miguelev1/gerador-de-personagem-rpg.git
cd gerador-de-personagem-rpg

# 2. Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 3. Instale as dependências
pip install django

# 4. Rode as migrações
python manage.py migrate

# 5. Inicie o servidor
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.

---

## 🎮 Como usar

1. Abra `http://127.0.0.1:8000/` no navegador
2. Uma ficha de personagem é gerada automaticamente
3. Clique em **"Gerar Novo Personagem"** para criar outro instantaneamente
4. A geração é feita via AJAX — sem recarregar a página

---

## ⚙️ Sistema de Atributos

Os 75 pontos são distribuídos em três camadas com hierarquia garantida:

| Camada | Atributos | Faixa de valores |
|---|---|---|
| **Primária** ★ | Definidos pela subclasse | 16 – 20 |
| **Secundária** | 1 ou 2 atributos de suporte | 12 – 15 |
| **Terciária** | Demais atributos | 5 – 11 |

> Os atributos primários são **sempre** maiores que os secundários, que são **sempre** maiores que os terciários.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: minha feature'`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🔜 Próximas funcionalidades
- [ ] Salvar fichas geradas (banco de dados)
- [ ] Exportar ficha em PDF
- [ ] Histórico de personagens
      
<p align="center">
  Feito com ☕ e dados de RPG
</p>

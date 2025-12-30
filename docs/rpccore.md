# RPC-Core
## Roleplay por Cartas — Núcleo do Sistema

> Especificação oficial do núcleo do sistema RPC (Roleplay por Cartas)

---

## 📌 Visão Geral

O **RPC-Core** é o conjunto mínimo de regras e conceitos necessários para jogar **qualquer versão do sistema RPC (Roleplay por Cartas)**.

Ele não é um jogo completo, mas um **núcleo estrutural**, sobre o qual jogos, cenários e módulos podem ser construídos.

O RPC-Core foi projetado para ser:

- simples  
- genérico  
- modular  
- independente de interface  
- independente de gênero  

> O RPC-Core não define como jogar, apenas **como organizar o jogo**.

---

## 📖 Índice

1. [Princípios Fundamentais](#princípios-fundamentais)  
2. [Carta](#carta)  
3. [Atributos da Carta](#atributos-da-carta)  
4. [Tipos de Carta](#tipos-de-carta)  
5. [Unidades e Associação](#unidades-e-associação)  
6. [Pontos de Vida (PV)](#pontos-de-vida-pv)  
7. [Dano](#dano)  
8. [Aplicação de Dano](#aplicação-de-dano)  
9. [PV Igual a Zero](#pv-igual-a-zero)  
10. [Economia Básica](#economia-básica)  
11. [Interface Independente](#interface-independente)  
12. [O que o RPC-Core Não Define](#o-que-o-rpc-core-não-define)  
13. [Filosofia do Sistema](#filosofia-do-sistema)  
14. [Anexos](#anexos)  

---

## Princípios Fundamentais

O RPC-Core se baseia nos seguintes princípios:

- Tudo no jogo é representado por **cartas**
- As regras são independentes da interface
- A complexidade vem de **módulos**, não do núcleo
- Exceções pertencem ao cenário, não ao sistema
- O núcleo nunca impõe narrativa, gênero ou estilo

> O RPC-Core estrutura.  
> O jogo nasce da combinação.

---

## Carta

Uma **Carta** representa qualquer coisa existente no jogo.

Exemplos:

- personagens  
- criaturas  
- armas  
- itens  
- ambientes  
- efeitos  
- conceitos abstratos  

Não há limite conceitual para o que uma carta pode representar.

---

## Atributos da Carta

Toda carta possui os seguintes atributos básicos:

| Atributo | Função |
|--------|-------|
| **Nome** | Identificação da carta |
| **Tipo** | Função estrutural |
| **Custo** | Valor relativo |
| **Aparência** | Visual ou descritiva |
| **Descrição** | Função prática |
| **PV** | Integridade |
| **Dano** | Capacidade ofensiva |

Cartas que não utilizam **PV** ou **Dano** mantêm esses valores como `0` ou inativos.

---

## Tipos de Carta

O RPC-Core define apenas os tipos **estruturais essenciais**.

### Unidade

Uma **Unidade** é uma carta principal que pode conter outras cartas.

Exemplos:

- personagem  
- criatura  
- veículo  
- edifício  
- mochila  
- sala  
- cidade  

---

### Parte de Unidade

Carta associada diretamente a uma Unidade.

**Funções:**
- modificar atributos  
- adicionar capacidades  
- representar componentes  

**Exemplos:**
- arma equipada  
- armadura  
- braço  
- implante  
- efeito contínuo  

> Uma Parte **sempre pertence** a uma Unidade.

---

### Item

Carta portátil e transferível.

Exemplos:
- poção  
- ferramenta  
- alimento  
- munição  
- livro  

Um Item pode se tornar uma Parte quando equipado.

---

### Inventário

Unidade especializada em armazenar cartas.

Exemplos:
- mochila  
- bolso  
- baú  
- armazém  
- menu digital  

Inventários podem ter limites ou não.

---

### Realm

Um **Realm** é o contexto ativo do jogo.

Pode representar:
- local  
- cena  
- dimensão  
- estado narrativo  
- camada da realidade  

Uma carta só interage plenamente quando está no **realm ativo**.

---

## Unidades e Associação

### Regra de Associação

Uma Parte pertence a uma Unidade quando está associada a ela pela interface utilizada (mesa, lista, comando, etc.).

### Regra de Herança

Partes podem modificar os atributos da Unidade à qual pertencem.

A forma dessa modificação é definida por **módulos ou cenário**, nunca pelo Core.

---

## Pontos de Vida (PV)

PV representam a **integridade** de uma carta.

Podem significar:
- vida  
- resistência  
- durabilidade  
- funcionamento  

Toda carta possui PV, mesmo que não sejam usados ativamente.

---

## Dano

Dano é um valor numérico que representa a capacidade de causar impacto negativo.

Cartas sem ataque utilizam dano `0`.

---

## Aplicação de Dano

Quando uma carta causa dano a outra:

1. Subtrai-se o dano dos PV do alvo  
2. Registra-se o novo valor de PV  
3. Se os PV atingirem `0` ou menos, aplica-se a regra de estado  

> O RPC-Core não exige rolagens.

---

## PV Igual a Zero

Quando uma carta atinge **0 PV**, ela não pode mais operar normalmente.

O significado disso é definido por módulos ou cenário.

Exemplos:
- destruição  
- morte  
- quebra  
- desativação  
- inconsciência  
- remoção de jogo  

---

## Economia Básica

### Custo

Custo é uma medida de **valor relativo**.

Pode representar:
- dinheiro  
- recursos  
- tempo  
- esforço  
- raridade  
- pontos narrativos  

O RPC-Core não define moeda.

---

### Obtenção

Cartas podem ser obtidas por:
- compra  
- troca  
- recompensa  
- criação  
- saque  
- narrativa  

Nenhuma forma é obrigatória.

---

### Troca

Duas cartas podem ser trocadas se ambas as partes concordarem.

Trocas podem ser:
- simétricas  
- assimétricas  
- narrativas  

---

## Interface Independente

O RPC-Core funciona igualmente em:

- cartas físicas  
- mesas virtuais  
- interfaces gráficas  
- dispositivos móveis  
- terminais de texto  

A interface **não altera as regras**, apenas as representa.

---

## O que o RPC-Core Não Define

O RPC-Core **não define**:

- turnos  
- dados  
- iniciativa  
- progressão  
- classes  
- perícias  
- narrativa  
- gênero  

Tudo isso pertence a módulos.

---

## Filosofia do Sistema

- regras mínimas  
- máxima adaptação  
- modularidade total  
- simplicidade acima de realismo  

> O RPC-Core é a fundação.  
> O jogo é construído acima dela.

---

## Anexos

### O que são Anexos

Anexos são documentos complementares associados a cartas.

Eles armazenam informações adicionais sem sobrecarregar o sistema básico.

Anexos **não são cartas** e não participam diretamente das regras.

---

### Regra de Ouro dos Anexos

Nenhuma informação presente em um Anexo pode ser obrigatória para o funcionamento básico do jogo.

Tudo que é essencial:
- deve estar na carta  
- ou nas regras centrais do RPC-Core  

---

## Encerramento

O RPC-Core foi projetado para ser:

- pequeno  
- estável  
- expansível  
- atemporal  

Qualquer versão do RPC — visual, textual, digital ou experimental — deve ser **compatível com este núcleo**.

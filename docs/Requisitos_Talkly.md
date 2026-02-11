# 📋 Requisitos do Projeto – Talkly

Este documento descreve o levantamento inicial de requisitos do projeto **Talkly**, uma plataforma de aprendizado de inglês baseada em Inteligência Artificial, focada em conversação personalizada, contínua e adaptativa.

Este levantamento serve como base para refinamento, priorização e definição do escopo do MVP.

---

## 1. Requisitos Funcionais

### 1.1 Cadastro e Identificação do Usuário
- **RF01** – O sistema deve permitir o cadastro de usuários  
- **RF02** – O sistema deve gerar um ID único para cada usuário  
- **RF03** – O sistema deve permitir login do usuário  
- **RF04** – O sistema deve manter a sessão do usuário autenticado  
- **RF05** – O sistema deve permitir recuperação de acesso  

---

### 1.2 Questionário Inicial (Onboarding)
- **RF06** – O sistema deve aplicar um questionário inicial obrigatório  
- **RF07** – O questionário deve coletar o nível atual de inglês  
- **RF08** – O questionário deve coletar o objetivo do usuário ao aprender inglês  
- **RF09** – O questionário deve coletar o tempo diário disponível  
- **RF10** – O sistema deve permitir atualizar essas informações futuramente  

---

### 1.3 Nivelamento de Inglês
- **RF11** – A IA deve avaliar o nível inicial de inglês do usuário  
- **RF12** – A avaliação deve considerar compreensão e produção  
- **RF13** – O sistema deve registrar o nível inicial do usuário  
- **RF14** – O sistema deve permitir reavaliações periódicas  

---

### 1.4 Plano de Estudo Personalizado
- **RF15** – A IA deve gerar um plano de estudo personalizado  
- **RF16** – O plano deve considerar nível, objetivo e tempo disponível  
- **RF17** – O plano deve priorizar listening e speaking  
- **RF18** – O plano deve incluir writing como apoio  
- **RF19** – O sistema deve permitir ajuste automático do plano  
- **RF20** – O plano deve evoluir ao longo do tempo  

---

### 1.5 Sessões de Aprendizado com IA
- **RF21** – O usuário deve poder iniciar sessões de estudo  
- **RF22** – A IA deve conversar com o usuário em inglês  
- **RF23** – A IA deve simular diálogos reais  
- **RF24** – A IA deve adaptar a complexidade da conversa  
- **RF25** – A IA deve fornecer feedback contextual  
- **RF26** – A IA deve incentivar respostas em inglês  
- **RF27** – A IA deve corrigir erros quando necessário  
- **RF28** – A IA deve manter postura didática e encorajadora  

---

### 1.6 Listening
- **RF29** – O sistema deve trabalhar compreensão auditiva  
- **RF30** – A IA deve adaptar vocabulário e velocidade  
- **RF31** – O sistema deve registrar desempenho em listening  

---

### 1.7 Speaking
- **RF32** – O sistema deve priorizar prática de fala  
- **RF33** – A IA deve estimular respostas faladas ou simuladas  
- **RF34** – O sistema deve registrar evolução em speaking  

---

### 1.8 Writing (Secundário)
- **RF35** – O sistema deve permitir exercícios de escrita  
- **RF36** – A IA deve corrigir textos simples  
- **RF37** – O sistema deve usar writing como reforço, não foco  

---

### 1.9 Progresso e Histórico
- **RF38** – O sistema deve salvar histórico de interações  
- **RF39** – O sistema deve salvar progresso do usuário  
- **RF40** – O sistema deve permitir visualização de progresso  
- **RF41** – O sistema deve usar histórico para personalização  
- **RF42** – O sistema deve manter histórico por usuário  

---

### 1.10 Adaptação Contínua
- **RF43** – A IA deve analisar evolução do usuário  
- **RF44** – A IA deve ajustar dificuldade automaticamente  
- **RF45** – O sistema deve identificar estagnação  
- **RF46** – O sistema deve alterar estratégias quando necessário  

---

### 1.11 Configurações do Usuário
- **RF47** – O usuário deve poder alterar objetivos  
- **RF48** – O usuário deve poder alterar tempo disponível  
- **RF49** – O sistema deve recalcular o plano após alterações  

---

## 2. Requisitos Não Funcionais

### 2.1 Usabilidade
- **RNF01** – Interface simples e intuitiva  
- **RNF02** – Linguagem clara e amigável  
- **RNF03** – Fluxo de uso sem fricção  

---

### 2.2 Performance
- **RNF04** – Respostas da IA devem ser rápidas  
- **RNF05** – O sistema deve suportar múltiplos usuários simultâneos  

---

### 2.3 Escalabilidade
- **RNF06** – O sistema deve permitir crescimento de usuários  
- **RNF07** – Arquitetura deve suportar novas funcionalidades  

---

### 2.4 Segurança
- **RNF08** – Dados dos usuários devem ser protegidos  
- **RNF09** – Histórico e progresso não devem ser acessíveis por terceiros  
- **RNF10** – Comunicação deve ser segura  

---

### 2.5 Confiabilidade
- **RNF11** – O sistema deve salvar progresso automaticamente  
- **RNF12** – Falhas não devem causar perda de dados  

---

### 2.6 Manutenibilidade
- **RNF13** – Código deve ser organizado e extensível  
- **RNF14** – Regras de negócio devem ser desacopladas da IA  

---

## 3. Requisitos de Inteligência Artificial

- **RIA01** – A IA deve assumir o papel de falante nativo  
- **RIA02** – A IA deve atuar como tutor didático  
- **RIA03** – A IA deve adaptar linguagem ao nível do usuário  
- **RIA04** – A IA deve usar contexto histórico do usuário  
- **RIA05** – A IA deve manter consistência de comportamento  
- **RIA06** – A IA deve agir apenas dentro do escopo educacional  
- **RIA07** – A IA deve evitar respostas genéricas  

---

## 4. Requisitos de Dados

- **RD01** – O sistema deve armazenar perfil do usuário  
- **RD02** – O sistema deve armazenar histórico de interações  
- **RD03** – O sistema deve armazenar métricas de evolução  
- **RD04** – Os dados devem ser usados para personalização  
- **RD05** – Os dados devem permitir análises futuras  

---

## 5. Requisitos de Evolução Futura

- **RFU01** – Suporte a voz (speech-to-text / text-to-speech)  
- **RFU02** – Métricas avançadas de fluência  
- **RFU03** – Aplicativo mobile  
- **RFU04** – Suporte a outros idiomas  
- **RFU05** – Modo corporativo (B2B)  
- **RFU06** – Relatórios avançados  
- **RFU07** – Gamificação  
- **RFU08** – Certificação de nível  

---

## 📌 Observação Final

Este documento representa um levantamento inicial e abrangente de requisitos.  
Os itens aqui descritos serão refinados, priorizados e negociados para definição do escopo final do MVP e das próximas fases do produto.
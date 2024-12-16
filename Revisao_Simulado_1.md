Revisão Simulado 1


# Pergunta 4
---
# SQS Extended Client Library

## **Descrição**
A **SQS Extended Client Library** é uma extensão da Amazon SQS que facilita o envio e recebimento de mensagens grandes (com mais de 256 KB). Ela integra o Amazon S3 para armazenar mensagens maiores, enquanto mantém referências dessas mensagens na fila SQS.

---

## **Funcionamento**
- **Mensagens pequenas (< 256 KB)**: Armazenadas diretamente na fila SQS.
- **Mensagens grandes (> 256 KB)**: Armazenadas no Amazon S3. Apenas um ponteiro para o objeto no S3 é armazenado na fila SQS.

---

## **Vantagens**
1. **Armazenamento econômico**: Reduz custos ao armazenar mensagens grandes no S3, que é mais barato do que o uso de filas SQS.
2. **Suporte a mensagens grandes**: Possibilita o uso de mensagens acima do limite padrão de 256 KB.
3. **Melhor escalabilidade**: Ideal para arquiteturas que precisam gerenciar dados volumosos com alta eficiência.


# Pergunta 5
---

## Requisitos
1. **Criptografia em trânsito** para proteger dados durante a transferência.
2. **Criptografia em repouso** com gerenciamento de chaves feito pela equipe de conformidade.
3. **Conformidade** com regulamentos como HIPAA para proteger PHI.

Por que esta solução atende aos requisitos?
1. Criptografia em trânsito (HTTPS):
    Para garantir que os dados estejam seguros durante a transferência para o Amazon S3, é necessário usar o protocolo HTTPS.
    HTTPS utiliza o TLS (Transport Layer Security) para criptografar os dados em trânsito, protegendo as informações contra interceptação durante a transmissão.

2. Criptografia em repouso (AWS KMS com CMK):
    O Amazon S3 suporta criptografia em repouso por meio de integração com o AWS KMS.
    Utilizando Customer Managed Keys (CMK) no KMS, o hospital pode criar e gerenciar suas próprias chaves de criptografia, o que cumpre o requisito de que a equipe de conformidade gerencie as chaves.
    Os dados no S3 são automaticamente criptografados com a chave especificada ao serem gravados e descriptografados ao serem acessados, sem necessidade de alterações no aplicativo.


# Pergunta 8
---

## Requisitos
1. Banco de dados na memória para **baixa latência** e **alta taxa de transferência**.
2. Suporte para processar mais de **100.000 transações por minuto**.
3. Minimizar custos de transferência de dados.
4. Design econômico com instâncias Amazon EC2.

### **1. Design de Rede**
- Coloque todas as instâncias EC2 do banco de dados e do aplicativo na **mesma VPC** e na **mesma zona de disponibilidade (AZ)** para evitar taxas de transferência de dados entre zonas.
- Use **grupos de segurança** para controlar o acesso de rede entre as instâncias de forma segura.


Lançar todas as instâncias EC2 na mesma Zona de Disponibilidade dentro da mesma Região AWS. Especificar um grupo de colocação com estratégia de cluster ao lançar instâncias EC2.

# Pergunta 24
---

## Solução Recomendada: 
**AWS Batch com Instâncias de EC2 Otimizadas para Computação**

### **Por que usar AWS Batch?**
- **Gerenciamento Automático**:
  - AWS Batch gerencia a alocação de recursos (instâncias EC2) e a execução das tarefas em lote.
- **Redução da Sobrecarga Operacional**:
  - A configuração é mínima, sem necessidade de gerenciar servidores ou escalabilidade manual.
- **Customização de Recursos**:
  - É possível escolher tipos de instâncias adequados, como instâncias otimizadas para computação.

# Pergunta 33
---

## Solução Recomendada: 
**Usar DynamoDB com Capacidade Provisionada e Auto Scaling**

### **Por que Capacidade Provisionada?**
- A capacidade provisionada permite prever os custos, pois você define antecipadamente as **unidades de leitura (RCU)** e **unidades de gravação (WCU)** que serão utilizadas.
- A carga de trabalho previsível elimina a necessidade de usar **On-Demand Capacity**, que pode ser mais cara para cargas consistentes.

# Pergunta 38
---

## Solução Recomendada: 
**AWS Inspector**

### **1. AWS Inspector**
- **Descrição**: Serviço que automatiza a avaliação de vulnerabilidades e exposição a riscos em instâncias EC2.
- **Funcionalidade**:
  - Escaneia vulnerabilidades no sistema operacional, pacotes instalados e configurações de rede.
  - Gera relatórios detalhados com as vulnerabilidades identificadas e recomendações de correção.
  - Integra-se ao **AWS Security Hub** para centralizar o gerenciamento de segurança.
- **Dica**: Ative o **AWS Inspector** em todas as regiões onde as instâncias EC2 estão sendo usadas.


# Pergunta 40
---

## Solução Recomendada: 
**Amazon Aurora Serverless**

### **Por que Amazon Aurora Serverless?**
1. **Escalabilidade Automática**:
   - Ajusta automaticamente a capacidade com base na demanda dos usuários.
   - Sem necessidade de selecionar um tipo de instância ou gerenciar o dimensionamento.

2. **Alta Disponibilidade**:
   - Projetado para disponibilidade contínua com réplicas distribuídas em várias zonas de disponibilidade (AZs).

3. **Econômico**:
   - Cobra apenas pela capacidade utilizada, ideal para cargas de trabalho com acesso infrequente.

4. **Compatibilidade com MySQL**:
   - Aurora Serverless é totalmente compatível com MySQL, facilitando a migração e operação.


# Pergunta 41
---

# Solução Recomendada: 
**AWS Storage Gateway (Volume Gateway - modo Cache)**

## Por que usar esta solução?

1. **Minimiza o armazenamento local necessário**:
   - O Volume Gateway no modo Cache armazena apenas os dados acessados recentemente localmente, enquanto o restante dos dados é armazenado no Amazon S3.

2. **Expande o armazenamento de iSCSI**:
   - Permite que os servidores de aplicativos continuem acessando volumes de armazenamento iSCSI, mantendo compatibilidade com o ambiente local.

3. **Escalabilidade Automática**:
   - O armazenamento no Amazon S3 cresce automaticamente conforme necessário, eliminando a necessidade de gerenciar o dimensionamento manual local.

4. **Custo-Eficiência**:
   - Reduz a necessidade de comprar hardware adicional para armazenamento local, aproveitando o modelo pay-as-you-go do S3.

5. **Alta Performance para Dados Recentes**:
   - Dados frequentemente acessados permanecem no cache local, proporcionando baixa latência para operações críticas.

# Pergunta 56
---

# Solução Recomendada: 
**Usar AWS Lake Formation com Amazon Athena e Amazon QuickSight**

## Por que esta solução atende aos requisitos?

1. **Integração com o AWS Lake Formation**:
   - O **AWS Lake Formation** gerencia a governança do data lake, incluindo permissões em nível de coluna. Isso permite controlar quais colunas do data lake a equipe de marketing pode acessar.

2. **Amazon Athena para Consultas Federadas**:
   - O **Amazon Athena** pode unir dados do Amazon S3 (data lake) com dados operacionais armazenados no Amazon Aurora MySQL usando **consultas SQL federadas**.
   - Permite consultar ambos os conjuntos de dados em tempo real, sem necessidade de ETL (Extração, Transformação e Carga).

3. **Autorização em Nível de Coluna**:
   - Lake Formation permite configurar políticas detalhadas que limitam o acesso a colunas específicas. A equipe de marketing só terá acesso ao subconjunto permitido.

4. **Visualizações no Amazon QuickSight**:
   - O **Amazon QuickSight** se conecta diretamente ao Athena para criar visualizações baseadas nas consultas federadas, sem necessidade de replicar dados.
   - QuickSight herda as permissões definidas no Lake Formation, garantindo segurança em nível de coluna.

5. **Menor Sobrecarga Operacional**:
   - Não há necessidade de mover ou replicar dados entre o data lake e o banco de dados Aurora.
   - Governança e políticas são centralizadas no AWS Lake Formation, reduzindo complexidade de gerenciamento.

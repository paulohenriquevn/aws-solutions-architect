# Guia de Estudo: AWS Certified Solutions Architect - Associate (SAA-C03)

---

## **1. Introdução**
### O que é a Certificação AWS Certified Solutions Architect - Associate?
A certificação valida habilidades para projetar soluções escaláveis, seguras e econômicas na AWS. É ideal para profissionais que trabalham como arquitetos de soluções, desenvolvedores ou administradores de sistemas.

### Estrutura do Exame
- **Formato:** Questões de múltipla escolha e múltiplas respostas.
- **Duração:** 130 minutos.
- **Domínios do Exame:**
  - **Design de Arquiteturas Seguras (30%)**
  - **Design de Arquiteturas Resilientes (26%)**
  - **Design de Arquiteturas de Alto Desempenho (24%)**
  - **Design de Arquiteturas de Custo-Eficiente (20%)**

---

## **2. Domínios do Exame**

### **2.1. Design de Arquiteturas Seguras (30%)**
#### Principais Tópicos:
1. **Controle de Acesso:**
   - **IAM:** Políticas, usuários, grupos e roles.
   - **S3 Bucket Policies:** Controle granular de acesso a buckets.
   - **AWS KMS:** Criação e gerenciamento de chaves criptográficas.

2. **Segurança de Dados em Trânsito e em Repouso:**
   - **S3 Encryption:** Criptografia lado cliente (CSE) e servidor (SSE-KMS, SSE-S3).
   - **TLS/SSL:** Configuração em serviços como CloudFront e ALB.
   - **EBS Encryption:** Habilitação para volumes e snapshots.

3. **Proteção Contra Ameaças:**
   - **AWS WAF:** Criação de regras baseadas em IP e taxa.
   - **AWS Shield:** Proteção contra ataques DDoS.
   - **CloudTrail e Config:** Rastreamento de mudanças e auditoria.

#### Exemplo Prático:
- Cenário: Proteger objetos S3 contra exclusão acidental.
  - Solução: Habilitar versionamento e MFA Delete.

---

### **2.2. Design de Arquiteturas Resilientes (26%)**
#### Principais Tópicos:
1. **Alta Disponibilidade e Failover:**
   - **RDS Multi-AZ:** Failover automático entre zonas de disponibilidade.
   - **S3 CRR:** Replicação de dados entre regiões.

2. **Arquiteturas Desacopladas:**
   - **SNS e SQS:** Comunicação assíncrona para escalabilidade.
   - **Elastic Load Balancer (ALB, NLB):** Distribuição de tráfego.

3. **Estratégias de Backup e Recuperação:**
   - **EBS Snapshots:** Automação com AWS Data Lifecycle Manager.
   - **S3 Glacier:** Armazenamento de longo prazo.

#### Exemplo Prático:
- Cenário: Implementar failover para um site.
  - Solução: Route 53 com opção de failover para um bucket S3.

---

### **2.3. Design de Arquiteturas de Alto Desempenho (24%)**
#### Principais Tópicos:
1. **Armazenamento Escalável:**
   - **DynamoDB:** Performance consistente com latência baixa.
   - **Amazon FSx for Lustre:** Processamento de alto desempenho.

2. **Computação Escalável:**
   - **EC2 Auto Scaling:** Ajuste dinâmico baseado em métricas.
   - **Lambda:** Computação serverless para cargas de trabalho baseadas em eventos.

3. **Rede e Transferência de Dados:**
   - **CloudFront:** Redução de latência com cache global.
   - **Direct Connect:** Conexão dedicada e de baixa latência.

#### Exemplo Prático:
- Cenário: Reduzir latência em uma aplicação global.
  - Solução: Usar CloudFront com origem no S3.

---

### **2.4. Design de Arquiteturas de Custo-Eficiente (20%)**
#### Principais Tópicos:
1. **Otimização de Custos em Computação:**
   - **Savings Plans e Reserved Instances:** Redução de custos previsíveis em EC2.
   - **Lambda:** Pagamento por execução.

2. **Otimização de Custos em Armazenamento:**
   - **S3 Lifecycle Policies:** Movimentação automática de objetos para Glacier.
   - **EBS Cold HDD:** Para dados de acesso infrequente.

3. **Gerenciamento de Custos:**
   - **Cost Explorer:** Monitoramento e análise de gastos.
   - **AWS Budgets:** Alertas baseados em limites.

#### Exemplo Prático:
- Cenário: Reduzir custos de armazenamento.
  - Solução: Configurar regras de ciclo de vida no S3 para mover objetos para Glacier Deep Archive.

---

## **3. Serviços Principais no Exame**
### Compute:
- **EC2:** Tipos de instância, Auto Scaling, ELB.
- **Lambda:** Integração com S3, DynamoDB e API Gateway.
- **ECS e EKS:** Gerenciamento de contêineres.

### Armazenamento:
- **S3:** Classes de armazenamento, replicação e políticas.
- **EBS e EFS:** Diferenças e casos de uso.
- **FSx:** Sistemas otimizados para Lustre e Windows.

### Banco de Dados:
- **RDS:** Multi-AZ, read replicas.
- **DynamoDB:** Streams e DAX.
- **Aurora:** Global Database, Serverless.

### Rede:
- **VPC:** Subnets, NAT Gateways, VPN.
- **Route 53:** Políticas de roteamento.
- **Direct Connect e Transit Gateway:** Conectividade híbrida.

### Monitoramento:
- **CloudWatch:** Métricas, logs e alarmes.
- **CloudTrail:** Auditoria de atividades.
- **AWS Config:** Monitoramento de conformidade.

---

## **4. Dicas para o Exame**
1. **Pratique com Cenários:** Use questões baseadas em casos reais.
2. **Estude Comparações:** Exemplo: S3 vs EFS vs EBS.
3. **Foque em Boas Práticas:** Segurança, custos e escalabilidade.

---

**Conclusão:** Este guia abrange os domínios e serviços fundamentais para a certificação AWS Solutions Architect - Associate. Foque no aprendizado prático e nas melhores práticas para garantir o sucesso no exame.

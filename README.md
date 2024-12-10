### Questão 1
Uma empresa coleta dados de temperatura, umidade e pressão atmosférica em cidades de vários continentes. O volume médio de dados coletados diariamente de cada local é de 500 GB. Cada local possui uma conexão de Internet de alta velocidade.  
A empresa deseja agregar os dados de todos esses locais globais o mais rápido possível em um único bucket do Amazon S3. A solução deve minimizar a complexidade operacional.  

**Resposta correta:**  
**A.** Ative o S3 Transfer Acceleration no bucket de destino do S3. Use uploads em várias partes para carregar diretamente os dados do local no bucket de destino do S3.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Transfer Acceleration permite transferências globais mais rápidas para buckets do Amazon S3 ao alavancar a rede de borda da AWS. Ele reduz a latência e acelera o envio de dados, especialmente útil para o volume diário alto (500 GB). O upload em várias partes melhora a eficiência da transferência de arquivos grandes.

- **Por que as outras opções não são adequadas?**  
  - **B:** Embora Cross-Region Replication agregue os dados, ele adiciona complexidade operacional ao exigir buckets regionais intermediários e não é a solução mais rápida para transferência direta.  
  - **C:** O AWS Snowball é eficiente para grandes volumes offline, mas aqui o requisito é rapidez com conectividade de alta velocidade.  
  - **D:** Usar instâncias EC2 e snapshots de EBS é desnecessariamente complexo para um problema resolvível com recursos do S3.

---
### Questão 2
Uma empresa precisa analisar os arquivos de log de sua aplicação proprietária. Os logs estão armazenados no formato JSON em um bucket do Amazon S3. As consultas serão simples e executadas sob demanda.  

**Resposta correta:**  
**C.** Use Amazon Athena diretamente com o Amazon S3 para executar as consultas conforme necessário.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon Athena permite consultas SQL sob demanda diretamente nos dados armazenados no S3, sem necessidade de infraestrutura adicional, minimizando a sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Redshift é excessivo para consultas simples e adiciona complexidade desnecessária.  
  - **B:** O Amazon CloudWatch Logs não suporta diretamente consultas SQL nos dados do S3.  
  - **D:** O AWS Glue com EMR é uma solução mais complexa e cara para o caso apresentado.  

---

### Questão 3
Uma empresa usa AWS Organizations para gerenciar várias contas AWS de diferentes departamentos. A conta de gerenciamento possui um bucket do Amazon S3 contendo relatórios de projetos.  

**Resposta correta:**  
**A.** Adicione a chave global `aws:PrincipalOrgID` com referência ao ID da organização na política do bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  A chave `aws:PrincipalOrgID` limita o acesso ao bucket apenas para usuários dentro da organização no AWS Organizations, com baixa sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** `aws:PrincipalOrgPaths` exige uma estrutura complexa de OUs desnecessária.  
  - **C:** Monitorar eventos com CloudTrail é uma abordagem reativa, não preventiva.  
  - **D:** Usar tags de usuários adiciona mais complexidade para gerenciar acessos.  

---

### Questão 4
Uma aplicação roda em uma instância Amazon EC2 em uma VPC. A aplicação processa logs armazenados em um bucket do Amazon S3.  

**Resposta correta:**  
**A.** Crie um endpoint VPC Gateway para o bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway permite conectividade privada com o S3 sem a necessidade de acesso à Internet, reduzindo custos e melhorando a segurança.  

- **Por que as outras opções não são adequadas?**  
  - **B:** CloudWatch Logs não substitui o acesso privado ao S3.  
  - **C:** Um perfil de instância fornece permissões, mas não conectividade privada.  
  - **D:** API Gateway com PrivateLink é excessivo e mais caro.  

---

### Questão 5
Uma empresa hospeda uma aplicação web no AWS usando uma instância Amazon EC2 que armazena documentos enviados por usuários.  

**Resposta correta:**  
**C.** Copie os dados de ambos os volumes EBS para o Amazon EFS. Modifique a aplicação para salvar novos documentos no Amazon EFS.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon EFS oferece armazenamento compartilhado, consistente e acessível por múltiplas instâncias, garantindo que todos os documentos fiquem disponíveis.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Copiar manualmente os dados não resolve o problema de consistência em tempo real.  
  - **B:** Configurar o ALB para direcionar solicitações não resolve a inconsistência de dados.  
  - **D:** Direcionar solicitações para servidores específicos aumenta a complexidade e não consolida os documentos.  

---

### Questão 6
Uma empresa usa NFS para armazenar vídeos grandes em um NAS local. Cada vídeo varia de 1 MB a 500 GB.  

**Resposta correta:**  
**B.** Crie um trabalho AWS Snowball Edge. Receba um dispositivo Snowball Edge no local e use o cliente para transferir os dados para o dispositivo.

**Justificativa:**  
- **Por que essa opção?**  
  O Snowball Edge é ideal para transferências rápidas de grandes volumes de dados com largura de banda limitada, minimizando o uso de rede.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Copiar dados via CLI consome muita largura de banda.  
  - **C:** S3 File Gateway não é ideal para transferências massivas.  
  - **D:** Direct Connect exige mais tempo para configuração e custos contínuos.  

---
### Questão 7
Uma empresa possui uma aplicação que consome mensagens recebidas. Dezenas de outras aplicações e microsserviços consomem essas mensagens rapidamente.

**Resposta correta:**  
**D.** Publique as mensagens em um tópico do Amazon SNS com várias assinaturas do Amazon SQS. Configure os consumidores para processar as mensagens das filas.

**Justificativa:**  
- **Por que essa opção?**  
  Essa solução desacopla o processamento, aumenta a escalabilidade e permite o consumo de mensagens por múltiplos consumidores sem dependência direta.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Kinesis Data Analytics não é projetado para gerenciar picos de ingestão massiva.  
  - **B:** Escalar instâncias EC2 manualmente é menos eficiente e mais custoso.  
  - **C:** Um único shard no Kinesis limita o throughput.  

---

### Questão 8
Uma empresa está migrando uma aplicação distribuída para a AWS. A aplicação possui cargas de trabalho variáveis.

**Resposta correta:**  
**B.** Configure uma fila Amazon SQS como destino para os jobs. Implemente os nós de computação em uma Auto Scaling group de EC2.

**Justificativa:**  
- **Por que essa opção?**  
  O uso de filas SQS desacopla o processamento dos jobs e permite que a escala dos nós EC2 seja baseada no tamanho da fila, maximizando a resiliência e escalabilidade.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O agendamento fixo de escala não responde a mudanças de carga.  
  - **C:** CloudTrail não é adequado como destino de jobs.  
  - **D:** EventBridge é mais indicado para eventos, não para filas de processamento massivo.  

---

### Questão 9
Uma empresa opera um servidor de arquivos SMB em seu data center. Os arquivos são acessados frequentemente nos primeiros 7 dias após a criação.  

**Resposta correta:**  
**B.** Crie um Amazon S3 File Gateway para expandir o espaço de armazenamento. Configure uma política de ciclo de vida no S3 para mover os dados para o S3 Glacier Deep Archive após 7 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 File Gateway permite acesso de baixa latência para arquivos recentes e armazenamento econômico para arquivos antigos no S3 Glacier Deep Archive.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O DataSync é útil para migração de dados, mas não suporta acesso contínuo e eficiente.  
  - **C:** FSx oferece alta disponibilidade, mas com maior custo em comparação ao S3.  
  - **D:** Um utilitário direto não é suficiente para gerenciar o ciclo de vida dos arquivos.  

---

### Questão 10
Uma empresa está construindo uma aplicação de ecommerce que envia informações de pedidos para uma API REST do Amazon API Gateway.

**Resposta correta:**  
**B.** Use uma integração com o API Gateway para enviar mensagens para uma fila FIFO do Amazon SQS ao receber pedidos.

**Justificativa:**  
- **Por que essa opção?**  
  Uma fila FIFO do SQS garante a ordenação das mensagens, o que é essencial para processar os pedidos na sequência em que foram recebidos.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O SNS não garante a ordenação das mensagens.  
  - **C:** Bloquear requisições durante o processamento adiciona latência desnecessária.  
  - **D:** Uma fila SQS padrão não oferece garantia de ordenação.  

---

### Questão 11
Uma empresa possui uma aplicação que roda em instâncias Amazon EC2 e usa um banco de dados Amazon Aurora.

**Resposta correta:**  
**A.** Use o AWS Secrets Manager. Ative a rotação automática.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager simplifica o gerenciamento de credenciais, incluindo a rotação automática, reduzindo a sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Parameter Store não inclui rotação automática de credenciais.  
  - **C:** Usar o S3 para armazenamento é menos seguro e complexo para integração.  
  - **D:** Volumes EBS não gerenciam credenciais automaticamente.  

---

### Questão 12
Uma empresa global hospeda sua aplicação web em instâncias Amazon EC2 atrás de um Application Load Balancer (ALB).

**Resposta correta:**  
**A.** Crie uma distribuição Amazon CloudFront com o bucket S3 e o ALB como origens. Configure o Route 53 para rotear o tráfego para a distribuição CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront melhora o desempenho global e reduz a latência para conteúdo estático e dinâmico ao usar pontos de presença distribuídos.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Global Accelerator não é necessário quando o CloudFront já gerencia desempenho.  
  - **C:** Configurar múltiplos endpoints adiciona complexidade desnecessária.  
  - **D:** Dividir origens dinâmicas e estáticas não garante latência otimizada.  

---

### Questão 13
Uma empresa realiza manutenção mensal em sua infraestrutura AWS. Durante essas atividades, as credenciais RDS devem ser rotacionadas.

**Resposta correta:**  
**A.** Armazene as credenciais como segredos no AWS Secrets Manager. Use replicação multi-região e configure a rotação automática.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager simplifica a rotação e replicação de segredos em múltiplas regiões com mínima sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Parameter Store não possui suporte direto para rotação automática de segredos em várias regiões.  
  - **C:** Usar S3 com eventos EventBridge adiciona complexidade desnecessária.  
  - **D:** DynamoDB e Lambda introduzem mais componentes sem vantagens significativas.  

---

### Questão 14
Uma empresa opera uma aplicação de ecommerce em instâncias Amazon EC2 atrás de um ALB. O banco de dados é MySQL.

**Resposta correta:**  
**C.** Use Amazon Aurora com uma implantação Multi-AZ. Configure Auto Scaling com réplicas Aurora.

**Justificativa:**  
- **Por que essa opção?**  
  Aurora Multi-AZ oferece alta disponibilidade e escalabilidade automática, ideal para cargas de leitura imprevisíveis.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Redshift não é projetado para cargas OLTP.  
  - **B:** Uma implantação Single-AZ não garante alta disponibilidade.  
  - **D:** ElastiCache não substitui o banco de dados relacional.  

---

### Questão 15
Uma empresa recentemente migrou para a AWS e deseja inspecionar e filtrar o tráfego na VPC de produção.

**Resposta correta:**  
**C.** Use o AWS Network Firewall para criar as regras necessárias para inspeção e filtragem de tráfego.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Network Firewall é um serviço gerenciado que oferece inspeção e filtragem centralizada de tráfego.  

- **Por que as outras opções não são adequadas?**  
  - **A:** GuardDuty apenas detecta ameaças, mas não filtra tráfego.  
  - **B:** Traffic Mirroring não implementa inspeção ativa.  
  - **D:** Firewall Manager gerencia políticas, mas depende de outros serviços para inspeção.  

---

### Questão 16
Uma empresa hospeda um data lake no AWS com dados no Amazon S3 e no RDS PostgreSQL.

**Resposta correta:**  
**A.** Crie uma análise no Amazon QuickSight. Conecte todas as fontes de dados e compartilhe os dashboards com os papéis apropriados do IAM.

**Justificativa:**  
- **Por que essa opção?**  
  O QuickSight permite conectar várias fontes, criar visualizações e compartilhar acessos com controle granular.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A opção é redundante, pois sugere usuários e grupos ao invés de papéis IAM.  
  - **C:** Relatórios ETL no S3 não atendem ao requisito de visualização.  
  - **D:** Athena sozinho não gerencia visualizações e acesso restrito.  

---

### Questão 17
Uma empresa implementa uma nova aplicação que roda em duas instâncias Amazon EC2 e usa um bucket do Amazon S3.

**Resposta correta:**  
**A.** Crie uma role IAM que conceda acesso ao bucket S3 e anexe às instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  Roles IAM são a maneira mais segura e eficiente de conceder permissões temporárias para instâncias EC2.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Políticas IAM não podem ser diretamente anexadas a instâncias.  
  - **C:** Grupos IAM não são aplicáveis a instâncias EC2.  
  - **D:** Usuários IAM são menos seguros e não recomendados para esse caso.  

---

### Questão 18
Uma equipe de desenvolvimento está projetando um microsserviço para converter imagens grandes em versões compactadas.

**Resposta correta:**  
**A e B.** Crie uma fila Amazon SQS. Configure a função Lambda para usar a fila como fonte de invocação.

**Justificativa:**  
- **Por que essa opção?**  
  A fila SQS desacopla o processamento e a Lambda garante a execução automática com monitoramento integrado.  

- **Por que as outras opções não são adequadas?**  
  - **C:** Monitorar uploads diretamente é menos eficiente do que usar filas.  
  - **D:** Usar EC2 para monitorar filas é desnecessário com Lambda.  
  - **E:** Notificações do SNS não automatizam o processamento.  

---

### Questão 19
Uma empresa possui uma aplicação web de três camadas implantada no AWS com um appliance de firewall virtual.

**Resposta correta:**  
**D.** Implemente um Gateway Load Balancer na VPC de inspeção para rotear os pacotes ao appliance.

**Justificativa:**  
- **Por que essa opção?**  
  O Gateway Load Balancer simplifica o roteamento e inspeção de tráfego com alta disponibilidade.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** NLB e ALB não oferecem integração direta para inspeção.  
  - **C:** Transit Gateway é desnecessário para este fluxo específico.  

---

### Questão 20
Uma empresa deseja clonar grandes volumes de dados de produção para um ambiente de teste na mesma região AWS.

**Resposta correta:**  
**D.** Ative o recurso de restauração rápida de snapshots no EBS e restaure os snapshots em novos volumes.

**Justificativa:**  
- **Por que essa opção?**  
  A restauração rápida reduz significativamente o tempo necessário para disponibilizar os volumes clonados.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Restaurar sem o recurso de rápida restauração aumenta o tempo de indisponibilidade.  
  - **B:** Multi-Attach é inadequado para separar ambientes de teste e produção.  

---

### Questão 21
Uma empresa quer lançar um site com uma promoção por dia na AWS, lidando com milhões de requisições por hora.

**Resposta correta:**  
**D.** Use um bucket Amazon S3 para hospedar o conteúdo estático, Amazon CloudFront para distribuição e API Gateway com AWS Lambda para backend.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 e o CloudFront são altamente escaláveis e de baixa latência para conteúdo estático, enquanto API Gateway e Lambda gerenciam APIs de backend sem a necessidade de infraestrutura.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar apenas S3 não gerencia a lógica de backend.  
  - **B:** Instâncias EC2 e ALB têm maior complexidade e custos.  
  - **C:** Containers em EKS introduzem mais sobrecarga operacional.  

---

### Questão 22
Um arquiteto de soluções está projetando a arquitetura de armazenamento para uma aplicação de mídia digital no Amazon S3.

**Resposta correta:**  
**B.** S3 Intelligent-Tiering.

**Justificativa:**  
- **Por que essa opção?**  
  O Intelligent-Tiering ajusta automaticamente os níveis de armazenamento com base nos padrões de acesso, reduzindo custos para dados raramente acessados sem comprometer a resiliência.  

- **Por que as outras opções não são adequadas?**  
  - **A:** S3 Standard é mais caro para dados raramente acessados.  
  - **C:** S3 Standard-IA não ajusta dinamicamente os níveis de armazenamento.  
  - **D:** S3 One Zone-IA não oferece resiliência para múltiplas zonas.  

---

### Questão 23
Uma empresa armazena backups no S3 Standard e precisa de uma solução econômica para dados raramente acessados.

**Resposta correta:**  
**B.** Configure uma política de ciclo de vida no S3 para mover objetos para o S3 Glacier Deep Archive após 1 mês.

**Justificativa:**  
- **Por que essa opção?**  
  S3 Glacier Deep Archive é a opção mais econômica para armazenamento de longo prazo, ideal para dados raramente acessados após 1 mês.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Intelligent-Tiering não é tão econômico quanto Glacier para dados arquivados.  
  - **C e D:** Standard-IA e One Zone-IA têm custos mais altos para armazenamento de longo prazo.  

---

### Questão 24
Uma empresa observa um aumento nos custos do Amazon EC2 devido a escalonamento vertical indesejado.

**Resposta correta:**  
**B.** Use o recurso de filtragem granular do Cost Explorer para analisar os custos do EC2 com base nos tipos de instância.

**Justificativa:**  
- **Por que essa opção?**  
  O Cost Explorer fornece análises detalhadas e insights sobre custos com filtros baseados em instâncias.  

- **Por que as outras opções não são adequadas?**  
  - **A:** AWS Budgets não fornece visualizações detalhadas de custos.  
  - **C:** O dashboard de Billing é limitado para análises detalhadas.  
  - **D:** Usar QuickSight adiciona complexidade desnecessária.  

---

### Questão 25
Uma empresa está projetando uma aplicação que usa AWS Lambda para processar dados em alta escala e armazená-los no Amazon Aurora.

**Resposta correta:**  
**D.** Configure duas funções Lambda: uma para receber dados e outra para carregá-los no banco de dados. Integre-as com uma fila Amazon SQS.

**Justificativa:**  
- **Por que essa opção?**  
  Separar as funções Lambda reduz gargalos e integrações com SQS garantem processamento escalável e confiável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** EC2 introduz complexidade e custos elevados.  
  - **B:** DynamoDB não é mencionado como requisito no caso.  
  - **C:** SNS não gerencia filas para processamento ordenado.  

---

### Questão 26
Uma empresa precisa revisar sua implantação na AWS para evitar alterações não autorizadas em seus buckets do S3.

**Resposta correta:**  
**A.** Ative o AWS Config com as regras apropriadas.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config rastreia alterações em configurações de recursos e oferece alertas de conformidade.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Trusted Advisor não monitora configurações de buckets.  
  - **C:** Amazon Inspector é usado para vulnerabilidades, não configuração de buckets.  
  - **D:** Logs de acesso não previnem mudanças, apenas registram eventos.  

---

### Questão 27
Uma empresa quer disponibilizar um dashboard do CloudWatch para um gerente de produto sem conta AWS.

**Resposta correta:**  
**A.** Compartilhe o dashboard a partir do console do CloudWatch e forneça um link compartilhável.

**Justificativa:**  
- **Por que essa opção?**  
  O compartilhamento direto do dashboard é a abordagem mais simples e segura, seguindo o princípio do menor privilégio.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar usuários IAM adiciona complexidade e supera o escopo necessário.  
  - **C:** O acesso ViewOnlyAccess permite mais permissões do que o necessário.  
  - **D:** Usar um bastion server é excessivamente complexo.  

---

### Questão 28
Uma empresa está migrando aplicativos para AWS e precisa de SSO entre contas usando Active Directory local.

**Resposta correta:**  
**A.** Ative o AWS SSO e conecte-se ao Active Directory local usando AWS Directory Service.

**Justificativa:**  
- **Por que essa opção?**  
  Essa solução integra o SSO ao Active Directory local sem necessidade de gerenciar infraestrutura adicional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Two-way trust adiciona complexidade desnecessária.  
  - **C:** AWS Directory Service sozinho não oferece SSO para múltiplas contas.  
  - **D:** Usar um IdP local é menos eficiente e requer mais configuração.  

---

### Questão 29
Uma empresa oferece serviços VoIP usando UDP e precisa de roteamento baseado em menor latência.

**Resposta correta:**  
**A.** Use um Network Load Balancer (NLB) associado ao AWS Global Accelerator em cada região.

**Justificativa:**  
- **Por que essa opção?**  
  O NLB fornece suporte para UDP, enquanto o Global Accelerator roteia tráfego com baixa latência e failover automático.  

- **Por que as outras opções não são adequadas?**  
  - **B:** ALB não suporta tráfego UDP.  
  - **C:** Route 53 sozinho não fornece failover automático eficiente.  
  - **D:** ALB com Route 53 não é otimizado para UDP.  

---

### Questão 30
Uma equipe executa testes intensivos mensais em um banco RDS MySQL e deseja reduzir custos.

**Resposta correta:**  
**C.** Crie um snapshot após os testes e restaure o banco de dados somente quando necessário.

**Justificativa:**  
- **Por que essa opção?**  
  Restaurar snapshots economiza custos ao evitar execução contínua do banco de dados quando não está em uso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Parar o banco é menos eficiente do que restaurar snapshots.  
  - **B:** Auto Scaling não aplica-se diretamente ao RDS.  
  - **D:** Alterar a capacidade manualmente adiciona complexidade.  

---

### Questão 31
Uma empresa deseja garantir que todas as instâncias Amazon EC2, Amazon RDS e clusters Amazon Redshift sejam configurados com tags.

**Resposta correta:**  
**A.** Use regras do AWS Config para definir e detectar recursos que não estão devidamente etiquetados.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config oferece monitoramento contínuo e conformidade automatizada, facilitando a identificação de recursos sem tags.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Cost Explorer apenas exibe os recursos, sem capacidade de correção.  
  - **C e D:** Criar APIs personalizadas adiciona complexidade operacional desnecessária.  

---

### Questão 32
Uma equipe de desenvolvimento precisa hospedar um site acessado por outras equipes, com HTML, CSS, JavaScript e imagens.

**Resposta correta:**  
**B.** Crie um bucket Amazon S3 e hospede o site nele.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 é a opção mais econômica para hospedar conteúdo estático com baixa sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Fargate é projetado para microsserviços, não para sites estáticos.  
  - **C:** Usar EC2 é mais caro e desnecessário para este caso.  
  - **D:** ALB e Lambda introduzem complexidade sem benefícios adicionais.  

---

### Questão 33
Uma empresa opera um marketplace online e precisa processar milhões de transações financeiras quase em tempo real.

**Resposta correta:**  
**C.** Transmita os dados das transações para o Amazon Kinesis Data Streams e use AWS Lambda para remover dados sensíveis.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis gerencia grandes volumes de dados em tempo real, enquanto o Lambda processa e armazena os dados no DynamoDB.  

- **Por que as outras opções não são adequadas?**  
  - **A e D:** Processar em DynamoDB ou S3 diretamente não é ideal para grandes volumes em tempo real.  
  - **B:** Kinesis Firehose não oferece processamento detalhado como o Lambda.  

---

### Questão 34
Uma empresa hospeda aplicações em várias camadas na AWS e precisa rastrear mudanças de configuração e histórico de chamadas de API.

**Resposta correta:**  
**B.** Use AWS Config para rastrear mudanças de configuração e AWS CloudTrail para registrar chamadas de API.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config e CloudTrail são projetados para fornecer histórico detalhado de mudanças e chamadas de API, atendendo requisitos de conformidade.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Misturam serviços que não são adequados para todas as necessidades.  
  - **D:** CloudWatch não é usado para rastrear mudanças de configuração.  

---

### Questão 35
Uma empresa está lançando uma aplicação pública na AWS e precisa se proteger contra ataques DDoS em grande escala.

**Resposta correta:**  
**D.** Ative o AWS Shield Advanced e associe-o ao ELB.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Shield Advanced oferece proteção DDoS avançada e relatórios detalhados para recursos como ELB.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** GuardDuty e Inspector detectam, mas não mitigam ataques DDoS.  
  - **C:** Shield padrão não inclui suporte avançado ou resposta a incidentes.  

---

### Questão 36
Uma empresa precisa armazenar dados criptografados em buckets S3 em duas regiões, usando a mesma chave KMS.

**Resposta correta:**  
**B.** Crie uma chave KMS multi-região gerenciada. Configure replicação entre os buckets S3.

**Justificativa:**  
- **Por que essa opção?**  
  Chaves KMS multi-região permitem criptografia e descriptografia consistentes em várias regiões com mínima sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Usar SSE-S3 não atende ao requisito de chaves KMS consistentes.  
  - **D:** Chaves gerenciadas por região não oferecem interoperabilidade.  

---

### Questão 37
Uma empresa precisa acessar e administrar instâncias EC2 de forma remota e segura, seguindo o AWS Well-Architected Framework.

**Resposta correta:**  
**B.** Anexe a role IAM apropriada às instâncias e use o AWS Systems Manager Session Manager.

**Justificativa:**  
- **Por que essa opção?**  
  O Session Manager elimina a necessidade de chaves SSH e simplifica o acesso remoto com segurança integrada.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O console serial não suporta conectividade remota comum.  
  - **C:** Bastion hosts introduzem complexidade e riscos adicionais.  
  - **D:** VPNs não são necessárias com o Session Manager.  

---

### Questão 38
Uma empresa hospeda um site estático no S3 e deseja reduzir a latência global para os usuários.

**Resposta correta:**  
**C.** Adicione uma distribuição do Amazon CloudFront em frente ao bucket S3. Edite as entradas do Route 53 para apontar para o CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront reduz a latência distribuindo o conteúdo estático em seus pontos de presença global.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Replicação S3 não reduz latência diretamente para acesso global.  
  - **B:** Global Accelerator não é necessário para sites estáticos no S3.  
  - **D:** Transfer Acceleration melhora uploads, não acessos globais.  

---

### Questão 39
Uma empresa armazena dados em um banco RDS MySQL, enfrentando problemas de performance para inserções.

**Resposta correta:**  
**A.** Altere o tipo de armazenamento para Provisioned IOPS SSD.

**Justificativa:**  
- **Por que essa opção?**  
  O Provisioned IOPS SSD oferece maior desempenho de leitura/escrita, resolvendo gargalos de I/O em cenários com alta carga.  

- **Por que as outras opções não são adequadas?**  
  - **B e C:** Alterar a classe da instância não resolve problemas de armazenamento.  
  - **D:** Réplicas de leitura não impactam a performance de gravações.  

---

### Questão 40
Uma empresa precisa ingerir e armazenar 1 TB diário de alertas de status, mantendo 14 dias disponíveis para análise.

**Resposta correta:**  
**A.** Crie um Kinesis Data Firehose para ingerir os alertas. Configure o Firehose para entregá-los a um bucket S3 e aplique políticas de ciclo de vida para arquivar os dados no Glacier após 14 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis Firehose oferece ingestão contínua e entrega direta ao S3, enquanto as políticas de ciclo de vida automatizam a retenção e arquivamento.  

- **Por que as outras opções não são adequadas?**  
  - **B:** EC2 com script adiciona mais complexidade e custos.  
  - **C:** OpenSearch Service tem custos maiores para dados de longo prazo.  
  - **D:** O SQS não é ideal para ingestão massiva e arquivamento.  

---

### Questão 41
Uma aplicação da empresa integra-se a várias fontes SaaS para coleta de dados e enfrenta lentidão de desempenho.

**Resposta correta:**  
**B.** Use Amazon AppFlow para transferir dados entre fontes SaaS e o bucket S3. Configure notificações S3 para enviar eventos ao SNS após o upload.

**Justificativa:**  
- **Por que essa opção?**  
  O AppFlow reduz a sobrecarga operacional ao automatizar transferências de dados entre SaaS e S3, enquanto o SNS simplifica notificações.  

- **Por que as outras opções não são adequadas?**  
  - **A:** EC2 com Auto Scaling adiciona complexidade sem melhorar significativamente o desempenho.  
  - **C e D:** EventBridge e ECS não são tão eficientes para este caso.  

---

### Questão 42
Uma empresa opera uma aplicação de processamento de imagens em EC2, enfrentando custos elevados de transferência de dados.

**Resposta correta:**  
**C.** Implemente um endpoint VPC Gateway para o S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway permite acesso ao S3 sem taxas de transferência regionais e com maior segurança.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Lançar múltiplos NAT Gateways aumenta os custos.  
  - **B:** NAT Instance não oferece a mesma escalabilidade de um endpoint.  
  - **D:** EC2 Dedicated Host não resolve problemas de transferência de dados.  

---

### Questão 43
Uma empresa precisa fazer backup de grandes volumes de dados no S3 sem impactar a conectividade local.

**Resposta correta:**  
**B.** Estabeleça uma conexão AWS Direct Connect e direcione o tráfego de backup por esta conexão.

**Justificativa:**  
- **Por que essa opção?**  
  O Direct Connect oferece conectividade dedicada e de baixa latência, minimizando impacto na rede local.  

- **Por que as outras opções não são adequadas?**  
  - **A:** AWS VPN não oferece o mesmo desempenho de largura de banda que o Direct Connect.  
  - **C:** Snowball não é adequado para backups contínuos.  
  - **D:** Pedir remoção de limites de serviço não resolve problemas de conectividade.  

---

### Questão 44
Uma empresa deve proteger dados críticos em um bucket S3 contra exclusão acidental.

**Resposta correta:**  
**A e B.** Ative o versionamento no bucket S3 e habilite a exclusão MFA.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento mantém versões antigas dos objetos e o MFA Delete adiciona uma camada de proteção contra exclusões não autorizadas.  

- **Por que as outras opções não são adequadas?**  
  - **C:** Políticas de bucket não impedem completamente exclusões acidentais.  
  - **D e E:** Criptografia e políticas de ciclo de vida não evitam exclusões.  

---

### Questão 45
Uma empresa possui um fluxo de ingestão de dados com SNS e Lambda que falha devido a problemas de conectividade.

**Resposta correta:**  
**B e E.** Subcreva um SQS à SNS e modifique a função Lambda para ler da fila SQS.

**Justificativa:**  
- **Por que essa opção?**  
  O SQS desacopla o fluxo e garante que dados sejam armazenados até serem processados com sucesso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Múltiplas zonas de disponibilidade não resolvem problemas de conectividade.  
  - **C e D:** Ajustar CPU/memória ou throughput não resolve falhas transitórias de rede.  

---

### Questão 46
Uma empresa processa dados de transações e precisa detectar automaticamente informações sensíveis (PII).

**Resposta correta:**  
**B.** Use um bucket S3 como ponto de transferência e Amazon Macie para identificar PII.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon Macie é projetado para detectar PII automaticamente com baixa necessidade de desenvolvimento adicional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Inspector não suporta diretamente detecção de PII em dados S3.  
  - **C e D:** Algoritmos personalizados adicionam desenvolvimento desnecessário.  

---

### Questão 47
Uma empresa precisa garantir capacidade EC2 em três zonas de disponibilidade específicas.

**Resposta correta:**  
**D.** Crie uma reserva de capacidade sob demanda que especifica a região e as três zonas de disponibilidade.

**Justificativa:**  
- **Por que essa opção?**  
  Reservas de capacidade sob demanda garantem capacidade nas zonas selecionadas sem necessidade de instâncias reservadas.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Instâncias reservadas não garantem capacidade específica por zona.  
  - **B:** Reservar capacidade sem zonas definidas não atende ao requisito.  

---

### Questão 48
Uma empresa precisa garantir alta disponibilidade e durabilidade para o catálogo de seu site.

**Resposta correta:**  
**D.** Mova o catálogo para um sistema de arquivos Amazon EFS.

**Justificativa:**  
- **Por que essa opção?**  
  O EFS oferece armazenamento altamente disponível e durável, acessível por múltiplas instâncias EC2.  

- **Por que as outras opções não são adequadas?**  
  - **A:** ElastiCache não é ideal para armazenamento de longo prazo.  
  - **B:** Aumentar a capacidade da instância não resolve durabilidade.  
  - **C:** S3 Glacier é para arquivamento, não para acesso frequente.  

---

### Questão 49
Uma empresa armazena transcrições de chamadas, acessadas com frequência no primeiro ano e raramente após isso.

**Resposta correta:**  
**B.** Use S3 Intelligent-Tiering com políticas de ciclo de vida para mover os arquivos para Glacier após 1 ano.

**Justificativa:**  
- **Por que essa opção?**  
  Intelligent-Tiering reduz custos para dados raramente acessados, enquanto Glacier é ideal para arquivamento de longo prazo.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Glacier Instant Retrieval é mais caro que Intelligent-Tiering para o primeiro ano.  
  - **C e D:** Usar metadados adiciona complexidade desnecessária.  

---

### Questão 50
Uma empresa precisa aplicar patches críticos de software em 1.000 instâncias EC2 rapidamente.

**Resposta correta:**  
**B.** Configure o AWS Systems Manager Patch Manager para aplicar o patch em todas as instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  O Patch Manager automatiza a aplicação de patches em larga escala com mínima sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Lambda não é adequado para aplicar patches diretamente.  
  - **C:** Janelas de manutenção são úteis, mas Patch Manager é mais específico.  
  - **D:** Comandos Run Command exigem mais esforço manual.  

---
### Questão 51
Uma empresa está desenvolvendo uma aplicação que fornece estatísticas de envio de pedidos, acessíveis por uma API REST. A empresa quer extrair as estatísticas, organizá-las em um formato HTML de fácil leitura e enviar o relatório para vários endereços de e-mail no mesmo horário todas as manhãs.

**Resposta correta:**  
**D.** Crie um evento agendado do Amazon EventBridge (Amazon CloudWatch Events) que invoque uma função AWS Lambda para consultar os dados da API da aplicação.  
**B.** Use o Amazon Simple Email Service (Amazon SES) para formatar os dados e enviar o relatório por e-mail.

**Justificativa:**  
- **Por que essas opções?**  
  - **D:** O EventBridge permite agendar eventos que acionam a função Lambda para acessar os dados da API. A Lambda pode processar os dados para formatá-los conforme necessário.  
  - **B:** O Amazon SES é ideal para envio de e-mails em massa e suporta HTML formatado, tornando-o perfeito para criar e enviar relatórios.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Kinesis Data Firehose não é necessário, pois os dados não estão sendo transmitidos em tempo real.  
  - **C:** O AWS Glue é mais complexo do que o necessário para extrair dados simples de uma API REST.  
  - **E:** O SNS não fornece funcionalidades suficientes para formatar e-mails em HTML.

---

### Questão 52
Uma empresa está migrando uma aplicação com um sistema de arquivos compartilhado usado por múltiplos servidores.

**Resposta correta:**  
**A.** Use o Amazon EFS para criar um sistema de arquivos compartilhado acessível por instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  O EFS é altamente escalável e projetado para compartilhamento de arquivos entre instâncias EC2, reduzindo complexidade.  

- **Por que as outras opções não são adequadas?**  
  - **B:** S3 não é um sistema de arquivos POSIX.  
  - **C:** ElastiCache não suporta armazenamento compartilhado persistente.  
  - **D:** Usar volumes EBS replicados aumenta a complexidade operacional.  

---
### Questão 53
Uma empresa precisa armazenar registros contábeis no Amazon S3. Os registros devem estar imediatamente acessíveis por 1 ano e depois arquivados por mais 9 anos. Ninguém na empresa, incluindo usuários administrativos e root, pode excluir os registros durante o período de 10 anos. Os registros devem ser armazenados com resiliência máxima.

**Resposta correta:**  
**C.** Use uma política de ciclo de vida do S3 para transferir os registros do S3 Standard para o S3 Glacier Deep Archive após 1 ano. Use S3 Object Lock em modo de conformidade por um período de 10 anos.

**Justificativa:**  
- **Por que essa opção?**  
  A combinação de S3 Object Lock e o ciclo de vida fornece retenção e segurança necessárias durante os 10 anos, com transição automática para armazenamento mais econômico.  

- **Por que as outras opções não são adequadas?**  
  - **A:** S3 Glacier sozinho não garante acessibilidade imediata no primeiro ano.  
  - **B:** S3 Intelligent-Tiering não é necessário e não bloqueia a exclusão.  
  - **D:** S3 One Zone-IA não atende aos requisitos de resiliência.  

---

### Questão 54
Uma empresa executa várias cargas de trabalho Windows na AWS. Os funcionários usam compartilhamentos de arquivos Windows hospedados em duas instâncias Amazon EC2. A empresa quer uma solução de armazenamento altamente disponível e durável que preserve como os usuários acessam os arquivos.

**Resposta correta:**  
**C.** Expanda o ambiente de compartilhamento de arquivos para o Amazon FSx para Windows File Server com uma configuração Multi-AZ. Migre todos os dados para o FSx.

**Justificativa:**  
- **Por que essa opção?**  
  O FSx para Windows File Server é altamente disponível, durável e compatível com protocolos de arquivos do Windows.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O S3 não suporta diretamente compartilhamentos de arquivos no Windows.  
  - **B:** S3 File Gateway adiciona latência e não é adequado para acesso de arquivos nativo no Windows.  
  - **D:** O EFS não é compatível com protocolos de arquivos do Windows.  

---

### Questão 55
Um arquiteto de soluções está desenvolvendo uma arquitetura VPC com múltiplas sub-redes para hospedar aplicações que usam instâncias EC2 e bancos RDS.

**Resposta correta:**  
**C.** Crie um grupo de segurança que permita tráfego de entrada do grupo de segurança atribuído às instâncias nas sub-redes privadas. Anexe o grupo de segurança às instâncias de banco de dados.

**Justificativa:**  
- **Por que essa opção?**  
  Utilizar grupos de segurança para controlar acesso é eficiente e segue o princípio de menor privilégio.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Alterar tabelas de rota não é suficiente para limitar o tráfego por sub-rede.  
  - **B:** Bloquear tráfego das sub-redes públicas pode impactar funcionalidades legítimas.  
  - **D:** Conexões de emparelhamento não são necessárias nesse caso.  

---

### Questão 56
Uma empresa registrou seu domínio no Route 53 e usa o API Gateway como interface pública para APIs de microsserviços.

**Resposta correta:**  
**C.** Crie um endpoint Regional no API Gateway. Associe-o ao domínio da empresa. Importe o certificado público associado ao domínio no AWS Certificate Manager (ACM) na mesma região e configure o Route 53 para rotear o tráfego.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint Regional com suporte a HTTPS e certificado no ACM garante segurança e compatibilidade com o domínio.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Não atendem ao requisito de configuração na mesma região do API Gateway.  
  - **D:** Usar ACM na região us-east-1 é desnecessário neste caso.  

---

### Questão 57
Uma empresa administra um site de rede social popular e quer garantir que imagens carregadas pelos usuários não contenham conteúdo impróprio.

**Resposta correta:**  
**B.** Use o Amazon Rekognition para detectar conteúdo impróprio. Use revisão humana para previsões com baixa confiança.

**Justificativa:**  
- **Por que essa opção?**  
  O Rekognition é otimizado para análise de imagens e pode identificar conteúdo impróprio de maneira automática e eficaz.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon Comprehend é voltado para análise de texto, não imagens.  
  - **C e D:** Usar SageMaker ou modelos personalizados adiciona complexidade desnecessária.  

---

### Questão 58
Uma empresa deseja executar aplicações críticas em containers, atendendo requisitos de escalabilidade e disponibilidade, sem gerenciar infraestrutura.

**Resposta correta:**  
**C.** Use o Amazon ECS no AWS Fargate.

**Justificativa:**  
- **Por que essa opção?**  
  O Fargate elimina a necessidade de gerenciar a infraestrutura subjacente, permitindo foco apenas nas aplicações.  

- **Por que as outras opções não são adequadas?**  
  - **A e D:** EC2 requer gerenciamento da infraestrutura.  
  - **B:** ECS com EC2 worker nodes ainda exige manutenção da infraestrutura.  

---

Deseja que continue com mais questões?
### Questão 59
Uma empresa hospeda mais de 300 sites e aplicativos globais. A empresa precisa de uma plataforma para analisar mais de 30 TB de dados de clickstream diariamente.

**Resposta correta:**  
**D.** Colete os dados do Amazon Kinesis Data Streams. Use o Amazon Kinesis Data Firehose para transmitir os dados para um data lake no Amazon S3. Carregue os dados no Amazon Redshift para análise.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis Data Streams e Firehose são projetados para lidar com grandes volumes de dados em tempo real, e o Redshift é ideal para análise massiva de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Data Pipeline é mais complexo e menos eficiente para ingestão em tempo real.  
  - **B:** EC2 é menos escalável e mais caro para lidar com grandes volumes de dados.  
  - **C:** CloudFront não é adequado para análise de dados clickstream.  

---

### Questão 60
Uma empresa tem um site hospedado na AWS. O site está atrás de um Application Load Balancer (ALB) configurado para lidar separadamente com HTTP e HTTPS. A empresa deseja que todas as solicitações sejam redirecionadas para HTTPS.

**Resposta correta:**  
**C.** Crie uma regra de listener no ALB para redirecionar o tráfego HTTP para HTTPS.

**Justificativa:**  
- **Por que essa opção?**  
  Configurar uma regra de redirecionamento no listener é simples, eficaz e elimina a necessidade de configurações adicionais.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar a ACL da rede não realiza redirecionamento.  
  - **B:** Substituir HTTP por HTTPS na URL requer alterações adicionais no lado do cliente.  
  - **D:** Um Network Load Balancer não é necessário para este caso.  

---

### Questão 61
Uma empresa está desenvolvendo uma aplicação web de duas camadas na AWS. A aplicação conecta diretamente a um banco de dados RDS.

**Resposta correta:**  
**C.** Armazene as credenciais do banco como um segredo no AWS Secrets Manager. Ative a rotação automática para o segredo. Anexe a permissão necessária ao role da instância EC2 para acessar o segredo.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager oferece rotação automática e gerenciamento seguro de credenciais com integração nativa ao EC2.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Armazenar credenciais nos metadados da instância não é seguro.  
  - **B:** Armazenar credenciais em arquivos de configuração no S3 adiciona complexidade e reduz a segurança.  
  - **D:** O Parameter Store não possui rotação automática nativa como o Secrets Manager.  

---

### Questão 62
Uma empresa está implementando uma aplicação web pública na AWS, que será executada atrás de um ALB. A aplicação precisa ser criptografada na borda com um certificado SSL/TLS emitido por uma autoridade certificadora externa (CA).

**Resposta correta:**  
**D.** Use o AWS Certificate Manager (ACM) para importar um certificado SSL/TLS. Aplique o certificado ao ALB. Use o Amazon EventBridge (Amazon CloudWatch Events) para enviar notificações quando o certificado estiver próximo do vencimento. Faça a rotação do certificado manualmente.

**Justificativa:**  
- **Por que essa opção?**  
  Importar certificados externos no ACM é necessário para atender ao requisito de usar um CA externo, e o EventBridge permite notificações automatizadas para gerenciar a rotação.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** O ACM só pode gerenciar renovações automáticas para certificados emitidos por ele.  
  - **C:** O ACM Private CA não é compatível com certificados de CA externa.  

---

### Questão 63
Uma empresa opera sua infraestrutura na AWS e tem 700.000 usuários registrados em seu aplicativo de gerenciamento de documentos.

**Resposta correta:**  
**A.** Salve os arquivos PDF no Amazon S3. Configure um evento PUT no S3 para invocar uma função AWS Lambda que converte os arquivos para o formato JPG e os armazena novamente no S3.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 e o Lambda são escaláveis e econômicos, permitindo ingestão automática e processamento de arquivos sem infraestrutura adicional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** DynamoDB Streams não é projetado para processar arquivos grandes como PDFs.  
  - **C e D:** Elastic Beanstalk e EC2 aumentam a complexidade e o custo operacional.  

---

### Questão 64
Uma empresa possui mais de 5 TB de dados em servidores de arquivos Windows locais. A empresa está migrando cargas de trabalho para AWS, mas precisa manter o acesso aos arquivos com baixa latência tanto no local quanto na nuvem.

**Resposta correta:**  
**D.** Implante e configure Amazon FSx for Windows File Server na AWS. Implante e configure um Amazon FSx File Gateway no local. Mova os dados locais para o FSx File Gateway.

**Justificativa:**  
- **Por que essa opção?**  
  O FSx for Windows File Server oferece um sistema de arquivos totalmente gerenciado e compatível com Windows. O FSx File Gateway garante acesso contínuo e com baixa latência para os usuários locais.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Apenas o FSx ou o S3 File Gateway não atendem ao requisito de baixa latência para acessos locais e na nuvem.  
  - **B:** O S3 File Gateway sozinho não é compatível com os padrões de compartilhamento de arquivos do Windows.  

---

### Questão 65
Um hospital usa API Gateway e Lambda para carregar relatórios em formatos PDF e JPEG. Eles precisam identificar informações protegidas de saúde (PHI) nos relatórios com o menor esforço operacional.

**Resposta correta:**  
**C.** Use Amazon Textract para extrair texto dos relatórios. Use Amazon Comprehend Medical para identificar PHI no texto extraído.

**Justificativa:**  
- **Por que essa opção?**  
  O Textract automatiza a extração de texto de PDFs e imagens, enquanto o Comprehend Medical é otimizado para detectar informações de saúde protegidas, minimizando o esforço operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Bibliotecas Python exigem mais desenvolvimento e manutenção manual.  
  - **B e D:** SageMaker e Rekognition adicionam complexidade desnecessária para o caso específico de PHI.  

---

### Questão 66
Uma empresa precisa armazenar arquivos em S3 com acessibilidade imediata por 4 anos. Os arquivos são acessados com frequência nos primeiros 30 dias e raramente depois disso.

**Resposta correta:**  
**C.** Crie uma política de ciclo de vida para mover arquivos do S3 Standard para S3 Standard-Infrequent Access (S3 Standard-IA) após 30 dias. Exclua os arquivos após 4 anos.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Standard-IA oferece armazenamento mais barato para dados acessados raramente, mantendo acessibilidade imediata.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Glacier não é adequado para acessos frequentes nos primeiros 30 dias.  
  - **B:** One Zone-IA compromete a resiliência.  
  - **D:** Mover para Glacier depois de 4 anos adiciona complexidade desnecessária.  

---

### Questão 67
Uma aplicação processa mensagens de uma fila SQS e grava em um banco de dados RDS. Mensagens duplicadas são registradas ocasionalmente no banco.

**Resposta correta:**  
**D.** Use a chamada ChangeMessageVisibility API para aumentar o timeout de visibilidade.

**Justificativa:**  
- **Por que essa opção?**  
  Um timeout de visibilidade maior garante que mensagens em processamento não sejam entregues novamente antes de serem excluídas.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Criar uma nova fila não resolve o problema.  
  - **B:** Adicionar permissões não impacta duplicidade de mensagens.  
  - **C:** Ajustar o tempo de espera na API ReceiveMessage não evita o problema de timeout.  

---

### Questão 68
Uma empresa requer uma conexão híbrida altamente disponível e com latência consistente para a AWS, aceitando tráfego mais lento em caso de falha da conexão primária.

**Resposta correta:**  
**A.** Configure uma conexão AWS Direct Connect para a região. Configure uma conexão VPN como backup.

**Justificativa:**  
- **Por que essa opção?**  
  O Direct Connect oferece latência consistente, e a VPN serve como uma solução de backup mais barata.  

- **Por que as outras opções não são adequadas?**  
  - **B:** VPNs não oferecem a mesma consistência de latência que o Direct Connect.  
  - **C:** Usar duas conexões Direct Connect aumenta os custos desnecessariamente.  
  - **D:** O atributo failover não cria automaticamente uma conexão de backup.  

---

### Questão 69
Uma empresa está executando uma aplicação web crítica em instâncias Amazon EC2 atrás de um Application Load Balancer. As instâncias estão em um Auto Scaling Group e usam um banco Aurora PostgreSQL implantado em uma única zona de disponibilidade. A empresa precisa garantir alta disponibilidade com mínimo tempo de inatividade e mínima perda de dados.

**Resposta correta:**  
**B.** Configure o Auto Scaling Group para usar múltiplas zonas de disponibilidade. Configure o banco de dados como Multi-AZ. Configure uma instância Amazon RDS Proxy para o banco de dados.

**Justificativa:**  
- **Por que essa opção?**  
  Configurar instâncias em múltiplas zonas e usar Multi-AZ no Aurora PostgreSQL garante alta disponibilidade e resiliência. O RDS Proxy melhora o gerenciamento de conexões e minimiza o impacto de falhas.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar múltiplas regiões e replicação cross-region aumenta complexidade e latência.  
  - **C:** Backups por snapshots não garantem alta disponibilidade ou recuperação rápida.  
  - **D:** Usar múltiplas regiões para dados críticos adiciona desafios de sincronização e latência.  

---

### Questão 70
A aplicação HTTP de uma empresa está atrás de um Network Load Balancer (NLB). O grupo de destino do NLB usa um Auto Scaling Group com várias instâncias EC2 executando o serviço web.

**Resposta correta:**  
**C.** Substitua o NLB por um Application Load Balancer. Habilite verificações de integridade HTTP fornecendo o URL da aplicação. Configure uma ação de Auto Scaling para substituir instâncias não saudáveis.

**Justificativa:**  
- **Por que essa opção?**  
  Um Application Load Balancer (ALB) é mais adequado para aplicações HTTP/HTTPS e suporta verificações de integridade baseadas em URL.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O NLB não oferece suporte a verificações de integridade baseadas em HTTP.  
  - **B:** Adicionar um cron job aumenta a complexidade sem resolver o problema da detecção automática.  
  - **D:** Alarmes do CloudWatch monitoram, mas não substituem o NLB inadequado para HTTP.  

---

### Questão 71
Uma empresa opera uma aplicação de compras que usa DynamoDB para armazenar informações de clientes. Em caso de corrupção de dados, é necessário atender a um RPO de 15 minutos e um RTO de 1 hora.

**Resposta correta:**  
**B.** Configure a recuperação point-in-time (PITR) do DynamoDB. Para recuperação, restaure para o ponto desejado no tempo.

**Justificativa:**  
- **Por que essa opção?**  
  O PITR do DynamoDB fornece restauração granular em até 35 dias, permitindo recuperação rápida e precisa dentro do RPO/RTO.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Global tables não são projetadas para recuperação de dados corrompidos.  
  - **C:** Exportar para Glacier não atende ao RTO de 1 hora devido ao tempo de recuperação.  
  - **D:** Snapshots do EBS não são uma funcionalidade nativa do DynamoDB.  

---

### Questão 72
Uma empresa executa uma aplicação de processamento de fotos que precisa carregar e baixar fotos frequentemente de buckets S3 na mesma região da AWS. Um arquiteto de soluções notou um aumento nos custos de transferência de dados e precisa implementar uma solução para reduzir esses custos.

**Resposta correta:**  
**D.** Implemente um endpoint de gateway S3 VPC na VPC e anexe uma política de endpoint que permita acesso aos buckets S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint de gateway para S3 permite que instâncias na VPC acessem o S3 sem usar a internet pública, eliminando custos adicionais de transferência de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** O uso de NAT ou API Gateway adiciona complexidade e custos desnecessários.  
  - **C:** Encaminhar pelo internet gateway não resolve os custos de transferência dentro da mesma região.  

---

### Questão 73
Uma empresa lançou instâncias de aplicação baseadas em Linux no EC2 em uma sub-rede privada e um bastion host em uma sub-rede pública de uma VPC. O arquiteto precisa configurar os grupos de segurança para permitir acesso seguro.

**Resposta correta:**  
**B, D.** Substitua o grupo de segurança do bastion host para permitir acesso apenas do IP interno da empresa. Configure o grupo de segurança das instâncias de aplicação para permitir acesso SSH apenas do IP privado do bastion host.

**Justificativa:**  
- **Por que essas opções?**  
  Garantem segurança adequada, limitando o acesso ao bastion host e protegendo as instâncias privadas de acessos não autorizados.  

- **Por que as outras opções não são adequadas?**  
  - **A e E:** Permitir acesso direto de endereços externos ou públicos compromete a segurança.  

---

### Questão 74
Um arquiteto está projetando uma aplicação web de duas camadas com o front-end em sub-redes públicas e o banco de dados SQL Server em uma sub-rede privada.

**Resposta correta:**  
**A, C.** Configure o grupo de segurança da camada web para permitir tráfego de entrada na porta 443 de 0.0.0.0/0. Configure o grupo de segurança da camada de banco de dados para permitir tráfego de entrada na porta 1433 do grupo de segurança da camada web.

**Justificativa:**  
- **Por que essas opções?**  
  Garantem acesso seguro ao front-end público e tráfego controlado para o banco de dados.  

- **Por que as outras opções não são adequadas?**  
  - **B, D, E:** Configurações de saída não atendem ao requisito principal de tráfego controlado entre as camadas.  

---

### Questão 75
Uma empresa quer migrar uma aplicação multi-camadas para a AWS para melhorar o desempenho e modernizar a aplicação.

**Resposta correta:**  
**A.** Use o Amazon API Gateway para direcionar transações para funções AWS Lambda como camada de aplicação. Use o SQS como camada de comunicação entre os serviços de aplicação.

**Justificativa:**  
- **Por que essa opção?**  
  Moderniza a arquitetura, reduz custos operacionais e melhora a escalabilidade com um design serverless.  

- **Por que as outras opções não são adequadas?**  
  - **B, C, D:** Soluções baseadas em EC2 ou SNS adicionam complexidade e não otimizam a eficiência operacional.  

---

### Questão 76
Uma empresa recebe 10 TB de dados de instrumentação por dia de máquinas localizadas em uma única fábrica. Eles precisam transferir esses dados para o S3 com segurança.

**Resposta correta:**  
**B.** Use o AWS DataSync sobre AWS Direct Connect.

**Justificativa:**  
- **Por que essa opção?**  
  O DataSync é confiável e eficiente para transferências em grande escala, enquanto o Direct Connect garante segurança e baixa latência.  

- **Por que as outras opções não são adequadas?**  
  - **A, C, D:** Usar a internet pública ou DMS não oferece o nível de segurança e desempenho exigido para esse volume de dados.  

---

### Questão 77
Uma empresa precisa configurar uma arquitetura de ingestão de dados em tempo real para sua aplicação. A empresa precisa de uma API, um processo para transformar dados enquanto são transmitidos, e uma solução de armazenamento para os dados.

**Resposta correta:**  
**C.** Configure uma API no Amazon API Gateway para enviar dados para um fluxo de dados do Amazon Kinesis. Crie um fluxo de entrega do Amazon Kinesis Data Firehose que use o fluxo de dados do Kinesis como fonte de dados. Use funções AWS Lambda para transformar os dados. Use o Kinesis Data Firehose para enviar os dados para o Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  A combinação de Kinesis, Firehose e Lambda permite ingestão, transformação e armazenamento em tempo real, com o menor overhead operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar EC2 aumenta o custo e a complexidade em relação à solução serverless.  
  - **B:** O AWS Glue é mais adequado para ETL em grande escala, mas não é ideal para transformações em tempo real.  
  - **D:** A solução de Lambda com Glue adiciona complexidade sem necessidade de integração com Firehose.  

---

### Questão 78
Uma empresa precisa manter dados de transações de usuários em uma tabela DynamoDB. Os dados devem ser retidos por 7 anos.

**Resposta correta:**  
**B.** Use o AWS Backup para criar agendamentos de backup e políticas de retenção para a tabela.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Backup oferece uma solução centralizada e de baixo overhead para gerenciar backups e políticas de retenção de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O DynamoDB point-in-time recovery (PITR) não é uma solução de backup de longo prazo.  
  - **C:** Armazenar backups em S3 não é automatizado e adiciona complexidade.  
  - **D:** Usar Lambda para backups manualmente exigiria mais configuração e não é tão eficiente quanto o AWS Backup.  

---

### Questão 79
Uma empresa planeja usar uma tabela DynamoDB para armazenamento de dados. A empresa está preocupada com a otimização de custos. A tabela não será usada na maioria das manhãs, mas o tráfego de leitura e escrita será imprevisível durante as noites. Quando ocorrerem picos de tráfego, eles acontecerão muito rapidamente.

**Resposta correta:**  
**C.** Crie uma tabela DynamoDB com capacidade provisionada e auto scaling.

**Justificativa:**  
- **Por que essa opção?**  
  O auto scaling do DynamoDB ajusta automaticamente a capacidade com base na demanda, otimizando custos durante os períodos de baixo tráfego e aumentando durante picos.  

- **Por que as outras opções não são adequadas?**  
  - **A:** A capacidade sob demanda pode ser cara durante picos de tráfego.  
  - **B:** Criar um índice global secundário não resolve o problema de otimização de capacidade.  
  - **D:** Global tables não são necessárias para este cenário, já que não há exigência de múltiplas regiões.  

---

### Questão 80
Uma empresa recentemente assinou um contrato com um parceiro AWS MSP para ajudar com a migração de uma aplicação. Um arquiteto de soluções precisa compartilhar uma Amazon Machine Image (AMI) de uma conta AWS existente com a conta AWS do parceiro MSP. A AMI é suportada por volumes EBS criptografados com uma chave gerenciada pelo AWS KMS.

**Resposta correta:**  
**B.** Modifique a propriedade launchPermission da AMI. Compartilhe a AMI apenas com a conta AWS do parceiro MSP. Modifique a política da chave para permitir que a conta AWS do parceiro MSP use a chave.

**Justificativa:**  
- **Por que essa opção?**  
  Modificar as permissões de lançamento e as políticas da chave KMS permite compartilhar a AMI de maneira segura, sem torná-la pública.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Tornar a AMI pública compromete a segurança.  
  - **C:** Usar uma chave do MSP comprometeria o controle sobre a criptografia.  
  - **D:** Exportar a AMI para S3 não é a abordagem mais eficiente para compartilhar uma AMI.  

---

Deseja que continue com mais questões?
### Questão 81
Um arquiteto de soluções está projetando a arquitetura em nuvem para uma nova aplicação. O processo deve ser executado em paralelo, adicionando e removendo nós conforme necessário, com base no número de trabalhos a serem processados. A aplicação de processamento é sem estado. O arquiteto precisa garantir que a aplicação seja desacoplada e os itens de trabalho sejam armazenados de forma durável.

**Resposta correta:**  
**C.** Crie uma fila SQS para armazenar os trabalhos a serem processados. Crie uma Amazon Machine Image (AMI) que consista na aplicação de processamento. Crie um modelo de lançamento que use a AMI. Crie um Auto Scaling group usando o modelo de lançamento. Defina a política de escalabilidade do Auto Scaling para adicionar e remover nós com base no número de itens na fila SQS.

**Justificativa:**  
- **Por que essa opção?**  
  Usar uma fila SQS desacopla os componentes, e a política de escalabilidade baseada no número de itens na fila permite um ajuste dinâmico da capacidade da aplicação.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O SNS não é adequado para filas duráveis como o SQS.  
  - **B:** Usar o tráfego de rede como base para escalabilidade não é eficaz para garantir que os trabalhos sejam processados.  
  - **D:** Usar o SNS e a política de escalabilidade baseada no número de mensagens não é tão eficaz quanto o SQS.  

---

### Questão 82
A empresa hospeda suas aplicações web na nuvem AWS. A empresa configura Elastic Load Balancers para usar certificados importados no AWS Certificate Manager (ACM). A equipe de segurança da empresa precisa ser notificada 30 dias antes do vencimento de cada certificado.

**Resposta correta:**  
**D.** Crie uma regra do Amazon EventBridge (Amazon CloudWatch Events) para detectar qualquer certificado que vá expirar dentro de 30 dias. Configure a regra para invocar uma função AWS Lambda. Configure a função Lambda para enviar um alerta personalizado por meio do Amazon Simple Notification Service (Amazon SNS).

**Justificativa:**  
- **Por que essa opção?**  
  Usar o EventBridge com a função Lambda fornece uma maneira escalável e automatizada de monitorar a expiração de certificados e enviar alertas.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Regras personalizadas no ACM não são adequadas para automação de alertas.  
  - **B:** O AWS Config não é o serviço mais eficiente para monitorar expiração de certificados.  
  - **C:** O Trusted Advisor não pode monitorar todos os certificados em tempo real.  

---

### Questão 83
O site dinâmico de uma empresa está hospedado em servidores locais nos Estados Unidos. A empresa está lançando seu produto na Europa e quer otimizar o tempo de carregamento do site para os novos usuários europeus. O backend do site deve permanecer nos Estados Unidos. O produto será lançado em poucos dias, e uma solução imediata é necessária.

**Resposta correta:**  
**C.** Use o Amazon CloudFront com uma origem personalizada apontando para os servidores locais.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront melhora significativamente os tempos de carregamento para usuários globais ao armazenar em cache o conteúdo estático em locais próximos aos usuários.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Mover a aplicação para outra região não é uma solução rápida.  
  - **D:** O Route 53 não resolve diretamente o problema de otimização de tempo de carregamento com servidores localizados em diferentes regiões.  

---

### Questão 84
Uma empresa quer reduzir os custos de sua arquitetura web de três camadas existente. Os servidores de web, aplicação e banco de dados estão sendo executados em instâncias Amazon EC2 para os ambientes de desenvolvimento, teste e produção.

**Resposta correta:**  
**B.** Use Reserved Instances para as instâncias EC2 de produção. Use instâncias sob demanda para os ambientes de desenvolvimento e teste.

**Justificativa:**  
- **Por que essa opção?**  
  Reserved Instances oferecem um desconto significativo para instâncias de produção que estão sempre em uso. Instâncias sob demanda são mais flexíveis e adequadas para ambientes de desenvolvimento e teste.  

- **Por que as outras opções não são adequadas?**  
  - **A, C, D:** Usar Spot ou Spot blocks pode não ser ideal para ambientes críticos de produção ou para instâncias que precisam ser executadas 24/7.  

---

### Questão 85
Uma empresa tem uma aplicação web de produção onde os usuários carregam documentos por meio de uma interface web ou aplicativo móvel. De acordo com uma nova exigência regulatória, novos documentos não podem ser modificados ou excluídos depois de armazenados.

**Resposta correta:**  
**A.** Armazene os documentos carregados em um bucket Amazon S3 com versionamento e S3 Object Lock habilitado.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento do S3 e o Object Lock garantem que os documentos não possam ser modificados ou excluídos após o armazenamento, atendendo às exigências regulatórias.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A política de ciclo de vida do S3 não garante que os documentos não possam ser excluídos ou modificados.  
  - **C:** Configurar ACLs não garante que documentos não possam ser alterados ou excluídos.  
  - **D:** O EFS é um sistema de arquivos, mas não oferece as funcionalidades necessárias para impedir alterações ou exclusões.  

---

Se deseja que eu continue para mais questões, por favor, avise!
### Questão 86
Uma empresa possui vários servidores web que precisam acessar com frequência uma instância Amazon RDS MySQL Multi-AZ. A empresa deseja um método seguro para que os servidores web se conectem ao banco de dados, atendendo à exigência de segurança para rotacionar credenciais de usuário com frequência.

**Resposta correta:**  
**A.** Armazene as credenciais do banco de dados no AWS Secrets Manager. Conceda as permissões IAM necessárias para permitir que os servidores web acessem o AWS Secrets Manager.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Secrets Manager permite gerenciar e rotacionar credenciais automaticamente, atendendo aos requisitos de segurança e flexibilidade.  

- **Por que as outras opções não são adequadas?**  
  - **B:** OpsCenter não é a ferramenta adequada para armazenamento de credenciais de banco de dados.  
  - **C:** Usar um bucket S3 não é uma prática recomendada para armazenar credenciais de banco de dados, pois pode comprometer a segurança.  
  - **D:** Armazenar credenciais criptografadas localmente nas instâncias pode ser inseguro e difícil de gerenciar em escala.  

---

### Questão 87
Uma empresa hospeda uma aplicação em funções AWS Lambda invocadas por uma API do Amazon API Gateway. As funções Lambda salvam dados de clientes em um banco de dados Amazon Aurora MySQL. Sempre que a empresa atualiza o banco de dados, as funções Lambda falham ao estabelecer conexões com o banco até que a atualização seja concluída.

**Resposta correta:**  
**A.** Provisione um proxy Amazon RDS para ficar entre as funções Lambda e o banco de dados. Configure as funções Lambda para se conectarem ao proxy RDS.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon RDS Proxy melhora a escalabilidade e a resiliência das conexões com o banco de dados, permitindo que as funções Lambda se conectem sem interrupções, mesmo durante atualizações.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Aumentar o tempo de execução da Lambda não resolve o problema de falha de conexão.  
  - **C:** Armazenar dados localmente nas funções Lambda não resolve o problema de dependência do banco de dados.  
  - **D:** Usar uma fila SQS não resolve diretamente o problema de falhas de conexão com o banco de dados.  

---

### Questão 88
Uma empresa de pesquisa reuniu dados por vários anos de áreas nos Estados Unidos. A empresa hospeda os dados em um bucket S3 de 3 TB e em crescimento. A empresa começou a compartilhar os dados com uma firma de marketing europeia que possui buckets S3. A empresa deseja garantir que seus custos de transferência de dados permaneçam o mais baixo possível.

**Resposta correta:**  
**A.** Configure o recurso Requester Pays no bucket S3 da empresa.

**Justificativa:**  
- **Por que essa opção?**  
  A configuração de Requester Pays permite que os custos de transferência de dados sejam arcados pela empresa de marketing, reduzindo os custos para a empresa.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A replicação cross-region resulta em custos adicionais de armazenamento e transferência.  
  - **C:** O acesso cross-account não resolve diretamente os custos de transferência de dados.  
  - **D:** O uso do S3 Intelligent-Tiering não reduz custos de transferência de dados entre contas e regiões.  

---

### Questão 89
Uma empresa usa o Amazon S3 para armazenar seus documentos confidenciais de auditoria. O bucket S3 usa políticas de bucket para restringir o acesso às credenciais de usuário IAM da equipe de auditoria conforme o princípio do menor privilégio. Os gerentes da empresa estão preocupados com a exclusão acidental de documentos no bucket S3 e desejam uma solução mais segura.

**Resposta correta:**  
**A.** Habilite as funcionalidades de versionamento e MFA Delete no bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento e o MFA Delete protegem contra a exclusão acidental de objetos no S3, exigindo autenticação multifatorial para exclusão de versões.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O MFA em credenciais IAM não impede a exclusão acidental de documentos.  
  - **C:** A política de Lifecycle não impede exclusões acidentais.  
  - **D:** O KMS não impede a exclusão de objetos no S3.  

---

### Questão 90
Uma empresa usa um banco de dados SQL para armazenar dados de filmes acessíveis publicamente. O banco de dados está em uma instância Amazon RDS Single-AZ. Um script executa consultas aleatórias todos os dias para registrar o número de novos filmes adicionados ao banco de dados.

**Resposta correta:**  
**B.** Crie uma réplica de leitura do banco de dados. Configure o script para consultar apenas a réplica de leitura.

**Justificativa:**  
- **Por que essa opção?**  
  A réplica de leitura permite que o script faça consultas sem afetar a performance do banco de dados principal.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Modificar para Multi-AZ não resolve o problema de sobrecarga de leitura.  
  - **C:** Exportar manualmente é uma solução menos eficiente e mais trabalhosa.  
  - **D:** O ElastiCache não é necessário para consultas simples e frequentes em um banco de dados SQL.  

---

### Questão 91
Uma empresa tem aplicações que rodam em instâncias Amazon EC2 em uma VPC. Uma das aplicações precisa chamar a API do Amazon S3 para armazenar e ler objetos. De acordo com as regulamentações de segurança da empresa, nenhum tráfego das aplicações pode viajar pela internet.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Crie um endpoint VPC Gateway para o S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway para o S3 permite que o tráfego entre as instâncias EC2 e o S3 ocorra dentro da VPC, sem necessidade de tráfego pela internet, atendendo às exigências de segurança.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar um internet gateway permitiria tráfego pela internet, o que viola as regulamentações de segurança.  
  - **C:** Usar um NAT Gateway também envolve tráfego pela internet, o que não é permitido.  
  - **D:** Um VPC Peering não resolveria o problema de acessar o S3 de forma segura dentro da mesma VPC.  

---

### Questão 92
Uma empresa está armazenando informações sensíveis de usuários em um bucket Amazon S3. A empresa deseja fornecer acesso seguro a esse bucket a partir da camada de aplicação que está sendo executada em instâncias Amazon EC2 dentro de uma VPC.  
Qual combinação de etapas um arquiteto de soluções deve tomar para realizar isso? (Escolha duas.)

**Resposta correta:**  
**A.** Configure um endpoint de gateway VPC para o Amazon S3 dentro da VPC.  
**C.** Crie uma política de bucket que limita o acesso apenas à camada de aplicação em execução na VPC.

**Justificativa:**  
- **Por que essa opção?**  
  O uso de um endpoint de gateway VPC permite que o tráfego para o S3 seja roteado diretamente dentro da VPC, sem precisar passar pela internet, atendendo aos requisitos de segurança. A política de bucket que limita o acesso à camada de aplicação garante que apenas as instâncias EC2 autorizadas possam acessar o S3.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Tornar os objetos públicos comprometeria a segurança, permitindo que qualquer pessoa acessasse o conteúdo do S3.  
  - **D:** Usar uma instância NAT não é necessário para o acesso do EC2 ao S3 quando um endpoint VPC é configurado.  
  - **E:** A criação de um usuário IAM específico para as instâncias EC2 não é necessária se uma política de bucket adequada for configurada.

---

Deseja que eu continue com a **questão 93**?
### Questão 93
Uma empresa executa uma aplicação local que é alimentada por um banco de dados MySQL. A empresa está migrando a aplicação para a AWS para aumentar a elasticidade e a disponibilidade da aplicação.  
A arquitetura atual mostra alta atividade de leitura no banco de dados durante os períodos de operação normal. A cada 4 horas, a equipe de desenvolvimento da empresa faz uma exportação completa do banco de dados de produção para popular um banco de dados no ambiente de teste. Durante esse período, os usuários experimentam latência inaceitável na aplicação. A equipe de desenvolvimento não consegue usar o ambiente de teste até que o procedimento seja concluído.  
Um arquiteto de soluções deve recomendar uma arquitetura substituta que alivie o problema de latência da aplicação. A arquitetura substituta também deve dar à equipe de desenvolvimento a capacidade de continuar usando o ambiente de teste sem demora.  
Qual solução atende a esses requisitos?

**Resposta correta:**  
**B.** Use Amazon Aurora MySQL com réplicas Aurora Multi-AZ para produção. Use clonagem de banco de dados para criar o banco de dados de teste sob demanda.

**Justificativa:**  
- **Por que essa opção?**  
  A Aurora MySQL com réplicas Multi-AZ proporciona alta disponibilidade e pode ser escalada para lidar com tráfego de leitura. A clonagem de banco de dados permite que o banco de dados de teste seja criado rapidamente, sem afetar o banco de dados de produção.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o mysqldump para backup e restauração pode causar latência devido à interrupção de produção durante o processo.  
  - **C:** Usar instâncias standby para o ambiente de teste pode resultar em um processo de configuração mais complexo e menos eficiente.  
  - **D:** A replicação com mysqldump não resolve o problema de latência de maneira eficiente.  

---

Devo continuar com a **questão 94**?  
### Questão 94
Uma empresa está projetando uma aplicação onde os usuários carregam pequenos arquivos no Amazon S3. Após o carregamento de um arquivo, é necessário um processamento simples para transformar os dados e salvar em formato JSON para análise posterior.  
Cada arquivo deve ser processado o mais rápido possível após o upload. A demanda variará. Em alguns dias, os usuários carregarão um grande número de arquivos. Em outros dias, os usuários carregarão poucos ou nenhum arquivo.  
Qual solução atende a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**C.** Configure o Amazon S3 para enviar uma notificação de evento para uma fila Amazon Simple Queue Service (Amazon SQS). Use uma função AWS Lambda para ler da fila e processar os dados. Armazene o arquivo JSON resultante no Amazon DynamoDB.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o SQS com Lambda permite o processamento assíncrono dos arquivos sem sobrecarga adicional, e o DynamoDB fornece armazenamento de dados escalável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon EMR introduz complexidade operacional desnecessária para um processamento simples de arquivos.  
  - **B:** Usar EC2 não é escalável nem ideal para processar arquivos individualmente com alta variabilidade de demanda.  
  - **D:** O Kinesis Data Streams não é necessário para esse tipo de processamento, e a Lambda com SQS é uma solução mais simples.

---

### Questão 95
Uma aplicação permite que usuários na sede da empresa acessem dados de produto. Os dados do produto estão armazenados em uma instância Amazon RDS MySQL. A equipe de operações isolou uma desaceleração de desempenho da aplicação e deseja separar o tráfego de leitura do tráfego de escrita. O arquiteto de soluções precisa otimizar o desempenho da aplicação rapidamente.  
O que o arquiteto de soluções deve recomendar?

**Resposta correta:**  
**D.** Crie réplicas de leitura para o banco de dados. Configure as réplicas de leitura com os mesmos recursos de computação e armazenamento da instância de origem.

**Justificativa:**  
- **Por que essa opção?**  
  Criar réplicas de leitura distribui o tráfego de leitura e melhora o desempenho sem afetar o tráfego de escrita.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** O Multi-AZ pode aumentar a disponibilidade, mas não resolve o problema específico de separação de tráfego de leitura e escrita.  
  - **C:** Usar réplicas com menos recursos não seria ideal para lidar com picos de tráfego de leitura.

---

### Questão 96
Um administrador do Amazon EC2 criou a seguinte política associada a um grupo IAM contendo vários usuários:  
Qual é o efeito dessa política?

**Resposta correta:**  
**C.** Os usuários podem terminar uma instância EC2 na região us-east-1 quando o IP de origem do usuário for 10.100.100.254.

**Justificativa:**  
- **Por que essa opção?**  
  A política específica permite que instâncias EC2 sejam terminadas, mas com a restrição de que o IP de origem seja 10.100.100.254 na região us-east-1.  

- **Por que as outras opções não são adequadas?**  
  - **A:** A política não permite que instâncias sejam terminadas em regiões diferentes de us-east-1.  
  - **B:** A política não permite a terminação de instâncias com o IP 10.100.100.1.  
  - **D:** A política não bloqueia a terminação de instâncias com o IP 10.100.100.254.

---

### Questão 97
Uma empresa tem uma grande implantação do Microsoft SharePoint em servidores locais, que requer armazenamento compartilhado de arquivos Windows. A empresa deseja migrar essa carga de trabalho para a AWS e está considerando várias opções de armazenamento. A solução de armazenamento deve ser altamente disponível e integrada ao Active Directory para controle de acesso.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**D.** Crie um sistema de arquivos Amazon FSx for Windows File Server na AWS e defina o domínio Active Directory para autenticação.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon FSx for Windows File Server é totalmente gerenciado, altamente disponível e integrado com o Active Directory, atendendo aos requisitos de armazenamento e controle de acesso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon EFS não oferece suporte para compartilhamento de arquivos do Windows.  
  - **B:** O Storage Gateway não é ideal para integrar com Active Directory.  
  - **C:** O S3 não oferece suporte nativo para arquivos compartilhados com o Windows.

---

### Questão 98
Uma empresa de processamento de imagens tem uma aplicação web que os usuários utilizam para carregar imagens. A aplicação carrega as imagens em um bucket Amazon S3. A empresa configurou notificações de eventos S3 para publicar os eventos de criação de objetos em uma fila padrão do Amazon SQS. A fila SQS serve como fonte de eventos para uma função AWS Lambda que processa as imagens e envia os resultados aos usuários por email.  
Os usuários relatam que estão recebendo várias mensagens de email para cada imagem carregada. Um arquiteto de soluções determina que as mensagens SQS estão invocando a função Lambda mais de uma vez, resultando em mensagens duplicadas.  
O que o arquiteto de soluções deve fazer para resolver esse problema com o MENOR overhead operacional?

**Resposta correta:**  
**B.** Mude a fila SQS padrão para uma fila SQS FIFO. Use o ID de deduplicação da mensagem para descartar mensagens duplicadas.

**Justificativa:**  
- **Por que essa opção?**  
  As filas FIFO do SQS permitem a deduplicação automática de mensagens com base no ID, resolvendo o problema de múltiplas invocações da função Lambda.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Long polling ajuda na eficiência, mas não resolve a duplicação de mensagens.  
  - **C:** Aumentar o timeout de visibilidade não resolve a duplicação.  
  - **D:** A exclusão imediata das mensagens não elimina a duplicação e pode afetar o processamento de falhas.

---

Posso continuar com mais questões ou fornecer mais detalhes?
### Questão 99
Uma empresa está implementando uma solução de armazenamento compartilhado para uma aplicação de jogos que está hospedada em um data center local. A empresa precisa da capacidade de usar clientes Lustre para acessar dados. A solução deve ser totalmente gerenciada.  
Qual solução atende a esses requisitos?

**Resposta correta:**  
**D.** Crie um sistema de arquivos Amazon FSx for Lustre. Anexe o sistema de arquivos ao servidor de origem. Conecte o servidor de aplicação ao sistema de arquivos.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon FSx for Lustre é totalmente gerenciado e oferece suporte nativo para Lustre, tornando a solução ideal para esse tipo de carga de trabalho de jogos.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Storage Gateway não oferece suporte a clientes Lustre.  
  - **B:** Usar uma instância EC2 não seria totalmente gerenciado e introduziria complexidade adicional.  
  - **C:** O Amazon EFS não suporta o Lustre como um protocolo de acesso.  

---

### Questão 100
A aplicação conteinerizada de uma empresa está sendo executada em uma instância Amazon EC2. A aplicação precisa baixar certificados de segurança antes que possa se comunicar com outros aplicativos de negócios. A empresa deseja uma solução altamente segura para criptografar e descriptografar os certificados em tempo real. A solução também precisa armazenar dados em armazenamento altamente disponível após a criptografia.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**C.** Crie uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). Permita que a função EC2 use a chave KMS para operações de criptografia. Armazene os dados criptografados no Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS KMS oferece uma solução segura e gerenciada para criptografar e descriptografar dados em tempo real. O S3 fornece armazenamento altamente disponível.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o AWS Secrets Manager manualmente para atualizar os certificados não é tão eficiente quanto usar o KMS.  
  - **B:** A Lambda não é necessária para criptografar e descriptografar dados em tempo real em um caso simples como este.  
  - **D:** Usar o Amazon EBS para armazenar os dados criptografados não oferece o mesmo nível de disponibilidade e simplicidade que o S3.  

---

### Questão 101
A aplicação conteinerizada de uma empresa está sendo executada em instâncias Amazon EC2. A aplicação precisa baixar certificados de segurança antes que possa se comunicar com outros aplicativos de negócios. A empresa deseja uma solução altamente segura para criptografar e descriptografar os certificados em tempo real. A solução também precisa armazenar dados em armazenamento altamente disponível após a criptografia.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**C.** Crie uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). Permita que a função EC2 use a chave KMS para operações de criptografia. Armazene os dados criptografados no Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS KMS oferece uma solução segura e gerenciada para criptografar e descriptografar dados em tempo real. O S3 fornece armazenamento altamente disponível.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o AWS Secrets Manager manualmente para atualizar os certificados não é tão eficiente quanto usar o KMS.  
  - **B:** A Lambda não é necessária para criptografar e descriptografar dados em tempo real em um caso simples como este.  
  - **D:** Usar o Amazon EBS para armazenar os dados criptografados não oferece o mesmo nível de disponibilidade e simplicidade que o S3.  

---

### Questão 102
Uma empresa deseja migrar um data center local para a AWS. O data center hospeda um servidor SFTP que armazena seus dados em um sistema de arquivos baseado em NFS. O servidor possui 200 GB de dados que precisam ser transferidos. O servidor deve ser hospedado em uma instância Amazon EC2 que usa um sistema de arquivos Amazon Elastic File System (Amazon EFS).  
Qual combinação de etapas um arquiteto de soluções deve tomar para automatizar essa tarefa? (Escolha duas.)

**Resposta correta:**  
**A.** Lance a instância EC2 na mesma Zona de Disponibilidade do sistema de arquivos EFS.  
**E.** Use o AWS DataSync para criar uma configuração de local apropriada para o servidor SFTP local.

**Justificativa:**  
- **Por que essa opção?**  
  Lançar a instância EC2 na mesma zona de disponibilidade do EFS garante baixa latência e alta disponibilidade. O DataSync facilita a transferência de grandes volumes de dados de forma automatizada e eficiente.  

- **Por que as outras opções não são adequadas?**  
  - **B e C:** Criar volumes EBS e usar comandos manuais não são soluções automatizadas e podem introduzir overhead operacional.  
  - **D:** A transferência manual não é uma solução escalável ou eficiente.

---

### Questão 103
Uma empresa tem um trabalho AWS Glue de extração, transformação e carga (ETL) que é executado todos os dias no mesmo horário. O trabalho processa dados XML que estão em um bucket Amazon S3. Novos dados são adicionados ao bucket S3 todos os dias. Um arquiteto de soluções percebe que o AWS Glue está processando todos os dados durante cada execução.  
O que o arquiteto de soluções deve fazer para evitar que o AWS Glue reprocessamento dados antigos?

**Resposta correta:**  
**A.** Edite o trabalho para usar marcadores de trabalho.

**Justificativa:**  
- **Por que essa opção?**  
  O uso de marcadores de trabalho no AWS Glue permite que o trabalho identifique e processe apenas dados novos, evitando o reprocessamento de dados antigos.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Excluir dados após o processamento não é uma prática recomendada e pode afetar a integridade dos dados.  
  - **C:** A configuração do número de trabalhadores não afeta diretamente o problema de reprocessamento.  
  - **D:** O uso de uma transformação FindMatches não é necessário para esse tipo de tarefa.

---

Se desejar, posso continuar processando as próximas questões.
### Questão 104
Um arquiteto de soluções deve projetar uma infraestrutura altamente disponível para um site. O site é alimentado por servidores web Windows que rodam em instâncias Amazon EC2. O arquiteto de soluções deve implementar uma solução que possa mitigar um ataque DDoS em grande escala que se origina de milhares de endereços IP. O tempo de inatividade não é aceitável para o site.  
Quais ações o arquiteto de soluções deve tomar para proteger o site contra tal ataque? (Escolha duas.)

**Resposta correta:**  
**A.** Use o AWS Shield Advanced para impedir o ataque DDoS.  
**C.** Configure o site para usar o Amazon CloudFront para conteúdo estático e dinâmico.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Shield Advanced oferece proteção DDoS avançada e o CloudFront distribui o conteúdo de forma eficiente, melhorando a disponibilidade e a segurança contra ataques.

- **Por que as outras opções não são adequadas?**  
  - **B:** O Amazon GuardDuty não bloqueia automaticamente os atacantes.  
  - **D:** A Lambda não é adequada para bloqueios automáticos em grande escala.  
  - **E:** O uso de EC2 Spot Instances pode aumentar a vulnerabilidade a falhas no tráfego.

---

### Questão 105
Uma empresa está se preparando para implantar uma nova carga de trabalho serverless. Um arquiteto de soluções deve usar o princípio do menor privilégio para configurar permissões que serão usadas para executar uma função AWS Lambda. Uma regra do Amazon EventBridge (Amazon CloudWatch Events) invocará a função.  
Qual solução atende a esses requisitos?

**Resposta correta:**  
**D.** Adicione uma política baseada em recursos à função com lambda:InvokeFunction como a ação e Service: events.amazonaws.com como o principal.

**Justificativa:**  
- **Por que essa opção?**  
  A política baseada em recursos permite restringir o acesso à função Lambda para um serviço específico, como o EventBridge, garantindo a configuração de segurança mínima necessária.

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Permitir permissões amplas de invocação comprometeria o princípio do menor privilégio.  
  - **C:** Permissões lambda:* não são específicas o suficiente para limitar o acesso de forma segura.

---

### Questão 106
Uma empresa está se preparando para armazenar dados confidenciais no Amazon S3. Por razões de conformidade, os dados devem ser criptografados em repouso. O uso das chaves de criptografia deve ser registrado para fins de auditoria. As chaves devem ser rotacionadas a cada ano.  
Qual solução atende a esses requisitos e é a MAIS eficiente operacionalmente?

**Resposta correta:**  
**D.** Criptografia do lado do servidor com chaves AWS KMS (SSE-KMS) com rotação automática.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS KMS fornece criptografia automatizada com rotação das chaves e logs de uso, minimizando a sobrecarga operacional enquanto atende aos requisitos de conformidade.

- **Por que as outras opções não são adequadas?**  
  - **A:** SSE-C exige que o cliente gerencie as chaves, aumentando a complexidade operacional.  
  - **B e C:** SSE-KMS com rotação manual aumenta a carga operacional, pois requer ações manuais anuais.

---

### Questão 107
Uma empresa de compartilhamento de bicicletas está desenvolvendo uma arquitetura de várias camadas para rastrear a localização de suas bicicletas durante os horários de pico. A empresa deseja usar esses pontos de dados em sua plataforma de análise existente. Um arquiteto de soluções deve determinar a opção de múltiplas camadas mais viável para apoiar essa arquitetura. Os pontos de dados devem ser acessíveis pela API REST.  
Qual ação atende a esses requisitos para armazenar e recuperar dados de localização?

**Resposta correta:**  
**D.** Use o Amazon API Gateway com o Amazon Kinesis Data Analytics.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon API Gateway facilita a entrega de dados via API REST, e o Kinesis Data Analytics permite o processamento e análise de dados em tempo real.

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon Athena não é uma solução para fornecer acesso em tempo real via API.  
  - **B:** O AWS Lambda não é uma solução eficiente para processar grandes volumes de dados em tempo real como o Kinesis.  
  - **C:** O Amazon QuickSight é uma ferramenta de visualização, não ideal para processamento de dados em tempo real.

---

### Questão 108
Uma empresa tem um site de vendas de automóveis que armazena seus anúncios em um banco de dados no Amazon RDS. Quando um automóvel é vendido, o anúncio precisa ser removido do site e os dados devem ser enviados para vários sistemas de destino.  
Qual design um arquiteto de soluções deve recomendar?

**Resposta correta:**  
**C.** Inscreva-se em uma notificação de evento do RDS e envie para uma fila do Amazon SQS, espalhada para vários tópicos do Amazon SNS. Use funções AWS Lambda para atualizar os sistemas de destino.

**Justificativa:**  
- **Por que essa opção?**  
  Usar SQS e SNS permite o envio eficiente e distribuído de dados para múltiplos sistemas, com a Lambda processando a lógica necessária para cada sistema de destino.

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Não garantem a escalabilidade e o processamento eficiente de múltiplos sistemas.  
  - **D:** Usar o SQS e SNS diretamente sem o fanned out pode não ser suficiente para sistemas de destino múltiplos.

---

### Questão 109
Uma empresa precisa armazenar dados no Amazon S3 e deve impedir que os dados sejam alterados. A empresa deseja que novos objetos carregados no Amazon S3 permaneçam imutáveis por um período de tempo não especificado até que a empresa decida modificar os objetos. Somente usuários específicos na conta AWS da empresa devem ter a capacidade de excluir os objetos.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**B.** Crie um bucket S3 com S3 Object Lock ativado. Habilite versionamento. Defina um período de retenção de 100 anos. Use o modo de governança como o modo de retenção padrão do bucket S3 para novos objetos.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Object Lock com versionamento permite que os dados sejam imutáveis por um período de retenção especificado e controla a exclusão dos objetos apenas por usuários autorizados.

- **Por que as outras opções não são adequadas?**  
  - **A:** O S3 Glacier é mais adequado para arquivamento de dados e não para evitar alterações.  
  - **C:** O CloudTrail não pode impedir a modificação de objetos, apenas pode registrar as modificações.  
  - **D:** O Legal Hold não é tão adequado quanto a configuração de retenção no S3 Object Lock.

---

### Questão 110
Uma empresa de mídia social permite que os usuários carreguem imagens para o seu site. O site está hospedado em instâncias Amazon EC2. Durante os pedidos de upload, o site redimensiona as imagens para um tamanho padrão e armazena as imagens redimensionadas no Amazon S3. Os usuários estão experimentando pedidos de upload lentos para o site.  
A empresa precisa reduzir o acoplamento dentro da aplicação e melhorar o desempenho do site. Um arquiteto de soluções deve projetar o processo mais eficiente operacionalmente para uploads de imagens.  
Qual combinação de ações o arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)

**Resposta correta:**  
**C.** Configure a aplicação para carregar imagens diretamente do navegador de cada usuário para o Amazon S3 por meio do uso de uma URL pré-assinada.  
**D.** Configure Notificações de Evento do S3 para invocar uma função AWS Lambda quando uma imagem for carregada. Use a função para redimensionar a imagem.

**Justificativa:**  
- **Por que essa opção?**  
  Usar URLs pré-assinadas para o upload direto reduz a carga sobre o servidor EC2 e melhora o desempenho. Usar o Lambda para redimensionar a imagem após o upload melhora a separação de responsabilidades e minimiza o acoplamento.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O uso do S3 Glacier não é adequado para uploads rápidos e de baixa latência.  
  - **B:** Carregar a imagem no servidor e depois redimensioná-la cria mais acoplamento e carga para o servidor EC2.  
  - **E:** Usar o EventBridge para agendar a tarefa de redimensionamento é desnecessário e não tão eficiente quanto o uso de S3 Event Notifications.

---

### Questão 111
Uma empresa migrou recentemente um sistema de processamento de mensagens para a AWS. O sistema recebe mensagens em uma fila ActiveMQ executada em uma instância Amazon EC2. As mensagens são processadas por uma aplicação consumidora executada em Amazon EC2. A aplicação consumidora processa as mensagens e escreve os resultados em um banco de dados MySQL executado no Amazon EC2. A empresa deseja que essa aplicação tenha alta disponibilidade com baixa complexidade operacional.  
Qual arquitetura oferece a MAIOR disponibilidade?

**Resposta correta:**  
**C.** Use o Amazon MQ com brokers ativo/standby configurados em duas Zonas de Disponibilidade. Adicione uma instância EC2 consumidora adicional em outra Zona de Disponibilidade. Use o Amazon RDS para MySQL com Multi-AZ habilitado.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o Amazon MQ com brokers ativo/standby garante alta disponibilidade para o serviço de mensagens. O Amazon RDS com Multi-AZ garante a alta disponibilidade e a recuperação automática de falhas para o banco de dados MySQL.

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Adicionar servidores ActiveMQ manualmente e replicar o banco de dados MySQL não é tão eficiente quanto usar soluções gerenciadas como o Amazon MQ e o Amazon RDS com Multi-AZ.  
  - **D:** O uso de Auto Scaling para instâncias EC2 e replicação manual do banco de dados não é tão eficiente quanto usar o Amazon RDS com Multi-AZ.

---

### Questão 112
Uma empresa hospeda uma aplicação web conteinerizada em um conjunto de servidores locais que processam as requisições recebidas. O número de requisições está crescendo rapidamente. Os servidores locais não conseguem lidar com o aumento do número de requisições. A empresa deseja mover a aplicação para a AWS com o mínimo de mudanças de código e o mínimo de esforço de desenvolvimento.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**A.** Use o AWS Fargate no Amazon Elastic Container Service (Amazon ECS) para executar a aplicação web conteinerizada com Auto Scaling do serviço. Use um Application Load Balancer para distribuir as requisições recebidas.

**Justificativa:**  
- **Por que essa opção?**  
  O Fargate permite rodar containers de forma totalmente gerenciada, sem necessidade de gerenciar a infraestrutura subjacente, oferecendo a solução mais simples e escalável para esse caso.

- **Por que as outras opções não são adequadas?**  
  - **B:** Usar EC2 requer mais gerenciamento de infraestrutura e maior complexidade operacional.  
  - **C:** Usar Lambda pode não ser a solução ideal para uma aplicação com contêineres, pois envolveria mudanças no código e na arquitetura.  
  - **D:** O HPC não é necessário para o tipo de carga de trabalho que a empresa está enfrentando, sendo excessivo.

---

### Questão 113
Uma empresa usa 50 TB de dados para relatórios. A empresa deseja mover esses dados de seu local para a AWS. Uma aplicação personalizada no data center da empresa executa um trabalho de transformação de dados semanal. A empresa planeja pausar a aplicação até que a transferência de dados seja concluída e precisa iniciar o processo de transferência o mais rápido possível.  
O data center não tem largura de banda de rede disponível para cargas de trabalho adicionais. Um arquiteto de soluções deve transferir os dados e deve configurar o trabalho de transformação para continuar a ser executado na AWS Cloud.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**A.** Use o AWS DataSync para mover os dados. Crie um trabalho de transformação personalizado usando o AWS Glue.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS DataSync é uma solução rápida e eficiente para transferir grandes volumes de dados para a AWS. O AWS Glue permite executar tarefas de transformação de dados de forma totalmente gerenciada, reduzindo o overhead operacional.

- **Por que as outras opções não são adequadas?**  
  - **B:** O AWS Snowcone não é adequado para mover grandes volumes de dados.  
  - **C:** O AWS Snowball Edge é mais adequado para dados maiores e não necessariamente para transformação de dados personalizada.  
  - **D:** O uso de EC2 para realizar o trabalho de transformação requer mais gerenciamento e operação manual.

---

### Questão 114
Uma empresa criou uma aplicação de análise de imagens onde os usuários podem enviar fotos e adicionar molduras às imagens. Os usuários carregam imagens e metadados para indicar quais molduras querem adicionar às suas imagens. A aplicação usa uma única instância Amazon EC2 e o Amazon DynamoDB para armazenar os metadados.  
A aplicação está se tornando mais popular, e o número de usuários está aumentando. A empresa espera que o número de usuários simultâneos varie significativamente dependendo do horário do dia e do dia da semana. A empresa deve garantir que a aplicação possa escalar para atender às necessidades da base de usuários crescente.  
Qual solução atende a esses requisitos?

**Resposta correta:**  
**C.** Use AWS Lambda para processar as fotos. Armazene as fotos no Amazon S3. Mantenha o DynamoDB para armazenar os metadados.

**Justificativa:**  
- **Por que essa opção?**  
  Usar Lambda permite que o processamento seja escalável sem intervenção manual. Armazenar as fotos no S3 proporciona armazenamento altamente disponível e barato.  
- **Por que as outras opções não são adequadas?**  
  - **A e B:** O uso do Kinesis ou apenas do Lambda não resolve eficientemente o problema de escalabilidade e persistência dos dados.  
  - **D:** A adição de EC2 manualmente aumenta a complexidade operacional e não é ideal para uma carga de trabalho altamente variável.

---

### Questão 115
Uma empresa de registros médicos está hospedando uma aplicação em instâncias Amazon EC2. A aplicação processa arquivos de dados de clientes que estão armazenados no Amazon S3. As instâncias EC2 estão hospedadas em sub-redes públicas. As instâncias EC2 acessam o Amazon S3 pela internet, mas não requerem nenhum outro acesso à rede.  
Um novo requisito exige que o tráfego de rede para transferências de arquivos tome uma rota privada e não seja enviado pela internet.  
Qual alteração na arquitetura de rede um arquiteto de soluções deve recomendar para atender a esse requisito?

**Resposta correta:**  
**C.** Mova as instâncias EC2 para sub-redes privadas. Crie um VPC endpoint para o Amazon S3 e vincule o endpoint à tabela de rotas das sub-redes privadas.

**Justificativa:**  
- **Por que essa opção?**  
  Criar um endpoint VPC para o S3 garante que o tráfego entre EC2 e S3 não passe pela internet, atendendo ao requisito de privacidade de tráfego.  
- **Por que as outras opções não são adequadas?**  
  - **A:** A NAT gateway ainda faz o tráfego passar pela internet.  
  - **B:** A configuração do security group não garante que o tráfego entre EC2 e S3 seja privado.  
  - **D:** O uso de Direct Connect é uma solução mais cara e complexa do que um VPC endpoint.

---

### Questão 116
Uma empresa usa um sistema de gerenciamento de conteúdo (CMS) popular para seu site corporativo. No entanto, a manutenção e atualização exigem muito esforço. A empresa está redesenhando seu site e quer uma nova solução. O site será atualizado quatro vezes por ano e não precisa de conteúdo dinâmico disponível. A solução deve fornecer alta escalabilidade e segurança aprimorada.  
Qual combinação de alterações atenderá a esses requisitos com o MENOR overhead operacional? (Escolha duas.)

**Resposta correta:**  
**D.** Crie o novo site e um bucket Amazon S3. Implante o site no bucket S3 com o hosting de site estático habilitado.  
**A.** Configure o Amazon CloudFront na frente do site para usar a funcionalidade HTTPS.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 oferece uma solução de hospedagem de site estático escalável e de baixo custo. O CloudFront melhora a segurança e a distribuição de conteúdo.  
- **Por que as outras opções não são adequadas?**  
  - **B:** Usar WAF não é necessário para sites estáticos e simples.  
  - **C:** Usar Lambda para servir conteúdo pode introduzir complexidade desnecessária.  
  - **E:** Usar EC2 para hospedar o site aumenta o overhead operacional.

---

### Questão 117
Uma empresa armazena seus logs de aplicação em um grupo de logs do Amazon CloudWatch Logs. Uma nova política exige que a empresa armazene todos os logs de aplicação no Amazon OpenSearch Service (Amazon Elasticsearch Service) em tempo quase real.  
Qual solução atenderá a esse requisito com o MENOR overhead operacional?

**Resposta correta:**  
**A.** Configure uma assinatura do CloudWatch Logs para transmitir os logs para o Amazon OpenSearch Service (Amazon Elasticsearch Service).

**Justificativa:**  
- **Por que essa opção?**  
  A assinatura de logs do CloudWatch transmite os logs para o OpenSearch Service de forma automática e eficiente, com o menor overhead.  
- **Por que as outras opções não são adequadas?**  
  - **B:** Criar uma função Lambda adiciona complexidade ao processo.  
  - **C:** Usar o Kinesis Data Firehose é útil, mas mais complexo e com mais sobrecarga do que a solução com CloudWatch Logs.  
  - **D:** Instalar o Kinesis Agent em cada servidor requer gerenciamento adicional.

---

### Questão 118
Uma empresa está construindo uma aplicação web baseada em EC2 em várias zonas de disponibilidade. A aplicação web fornecerá acesso a um repositório de documentos de texto totalizando cerca de 900 TB de tamanho. A empresa prevê que a aplicação web terá períodos de alta demanda. Um arquiteto de soluções deve garantir que o componente de armazenamento dos documentos de texto possa escalar para atender à demanda da aplicação o tempo todo. A empresa está preocupada com o custo geral da solução.  
Qual solução de armazenamento atende a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**D.** Amazon S3

**Justificativa:**  
- **Por que essa opção?**  
  O S3 é altamente escalável e econômico para grandes volumes de dados. Ele pode suportar grandes volumes de dados com alta durabilidade e sem comprometer o custo.  
- **Por que as outras opções não são adequadas?**  
  - **A, B e C:** Outras opções, como EBS ou EFS, não são tão escaláveis ou econômicas para esse volume de dados.

---

### Questão 119
Uma empresa global está usando o Amazon API Gateway para projetar APIs REST para seus usuários de clube de fidelidade nas regiões us-east-1 e ap-southeast-2. Um arquiteto de soluções deve projetar uma solução para proteger essas APIs REST gerenciadas pelo API Gateway em várias contas contra injeção de SQL e ataques de cross-site scripting.  
Qual solução atenderá a esses requisitos com o MENOR esforço administrativo?

**Resposta correta:**  
**A.** Configure o AWS WAF em ambas as regiões. Associe ACLs da web regionais com um estágio de API.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS WAF é projetado para proteger contra ataques de SQL injection e cross-site scripting de forma simples e eficaz, com pouco esforço de gerenciamento. A associação de ACLs regionais com os estágios da API garante proteção centralizada e eficiente.

- **Por que as outras opções não são adequadas?**  
  - **B:** O AWS Firewall Manager adiciona complexidade adicional e não é necessário para esse caso.  
  - **C e D:** O AWS Shield oferece proteção contra DDoS, mas não é tão eficaz para bloquear injeções de SQL ou XSS como o AWS WAF.

---

### Questão 120
Uma empresa implementou uma solução DNS autogerida em três instâncias Amazon EC2 atrás de um Network Load Balancer (NLB) na região us-west-2. A maioria dos usuários da empresa está localizada nos Estados Unidos e na Europa. A empresa deseja melhorar o desempenho e a disponibilidade da solução. A empresa lança e configura três instâncias EC2 na região eu-west-1 e adiciona as instâncias EC2 como destinos para um novo NLB.  
Qual solução a empresa pode usar para rotear o tráfego para todas as instâncias EC2?

**Resposta correta:**  
**B.** Crie um acelerador padrão no AWS Global Accelerator. Crie grupos de pontos de extremidade em us-west-2 e eu-west-1. Adicione os dois NLBs como pontos de extremidade para os grupos de pontos de extremidade.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Global Accelerator oferece uma solução de roteamento altamente disponível e com baixa latência, além de otimizar o desempenho de tráfego global, tornando os NLBs mais eficientes em várias regiões.

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar uma política de roteamento geográfico do Route 53 e CloudFront é menos eficiente em termos de latência e não oferece a mesma escalabilidade do Global Accelerator.  
  - **C e D:** As opções que envolvem CloudFront ou ALBs não são ideais para esse caso específico de NLB com tráfego global.

---

### Questão 121
Uma empresa está executando uma carga de trabalho de processamento de transações online (OLTP) na AWS. Essa carga de trabalho usa uma instância Amazon RDS DB não criptografada em uma implantação Multi-AZ. Instantâneos diários do banco de dados são feitos dessa instância.  
O que um arquiteto de soluções deve fazer para garantir que o banco de dados e os instantâneos sejam sempre criptografados daqui para frente?

**Resposta correta:**  
**A.** Criptografe uma cópia do último instantâneo do DB. Substitua a instância DB existente restaurando o instantâneo criptografado.

**Justificativa:**  
- **Por que essa opção?**  
  Criar uma cópia criptografada do último instantâneo e restaurá-lo é uma maneira direta e eficiente de garantir que a instância e seus instantâneos futuros sejam criptografados.

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar um volume EBS criptografado e copiar os instantâneos não resolve a criptografia no nível do banco de dados.  
  - **C:** Copiar os instantâneos e habilitar a criptografia com KMS pode ser redundante e envolve etapas adicionais.  
  - **D:** Armazenar os instantâneos no S3 não é a solução ideal para manter a criptografia dos dados de produção.

---

### Questão 122
Uma empresa deseja construir uma infraestrutura escalável de gerenciamento de chaves para apoiar desenvolvedores que precisam criptografar dados em suas aplicações.  
O que um arquiteto de soluções deve fazer para reduzir o ônus operacional?

**Resposta correta:**  
**B.** Use o AWS Key Management Service (AWS KMS) para proteger as chaves de criptografia.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS KMS oferece uma solução totalmente gerenciada, escalável e segura para gerenciamento de chaves, reduzindo significativamente o overhead operacional.

- **Por que as outras opções não são adequadas?**  
  - **A:** O uso de MFA não é necessário para o gerenciamento de chaves de criptografia e não resolve o problema de carga operacional.  
  - **C:** O AWS Certificate Manager não é ideal para a gestão de chaves de criptografia para dados de aplicações.  
  - **D:** O uso de políticas IAM limita o acesso, mas não resolve a questão de gerenciamento escalável de chaves.

---

### Questão 123
Uma empresa tem uma aplicação web dinâmica hospedada em duas instâncias Amazon EC2. A empresa tem seu próprio certificado SSL, que está em cada instância para realizar a terminação SSL.  
Houve um aumento no tráfego recentemente, e a equipe de operações determinou que a criptografia e descriptografia SSL estão causando o limite máximo da capacidade computacional dos servidores web.  
O que um arquiteto de soluções deve fazer para aumentar o desempenho da aplicação?

**Resposta correta:**  
**D.** Importe o certificado SSL para o AWS Certificate Manager (ACM). Crie um Application Load Balancer com um ouvinte HTTPS que use o certificado SSL do ACM.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o ACM para gerenciar o certificado SSL e delegar a terminação SSL para o ALB melhora a escalabilidade e performance, removendo a sobrecarga de SSL nas instâncias EC2.

- **Por que as outras opções não são adequadas?**  
  - **A, B e C:** Essas opções não distribuem a carga de trabalho de SSL de maneira eficiente e não aproveitam a escalabilidade do ALB.

---

### Questão 124
Uma empresa tem um trabalho de processamento em lote altamente dinâmico que usa muitas instâncias Amazon EC2 para completá-lo. O trabalho é sem estado, pode ser iniciado e interrompido a qualquer momento sem impacto negativo, e normalmente leva mais de 60 minutos para ser concluído. A empresa pediu a um arquiteto de soluções para projetar uma solução escalável e custo-efetiva que atenda aos requisitos do trabalho.  
O que o arquiteto de soluções deve recomendar?

**Resposta correta:**  
**A.** Implementar instâncias EC2 Spot.

**Justificativa:**  
- **Por que essa opção?**  
  Instâncias EC2 Spot são ideais para cargas de trabalho em lotes altamente dinâmicas, pois são econômicas e podem ser interrompidas sem impacto significativo, atendendo bem a esse tipo de tarefa.

- **Por que as outras opções não são adequadas?**  
  - **B e C:** Instâncias reservadas ou sob demanda não são tão custo-efetivas quanto as instâncias Spot para esse tipo de carga de trabalho.  
  - **D:** O uso de AWS Lambda não é ideal para trabalhos de processamento em lote de longo prazo.

---

### Questão 125

**Texto original:**  
Uma empresa executa seu site de ecommerce de duas camadas na AWS. A camada web consiste em um balanceador de carga que envia tráfego para instâncias Amazon EC2. A camada de banco de dados usa uma instância Amazon RDS DB. As instâncias EC2 e a instância DB RDS não devem ser expostas à internet pública.  
As instâncias EC2 requerem acesso à internet para concluir o processamento de pagamentos de pedidos por meio de um serviço web de terceiros. A aplicação deve ser altamente disponível.  
Qual combinação de opções de configuração atenderá a esses requisitos? (Escolha duas.)

**Resposta correta:**  
**A.** Use um grupo de Auto Scaling para lançar as instâncias EC2 em sub-redes privadas. Implante uma instância DB Multi-AZ RDS em sub-redes privadas.  
**C.** Use um grupo de Auto Scaling para lançar as instâncias EC2 em sub-redes públicas em duas Zonas de Disponibilidade. Implante uma instância DB RDS Multi-AZ em sub-redes privadas.

**Justificativa:**  
- **Por que essa opção?**  
  A configuração do Auto Scaling e do RDS Multi-AZ em sub-redes privadas proporciona alta disponibilidade e segurança para a aplicação. Instâncias EC2 em sub-redes públicas permitem o acesso à internet para pagamentos.

- **Por que as outras opções não são adequadas?**  
  - **B e D:** A configuração com NAT gateways ou sub-redes públicas adicionais não atende aos requisitos de segurança e disponibilidade da solução.

---

### Questão 126
Um arquiteto de soluções precisa implementar uma solução para reduzir os custos de armazenamento de uma empresa. Todos os dados da empresa estão na classe de armazenamento Amazon S3 Standard. A empresa deve manter todos os dados por pelo menos 25 anos. Os dados dos últimos 2 anos devem ser altamente disponíveis e imediatamente recuperáveis.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Configurar uma política de ciclo de vida do S3 para transitar objetos para o S3 Glacier Deep Archive após 2 anos.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Glacier Deep Archive é a opção mais econômica para armazenamento de longo prazo de dados que precisam ser acessados ocasionalmente.

- **Por que as outras opções não são adequadas?**  
  - **A e D:** O S3 Glacier Deep Archive deve ser usado após os 2 primeiros anos de dados, não imediatamente.  
  - **C:** O S3 Intelligent-Tiering não é ideal para a exigência de longo prazo de 25 anos.

---

### Questão 127
Uma empresa de mídia está avaliando a possibilidade de mover seus sistemas para a AWS Cloud. A empresa precisa de pelo menos 10 TB de armazenamento com o máximo desempenho de I/O possível para processamento de vídeo, 300 TB de armazenamento altamente durável para armazenar conteúdo de mídia, e 900 TB de armazenamento para atender aos requisitos de mídia arquivada que não está mais em uso.  
Qual conjunto de serviços um arquiteto de soluções deve recomendar para atender a esses requisitos?

**Resposta correta:**  
**A.** Amazon EBS para desempenho máximo, Amazon S3 para armazenamento de dados duráveis, e Amazon S3 Glacier para armazenamento arquivado.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon EBS oferece desempenho máximo para I/O, o Amazon S3 é altamente durável e adequado para armazenamento de mídia, enquanto o S3 Glacier oferece uma solução de armazenamento de longo prazo e custo-efetiva para dados arquivados.

- **Por que as outras opções não são adequadas?**  
  - **B e C:** O Amazon EFS e o EC2 Instance Store não são ideais para lidar com o desempenho necessário e o armazenamento de dados arquivados em larga escala.  
  - **D:** O uso de S3 para dados de alta performance não é tão eficiente quanto o uso do EBS para I/O de alto desempenho.

---

### Questão 128
Uma empresa deseja executar aplicações em contêineres na AWS Cloud. Essas aplicações são sem estado e podem tolerar interrupções na infraestrutura subjacente. A empresa precisa de uma solução que minimize os custos e a sobrecarga operacional.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**B.** Usar Spot Instances em um grupo de nós gerenciados do Amazon Elastic Kubernetes Service (Amazon EKS).

**Justificativa:**  
- **Por que essa opção?**  
  Usar Spot Instances no Amazon EKS é uma solução de baixo custo e eficiente, adequada para cargas de trabalho que podem tolerar interrupções.

- **Por que as outras opções não são adequadas?**  
  - **A:** Embora as Spot Instances no EC2 Auto Scaling sejam econômicas, o EKS é uma solução mais gerenciada e eficiente para contêineres.  
  - **C e D:** Instâncias sob demanda não são ideais para minimizar custos quando comparadas às Spot Instances.

---

### Questão 129
Uma empresa está executando uma aplicação web de múltiplas camadas no local. A aplicação web está conteinerizada e roda em diversos hosts Linux conectados a um banco de dados PostgreSQL que contém registros de usuários. O overhead operacional de manter a infraestrutura e o planejamento de capacidade está limitando o crescimento da empresa. Um arquiteto de soluções deve melhorar a infraestrutura da aplicação.  
Qual combinação de ações o arquiteto de soluções deve tomar para alcançar isso? (Escolha duas.)

**Resposta correta:**  
**A.** Migrar o banco de dados PostgreSQL para o Amazon Aurora.  
**E.** Migrar a aplicação web para ser hospedada no AWS Fargate com Amazon Elastic Container Service (Amazon ECS).

**Justificativa:**  
- **Por que essa opção?**  
  Migrar para o Amazon Aurora melhora a escalabilidade e a durabilidade do banco de dados, enquanto o uso do Fargate com ECS oferece uma solução sem servidor para execução de containers, minimizando o overhead operacional.

- **Por que as outras opções não são adequadas?**  
  - **B:** Hospedar a aplicação em instâncias EC2 não resolve o problema de escalabilidade automática.  
  - **C:** O CloudFront não se aplica para lidar com a infraestrutura do banco de dados ou o gerenciamento de containers.  
  - **D:** Usar ElastiCache pode ser útil para melhorar o desempenho, mas não resolve o problema de escalabilidade da infraestrutura principal.

---

### Questão 130
Uma aplicação roda em instâncias Amazon EC2 em várias Zonas de Disponibilidade. As instâncias rodam em um grupo Auto Scaling do Amazon EC2 atrás de um Application Load Balancer. A aplicação tem o melhor desempenho quando a utilização da CPU das instâncias EC2 está em 40% ou perto disso.  
O que um arquiteto de soluções deve fazer para manter o desempenho desejado em todas as instâncias do grupo?

**Resposta correta:**  
**B.** Use uma política de rastreamento de alvo para escalar dinamicamente o grupo Auto Scaling.

**Justificativa:**  
- **Por que essa opção?**  
  A política de rastreamento de alvo ajusta automaticamente o tamanho do grupo Auto Scaling para manter a utilização da CPU perto do valor desejado, garantindo a escalabilidade com base no desempenho.

- **Por que as outras opções não são adequadas?**  
  - **A:** A política de escalonamento simples não é ideal para manter uma utilização precisa da CPU.  
  - **C e D:** Usar Lambda ou escalonamento programado não é necessário para esse caso de uso, onde a resposta dinâmica é necessária.

---

### Questão 131
Uma empresa está desenvolvendo uma aplicação de compartilhamento de arquivos que usará um bucket Amazon S3 para armazenamento. A empresa deseja servir todos os arquivos por meio de uma distribuição do Amazon CloudFront. A empresa não deseja que os arquivos sejam acessíveis por navegação direta na URL do S3.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**D.** Crie uma identidade de acesso de origem (OAI). Atribua o OAI à distribuição do CloudFront. Configure as permissões do bucket S3 para que apenas o OAI tenha permissão de leitura.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o OAI com o CloudFront garante que os arquivos sejam acessados apenas através do CloudFront, evitando o acesso direto ao S3.

- **Por que as outras opções não são adequadas?**  
  - **A e C:** As políticas de bucket S3 e a atribuição do CloudFront não são suficientes para garantir que o acesso direto ao S3 seja evitado.  
  - **B:** A criação de um IAM user não é necessária e pode gerar uma sobrecarga de gerenciamento.

---

### Questão 132
O site de uma empresa fornece aos usuários relatórios históricos de desempenho para download. O site precisa de uma solução que possa escalar para atender às demandas globais do site da empresa. A solução deve ser econômica, limitar o provisionamento de recursos de infraestrutura e fornecer o tempo de resposta mais rápido possível.  
Qual combinação o arquiteto de soluções deve recomendar para atender a esses requisitos?

**Resposta correta:**  
**A.** Amazon CloudFront e Amazon S3

**Justificativa:**  
- **Por que essa opção?**  
  O uso do CloudFront com o S3 oferece escalabilidade global, baixa latência e baixo custo para armazenar e distribuir conteúdo estático como relatórios históricos.

- **Por que as outras opções não são adequadas?**  
  - **B e D:** O uso de Lambda ou balanceadores de carga internos não oferece a mesma escalabilidade e custo-efetividade para um site de download de arquivos estáticos.  
  - **C:** O uso de Auto Scaling do EC2 não é necessário para servir arquivos estáticos como os relatórios.

---

### Questão 134
Uma empresa deseja mover sua aplicação para uma solução serverless. A solução serverless precisa analisar dados existentes e novos usando SL.  
A empresa armazena os dados em um bucket Amazon S3. Os dados requerem criptografia e devem ser replicados para uma região da AWS diferente.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

**Resposta correta:**  
**A.** Crie um novo bucket S3. Carregue os dados no novo bucket S3. Use a replicação entre regiões (CRR) do S3 para replicar objetos criptografados para um bucket S3 em outra região. Use a criptografia do lado do servidor com chaves KMS multi-região (SSE-KMS). Use o Amazon Athena para consultar os dados.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o CRR para replicar os dados entre regiões e o SSE-KMS para criptografar os dados é uma solução escalável e de baixo overhead. O Amazon Athena oferece consulta de dados sem a necessidade de gerenciar infraestrutura.

- **Por que as outras opções não são adequadas?**  
  - **B:** O uso do Amazon RDS não é necessário para dados armazenados em S3 e seria mais complexo.  
  - **C e D:** Usar SSE-S3 e RDS não minimiza tanto o overhead quanto a opção que usa Athena e SSE-KMS com CRR.

---

### Questão 135
Uma empresa executa cargas de trabalho na AWS. A empresa precisa se conectar a um serviço de um provedor externo. O serviço está hospedado no VPC do provedor. De acordo com a equipe de segurança da empresa, a conectividade deve ser privada e restrita ao serviço de destino. A conexão deve ser iniciada apenas do VPC da empresa.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**D.** Peça ao provedor para criar um endpoint VPC para o serviço de destino. Use o AWS PrivateLink para se conectar ao serviço de destino.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS PrivateLink fornece uma maneira segura e privada de acessar serviços em uma VPC de um provedor, sem expor o tráfego à internet.

- **Por que as outras opções não são adequadas?**  
  - **A:** VPC peering não é ideal para restringir o tráfego apenas ao serviço de destino.  
  - **B:** Criar um gateway privado virtual é desnecessário e mais complexo.  
  - **C:** Usar um NAT gateway expõe o tráfego à internet, o que não atende ao requisito de privacidade.

---

### Questão 136
Uma empresa está migrando seu banco de dados PostgreSQL local para o Amazon Aurora PostgreSQL. O banco de dados local deve permanecer online e acessível durante a migração. O banco de dados Aurora deve permanecer sincronizado com o banco de dados local.  
Qual combinação de ações um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)

**Resposta correta:**  
**A.** Crie uma tarefa de replicação contínua.  
**C.** Crie um servidor de replicação do AWS Database Migration Service (AWS DMS).

**Justificativa:**  
- **Por que essa opção?**  
  A replicação contínua do AWS DMS permite a migração em tempo real, garantindo que o Aurora e o banco de dados local permaneçam sincronizados.

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar um backup do banco de dados local não garante a sincronização em tempo real.  
  - **D:** Usar o AWS SCT é necessário para conversão de esquema, mas não para a replicação em tempo real.  
  - **E:** Criar uma regra do EventBridge não é necessária para a sincronização contínua do banco de dados.

---

### Questão 137
Uma empresa usa o AWS Organizations para criar contas dedicadas AWS para cada unidade de negócios, para gerenciar as contas de cada unidade de negócios de forma independente, conforme solicitado. O destinatário do e-mail da raiz perdeu uma notificação enviada para o endereço de e-mail do usuário root de uma conta. A empresa quer garantir que todas as futuras notificações não sejam perdidas. As futuras notificações devem ser limitadas aos administradores da conta.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Configure todos os endereços de e-mail do usuário root das contas AWS como listas de distribuição que encaminham para alguns administradores que podem responder aos alertas. Configure os contatos alternativos da conta AWS no console do AWS Organizations ou programaticamente.

**Justificativa:**  
- **Por que essa opção?**  
  Usar listas de distribuição e configurar contatos alternativos garante que as notificações sejam encaminhadas para os administradores sem sobrecarregar o usuário root.

- **Por que as outras opções não são adequadas?**  
  - **A:** O encaminhamento manual de e-mails pode ser ineficaz e propenso a erros.  
  - **C:** Enviar notificações para um único administrador limita a capacidade de resposta e não é tão eficiente quanto usar uma lista de distribuição.  
  - **D:** Usar o mesmo endereço de e-mail para todas as contas pode não ser prático e dificulta a organização.

---
### Questão 138
Uma empresa executa sua aplicação de comércio eletrônico na AWS. Cada novo pedido é publicado como uma mensagem em uma fila RabbitMQ que é executada em uma instância EC2 em uma única Zona de Disponibilidade. Essas mensagens são processadas por outra aplicação que roda em uma instância EC2 separada. Esta aplicação armazena os detalhes em um banco de dados PostgreSQL em outra instância EC2. Todas as instâncias EC2 estão na mesma Zona de Disponibilidade.  
A empresa precisa redesenhar sua arquitetura para fornecer a maior disponibilidade com o menor esforço operacional.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**B.** Migrar a fila para um par redundante (ativo/standby) de instâncias RabbitMQ no Amazon MQ. Criar um grupo de Auto Scaling Multi-AZ para as instâncias EC2 que hospedam a aplicação. Migrar o banco de dados para uma implantação Multi-AZ do Amazon RDS para PostgreSQL.

**Justificativa:**  
- **Por que essa opção?**  
  A alternativa B fornece alta disponibilidade para a fila RabbitMQ e o banco de dados PostgreSQL, utilizando soluções gerenciadas como o Amazon MQ e o RDS. Isso reduz o esforço operacional e fornece failover automático em caso de falhas na Zona de Disponibilidade.

- **Por que as outras opções não são adequadas?**  
  - **A:** Não utiliza o Amazon RDS, exigindo mais esforço operacional para gerenciar o banco de dados no EC2.  
  - **C:** Manter RabbitMQ no EC2 aumenta a carga de gerenciamento, enquanto o Amazon MQ oferece alta disponibilidade com menos esforço.  
  - **D:** Criar três grupos de Auto Scaling aumenta a complexidade e os custos sem fornecer benefícios adicionais significativos.

### Questão 139
Uma equipe de relatórios recebe arquivos diariamente em um bucket do Amazon S3. A equipe analisa e copia manualmente os arquivos desse bucket inicial para um bucket de análise do S3 todos os dias no mesmo horário para uso com o Amazon QuickSight. Outras equipes estão começando a enviar mais arquivos, em tamanhos maiores, para o bucket inicial do S3.  
A equipe de relatórios quer mover automaticamente os arquivos para o bucket de análise assim que forem enviados ao bucket inicial. Além disso, quer usar funções AWS Lambda para executar código de correspondência de padrões nos dados copiados. A equipe também deseja enviar os arquivos de dados para um pipeline no Amazon SageMaker Pipelines.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos com o MENOR esforço operacional?

**Resposta correta:**  
**C.** Configure a replicação do S3 entre os buckets do S3. Crie uma notificação de evento S3 para o bucket de análise. Configure o Lambda e o SageMaker Pipelines como destinos da notificação de evento. Configure o tipo de evento como `s3:ObjectCreated:Put`.

**Justificativa:**  
- **Por que essa opção?**  
  Usar a replicação do S3 automatiza a movimentação de arquivos entre os buckets sem a necessidade de manutenção manual ou código adicional. As notificações de eventos do S3 são integradas ao Lambda e ao SageMaker Pipelines para processar os dados conforme necessário, reduzindo o esforço operacional.

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar o Lambda diretamente para copiar arquivos adiciona complexidade e esforço operacional desnecessário.  
  - **B:** Utilizar o Amazon EventBridge para configurar notificações não é tão eficiente quanto usar notificações nativas do S3.  
  - **D:** Configurar replicação do S3 e EventBridge adiciona redundância desnecessária e aumenta a complexidade sem benefícios claros.

### Questão 139
Uma equipe de relatórios recebe arquivos diariamente em um bucket do Amazon S3. A equipe analisa e copia manualmente os arquivos desse bucket inicial para um bucket de análise do S3 todos os dias no mesmo horário para uso com o Amazon QuickSight. Outras equipes estão começando a enviar mais arquivos, em tamanhos maiores, para o bucket inicial do S3.  
A equipe de relatórios quer mover automaticamente os arquivos para o bucket de análise assim que forem enviados ao bucket inicial. Além disso, quer usar funções AWS Lambda para executar código de correspondência de padrões nos dados copiados. A equipe também deseja enviar os arquivos de dados para um pipeline no Amazon SageMaker Pipelines.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos com o MENOR esforço operacional?

**Resposta correta:**  
**C.** Configure a replicação do S3 entre os buckets do S3. Crie uma notificação de evento S3 para o bucket de análise. Configure o Lambda e o SageMaker Pipelines como destinos da notificação de evento. Configure o tipo de evento como `s3:ObjectCreated:Put`.

**Justificativa:**  
- **Por que essa opção?**  
  Usar a replicação do S3 automatiza a movimentação de arquivos entre os buckets sem a necessidade de manutenção manual ou código adicional. As notificações de eventos do S3 são integradas ao Lambda e ao SageMaker Pipelines para processar os dados conforme necessário, reduzindo o esforço operacional.

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar o Lambda diretamente para copiar arquivos adiciona complexidade e esforço operacional desnecessário.  
  - **B:** Utilizar o Amazon EventBridge para configurar notificações não é tão eficiente quanto usar notificações nativas do S3.  
  - **D:** Configurar replicação do S3 e EventBridge adiciona redundância desnecessária e aumenta a complexidade sem benefícios claros.

### Questão 140
Um arquiteto de soluções precisa ajudar uma empresa a otimizar o custo de execução de uma aplicação na AWS. A aplicação usará instâncias Amazon EC2, AWS Fargate e AWS Lambda para computação na arquitetura.  
As instâncias EC2 executarão a camada de ingestão de dados da aplicação. O uso do EC2 será esporádico e imprevisível. As cargas de trabalho que rodam nas instâncias EC2 podem ser interrompidas a qualquer momento. A interface da aplicação será executada no Fargate, e o Lambda servirá como camada de API. O uso da interface e da camada de API será previsível ao longo do próximo ano.  
Quais combinações de opções de compra fornecerão a solução MAIS econômica para hospedar essa aplicação? (Escolha duas.)

**Resposta correta:**  
**A.** Use Spot Instances para a camada de ingestão de dados.  
**C.** Compre um Compute Savings Plan de 1 ano para a interface e a camada de API.

**Justificativa:**  
- **Por que essas opções?**  
  - Spot Instances oferecem preços reduzidos para cargas de trabalho que podem ser interrompidas.  
  - Um Savings Plan para computação proporciona economia garantida para cargas previsíveis em Fargate e Lambda.

- **Por que as outras opções não são adequadas?**  
  - **B:** Usar On-Demand para a camada de ingestão de dados não é econômico.  
  - **D:** Reservar instâncias para uso esporádico e imprevisível aumenta custos desnecessariamente.  
  - **E:** Savings Plan para EC2 não se aplica diretamente a Fargate e Lambda.

---

### Questão 141
Uma empresa opera um portal baseado na web que fornece aos usuários notícias globais de última hora, alertas locais e atualizações meteorológicas. O portal entrega uma visão personalizada para cada usuário usando uma mistura de conteúdo estático e dinâmico. O conteúdo é servido via HTTPS por meio de um servidor de API rodando em uma instância Amazon EC2 atrás de um Application Load Balancer (ALB). A empresa quer fornecer esse conteúdo aos seus usuários em todo o mundo da maneira mais rápida possível.  
Como um arquiteto de soluções deve projetar a aplicação para garantir a MENOR latência para todos os usuários?

**Resposta correta:**  
**A.** Implante a pilha de aplicativos em uma única região da AWS. Use o Amazon CloudFront para servir todo o conteúdo estático e dinâmico especificando o ALB como uma origem.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon CloudFront reduz a latência globalmente, armazenando em cache o conteúdo próximo aos usuários.

- **Por que as outras opções não são adequadas?**  
  - **B:** Implantar em várias regiões aumenta custos e complexidade.  
  - **C:** Não utiliza o cache para conteúdo dinâmico, aumentando a latência.  
  - **D:** Geolocalização não resolve problemas de latência para conteúdo global.

---

### Questão 142

**Texto original:**  
Uma empresa de jogos está projetando uma arquitetura altamente disponível. A aplicação roda em um kernel Linux modificado e suporta apenas tráfego baseado em UDP. A empresa precisa que a camada de front-end forneça a melhor experiência possível ao usuário. Essa camada deve ter baixa latência, rotear tráfego para o local de borda mais próximo e fornecer endereços IP estáticos para entrada nos endpoints da aplicação.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**C.** Configure o AWS Global Accelerator para encaminhar solicitações para um Network Load Balancer. Use instâncias Amazon EC2 para a aplicação em um Auto Scaling group.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Global Accelerator fornece baixa latência, roteamento geográfico e endereços IP estáticos, enquanto o NLB suporta tráfego UDP.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Não oferecem suporte completo para tráfego UDP com baixa latência global e IPs estáticos.

---

### Questão 143
Uma empresa quer migrar sua aplicação monolítica on-premises para a AWS. A empresa quer manter o máximo possível do código front-end e back-end. No entanto, a empresa quer dividir a aplicação em aplicações menores. Equipes diferentes irão gerenciar cada aplicação. A empresa precisa de uma solução altamente escalável que minimize o esforço operacional.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**D.** Hospede a aplicação no Amazon Elastic Container Service (Amazon ECS). Configure um Application Load Balancer com o ECS como destino.

**Justificativa:**  
- **Por que essa opção?**  
  O ECS permite gerenciar contêineres de forma eficiente, com separação de responsabilidades e escalabilidade integrada.

- **Por que as outras opções não são adequadas?**  
  - **A/B:** Amplify e Lambda não mantêm o backend existente.  
  - **C:** EC2 sozinho não oferece gerenciamento eficiente de aplicações segmentadas.

---

### Questão 144
Uma empresa começou recentemente a usar o Amazon Aurora como armazenamento de dados para sua aplicação global de comércio eletrônico. Quando relatórios grandes são executados, os desenvolvedores relatam que a aplicação apresenta baixo desempenho. Após revisar métricas no Amazon CloudWatch, um arquiteto de soluções identifica picos nas métricas de ReadIOPS e CPUUtilization durante a execução dos relatórios mensais.  
Qual é a solução MAIS econômica?

**Resposta correta:**  
**B.** Migre a execução de relatórios mensais para uma réplica do Aurora.

**Justificativa:**  
- **Por que essa opção?**  
  Uma réplica do Aurora alivia a carga no banco de dados principal, mantendo os custos baixos e sem impactar as operações normais.

- **Por que as outras opções não são adequadas?**  
  - **A:** Migrar para o Amazon Redshift é mais caro e complexo.  
  - **C:** Alterar para uma instância maior aumenta custos.  
  - **D:** Incrementar IOPS provisionados pode ser desnecessariamente caro.

---

### Questão 145
Uma empresa hospeda uma aplicação de análise de sites em uma única instância Amazon EC2 On-Demand. O software de análise é escrito em PHP e utiliza um banco de dados MySQL. O software de análise, o servidor web que fornece o PHP e o banco de dados estão todos hospedados na instância EC2. A aplicação apresenta sinais de degradação de desempenho em momentos de pico e erros 5xx. A empresa precisa que a aplicação escale de forma transparente.  
Qual solução atenderá a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**A.** Migre o banco de dados para uma instância Amazon RDS para MySQL. Crie uma AMI da aplicação web. Use a AMI para lançar uma segunda instância EC2. Use um Application Load Balancer para distribuir a carga entre as instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  Separar o banco de dados em uma instância RDS e distribuir a carga entre instâncias EC2 melhora a escalabilidade e desempenho com custos otimizados.

- **Por que as outras opções não são adequadas?**  
  - **B:** Route 53 não gerencia balanceamento de carga de maneira eficiente.  
  - **C:** Alterar o tipo de instância não resolve o problema de escalabilidade.  
  - **D:** Utilizar Spot Fleet pode ser complexo e não é ideal para cargas sensíveis.

---

### Questão 146
Uma empresa executa uma aplicação web stateless em produção em um grupo de instâncias Amazon EC2 On-Demand atrás de um Application Load Balancer. A aplicação experimenta uso intenso durante um período de 8 horas em dias úteis. O uso da aplicação é moderado e estável durante a noite, e baixo nos fins de semana.  
A empresa quer minimizar os custos do EC2 sem afetar a disponibilidade da aplicação.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Use Reserved Instances para o nível base de uso. Use Spot Instances para qualquer capacidade adicional que a aplicação precisar.

**Justificativa:**  
- **Por que essa opção?**  
  Reservar instâncias para o uso consistente reduz custos fixos, enquanto Spot Instances oferecem economia adicional para picos.

- **Por que as outras opções não são adequadas?**  
  - **A:** Spot Instances exclusivamente não garantem disponibilidade.  
  - **C:** On-Demand para carga base é mais caro.  
  - **D:** Dedicated Instances são desnecessárias para essa aplicação.

---

### Questão 147
Uma empresa precisa reter arquivos de log de uma aplicação crítica por 10 anos. A equipe de aplicação acessa regularmente logs do último mês para solução de problemas, mas logs mais antigos raramente são acessados. A aplicação gera mais de 10 TB de logs por mês.  
Qual opção de armazenamento atende a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**B.** Armazene os logs no Amazon S3. Use políticas do ciclo de vida do S3 para mover logs com mais de 1 mês para o S3 Glacier Deep Archive.

**Justificativa:**  
- **Por que essa opção?**  
  Políticas do ciclo de vida reduzem custos transferindo logs raramente acessados para um armazenamento mais barato, mantendo os acessados recentes no S3 Standard.

- **Por que as outras opções não são adequadas?**  
  - **A:** AWS Backup adiciona complexidade desnecessária.  
  - **C/D:** CloudWatch Logs é mais caro e inadequado para retenção de longo prazo.

---

### Questão 148
Uma empresa possui um fluxo de ingestão de dados com os seguintes componentes:  
- Um tópico Amazon SNS que recebe notificações sobre novas entregas de dados.  
- Uma função AWS Lambda que processa e armazena os dados.  
O fluxo de ingestão ocasionalmente falha devido a problemas de conectividade de rede. Quando ocorre falha, os dados correspondentes não são ingeridos, a menos que a empresa reexecute o trabalho manualmente.  
O que um arquiteto de soluções deve fazer para garantir que todas as notificações sejam eventualmente processadas?

**Resposta correta:**  
**D.** Configure uma fila Amazon SQS como destino em caso de falha. Modifique a função Lambda para processar mensagens na fila.

**Justificativa:**  
- **Por que essa opção?**  
  O SQS armazena mensagens em caso de falha, garantindo reprocessamento automático sem intervenção manual.

- **Por que as outras opções não são adequadas?**  
  - **A/B:** Melhorar o Lambda ou conectividade não resolve problemas de entrega confiável.  
  - **C:** Retries do SNS sozinho não garantem reprocessamento em falhas prolongadas.

---

### Questão 149
Uma empresa possui um serviço que produz dados de eventos. A empresa quer usar a AWS para processar os dados de eventos conforme são recebidos. Os dados são gravados em uma ordem específica que deve ser mantida durante o processamento. A empresa quer implementar uma solução que minimize o esforço operacional.  
Como um arquiteto de soluções deve fazer isso?

**Resposta correta:**  
**A.** Crie uma fila Amazon SQS FIFO para armazenar mensagens. Configure uma função AWS Lambda para processar as mensagens na fila.

**Justificativa:**  
- **Por que essa opção?**  
  O SQS FIFO garante ordem de processamento e o Lambda reduz a sobrecarga operacional.

- **Por que as outras opções não são adequadas?**  
  - **B/D:** O SNS não mantém ordem de mensagens.  
  - **C:** Fila padrão do SQS não mantém a ordem necessária.

### Questão 150
Uma empresa está migrando uma aplicação de servidores on-premises para instâncias Amazon EC2. Como parte dos requisitos de design da migração, um arquiteto de soluções deve implementar alarmes de métricas de infraestrutura. A empresa não precisa agir se a utilização de CPU aumentar para mais de 50% por um curto período. No entanto, se a utilização de CPU aumentar para mais de 50% e os IOPS de leitura no disco também forem altos, a empresa precisa agir imediatamente. O arquiteto também deve reduzir alarmes falsos.  
O que o arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**A.** Crie alarmes compostos do Amazon CloudWatch sempre que possível.

**Justificativa:**  
- **Por que essa opção?**  
  Os alarmes compostos permitem combinar várias condições e reduzir alarmes falsos ao acionar ações apenas quando múltiplas condições são atendidas.

- **Por que as outras opções não são adequadas?**  
  - **B:** Dashboards apenas fornecem visualização, sem acionar ações.  
  - **C:** Canários do CloudWatch Synthetics não atendem ao requisito de métricas específicas.  
  - **D:** Alarmes individuais com múltiplos limites não oferecem controle granular suficiente.

---

### Questão 151
Uma empresa quer migrar seu data center on-premises para a AWS. De acordo com os requisitos de conformidade da empresa, ela pode usar apenas a região ap-northeast-3. Os administradores da empresa não têm permissão para conectar VPCs à internet.  
Quais soluções atenderão a esses requisitos? (Escolha duas.)

**Resposta correta:**  
**A.** Use o AWS Control Tower para implementar políticas de residência de dados que neguem acesso à internet e a todas as regiões AWS, exceto ap-northeast-3.  
**C.** Use o AWS Organizations para configurar políticas de controle de serviço (SCPs) que impeçam as VPCs de obter acesso à internet e neguem acesso a todas as regiões, exceto ap-northeast-3.

**Justificativa:**  
- **Por que essas opções?**  
  - Ambas oferecem controle centralizado para negar acesso não permitido à internet e restringir o uso de regiões AWS.

- **Por que as outras opções não são adequadas?**  
  - **B/D/E:** Soluções alternativas como regras de ACL ou AWS Config são insuficientes para implementar restrições completas e centralizadas.

---

### Questão 152
Uma empresa usa uma aplicação web de três camadas para fornecer treinamento a novos funcionários. A aplicação é acessada apenas 12 horas por dia. A empresa está usando uma instância Amazon RDS para MySQL para armazenar informações e quer minimizar os custos.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

**Resposta correta:**  
**D.** Crie funções AWS Lambda para iniciar e parar a instância do banco de dados. Crie regras agendadas no Amazon EventBridge para acionar as funções Lambda.

**Justificativa:**  
- **Por que essa opção?**  
  Permitir que o banco de dados seja interrompido fora do horário de uso reduz significativamente os custos.

- **Por que as outras opções não são adequadas?**  
  - **A/B/C:** Soluções mais complexas ou caras para um problema simples de agendamento.

---

### Questão 153
Uma empresa vende toques criados a partir de trechos de músicas populares. Os arquivos contendo os toques estão armazenados no Amazon S3 Standard e têm pelo menos 128 KB de tamanho. A empresa tem milhões de arquivos, mas downloads são raros para toques com mais de 90 dias. A empresa precisa economizar no armazenamento enquanto mantém os arquivos mais acessados disponíveis para seus usuários.  
Qual ação a empresa deve tomar para atender a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**D.** Implemente uma política do ciclo de vida do S3 que mova os objetos do S3 Standard para S3 Standard-Infrequent Access (S3 Standard-IA) após 90 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Standard-IA reduz custos para arquivos raramente acessados, mantendo acesso rápido quando necessário.

- **Por que as outras opções não são adequadas?**  
  - **A/B/C:** Outras soluções são mais caras ou inadequadas para arquivos com uso infrequente.

---

### Questão 154
Uma empresa precisa salvar os resultados de um teste médico em um repositório Amazon S3. O repositório deve permitir que alguns cientistas adicionem novos arquivos e restringir todos os outros usuários ao acesso somente leitura. Nenhum usuário deve ter a capacidade de modificar ou excluir arquivos no repositório. A empresa deve manter cada arquivo no repositório por pelo menos 1 ano após sua criação.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Use o S3 Object Lock no modo de conformidade com um período de retenção de 365 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Object Lock no modo de conformidade impede alterações ou exclusões de arquivos, atendendo aos requisitos de retenção.

- **Por que as outras opções não são adequadas?**  
  - **A/C/D:** Não fornecem proteção contra exclusão ou não atendem ao requisito de retenção mínima.

---

### Questão 155
Uma grande empresa de mídia hospeda uma aplicação web na AWS. A empresa quer começar a armazenar em cache arquivos de mídia confidenciais para que usuários ao redor do mundo tenham acesso confiável aos arquivos. O conteúdo está armazenado em buckets do Amazon S3. A empresa deve entregar o conteúdo rapidamente, independentemente de onde as solicitações se originem geograficamente.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**C.** Implante o Amazon CloudFront para conectar os buckets S3 aos servidores de borda do CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront reduz a latência ao armazenar em cache o conteúdo em locais de borda globais.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Não oferecem caching global eficiente e seguro para mídia armazenada no S3.

### Questão 156
Uma empresa produz dados em lote de diferentes bancos de dados. A empresa também produz dados de streaming ao vivo de sensores de rede e APIs de aplicações. A empresa precisa consolidar todos os dados em um único local para análises empresariais. A empresa precisa processar os dados recebidos e então organizá-los em diferentes buckets do Amazon S3. As equipes posteriormente executarão consultas pontuais e importarão os dados para uma ferramenta de inteligência empresarial para exibir indicadores-chave de desempenho (KPIs).  
Quais combinações de etapas atenderão a esses requisitos com o MENOR esforço operacional? (Escolha duas.)

**Resposta correta:**  
**A.** Use o Amazon Athena para consultas pontuais. Use o Amazon QuickSight para criar painéis para os KPIs.  
**E.** Use modelos no AWS Lake Formation para identificar os dados que podem ser ingeridos em um data lake. Use o AWS Glue para rastrear as fontes, extrair os dados e carregá-los no Amazon S3 no formato Apache Parquet.

**Justificativa:**  
- **Por que essas opções?**  
  - Athena e QuickSight oferecem consultas ad hoc e visualizações com baixa sobrecarga operacional.  
  - O Lake Formation e o Glue automatizam a ingestão e organização de dados no S3.

- **Por que as outras opções não são adequadas?**  
  - **B:** Kinesis Data Analytics não é necessário para consultas pontuais.  
  - **C/D:** Soluções mais complexas e inadequadas para o objetivo descrito.

---

### Questão 157
Uma empresa armazena dados em um cluster Amazon Aurora PostgreSQL. A empresa deve armazenar todos os dados por 5 anos e excluí-los após esse período. A empresa também deve manter indefinidamente logs de auditoria de ações realizadas no banco de dados. Atualmente, a empresa possui backups automáticos configurados para o Aurora.  
Quais combinações de etapas um arquiteto de soluções deve realizar para atender a esses requisitos? (Escolha duas.)

**Resposta correta:**  
**D.** Configure a exportação de logs do Amazon CloudWatch Logs para o cluster do banco de dados.  
**E.** Use o AWS Backup para fazer backups e mantê-los por 5 anos.

**Justificativa:**  
- **Por que essas opções?**  
  - Exportar logs para o CloudWatch Logs atende ao requisito de retenção indefinida de logs de auditoria.  
  - O AWS Backup gerencia backups com políticas de retenção de longo prazo.

- **Por que as outras opções não são adequadas?**  
  - **A/B/C:** Não atendem aos requisitos específicos de retenção e exclusão de dados.

---

### Questão 158
Um arquiteto de soluções está otimizando um site para um evento musical que se aproxima. Vídeos das apresentações serão transmitidos em tempo real e, posteriormente, estarão disponíveis sob demanda. Espera-se que o evento atraia um público global online.  
Qual serviço melhorará o desempenho tanto do streaming em tempo real quanto sob demanda?

**Resposta correta:**  
**A.** Amazon CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront reduz a latência para streaming globalmente, tanto ao vivo quanto sob demanda, utilizando servidores de borda.

- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Não oferecem suporte completo para otimização de streaming em tempo real e sob demanda.

---

### Questão 159
Uma empresa está executando uma aplicação serverless publicamente acessível que usa o Amazon API Gateway e o AWS Lambda. O tráfego da aplicação recentemente disparou devido a solicitações fraudulentas de botnets.  
Quais etapas um arquiteto de soluções deve realizar para bloquear solicitações de usuários não autorizados? (Escolha duas.)

**Resposta correta:**  
**A.** Crie um plano de uso com uma chave de API compartilhada apenas com usuários legítimos.  
**C.** Implemente uma regra do AWS WAF para direcionar solicitações maliciosas e acionar ações para filtrá-las.

**Justificativa:**  
- **Por que essas opções?**  
  - O plano de uso limita o acesso a usuários legítimos.  
  - O WAF detecta e bloqueia solicitações maliciosas automaticamente.

- **Por que as outras opções não são adequadas?**  
  - **B:** Adicionar lógica no Lambda não é eficiente para lidar com grande volume de solicitações.  
  - **D/E:** Alternativas menos robustas para mitigação de tráfego malicioso.

---

### Questão 160
Uma empresa de comércio eletrônico hospeda sua aplicação de análise na nuvem AWS. A aplicação gera cerca de 300 MB de dados por mês. Os dados são armazenados no formato JSON. A empresa está avaliando uma solução de recuperação de desastres para fazer backup dos dados. Os dados devem ser acessíveis em milissegundos, se necessário, e devem ser mantidos por 30 dias.  
Qual solução atende a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**C.** Amazon S3 Standard.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Standard oferece acesso rápido em milissegundos, com custos adequados para dados com retenção de curto prazo.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Alternativas mais caras ou inadequadas para os requisitos de acesso e retenção.

### Questão 161
Uma empresa tem uma pequena aplicação em Python que processa documentos JSON e envia os resultados para um banco de dados SQL on-premises. A aplicação é executada milhares de vezes por dia. A empresa quer migrar a aplicação para a nuvem AWS. A empresa precisa de uma solução altamente disponível que maximize a escalabilidade e minimize o esforço operacional.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**B.** Coloque os documentos JSON em um bucket Amazon S3. Crie uma função AWS Lambda que execute o código Python para processar os documentos ao serem enviados ao bucket S3. Armazene os resultados em um cluster Amazon Aurora DB.

**Justificativa:**  
- **Por que essa opção?**  
  O Lambda oferece escalabilidade automática, enquanto o Aurora gerencia a alta disponibilidade do banco de dados.

- **Por que as outras opções não são adequadas?**  
  - **A/C/D:** Requerem mais gerenciamento operacional e não oferecem a mesma escalabilidade ou simplicidade.

---

### Questão 162
Uma empresa quer usar infraestrutura de computação de alto desempenho (HPC) na AWS para modelagem de risco financeiro. As cargas de trabalho HPC da empresa rodam no Linux. Cada fluxo de trabalho HPC executa centenas de instâncias Spot do Amazon EC2, é de curta duração e gera milhares de arquivos de saída que são armazenados em um armazenamento persistente para análises e uso futuro a longo prazo.  
Qual combinação de serviços AWS atende a esses requisitos?

**Resposta correta:**  
**A.** Amazon FSx for Lustre integrado ao Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  FSx for Lustre é ideal para cargas de trabalho HPC, enquanto o S3 oferece armazenamento persistente e escalável.

- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Não fornecem desempenho ou escalabilidade suficientes para cargas HPC.

---

### Questão 163
Uma empresa está construindo uma aplicação conteinerizada on-premises e decide migrar a aplicação para a AWS. A aplicação terá milhares de usuários logo após ser implantada. A empresa não tem certeza de como gerenciar a implantação de contêineres em escala.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**A.** Armazene as imagens de contêiner no Amazon Elastic Container Registry (ECR). Use um cluster Amazon ECS com o tipo de inicialização AWS Fargate para executar os contêineres. Use rastreamento de destino para escalar automaticamente com base na demanda.

**Justificativa:**  
- **Por que essa opção?**  
  O Fargate elimina a necessidade de gerenciar servidores, permitindo escalabilidade automática com baixa sobrecarga operacional.

- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Requerem mais gerenciamento ou não oferecem escalabilidade integrada.

---

### Questão 164
Uma empresa tem duas aplicações: uma aplicação remetente que envia mensagens com cargas úteis para serem processadas e uma aplicação de processamento destinada a receber as mensagens. A empresa quer implementar um serviço AWS para gerenciar as mensagens entre as duas aplicações.  
Qual solução atende a esses requisitos e é a MAIS eficiente operacionalmente?

**Resposta correta:**  
**C.** Integre as aplicações com uma fila do Amazon SQS. Configure uma fila de mensagens descartadas (dead-letter queue) para coletar mensagens que falharam no processamento.

**Justificativa:**  
- **Por que essa opção?**  
  O SQS fornece uma solução gerenciada para comunicação assíncrona com suporte integrado para filas de mensagens descartadas.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Soluções mais complexas ou inadequadas para processamento confiável e eficiente.

---

### Questão 165
Um arquiteto de soluções deve projetar uma solução que use o Amazon CloudFront com um bucket Amazon S3 como origem para armazenar um site estático. A política de segurança da empresa exige que todo o tráfego do site seja inspecionado pelo AWS WAF.  
Como o arquiteto de soluções deve cumprir esses requisitos?

**Resposta correta:**  
**D.** Configure o Amazon CloudFront e o Amazon S3 para usar uma identidade de acesso de origem (OAI) para restringir o acesso ao bucket S3. Habilite o AWS WAF na distribuição CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O WAF integrado ao CloudFront inspeciona todo o tráfego antes que ele alcance o S3, enquanto a OAI garante acesso seguro.

- **Por que as outras opções não são adequadas?**  
  - **A/B/C:** Não oferecem a mesma segurança integrada e controle de acesso.

### Questão 166
Organizadores de um evento global querem colocar relatórios diários online como páginas HTML estáticas. Espera-se que as páginas gerem milhões de visualizações de usuários em todo o mundo. Os arquivos estão armazenados em um bucket Amazon S3. Um arquiteto de soluções foi solicitado para projetar uma solução eficiente e eficaz.  
Qual ação o arquiteto de soluções deve tomar para realizar isso?

**Resposta correta:**  
**D.** Use Amazon CloudFront with the S3 bucket as its origin.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront oferece caching global, reduzindo a latência para usuários em diferentes localidades e melhorando o desempenho para acessos de alta escala.

- **Por que as outras opções não são adequadas?**  
  - **A:** Presigned URLs não são escaláveis para alto tráfego.  
  - **B:** Replicação cross-region adiciona custos desnecessários.  
  - **C:** A geoproximidade do Route 53 não é suficiente para otimizar o desempenho global.

---

### Questão 167
Uma empresa executa uma aplicação de produção em um conjunto de instâncias Amazon EC2. A aplicação lê os dados de uma fila Amazon SQS e processa as mensagens em paralelo. O volume de mensagens é imprevisível e frequentemente apresenta tráfego intermitente. Esta aplicação deve processar mensagens continuamente sem tempo de inatividade.  
Qual solução atende a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**C.** Use Reserved Instances for the baseline capacity and use Spot Instances to handle additional capacity.

**Justificativa:**  
- **Por que essa opção?**  
  Usar Reserved Instances para capacidade básica reduz custos fixos, enquanto Spot Instances gerenciam picos de demanda de forma econômica.

- **Por que as outras opções não são adequadas?**  
  - **A/B:** Usar apenas Spot ou Reserved Instances não é eficiente para tráfego imprevisível.  
  - **D:** On-Demand Instances aumentam significativamente os custos.

---

### Questão 168
Uma equipe de segurança quer limitar o acesso a serviços ou ações específicas em todas as contas da equipe na AWS. Todas as contas pertencem a uma organização grande no AWS Organizations. A solução deve ser escalável e ter um único ponto onde as permissões possam ser mantidas.  
O que um arquiteto de soluções deve fazer para realizar isso?

**Resposta correta:**  
**D.** Create a service control policy in the root organizational unit to deny access to the services or actions.

**Justificativa:**  
- **Por que essa opção?**  
  As políticas de controle de serviço (SCPs) no AWS Organizations oferecem um ponto central para gerenciar permissões em contas.

- **Por que as outras opções não são adequadas?**  
  - **A/B:** ACLs e security groups não gerenciam permissões organizacionais.  
  - **C:** Cross-account roles não fornecem controle centralizado.

---

### Questão 169
Uma empresa está preocupada com a segurança de sua aplicação web pública devido a recentes ataques na web. A aplicação usa um Application Load Balancer (ALB). Um arquiteto de soluções deve reduzir o risco de ataques DDoS contra a aplicação.  
O que o arquiteto de soluções deve fazer para atender a esse requisito?

**Resposta correta:**  
**C.** Enable AWS Shield Advanced to prevent attacks.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Shield Advanced fornece proteção contra DDoS com suporte integrado e resposta automática a ataques.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Macie e GuardDuty não fornecem proteção direta contra DDoS.

---

### Questão 170
Uma aplicação web de uma empresa está rodando em instâncias Amazon EC2 atrás de um Application Load Balancer. A empresa recentemente alterou sua política, que agora exige que a aplicação seja acessada apenas de um país específico.  
Qual configuração atenderá a esse requisito?

**Resposta correta:**  
**C.** Configure AWS WAF on the Application Load Balancer in a VPC.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS WAF permite criar regras geográficas para restringir o acesso ao ALB com base na origem dos usuários.

- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Security groups e NACLs não oferecem regras de geolocalização.

---

### Question #171
Uma empresa fornece uma API para seus usuários que automatiza consultas para cálculos de impostos com base nos preços dos itens. Durante a temporada de férias, a empresa experimenta um aumento no número de consultas, resultando em tempos de resposta mais lentos. Um arquiteto de soluções precisa projetar uma solução escalável e elástica.  
O que o arquiteto de soluções deve fazer para atingir esse objetivo?

**Resposta correta:**  
**B.** Design a REST API using Amazon API Gateway that accepts the item names. API Gateway passes item names to AWS Lambda for tax computations.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o API Gateway com Lambda oferece escalabilidade automática e elasticidade para lidar com picos de tráfego de forma eficiente.  
- **Por que as outras opções não são adequadas?**  
  - **A/C/D:** Estas soluções dependem de EC2, o que não é tão elástico ou escalável quanto o uso do API Gateway e Lambda.

---

### Question #172
Um arquiteto de soluções está criando uma nova distribuição Amazon CloudFront para uma aplicação. Algumas das informações enviadas pelos usuários são sensíveis. A aplicação usa HTTPS, mas precisa de outra camada de segurança. As informações sensíveis devem ser protegidas em toda a pilha da aplicação, e o acesso às informações deve ser restrito a certas aplicações.  
Qual ação o arquiteto de soluções deve tomar?

**Resposta correta:**  
**C.** Configure a CloudFront field-level encryption profile.

**Justificativa:**  
- **Por que essa opção?**  
  A criptografia em nível de campo do CloudFront protege dados sensíveis em toda a aplicação, adicionando uma camada de segurança específica para determinados campos.  
- **Por que as outras opções não são adequadas?**  
  - **A/B/D:** Não fornecem proteção granular para dados sensíveis.

---

### Question #173
Uma empresa de jogos hospeda uma aplicação baseada em navegador na AWS. Os usuários da aplicação consomem um grande número de vídeos e imagens armazenados no Amazon S3. Este conteúdo é o mesmo para todos os usuários.  
A aplicação aumentou em popularidade, com milhões de usuários em todo o mundo acessando esses arquivos de mídia. A empresa deseja fornecer os arquivos aos usuários enquanto reduz a carga na origem.  
Qual solução atende a esses requisitos da maneira MAIS econômica?

**Resposta correta:**  
**B.** Deploy an Amazon CloudFront web distribution in front of the S3 bucket.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront reduz a carga na origem ao armazenar o conteúdo em cache e distribuí-lo a partir de servidores de borda globais.  
- **Por que as outras opções não são adequadas?**  
  - **A/C/D:** Não fornecem caching global eficiente.

---

### Question #174
Uma empresa tem uma aplicação de múltiplas camadas que executa seis servidores web front-end em um grupo de Auto Scaling Amazon EC2 em uma única Zona de Disponibilidade atrás de um Application Load Balancer (ALB). Um arquiteto de soluções precisa modificar a infraestrutura para ser altamente disponível sem modificar a aplicação.  
Qual arquitetura o arquiteto de soluções deve escolher para fornecer alta disponibilidade?

**Resposta correta:**  
**B.** Modify the Auto Scaling group to use three instances across each of two Availability Zones.

**Justificativa:**  
- **Por que essa opção?**  
  Usar múltiplas Zonas de Disponibilidade aumenta a disponibilidade e reduz o risco de falhas.  
- **Por que as outras opções não são adequadas?**  
  - **A/C/D:** Não garantem alta disponibilidade ou são inadequadas para o cenário.

---

### Question #175
Uma empresa de comércio eletrônico possui uma aplicação de processamento de pedidos que utiliza o Amazon API Gateway e uma função AWS Lambda. A aplicação armazena dados em um banco de dados Amazon Aurora PostgreSQL. Durante um recente evento de vendas, houve um aumento repentino nos pedidos de clientes. Alguns clientes experimentaram erros de timeout, e a aplicação não processou os pedidos desses clientes.  
Um arquiteto de soluções determinou que a utilização de CPU e memória estava alta no banco de dados devido a um grande número de conexões abertas. O arquiteto de soluções precisa evitar os erros de timeout fazendo as menores alterações possíveis na aplicação.  
Qual solução atenderá a esses requisitos?  

**Resposta correta:**  
**B.** Use Amazon RDS Proxy to create a proxy for the database. Modify the Lambda function to use the RDS Proxy endpoint instead of the database endpoint.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon RDS Proxy gerencia conexões de forma eficiente, reduzindo a carga no banco de dados e prevenindo erros de timeout com alterações mínimas no código da aplicação.  
- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar provisioned concurrency para Lambda não reduz o número de conexões abertas no banco de dados.  
  - **C:** Usar réplicas de leitura não resolve problemas de conexões simultâneas no banco principal.  
  - **D:** Migrar para DynamoDB implica mudanças significativas no código da aplicação, contrariando os requisitos.

**Fonte:** Arquivo exam_formatted-138-250.txt&#8203;:contentReference[oaicite:0]{index=0}.

### Question #176
Uma aplicação é executada em instâncias Amazon EC2 em sub-redes privadas. A aplicação precisa acessar uma tabela Amazon DynamoDB.  
Qual é a forma MAIS segura de acessar a tabela garantindo que o tráfego não saia da rede AWS?

**Resposta correta:**  
**A.** Use a VPC endpoint for DynamoDB.

**Justificativa:**  
- **Por que essa opção?**  
  O endpoint da VPC para DynamoDB permite o acesso privado à tabela sem que o tráfego saia da rede da AWS.  
- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Usar NAT gateway, NAT instance ou internet gateway expõe o tráfego à rede pública, contrariando o requisito de segurança.

---

### Question #177
Uma empresa de entretenimento está usando o Amazon DynamoDB para armazenar metadados de mídia. A aplicação é intensiva em leitura e está enfrentando atrasos. A empresa não possui equipe para lidar com o overhead operacional adicional e precisa melhorar a eficiência do desempenho do DynamoDB sem reconfigurar a aplicação.  
O que um arquiteto de soluções deve recomendar para atender a esse requisito?

**Resposta correta:**  
**B.** Use Amazon DynamoDB Accelerator (DAX).

**Justificativa:**  
- **Por que essa opção?**  
  O DAX fornece um cache gerenciado para DynamoDB, melhorando o desempenho de leitura sem necessidade de reconfigurar a aplicação.  
- **Por que as outras opções não são adequadas?**  
  - **A/D:** ElastiCache requer alterações na aplicação.  
  - **C:** As tabelas globais não são projetadas para melhorar desempenho de leitura local.

---

### Question #178
A infraestrutura de uma empresa consiste em instâncias Amazon EC2 e uma instância Amazon RDS em uma única região AWS. A empresa deseja fazer backup de seus dados em uma região separada.  
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?

**Resposta correta:**  
**A.** Use AWS Backup to copy EC2 backups and RDS backups to the separate Region.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Backup automatiza o gerenciamento de backups entre regiões com esforço operacional mínimo.  
- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Requerem configurações mais complexas e não automatizam completamente o processo.

---

### Question #179
Um arquiteto de soluções precisa armazenar com segurança um nome de usuário e senha de banco de dados que uma aplicação usa para acessar uma instância Amazon RDS. A aplicação que acessa o banco de dados é executada em uma instância Amazon EC2. O arquiteto deseja criar um parâmetro seguro no AWS Systems Manager Parameter Store.  
O que o arquiteto deve fazer para atender a esse requisito?

**Resposta correta:**  
**A.** Create an IAM role that has read access to the Parameter Store parameter. Allow Decrypt access to an AWS KMS key that is used to encrypt the parameter. Assign this IAM role to the EC2 instance.

**Justificativa:**  
- **Por que essa opção?**  
  Esta configuração usa IAM e KMS para proteger as credenciais e garantir que apenas a instância EC2 autorizada tenha acesso.  
- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Alternativas que não garantem segurança ou requerem maior esforço operacional.

---

### Question #180
Uma empresa está projetando uma plataforma de comunicações na nuvem baseada em APIs. A aplicação está hospedada em instâncias Amazon EC2 atrás de um Network Load Balancer (NLB). A empresa usa o Amazon API Gateway para fornecer aos usuários externos acesso à aplicação por meio de APIs. A empresa quer proteger a plataforma contra explorações na web, como injeção de SQL, e também detectar e mitigar grandes ataques DDoS sofisticados.  
Qual combinação de soluções fornece a MAIOR proteção? (Escolha duas.)  

**Resposta correta:**  
**B.** Use AWS Shield Advanced with the NLB.  
**C.** Use AWS WAF to protect Amazon API Gateway.  

**Justificativa:**  
- **Por que essas opções?**  
  - **B:** O AWS Shield Advanced oferece proteção avançada contra ataques DDoS sofisticados e inclui suporte adicional para mitigação.  
  - **C:** O AWS WAF protege a API contra explorações na web, como injeção de SQL, fornecendo uma camada de segurança adicional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Proteger o NLB com WAF não oferece a mesma proteção granular para APIs.  
  - **D/E:** Shield Standard não detecta ou mitiga ataques sofisticados como o Shield Advanced.
---


### Question #181

**Texto original:**  
Uma empresa tem uma aplicação legada de processamento de dados que roda em instâncias Amazon EC2. Os dados são processados sequencialmente, mas a ordem dos resultados não importa. A aplicação usa uma arquitetura monolítica. A única forma que a empresa encontrou para escalar a aplicação é aumentar o tamanho das instâncias.  
Os desenvolvedores decidiram reescrever a aplicação usando uma arquitetura de microsserviços no Amazon Elastic Container Service (Amazon ECS).  
O que um arquiteto de soluções deve recomendar para a comunicação entre os microsserviços?

**Resposta correta:**  
**A.** Create an Amazon Simple Queue Service (Amazon SQS) queue. Add code to the data producers, and send data to the queue. Add code to the data consumers to process data from the queue.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon SQS é uma solução ideal para microsserviços porque desacopla os produtores e consumidores, além de permitir a escalabilidade e processamento paralelo dos dados.  
- **Por que as outras opções não são adequadas?**  
  - **B:** O Amazon SNS é mais adequado para notificações e não para filas com alto volume de mensagens.  
  - **C:** AWS Lambda adiciona complexidade desnecessária ao fluxo de mensagens.  
  - **D:** DynamoDB Streams não foi projetado para o cenário descrito.

---

### Question #182
Uma empresa deseja migrar seu banco de dados MySQL do ambiente local para a AWS. Recentemente, a empresa enfrentou uma interrupção no banco de dados que impactou significativamente os negócios. Para garantir que isso não aconteça novamente, a empresa quer uma solução confiável na AWS que minimize a perda de dados e armazene todas as transações em pelo menos dois nós.  
Qual solução atende a esses requisitos?

**Resposta correta:**  
**B.** Create an Amazon RDS MySQL DB instance with Multi-AZ functionality enabled to synchronously replicate the data.

**Justificativa:**  
- **Por que essa opção?**  
  O recurso Multi-AZ do Amazon RDS garante alta disponibilidade e replicação síncrona para evitar perda de dados.  
- **Por que as outras opções não são adequadas?**  
  - **A:** Não menciona Multi-AZ e pode não ser aplicável para replicação síncrona.  
  - **C:** Réplicas de leitura não oferecem replicação síncrona.  
  - **D:** A configuração manual adiciona complexidade desnecessária e não é otimizada para recuperação automática.

---

### Question #183
Uma empresa está construindo um novo site de pedidos dinâmicos. A empresa deseja minimizar a manutenção e atualização de servidores. O site deve ser altamente disponível e escalar a capacidade de leitura e escrita o mais rápido possível para atender às mudanças na demanda dos usuários.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**A.** Host static content in Amazon S3. Host dynamic content by using Amazon API Gateway and AWS Lambda. Use Amazon DynamoDB with on-demand capacity for the database. Configure Amazon CloudFront to deliver the website content.

**Justificativa:**  
- **Por que essa opção?**  
  Combina os serviços AWS para minimizar a manutenção do servidor e garantir escalabilidade e alta disponibilidade.  
- **Por que as outras opções não são adequadas?**  
  - **B:** Aurora pode introduzir atrasos na escalabilidade comparado ao DynamoDB com on-demand capacity.  
  - **C/D:** Usar EC2 exige mais esforço de manutenção e escalabilidade manual.

---

### Question #184
Uma empresa possui uma conta AWS usada para engenharia de software. A conta AWS tem acesso ao data center on-premises da empresa por meio de duas conexões AWS Direct Connect. Todo o tráfego não pertencente à VPC é roteado para o gateway privado virtual.  
Uma equipe de desenvolvimento criou recentemente uma função AWS Lambda por meio do console. A equipe precisa permitir que a função acesse um banco de dados que roda em uma sub-rede privada no data center da empresa.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**A.** Configure the Lambda function to run in the VPC with the appropriate security group.

**Justificativa:**  
- **Por que essa opção?**  
  Configurar a função Lambda na VPC permite que ela se comunique com o banco de dados usando as conexões Direct Connect, respeitando os roteamentos e grupos de segurança adequados.  
- **Por que as outras opções não são adequadas?**  
  - **B:** Configurar uma VPN é redundante com Direct Connect já configurado.  
  - **C:** Atualizar tabelas de roteamento sem colocar a Lambda na VPC não resolve a conectividade.  
  - **D:** Elastic IPs não são necessários e não funcionariam sem a rede adequada.

---

### Question #185
Uma empresa executa uma aplicação usando Amazon ECS. A aplicação cria versões redimensionadas de uma imagem original e faz chamadas de API Amazon S3 para armazenar as imagens redimensionadas no Amazon S3.  
Como um arquiteto de soluções pode garantir que a aplicação tenha permissão para acessar o Amazon S3?

**Resposta correta:**  
**B.** Create an IAM role with S3 permissions, and then specify that role as the taskRoleArn in the task definition.

**Justificativa:**  
- **Por que essa opção?**  
  Especificar uma função IAM na definição da tarefa (taskRoleArn) permite que o ECS gerencie permissões temporárias e seguras para acessar o S3.  
- **Por que as outras opções não são adequadas?**  
  - **A:** Atualizar um papel S3 não vinculado ao ECS não garante permissões seguras.  
  - **C:** Security groups não gerenciam permissões de API.  
  - **D:** IAM users são uma abordagem manual e menos segura.

---

### Question #186
Uma empresa possui uma aplicação baseada em Windows que deve ser migrada para a AWS. A aplicação requer o uso de um sistema de arquivos Windows compartilhado anexado a várias instâncias Amazon EC2 Windows implantadas em várias Zonas de Disponibilidade.  
O que um arquiteto de soluções deve fazer para atender a esse requisito?

**Resposta correta:**  
**B.** Configure Amazon FSx for Windows File Server. Mount the Amazon FSx file system to each Windows instance.

**Justificativa:**  
- **Por que essa opção?**  
  O FSx for Windows File Server é projetado para fornecer sistemas de arquivos Windows totalmente gerenciados e compartilháveis entre instâncias em diferentes Zonas de Disponibilidade.  
- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Storage Gateway não é ideal para múltiplas Zonas de Disponibilidade.  
  - **C:** O EFS não é compatível com sistemas de arquivos nativos do Windows.  
  - **D:** O Amazon EBS não suporta anexos simultâneos entre várias instâncias.

### Question #187
Uma empresa está desenvolvendo uma aplicação de comércio eletrônico que consistirá em um front-end balanceado, uma aplicação baseada em contêineres e um banco de dados relacional. Um arquiteto de soluções precisa criar uma solução altamente disponível que opere com o mínimo de intervenção manual possível.  
Quais soluções atendem a esses requisitos? (Escolha duas.)

**Respostas corretas:**  
**A.** Create an Amazon RDS DB instance in Multi-AZ mode.  
**D.** Create an Amazon Elastic Container Service (Amazon ECS) cluster with a Fargate launch type to handle the dynamic application load.

**Justificativa:**  
- **Por que essas opções?**  
  - O RDS Multi-AZ oferece alta disponibilidade automática para bancos de dados relacionais.  
  - O ECS com Fargate elimina a necessidade de gerenciar servidores subjacentes, garantindo alta disponibilidade e escalabilidade para a aplicação baseada em contêineres.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Réplicas de leitura não oferecem alta disponibilidade automática.  
  - **C/E:** Usar EC2 para o cluster adiciona complexidade operacional desnecessária.  

---

### Question #188
Uma empresa usa o Amazon S3 como seu data lake. A empresa tem um novo parceiro que deve usar SFTP para enviar arquivos de dados. Um arquiteto de soluções precisa implementar uma solução SFTP altamente disponível que minimize o esforço operacional.  
Qual solução atenderá a esses requisitos?

**Resposta correta:**  
**A.** Use AWS Transfer Family to configure an SFTP-enabled server with a publicly accessible endpoint. Choose the S3 data lake as the destination.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Transfer Family fornece uma solução gerenciada e integrada para SFTP, conectando diretamente ao bucket S3 com alta disponibilidade e baixo esforço operacional.  
- **Por que as outras opções não são adequadas?**  
  - **B/C/D:** Requerem infraestrutura adicional e maior esforço de manutenção.

---

### Question #189
Uma empresa precisa armazenar documentos de contrato. Um contrato dura 5 anos. Durante o período de 5 anos, a empresa deve garantir que os documentos não possam ser sobrescritos ou excluídos. A empresa precisa criptografar os documentos em repouso e rodar as chaves de criptografia automaticamente a cada ano.  
Quais combinações de etapas um arquiteto de soluções deve realizar para atender a esses requisitos com o MENOR esforço operacional? (Escolha duas.)

**Respostas corretas:**  
**B.** Store the documents in Amazon S3. Use S3 Object Lock in compliance mode.  
**D.** Use server-side encryption with AWS Key Management Service (AWS KMS) customer managed keys. Configure key rotation.

**Justificativa:**  
- **Por que essas opções?**  
  - O S3 Object Lock em modo de conformidade impede exclusões ou alterações nos dados durante o período de retenção.  
  - O KMS com chaves gerenciadas oferece rotação automática de chaves com segurança integrada.  

- **Por que as outras opções não são adequadas?**  
  - **A/C/E:** Não atendem a todos os requisitos ou requerem maior esforço operacional.

### Question #190
Uma empresa tem um aplicativo web baseado em Java e PHP. A empresa planeja mover o aplicativo de um ambiente local para a AWS. A empresa precisa da capacidade de testar novos recursos do site frequentemente. A solução deve ser altamente disponível e gerenciada, com o mínimo de sobrecarga operacional.  
Qual solução atenderá a esses requisitos?  
A. Criar um bucket Amazon S3. Habilitar hospedagem estática no bucket. Fazer upload do conteúdo estático para o bucket. Usar AWS Lambda para processar todo o conteúdo dinâmico.  
B. Implantar o aplicativo web em um ambiente AWS Elastic Beanstalk. Usar a troca de URLs para alternar entre múltiplos ambientes do Elastic Beanstalk para testes de recursos.  
C. Implantar o aplicativo web em instâncias Amazon EC2 configuradas com Java e PHP. Usar grupos de Auto Scaling e um Application Load Balancer para gerenciar a disponibilidade do site.  
D. Containerizar o aplicativo web. Implantar o aplicativo em instâncias Amazon EC2. Usar o AWS Load Balancer Controller para rotear dinamicamente o tráfego entre os contêineres com os novos recursos do site para teste.

**Resposta correta:**  
**B.** Deploy the web application to an AWS Elastic Beanstalk environment. Use URL swapping to switch between multiple Elastic Beanstalk environments for feature testing.

**Justificativa:**  
- **Por que essa opção?**  
  - O Elastic Beanstalk é uma solução gerenciada que reduz a sobrecarga operacional e facilita o teste de novos recursos com ambientes dedicados e troca de URLs. Isso garante alta disponibilidade e eficiência.  

- **Por que as outras opções não são adequadas?**  
  - **A:** A combinação de S3 com Lambda não é adequada para aplicações que demandam Java e PHP, além de não atender aos requisitos dinâmicos.  
  - **C:** Usar EC2 com Auto Scaling exige maior esforço de gerenciamento operacional.  
  - **D:** Containerizar a aplicação adiciona complexidade e não fornece o gerenciamento simplificado que o Elastic Beanstalk oferece.

### Question #191
Uma empresa tem um aplicativo de pedidos que armazena informações de clientes em Amazon RDS para MySQL. Durante o horário comercial, os funcionários executam consultas únicas para relatórios, causando timeouts. A empresa precisa eliminar os timeouts sem impedir os funcionários de realizar consultas.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?  
A. Criar uma réplica de leitura. Mover consultas de relatório para a réplica.  
B. Criar uma réplica de leitura. Distribuir o aplicativo de pedidos para a instância DB primária e a réplica de leitura.  
C. Migrar o aplicativo de pedidos para Amazon DynamoDB com capacidade sob demanda.  
D. Agendar as consultas de relatório para horários fora de pico.

**Resposta correta:**  
**A.** Criar uma réplica de leitura. Mover consultas de relatório para a réplica.

**Justificativa:**  
- **Por que essa opção?**  
  - A réplica de leitura do RDS reduz a carga no banco de dados primário ao direcionar as consultas de relatórios para a réplica. Isso elimina os timeouts sem interromper as operações de pedidos.

- **Por que as outras opções não são adequadas?**  
  - **B:** Compartilhar o tráfego do aplicativo principal com a réplica pode causar inconsistências nos dados.  
  - **C:** Migrar para o DynamoDB é desnecessário e complexo para esse cenário.  
  - **D:** Agendar consultas para horários fora de pico limita a flexibilidade e não resolve o problema durante os horários comerciais.

---

### Question #192
Um hospital deseja criar cópias digitais de registros históricos e continuará adicionando centenas de novos documentos diariamente. A equipe de dados do hospital escaneará os documentos e os carregará para a AWS Cloud.  
Um arquiteto de soluções deve implementar uma solução para analisar os documentos, extrair as informações médicas e armazená-los para que um aplicativo possa executar consultas SQL nos dados. A solução deve maximizar a escalabilidade e a eficiência operacional.  
Qual combinação de etapas deve ser adotada? (Escolha duas.)  
A. Gravar as informações em uma instância Amazon EC2 com MySQL.  
B. Gravar as informações em um bucket Amazon S3. Usar Amazon Athena para consultar os dados.  
C. Criar um grupo de Auto Scaling de instâncias EC2 para processar arquivos digitalizados e extrair informações médicas.  
D. Criar uma função AWS Lambda para processar documentos carregados e usar Amazon Rekognition para converter os documentos em texto bruto. Usar Amazon Transcribe Medical para detectar informações relevantes.  
E. Criar uma função AWS Lambda para processar documentos carregados e usar Amazon Textract para converter documentos em texto bruto. Usar Amazon Comprehend Medical para extrair informações médicas relevantes.

**Respostas corretas:**  
**B.** Gravar as informações em um bucket Amazon S3. Usar Amazon Athena para consultar os dados.  
**E.** Criar uma função AWS Lambda para processar documentos carregados e usar Amazon Textract para converter documentos em texto bruto. Usar Amazon Comprehend Medical para extrair informações médicas relevantes.

**Justificativa:**  
- **Por que essas opções?**  
  - O Amazon S3 fornece armazenamento escalável para os documentos digitalizados, e o Athena permite consultas SQL eficientes nos dados.  
  - O Amazon Textract é otimizado para extrair texto de documentos escaneados, e o Comprehend Medical detecta informações médicas automaticamente.

- **Por que as outras opções não são adequadas?**  
  - **A:** MySQL em uma instância EC2 não oferece escalabilidade para o volume esperado de dados.  
  - **C:** Processamento com Auto Scaling de EC2 é menos eficiente e requer maior sobrecarga operacional.  
  - **D:** Rekognition e Transcribe Medical não são ideais para análise de documentos de texto.

---

### Question #193
Uma empresa está executando um aplicativo em lote em instâncias Amazon EC2. O aplicativo consiste em um backend com vários bancos de dados Amazon RDS. O aplicativo está causando um alto número de leituras nos bancos de dados. Um arquiteto de soluções deve reduzir o número de leituras no banco de dados enquanto garante alta disponibilidade.  
O que o arquiteto de soluções deve fazer para atender a este requisito?  
A. Adicionar réplicas de leitura no Amazon RDS.  
B. Usar o Amazon ElastiCache para Redis.  
C. Usar o Amazon Route 53 para cache DNS.  
D. Usar o Amazon ElastiCache para Memcached.

**Resposta correta:**  
**B.** Usar o Amazon ElastiCache para Redis.

**Justificativa:**  
- **Por que essa opção?**  
  - O ElastiCache para Redis é ideal para armazenar em cache os dados frequentemente acessados, reduzindo as leituras diretas nos bancos de dados e melhorando o desempenho.

- **Por que as outras opções não são adequadas?**  
  - **A:** Réplicas de leitura ajudam, mas não são tão eficazes quanto o cache para reduzir leituras repetitivas.  
  - **C:** O Route 53 DNS caching não é adequado para otimizar leituras de banco de dados.  
  - **D:** O Memcached é menos adequado que o Redis para casos de uso avançados, como cache persistente.

---

### Question #194
Uma empresa precisa executar um aplicativo crítico na AWS. A empresa precisa usar Amazon EC2 para o banco de dados do aplicativo. O banco de dados deve ter alta disponibilidade e deve alternar automaticamente em caso de evento disruptivo.  
Qual solução atenderá a esses requisitos?  
A. Iniciar duas instâncias EC2, cada uma em uma Zona de Disponibilidade diferente, na mesma região da AWS. Instalar o banco de dados em ambas as instâncias e configurá-las como um cluster com replicação.  
B. Iniciar uma instância EC2 em uma Zona de Disponibilidade. Instalar o banco de dados e usar uma Amazon Machine Image (AMI) para backup. Usar o AWS CloudFormation para provisionar automaticamente a instância em caso de evento disruptivo.  
C. Iniciar duas instâncias EC2, cada uma em uma região da AWS diferente. Instalar o banco de dados em ambas as instâncias. Configurar a replicação do banco de dados. Alternar para a segunda região em caso de falha.  
D. Iniciar uma instância EC2 em uma Zona de Disponibilidade. Instalar o banco de dados e usar uma Amazon Machine Image (AMI) para backup. Usar a recuperação automática do EC2 para recuperar a instância em caso de evento disruptivo.

**Resposta correta:**  
**A.** Iniciar duas instâncias EC2, cada uma em uma Zona de Disponibilidade diferente, na mesma região da AWS. Instalar o banco de dados em ambas as instâncias e configurá-las como um cluster com replicação.

**Justificativa:**  
- **Por que essa opção?**  
  - O uso de duas Zonas de Disponibilidade com replicação em cluster garante alta disponibilidade e failover automático em caso de falhas.

- **Por que as outras opções não são adequadas?**  
  - **B:** O CloudFormation não fornece failover automático em tempo real.  
  - **C:** Configurar duas regiões diferentes adiciona latência e complexidade desnecessária para este caso.  
  - **D:** A recuperação automática é limitada a falhas de hardware e não fornece alta disponibilidade total.

---

### Question #195
O sistema de pedidos de uma empresa envia requisições de clientes para instâncias Amazon EC2. As instâncias EC2 processam os pedidos e os armazenam em um banco de dados no Amazon RDS. Os usuários relatam que precisam reprocessar pedidos quando o sistema falha. A empresa quer uma solução resiliente que possa processar pedidos automaticamente em caso de falha do sistema.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?  
A. Mover as instâncias EC2 para um grupo de Auto Scaling. Criar uma regra Amazon EventBridge que aponte para uma tarefa do Amazon ECS.  
B. Mover as instâncias EC2 para um grupo de Auto Scaling atrás de um Application Load Balancer (ALB). Atualizar o sistema de pedidos para enviar mensagens para o endpoint do ALB.  
C. Mover as instâncias EC2 para um grupo de Auto Scaling. Configurar o sistema de pedidos para enviar mensagens para uma fila do Amazon Simple Queue Service (Amazon SQS). Configurar as instâncias EC2 para consumir mensagens da fila.  
D. Criar um tópico Amazon Simple Notification Service (Amazon SNS). Criar uma função AWS Lambda e assiná-la ao tópico SNS. Configurar o sistema de pedidos para enviar mensagens ao tópico SNS. Enviar um comando às instâncias EC2 para processar as mensagens usando o AWS Systems Manager Run Command.

**Resposta correta:**  
**C.** Mover as instâncias EC2 para um grupo de Auto Scaling. Configurar o sistema de pedidos para enviar mensagens para uma fila do Amazon Simple Queue Service (Amazon SQS). Configurar as instâncias EC2 para consumir mensagens da fila.

**Justificativa:**  
- **Por que essa opção?**  
  - O uso do Amazon SQS desacopla o processamento de pedidos, garantindo resiliência e recuperação em caso de falhas, enquanto o Auto Scaling ajusta dinamicamente os recursos.

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar EventBridge e ECS para processar diretamente as ordens aumenta a complexidade sem resolver o problema de desacoplamento.  
  - **B:** Um ALB não oferece capacidade de fila e não resolve a necessidade de reprocessamento automático.  
  - **D:** O uso de SNS e Lambda não fornece armazenamento persistente para mensagens que aguardam processamento.

---

### Question #196
Uma empresa executa um aplicativo em uma grande frota de instâncias Amazon EC2. O aplicativo lê e grava entradas em uma tabela do Amazon DynamoDB. O tamanho da tabela aumenta continuamente, mas o aplicativo precisa apenas dos dados dos últimos 30 dias. A empresa precisa de uma solução que minimize os custos e o esforço de desenvolvimento.  
Qual solução atende a esses requisitos?  
A. Usar um template do AWS CloudFormation para implantar toda a solução. Reimplantar o stack do CloudFormation a cada 30 dias e excluir o stack original.  
B. Usar uma instância EC2 que execute um aplicativo de monitoramento do AWS Marketplace. Configurar o aplicativo para usar Amazon DynamoDB Streams e armazenar um timestamp para cada novo item criado na tabela. Usar um script para excluir itens com mais de 30 dias.  
C. Configurar o Amazon DynamoDB Streams para invocar uma função AWS Lambda quando um novo item for criado na tabela. Configurar a função Lambda para excluir itens com mais de 30 dias.  
D. Estender o aplicativo para adicionar um atributo com o timestamp atual + 30 dias a cada novo item. Configurar o DynamoDB para usar o atributo como TTL.

**Resposta correta:**  
**D.** Estender o aplicativo para adicionar um atributo com o timestamp atual + 30 dias a cada novo item. Configurar o DynamoDB para usar o atributo como TTL.

**Justificativa:**  
- **Por que essa opção?**  
  - O Time to Live (TTL) do DynamoDB é uma funcionalidade nativa que automaticamente exclui itens expirados, minimizando custos e esforço operacional.

- **Por que as outras opções não são adequadas?**  
  - **A:** Reimplantar o stack do CloudFormation manualmente é ineficiente e caro.  
  - **B:** Usar DynamoDB Streams com EC2 é mais complexo e menos escalável.  
  - **C:** Configurar Lambda para exclusão contínua adiciona custos desnecessários e maior complexidade.

---

### Question #197
Uma empresa possui um aplicativo Microsoft .NET que é executado em um servidor Windows no local. O aplicativo armazena dados usando um Oracle Database Standard Edition. A empresa está planejando uma migração para a AWS e deseja minimizar as alterações de desenvolvimento durante a migração. O ambiente da aplicação na AWS deve ser altamente disponível.  
Quais ações combinadas a empresa deve realizar para atender a esses requisitos? (Escolha duas.)  
A. Refatorar o aplicativo como serverless com funções AWS Lambda executando .NET Core.  
B. Re-hospedar o aplicativo no AWS Elastic Beanstalk com a plataforma .NET em uma implantação Multi-AZ.  
C. Replataformar o aplicativo para executá-lo no Amazon EC2 com o Amazon Linux AMI.  
D. Usar o AWS Database Migration Service (AWS DMS) para migrar do banco de dados Oracle para o Amazon DynamoDB em uma implantação Multi-AZ.  
E. Usar o AWS Database Migration Service (AWS DMS) para migrar do banco de dados Oracle para o Oracle no Amazon RDS em uma implantação Multi-AZ.

**Respostas corretas:**  
**B.** Re-hospedar o aplicativo no AWS Elastic Beanstalk com a plataforma .NET em uma implantação Multi-AZ.  
**E.** Usar o AWS Database Migration Service (AWS DMS) para migrar do banco de dados Oracle para o Oracle no Amazon RDS em uma implantação Multi-AZ.

**Justificativa:**  
- **Por que essas opções?**  
  - O Elastic Beanstalk reduz as alterações de desenvolvimento ao oferecer uma plataforma gerenciada para o aplicativo .NET.  
  - Migrar o banco de dados para o Oracle no Amazon RDS mantém a compatibilidade com o banco atual enquanto oferece alta disponibilidade com Multi-AZ.

- **Por que as outras opções não são adequadas?**  
  - **A:** Refatorar para Lambda e .NET Core exige alterações significativas no código.  
  - **C:** Replataformar para EC2 com Linux adiciona complexidade desnecessária e não oferece alta disponibilidade gerenciada.  
  - **D:** Migrar para DynamoDB pode ser incompatível com o aplicativo e requer alterações significativas.

---

### Question #198
Uma empresa executa um aplicativo containerizado em um cluster Kubernetes em um data center local. A empresa utiliza um banco de dados MongoDB para armazenamento. A empresa deseja migrar alguns desses ambientes para a AWS, mas não pode alterar o código ou o método de implantação no momento. A solução deve minimizar a sobrecarga operacional.  
Qual solução atenderá a esses requisitos?  
A. Usar o Amazon Elastic Container Service (Amazon ECS) com nós de trabalho Amazon EC2 para computação e MongoDB no EC2 para armazenamento.  
B. Usar o Amazon Elastic Container Service (Amazon ECS) com AWS Fargate para computação e Amazon DynamoDB para armazenamento.  
C. Usar o Amazon Elastic Kubernetes Service (Amazon EKS) com nós de trabalho Amazon EC2 para computação e Amazon DynamoDB para armazenamento.  
D. Usar o Amazon Elastic Kubernetes Service (Amazon EKS) com AWS Fargate para computação e Amazon DocumentDB (com compatibilidade com MongoDB) para armazenamento.

**Resposta correta:**  
**D.** Usar o Amazon Elastic Kubernetes Service (Amazon EKS) com AWS Fargate para computação e Amazon DocumentDB (com compatibilidade com MongoDB) para armazenamento.

**Justificativa:**  
- **Por que essa opção?**  
  - O EKS com Fargate reduz a sobrecarga operacional, eliminando a necessidade de gerenciar nós manualmente. O DocumentDB oferece compatibilidade com MongoDB, permitindo a migração sem mudanças no código.

- **Por que as outras opções não são adequadas?**  
  - **A:** Gerenciar EC2 manualmente para computação e MongoDB adiciona sobrecarga operacional.  
  - **B:** DynamoDB não é compatível com MongoDB, o que exigiria mudanças no código.  
  - **C:** EC2 para computação adiciona sobrecarga operacional, enquanto o DynamoDB não é compatível com MongoDB.

---

### Question #199
Uma empresa de telemarketing está projetando a funcionalidade do seu call center de atendimento ao cliente na AWS. A empresa precisa de uma solução que ofereça reconhecimento de múltiplos locutores e gere arquivos de transcrição. A empresa deseja consultar os arquivos de transcrição para analisar padrões de negócios. Os arquivos de transcrição devem ser armazenados por 7 anos para fins de auditoria.  
Qual solução atenderá a esses requisitos?  
A. Usar Amazon Rekognition para reconhecimento de múltiplos locutores. Armazenar os arquivos de transcrição no Amazon S3. Usar modelos de machine learning para análise dos arquivos de transcrição.  
B. Usar Amazon Transcribe para reconhecimento de múltiplos locutores. Usar Amazon Athena para análise dos arquivos de transcrição.  
C. Usar Amazon Translate para reconhecimento de múltiplos locutores. Armazenar os arquivos de transcrição no Amazon Redshift. Usar consultas SQL para análise.  
D. Usar Amazon Rekognition para reconhecimento de múltiplos locutores. Armazenar os arquivos de transcrição no Amazon S3. Usar Amazon Textract para análise dos arquivos de transcrição.

**Resposta correta:**  
**B.** Usar Amazon Transcribe para reconhecimento de múltiplos locutores. Usar Amazon Athena para análise dos arquivos de transcrição.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon Transcribe oferece reconhecimento de múltiplos locutores para arquivos de áudio. O Amazon Athena permite consultas SQL diretas nos arquivos de transcrição armazenados no S3, proporcionando uma solução escalável e eficiente.

- **Por que as outras opções não são adequadas?**  
  - **A:** O Rekognition não é adequado para transcrição ou reconhecimento de múltiplos locutores.  
  - **C:** O Translate não é apropriado para reconhecimento de locutores ou transcrição.  
  - **D:** O Textract não é utilizado para análise de áudio ou transcrição.

---

### Question #200
Uma empresa hospeda seu aplicativo na AWS. A empresa usa o Amazon Cognito para gerenciar usuários. Quando os usuários fazem login no aplicativo, este busca os dados necessários no Amazon DynamoDB usando uma API REST hospedada no Amazon API Gateway. A empresa quer uma solução gerenciada pela AWS que controle o acesso à API REST para reduzir o esforço de desenvolvimento.  
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?  
A. Configurar uma função AWS Lambda como autorizador no API Gateway para validar qual usuário fez a solicitação.  
B. Para cada usuário, criar e atribuir uma chave de API que deve ser enviada com cada solicitação. Validar a chave usando uma função AWS Lambda.  
C. Enviar o endereço de e-mail do usuário no cabeçalho de cada solicitação. Invocar uma função AWS Lambda para validar que o usuário com esse e-mail tem acesso adequado.  
D. Configurar um autorizador do Amazon Cognito no API Gateway para permitir que o Amazon Cognito valide cada solicitação.

**Resposta correta:**  
**D.** Configurar um autorizador do Amazon Cognito no API Gateway para permitir que o Amazon Cognito valide cada solicitação.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon Cognito, integrado ao API Gateway, é uma solução gerenciada que reduz o esforço de desenvolvimento ao validar as solicitações automaticamente com base no pool de usuários configurado.

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar Lambda como autorizador adiciona esforço de desenvolvimento desnecessário.  
  - **B:** Gerenciar chaves de API manualmente aumenta a complexidade e o esforço operacional.  
  - **C:** Validar por cabeçalhos é menos seguro e exige implementação adicional com Lambda.

---

### Question #201
Uma empresa está desenvolvendo um serviço de comunicação de marketing que tem como alvo usuários de aplicativos móveis. A empresa precisa enviar mensagens de confirmação via SMS para seus usuários. Os usuários devem poder responder às mensagens SMS. A empresa deve armazenar as respostas por um ano para análise.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?  
A. Criar um fluxo de contato no Amazon Connect para enviar as mensagens SMS. Usar o AWS Lambda para processar as respostas.  
B. Criar uma jornada no Amazon Pinpoint. Configurar o Pinpoint para enviar eventos para um stream do Amazon Kinesis para análise e arquivamento.  
C. Usar o Amazon Simple Queue Service (Amazon SQS) para distribuir as mensagens SMS. Usar o AWS Lambda para processar as respostas.  
D. Criar um tópico FIFO do Amazon Simple Notification Service (Amazon SNS). Inscrever um stream do Amazon Kinesis no tópico SNS para análise e arquivamento.

**Resposta correta:**  
**B.** Criar uma jornada no Amazon Pinpoint. Configurar o Pinpoint para enviar eventos para um stream do Amazon Kinesis para análise e arquivamento.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon Pinpoint é projetado para comunicações direcionadas e suporte SMS bidirecional. Ele pode integrar eventos diretamente ao Kinesis para análise e arquivamento, atendendo aos requisitos de armazenamento e análise.

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon Connect é mais adequado para call centers e não é otimizado para gerenciamento de SMS bidirecional.  
  - **C:** O SQS não gerencia diretamente comunicação bidirecional ou integração para análise avançada.  
  - **D:** SNS não fornece suporte completo para gerenciamento de respostas SMS bidirecionais.

---

### Question #202
Uma empresa está planejando mover seus dados para um bucket Amazon S3. Os dados devem ser criptografados quando armazenados no bucket S3. Além disso, a chave de criptografia deve ser automaticamente rodada a cada ano.  
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?  
A. Mover os dados para o bucket S3. Usar criptografia do lado do servidor com chaves de criptografia gerenciadas pelo Amazon S3 (SSE-S3). Usar o comportamento de rotação de chave embutido do SSE-S3.  
B. Criar uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). Habilitar a rotação automática de chaves. Configurar o comportamento padrão de criptografia do bucket S3 para usar a chave gerenciada pelo cliente no KMS. Mover os dados para o bucket S3.  
C. Criar uma chave gerenciada pelo cliente no AWS KMS. Configurar o comportamento padrão de criptografia do bucket S3 para usar a chave gerenciada pelo cliente no KMS. Mover os dados para o bucket S3. Rodar manualmente a chave KMS a cada ano.  
D. Criptografar os dados com material de chave gerenciado pelo cliente antes de movê-los para o bucket S3. Criar uma chave no AWS KMS sem material de chave. Importar o material de chave gerenciado pelo cliente para a chave KMS. Habilitar a rotação automática de chaves.

**Resposta correta:**  
**B.** Criar uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). Habilitar a rotação automática de chaves. Configurar o comportamento padrão de criptografia do bucket S3 para usar a chave gerenciada pelo cliente no KMS. Mover os dados para o bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS KMS permite rotação automática de chaves com gerenciamento centralizado. Configurar o S3 para usar essa chave garante criptografia contínua e eficiente.

- **Por que as outras opções não são adequadas?**  
  - **A:** O SSE-S3 não oferece controle sobre as chaves ou rotação manual pelo cliente.  
  - **C:** Rodar manualmente as chaves do KMS adiciona esforço operacional desnecessário.  
  - **D:** Importar material de chave gerenciado pelo cliente adiciona complexidade desnecessária.

---

### Question #203
Os clientes de uma empresa financeira solicitam compromissos com consultores financeiros enviando mensagens de texto. Um aplicativo web, executado em instâncias Amazon EC2, aceita as solicitações de compromissos. As mensagens de texto são publicadas em uma fila do Amazon Simple Queue Service (Amazon SQS) através do aplicativo web. Outro aplicativo, também executado em instâncias EC2, envia convites para reuniões e e-mails de confirmação para os clientes. Após o agendamento bem-sucedido, esse aplicativo armazena as informações das reuniões em um banco de dados Amazon DynamoDB.  
Com a expansão da empresa, os clientes relatam que os convites para reuniões estão demorando mais para chegar.  
O que um arquiteto de soluções deve recomendar para resolver esse problema?  
A. Adicionar um cluster DynamoDB Accelerator (DAX) na frente do banco de dados DynamoDB.  
B. Adicionar uma API do Amazon API Gateway na frente do aplicativo web que aceita as solicitações de compromissos.  
C. Adicionar uma distribuição Amazon CloudFront. Definir o aplicativo web como origem.  
D. Adicionar um grupo de Auto Scaling para o aplicativo que envia os convites. Configurar o Auto Scaling para escalar com base na profundidade da fila SQS.

**Resposta correta:**  
**D.** Adicionar um grupo de Auto Scaling para o aplicativo que envia os convites. Configurar o Auto Scaling para escalar com base na profundidade da fila SQS.

**Justificativa:**  
- **Por que essa opção?**  
  - A fila SQS permite monitorar a quantidade de mensagens pendentes. Configurar um grupo de Auto Scaling para dimensionar automaticamente com base na profundidade da fila garante que o sistema acompanhe o aumento na demanda sem atrasos.

- **Por que as outras opções não são adequadas?**  
  - **A:** O DAX acelera leituras no DynamoDB, mas não resolve o problema de envio de convites atrasados.  
  - **B:** O API Gateway não impacta diretamente o envio de convites, que é o gargalo identificado.  
  - **C:** O CloudFront melhora a entrega de conteúdo estático, mas não ajuda no processamento de mensagens pendentes na fila.

---

### Question #204
Uma empresa de varejo online possui mais de 50 milhões de clientes ativos e recebe mais de 25.000 pedidos por dia. A empresa coleta dados de compras de clientes e armazena esses dados no Amazon S3. Dados adicionais de clientes são armazenados no Amazon RDS.  
A empresa deseja tornar todos os dados disponíveis para várias equipes, permitindo que realizem análises. A solução deve fornecer a capacidade de gerenciar permissões detalhadas para os dados e minimizar a sobrecarga operacional.  
Qual solução atenderá a esses requisitos?  
A. Migrar os dados de compra diretamente para o Amazon RDS. Usar controles de acesso do RDS para limitar o acesso.  
B. Agendar uma função AWS Lambda para copiar periodicamente os dados do RDS para o S3. Criar um rastreador do AWS Glue e usar o Amazon Athena para consultar os dados. Usar políticas do S3 para limitar o acesso.  
C. Criar um data lake usando o AWS Lake Formation. Criar uma conexão JDBC do AWS Glue para o Amazon RDS. Registrar o bucket S3 no Lake Formation. Usar controles de acesso do Lake Formation para limitar o acesso.  
D. Criar um cluster Amazon Redshift. Agendar uma função AWS Lambda para copiar periodicamente os dados do S3 e do RDS para o Redshift. Usar controles de acesso do Redshift para limitar o acesso.

**Resposta correta:**  
**C.** Criar um data lake usando o AWS Lake Formation. Criar uma conexão JDBC do AWS Glue para o Amazon RDS. Registrar o bucket S3 no Lake Formation. Usar controles de acesso do Lake Formation para limitar o acesso.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Lake Formation simplifica a criação de data lakes seguros, fornecendo controle de acesso detalhado e integração direta com S3 e RDS. Isso minimiza a sobrecarga operacional e facilita o gerenciamento de permissões.

- **Por que as outras opções não são adequadas?**  
  - **A:** Migrar dados para o RDS não é escalável e limita o suporte para análise em grande escala.  
  - **B:** Copiar dados manualmente com Lambda adiciona complexidade e não gerencia permissões de forma eficiente.  
  - **D:** Usar Redshift é mais caro e envolve maior sobrecarga operacional para ingestão e manutenção de dados.

---

### Question #205
Uma empresa hospeda um site de marketing em um data center local. O site consiste em documentos estáticos e é executado em um único servidor. Um administrador atualiza o conteúdo do site ocasionalmente e usa um cliente SFTP para fazer upload de novos documentos.  
A empresa decide hospedar seu site na AWS e usar o Amazon CloudFront. O arquiteto de soluções da empresa cria uma distribuição CloudFront. O arquiteto deve projetar a arquitetura mais econômica e resiliente para hospedagem do site, que servirá como origem do CloudFront.  
Qual solução atenderá a esses requisitos?  
A. Criar um servidor virtual usando o Amazon Lightsail. Configurar o servidor web na instância Lightsail. Fazer upload do conteúdo do site usando um cliente SFTP.  
B. Criar um grupo de Auto Scaling para instâncias Amazon EC2. Usar um Application Load Balancer. Fazer upload do conteúdo do site usando um cliente SFTP.  
C. Criar um bucket Amazon S3 privado. Usar uma política de bucket S3 para permitir acesso de uma identidade de origem do CloudFront (OAI). Fazer upload do conteúdo do site usando o AWS CLI.  
D. Criar um bucket Amazon S3 público. Configurar o AWS Transfer for SFTP. Configurar o bucket S3 para hospedagem de sites. Fazer upload do conteúdo do site usando o cliente SFTP.

**Resposta correta:**  
**C.** Criar um bucket Amazon S3 privado. Usar uma política de bucket S3 para permitir acesso de uma identidade de origem do CloudFront (OAI). Fazer upload do conteúdo do site usando o AWS CLI.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon S3 fornece uma solução econômica, resiliente e gerenciada para armazenamento de conteúdo estático. Usar uma OAI garante segurança ao permitir que apenas o CloudFront acesse os dados.

- **Por que as outras opções não são adequadas?**  
  - **A:** O Lightsail não é tão econômico ou resiliente quanto o S3 para conteúdo estático.  
  - **B:** EC2 com Auto Scaling é excessivamente complexo e caro para esse caso de uso.  
  - **D:** Configurar S3 como público adiciona riscos desnecessários à segurança.

---

### Question #206
Uma empresa deseja gerenciar Amazon Machine Images (AMIs). Atualmente, a empresa copia AMIs para a mesma região da AWS onde elas foram criadas. A empresa precisa projetar um aplicativo que capture chamadas de API da AWS e envie alertas sempre que a operação CreateImage da API do Amazon EC2 for chamada na conta da empresa.  
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?  
A. Criar uma função AWS Lambda para consultar os logs do AWS CloudTrail e enviar um alerta quando uma chamada CreateImage for detectada.  
B. Configurar o AWS CloudTrail com uma notificação do Amazon SNS que ocorre quando os logs atualizados são enviados para o Amazon S3. Usar o Amazon Athena para consultar os logs em busca de chamadas CreateImage.  
C. Criar uma regra Amazon EventBridge para a chamada CreateImage da API. Configurar o destino como um tópico do Amazon SNS para enviar um alerta quando a chamada CreateImage for detectada.  
D. Configurar uma fila FIFO do Amazon SQS como destino para os logs do AWS CloudTrail. Criar uma função AWS Lambda para enviar um alerta para um tópico do Amazon SNS quando uma chamada CreateImage for detectada.

**Resposta correta:**  
**C.** Criar uma regra Amazon EventBridge para a chamada CreateImage da API. Configurar o destino como um tópico do Amazon SNS para enviar um alerta quando a chamada CreateImage for detectada.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon EventBridge permite configurar eventos em tempo real para chamadas de API específicas, como CreateImage, e encaminhá-los diretamente para o SNS para alertas. Isso minimiza a complexidade e a sobrecarga operacional.

- **Por que as outras opções não são adequadas?**  
  - **A:** Consultar logs do CloudTrail com Lambda introduz latência e complexidade adicional.  
  - **B:** Usar Athena para consultas manuais requer mais esforço operacional e não é uma solução em tempo real.  
  - **D:** Configurar SQS e Lambda adiciona camadas desnecessárias de complexidade.

---

### Question #207
Uma empresa possui uma API assíncrona usada para ingerir solicitações de usuários e, com base no tipo de solicitação, encaminhá-las para o microserviço apropriado para processamento. A empresa está usando o Amazon API Gateway para implantar a interface da API e uma função AWS Lambda que invoca o Amazon DynamoDB para armazenar solicitações de usuários antes de encaminhá-las aos microserviços de processamento.  
A empresa provisionou tanto throughput do DynamoDB quanto seu orçamento permite, mas ainda está enfrentando problemas de disponibilidade e perdendo solicitações de usuários.  
O que um arquiteto de soluções deve fazer para resolver esse problema sem impactar os usuários existentes?  
A. Adicionar limitação no API Gateway com limites de limitação do lado do servidor.  
B. Usar o DynamoDB Accelerator (DAX) e Lambda para armazenar em buffer as gravações no DynamoDB.  
C. Criar um índice secundário no DynamoDB para a tabela de solicitações de usuários.  
D. Usar o Amazon Simple Queue Service (Amazon SQS) e Lambda para armazenar em buffer as gravações no DynamoDB.

**Resposta correta:**  
**D.** Usar o Amazon Simple Queue Service (Amazon SQS) e Lambda para armazenar em buffer as gravações no DynamoDB.

**Justificativa:**  
- **Por que essa opção?**  
  - O SQS é ideal para buffer de mensagens, permitindo desacoplar o fluxo de solicitações do DynamoDB. Isso reduz a carga direta no DynamoDB e evita perda de dados em caso de picos de tráfego.

- **Por que as outras opções não são adequadas?**  
  - **A:** Limitar o tráfego no API Gateway não resolve os problemas de disponibilidade do DynamoDB.  
  - **B:** O DAX acelera leituras, mas não resolve problemas relacionados à gravação.  
  - **C:** Adicionar um índice secundário não reduz a carga geral de gravação e não evita perda de solicitações.

---

### Question #208
Uma empresa precisa mover dados de uma instância Amazon EC2 para um bucket Amazon S3. A empresa deve garantir que nenhuma chamada de API e nenhum dado sejam roteados por rotas públicas na internet. Apenas a instância EC2 pode ter acesso para fazer upload de dados para o bucket S3.  
Qual solução atenderá a esses requisitos?  
A. Criar um endpoint de VPC do tipo interface para o Amazon S3 na sub-rede onde a instância EC2 está localizada. Anexar uma política de recurso ao bucket S3 para permitir apenas o acesso da função IAM da instância EC2.  
B. Criar um endpoint de VPC do tipo gateway para o Amazon S3 na Zona de Disponibilidade onde a instância EC2 está localizada. Anexar os grupos de segurança apropriados ao endpoint. Anexar uma política de recurso ao bucket S3 para permitir apenas o acesso da função IAM da instância EC2.  
C. Executar a ferramenta `nslookup` dentro da instância EC2 para obter o endereço IP privado do endpoint da API de serviço S3. Criar uma rota na tabela de rotas da VPC para fornecer acesso ao bucket S3.  
D. Usar o arquivo público `ip-ranges.json` da AWS para obter o endereço IP privado do endpoint da API de serviço S3. Criar uma rota na tabela de rotas da VPC para fornecer acesso ao bucket S3.

**Resposta correta:**  
**B.** Criar um endpoint de VPC do tipo gateway para o Amazon S3 na Zona de Disponibilidade onde a instância EC2 está localizada. Anexar os grupos de segurança apropriados ao endpoint. Anexar uma política de recurso ao bucket S3 para permitir apenas o acesso da função IAM da instância EC2.

**Justificativa:**  
- **Por que essa opção?**  
  - O endpoint de VPC do tipo gateway permite comunicação direta entre a instância EC2 e o bucket S3 sem atravessar a internet pública, atendendo aos requisitos de segurança.

- **Por que as outras opções não são adequadas?**  
  - **A:** O endpoint de interface não é necessário para S3, pois o endpoint de gateway é mais eficiente.  
  - **C/D:** Configurar rotas manualmente com `nslookup` ou arquivos IP adiciona complexidade desnecessária e não é uma solução segura.

---

### Question #209
Um arquiteto de soluções está projetando a arquitetura de um novo aplicativo sendo implantado na AWS Cloud. O aplicativo será executado em instâncias Amazon EC2 sob demanda e escalará automaticamente em várias Zonas de Disponibilidade. As instâncias EC2 aumentarão e diminuirão frequentemente ao longo do dia. Um Application Load Balancer (ALB) gerenciará a distribuição de carga. A arquitetura precisa oferecer suporte ao gerenciamento de dados de sessão distribuídos.  
O que o arquiteto de soluções deve fazer para garantir que a arquitetura ofereça suporte ao gerenciamento de dados de sessão distribuídos?  
A. Usar o Amazon ElastiCache para gerenciar e armazenar dados de sessão.  
B. Usar afinidade de sessão (sessões persistentes) no ALB para gerenciar os dados de sessão.  
C. Usar o Session Manager do AWS Systems Manager para gerenciar a sessão.  
D. Usar a operação GetSessionToken da AWS Security Token Service (AWS STS) para gerenciar a sessão.

**Resposta correta:**  
**A.** Usar o Amazon ElastiCache para gerenciar e armazenar dados de sessão.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon ElastiCache (Redis ou Memcached) oferece um armazenamento rápido e escalável para dados de sessão, garantindo que as sessões sejam consistentes e acessíveis em todas as instâncias EC2, mesmo quando elas são escaladas dinamicamente.

- **Por que as outras opções não são adequadas?**  
  - **B:** Afinidade de sessão no ALB limita a escalabilidade e falha em fornecer uma solução distribuída robusta.  
  - **C:** O Session Manager é voltado para acesso remoto às instâncias e não para gerenciamento de dados de sessão do aplicativo.  
  - **D:** O GetSessionToken do AWS STS não é projetado para gerenciar dados de sessão em aplicativos.

---

### Question #210
Uma empresa oferece um serviço de entrega de alimentos que está crescendo rapidamente. Por causa do crescimento, o sistema de processamento de pedidos da empresa está enfrentando problemas de escalabilidade durante as horas de pico. A arquitetura atual inclui:  
- Um grupo de instâncias Amazon EC2 em um grupo de Auto Scaling para coletar pedidos do aplicativo.  
- Outro grupo de instâncias EC2 em um grupo de Auto Scaling para processar os pedidos.  
O processo de coleta de pedidos é rápido, mas o processamento pode demorar mais. Os dados não devem ser perdidos devido a um evento de escalabilidade.  
Qual solução atende a esses requisitos?  
A. Usar métricas do Amazon CloudWatch para monitorar a CPU de cada instância nos grupos de Auto Scaling. Configurar a capacidade mínima de cada grupo com base nos valores de pico de trabalho.  
B. Usar métricas do Amazon CloudWatch para monitorar a CPU de cada instância nos grupos de Auto Scaling. Configurar um alarme do CloudWatch para invocar um tópico do Amazon SNS que cria grupos de Auto Scaling adicionais sob demanda.  
C. Provisionar duas filas do Amazon Simple Queue Service (Amazon SQS): uma para coleta de pedidos e outra para processamento. Configurar as instâncias EC2 para buscar mensagens em suas filas respectivas. Escalar os grupos de Auto Scaling com base nas notificações enviadas pelas filas.  
D. Provisionar duas filas do Amazon Simple Queue Service (Amazon SQS): uma para coleta de pedidos e outra para processamento. Configurar as instâncias EC2 para buscar mensagens em suas filas respectivas. Criar uma métrica baseada em um cálculo de backlog por instância. Escalar os grupos de Auto Scaling com base nessa métrica.

**Resposta correta:**  
**D.** Provisionar duas filas do Amazon Simple Queue Service (Amazon SQS): uma para coleta de pedidos e outra para processamento. Configurar as instâncias EC2 para buscar mensagens em suas filas respectivas. Criar uma métrica baseada em um cálculo de backlog por instância. Escalar os grupos de Auto Scaling com base nessa métrica.

**Justificativa:**  
- **Por que essa opção?**  
  - O uso de SQS desacopla o fluxo de pedidos e processamento, enquanto a métrica de backlog por instância garante escalabilidade eficiente com base na carga real.

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar capacidade mínima fixa não é eficiente para lidar com variações dinâmicas de tráfego.  
  - **B:** Criar múltiplos grupos de Auto Scaling sob demanda adiciona complexidade desnecessária.  
  - **C:** Escalar apenas com notificações de fila pode não ser suficiente para equilibrar o backlog de forma precisa.

---

### Question #211
Uma empresa hospeda vários aplicativos de produção. Um dos aplicativos consiste em recursos do Amazon EC2, AWS Lambda, Amazon RDS, Amazon Simple Notification Service (Amazon SNS) e Amazon Simple Queue Service (Amazon SQS) em várias regiões da AWS. Todos os recursos da empresa são marcados com a tag “application” e um valor correspondente a cada aplicativo.  
O arquiteto de soluções deve fornecer a solução mais rápida para identificar todos os componentes marcados.  
Qual solução atenderá a esses requisitos?  
A. Usar o AWS CloudTrail para gerar uma lista de recursos com a tag “application”.  
B. Usar o AWS CLI para consultar cada serviço em todas as regiões e relatar os componentes marcados.  
C. Executar uma consulta no Amazon CloudWatch Logs Insights para relatar os componentes com a tag “application”.  
D. Executar uma consulta no AWS Resource Groups Tag Editor para relatar globalmente os recursos com a tag “application”.

**Resposta correta:**  
**D.** Executar uma consulta no AWS Resource Groups Tag Editor para relatar globalmente os recursos com a tag “application”.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Resource Groups Tag Editor permite buscar e relatar rapidamente todos os recursos marcados com uma tag específica em todas as regiões, economizando tempo e esforço.

- **Por que as outras opções não são adequadas?**  
  - **A:** O CloudTrail não é projetado para consultas eficientes de tags.  
  - **B:** Consultar manualmente cada serviço com AWS CLI é demorado e propenso a erros.  
  - **C:** O CloudWatch Logs Insights não oferece uma visão abrangente de recursos em todas as regiões.

---

### Question #212
Uma empresa precisa exportar seu banco de dados uma vez por dia para o Amazon S3 para que outras equipes possam acessá-lo. O tamanho do objeto exportado varia entre 2 GB e 5 GB. O padrão de acesso ao S3 é variável e muda rapidamente. Os dados devem estar imediatamente disponíveis e permanecer acessíveis por até 3 meses. A empresa precisa da solução mais econômica que não aumente o tempo de recuperação.  
Qual classe de armazenamento do S3 deve ser usada para atender a esses requisitos?  
A. S3 Intelligent-Tiering  
B. S3 Glacier Instant Retrieval  
C. S3 Standard  
D. S3 Standard-Infrequent Access (S3 Standard-IA)

**Resposta correta:**  
**A.** S3 Intelligent-Tiering

**Justificativa:**  
- **Por que essa opção?**  
  - O S3 Intelligent-Tiering ajusta automaticamente a classe de armazenamento com base nos padrões de acesso, garantindo economia de custos enquanto mantém acesso imediato aos dados sem impacto no tempo de recuperação.

- **Por que as outras opções não são adequadas?**  
  - **B:** O S3 Glacier Instant Retrieval não é necessário, pois o padrão de acesso é imediato e variável.  
  - **C:** O S3 Standard é mais caro para padrões de acesso variáveis.  
  - **D:** O S3 Standard-IA cobra por acessos frequentes, tornando-se mais caro para padrões de acesso dinâmicos.

---

### Question #213
Uma empresa está desenvolvendo um novo aplicativo móvel. A empresa deve implementar filtros de tráfego adequados para proteger seu Application Load Balancer (ALB) contra ataques comuns em nível de aplicação, como cross-site scripting ou SQL injection. A empresa tem uma equipe de infraestrutura e operação mínima. A empresa precisa reduzir sua responsabilidade no gerenciamento, atualização e segurança de servidores para seu ambiente AWS.  
O que um arquiteto de soluções deve recomendar para atender a esses requisitos?  
A. Configurar regras do AWS WAF e associá-las ao ALB.  
B. Implantar o aplicativo usando o Amazon S3 com hospedagem pública habilitada.  
C. Implantar o AWS Shield Advanced e adicionar o ALB como um recurso protegido.  
D. Criar um novo ALB que direciona o tráfego para uma instância EC2 executando um firewall de terceiros, que então encaminha o tráfego para o ALB atual.

**Resposta correta:**  
**A.** Configurar regras do AWS WAF e associá-las ao ALB.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS WAF é uma solução gerenciada pela AWS para proteger contra ataques em nível de aplicação, como XSS e SQL injection, e pode ser facilmente integrado ao ALB.

- **Por que as outras opções não são adequadas?**  
  - **B:** Usar S3 com hospedagem pública não fornece proteção contra ataques em nível de aplicação.  
  - **C:** O AWS Shield Advanced é mais adequado para ataques DDoS e não substitui o WAF para ataques em nível de aplicação.  
  - **D:** Configurar firewalls de terceiros adiciona complexidade operacional e gerencial.

---

### Question #214
O sistema de relatórios de uma empresa entrega centenas de arquivos .csv para um bucket Amazon S3 todos os dias. A empresa deve converter esses arquivos para o formato Apache Parquet e armazená-los em um bucket de dados transformados.  
Qual solução atenderá a esses requisitos com o MENOR esforço de desenvolvimento?  
A. Criar um cluster Amazon EMR com Apache Spark instalado. Escrever um aplicativo Spark para transformar os dados. Usar o EMR File System (EMRFS) para gravar os arquivos no bucket de dados transformados.  
B. Criar um rastreador AWS Glue para descobrir os dados. Criar um trabalho de ETL do AWS Glue para transformar os dados. Especificar o bucket de dados transformados na etapa de saída.  
C. Usar o AWS Batch para criar uma definição de trabalho com sintaxe Bash para transformar os dados e enviá-los para o bucket de dados transformados. Usar a definição de trabalho para enviar uma tarefa.  
D. Criar uma função AWS Lambda para transformar os dados e enviá-los para o bucket de dados transformados. Configurar uma notificação de evento para o bucket S3. Especificar a função Lambda como o destino para a notificação de evento.

**Resposta correta:**  
**B.** Criar um rastreador AWS Glue para descobrir os dados. Criar um trabalho de ETL do AWS Glue para transformar os dados. Especificar o bucket de dados transformados na etapa de saída.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Glue é uma solução gerenciada que automatiza a descoberta, transformação e armazenamento de dados, reduzindo o esforço de desenvolvimento.

- **Por que as outras opções não são adequadas?**  
  - **A:** O EMR exige configuração e gerenciamento mais complexos em comparação ao Glue.  
  - **C:** O AWS Batch não é otimizado para ETL e exige mais desenvolvimento manual.  
  - **D:** Usar Lambda para grandes volumes de dados pode ser ineficiente e limitado em termos de tamanho de arquivo e tempo de execução.

---

### Question #215
Uma empresa possui 700 TB de dados de backup armazenados em um NAS (Network-Attached Storage) em seu data center. Esses dados de backup precisam estar acessíveis para solicitações regulatórias infrequentes e devem ser retidos por 7 anos. A empresa decidiu migrar esses dados de backup do data center para a AWS. A migração deve ser concluída dentro de 1 mês. A empresa tem 500 Mbps de largura de banda dedicada disponível em sua conexão pública de internet para transferência de dados.  
O que um arquiteto de soluções deve fazer para migrar e armazenar os dados com o MENOR custo?  
A. Solicitar dispositivos AWS Snowball para transferir os dados. Usar uma política de ciclo de vida para transicionar os arquivos para o Amazon S3 Glacier Deep Archive.  
B. Implantar uma conexão VPN entre o data center e a Amazon VPC. Usar o AWS CLI para copiar os dados do local para o Amazon S3 Glacier.  
C. Provisionar uma conexão AWS Direct Connect de 500 Mbps e transferir os dados para o Amazon S3. Usar uma política de ciclo de vida para transicionar os arquivos para o Amazon S3 Glacier Deep Archive.  
D. Usar o AWS DataSync para transferir os dados e implantar um agente DataSync no local. Usar a tarefa DataSync para copiar os arquivos do NAS local para o Amazon S3 Glacier.

**Resposta correta:**  
**A.** Solicitar dispositivos AWS Snowball para transferir os dados. Usar uma política de ciclo de vida para transicionar os arquivos para o Amazon S3 Glacier Deep Archive.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Snowball é a solução mais eficiente para transferências de grandes volumes de dados, reduzindo custos e acelerando a migração. O uso de políticas de ciclo de vida para o S3 Glacier Deep Archive minimiza custos de armazenamento a longo prazo.

- **Por que as outras opções não são adequadas?**  
  - **B/C:** Usar internet pública ou Direct Connect para 700 TB levaria muito mais tempo do que o disponível.  
  - **D:** O DataSync é eficiente, mas a largura de banda limitada torna inviável transferir 700 TB em 1 mês.

---

### Question #216
Uma empresa possui um site sem servidor com milhões de objetos em um bucket Amazon S3. A empresa usa o bucket S3 como origem para uma distribuição Amazon CloudFront. A empresa não configurou a criptografia no bucket S3 antes de carregar os objetos. Um arquiteto de soluções precisa habilitar a criptografia para todos os objetos existentes e para todos os objetos que forem adicionados ao bucket S3 no futuro.  
Qual solução atenderá a esses requisitos com o MENOR esforço?  
A. Criar um novo bucket S3. Ativar as configurações padrão de criptografia para o novo bucket S3. Baixar todos os objetos existentes para um armazenamento local temporário. Fazer upload dos objetos para o novo bucket S3.  
B. Ativar as configurações padrão de criptografia para o bucket S3. Usar o recurso S3 Inventory para criar um arquivo .csv que liste os objetos não criptografados. Executar um trabalho S3 Batch Operations que use o comando de cópia para criptografar esses objetos.  
C. Criar uma nova chave de criptografia usando o AWS Key Management Service (AWS KMS). Alterar as configurações do bucket S3 para usar criptografia no lado do servidor com chaves de criptografia gerenciadas pelo AWS KMS (SSE-KMS). Ativar o versionamento para o bucket S3.  
D. Navegar no console do Amazon S3. Navegar pelos objetos do bucket S3. Ordenar pelo campo de criptografia. Selecionar cada objeto não criptografado. Usar o botão Modify para aplicar as configurações de criptografia padrão a cada objeto não criptografado no bucket S3.

**Resposta correta:**  
**B.** Ativar as configurações padrão de criptografia para o bucket S3. Usar o recurso S3 Inventory para criar um arquivo .csv que liste os objetos não criptografados. Executar um trabalho S3 Batch Operations que use o comando de cópia para criptografar esses objetos.

**Justificativa:**  
- **Por que essa opção?**  
  - O recurso de operações em lote do S3, combinado com o S3 Inventory, fornece uma maneira eficiente e automatizada de aplicar criptografia aos objetos existentes sem necessidade de baixá-los e recarregá-los. Além disso, ativar a criptografia padrão garante que os novos objetos sejam criptografados automaticamente.

- **Por que as outras opções não são adequadas?**  
  - **A:** Criar um novo bucket e fazer upload manualmente de todos os objetos é demorado e ineficiente.  
  - **C:** Usar SSE-KMS requer configuração adicional e pode não atender ao requisito de esforço mínimo.  
  - **D:** Modificar os objetos manualmente no console não é escalável para milhões de objetos.

---

### Question #217
Uma empresa executa um aplicativo global na web em instâncias Amazon EC2 atrás de um Application Load Balancer. O aplicativo armazena dados no Amazon Aurora. A empresa precisa criar uma solução de recuperação de desastres e pode tolerar até 30 minutos de inatividade e possível perda de dados. A solução não precisa lidar com a carga quando a infraestrutura primária está saudável.  
O que um arquiteto de soluções deve fazer para atender a esses requisitos?  
A. Implantar o aplicativo com os elementos de infraestrutura necessários. Usar o Amazon Route 53 para configurar failover ativo-passivo. Criar uma réplica do Aurora em uma segunda região da AWS.  
B. Hospedar uma implantação reduzida do aplicativo em uma segunda região da AWS. Usar o Amazon Route 53 para configurar failover ativo-ativo. Criar uma réplica do Aurora na segunda região.  
C. Replicar a infraestrutura primária em uma segunda região da AWS. Usar o Amazon Route 53 para configurar failover ativo-ativo. Criar um banco de dados Aurora restaurado a partir do snapshot mais recente.  
D. Fazer backup dos dados com o AWS Backup. Usar o backup para criar a infraestrutura necessária em uma segunda região da AWS. Usar o Amazon Route 53 para configurar failover ativo-passivo. Criar uma segunda instância principal do Aurora na segunda região.

**Resposta correta:**  
**A.** Implantar o aplicativo com os elementos de infraestrutura necessários. Usar o Amazon Route 53 para configurar failover ativo-passivo. Criar uma réplica do Aurora em uma segunda região da AWS.

**Justificativa:**  
- **Por que essa opção?**  
  - Uma configuração de failover ativo-passivo com uma réplica do Aurora oferece recuperação rápida com tolerância à perda de dados mínima, atendendo aos requisitos de tolerância de downtime de 30 minutos.

- **Por que as outras opções não são adequadas?**  
  - **B:** Um failover ativo-ativo exige mais recursos para manter a operação contínua, o que não é necessário para este caso.  
  - **C:** Restaurar um banco de dados de um snapshot aumenta o tempo de recuperação e pode exceder a tolerância de 30 minutos.  
  - **D:** Criar uma nova infraestrutura a partir de backups aumenta significativamente o tempo de recuperação.

---

### Question #218
Uma empresa possui um servidor web executando em uma instância Amazon EC2 em uma sub-rede pública com um endereço IP elástico. O grupo de segurança padrão está atribuído à instância EC2. A ACL de rede padrão foi modificada para bloquear todo o tráfego. Um arquiteto de soluções precisa tornar o servidor web acessível de qualquer lugar na porta 443.  
Quais combinações de etapas realizarão essa tarefa? (Escolha duas.)  
A. Criar um grupo de segurança com uma regra para permitir TCP na porta 443 da origem 0.0.0.0/0.  
B. Criar um grupo de segurança com uma regra para permitir TCP na porta 443 para o destino 0.0.0.0/0.  
C. Atualizar a ACL de rede para permitir TCP na porta 443 da origem 0.0.0.0/0.  
D. Atualizar a ACL de rede para permitir TCP de entrada/saída na porta 443 da origem 0.0.0.0/0 e para o destino 0.0.0.0/0.  
E. Atualizar a ACL de rede para permitir TCP de entrada na porta 443 da origem 0.0.0.0/0 e de saída na porta 32768-65535 para o destino 0.0.0.0/0.

**Respostas corretas:**  
**A.** Criar um grupo de segurança com uma regra para permitir TCP na porta 443 da origem 0.0.0.0/0.  
**E.** Atualizar a ACL de rede para permitir TCP de entrada na porta 443 da origem 0.0.0.0/0 e de saída na porta 32768-65535 para o destino 0.0.0.0/0.

**Justificativa:**  
- **Por que essas opções?**  
  - O grupo de segurança controla o tráfego de entrada e saída da instância EC2. Permitir TCP na porta 443 da origem 0.0.0.0/0 no grupo de segurança garante que o tráfego HTTPS seja permitido.  
  - As ACLs de rede controlam o tráfego em nível de sub-rede. Configurar as ACLs para permitir tráfego de entrada na porta 443 e de saída no intervalo de portas altas (32768-65535) é necessário para a comunicação correta de retorno.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Permitir tráfego para o destino 0.0.0.0/0 no grupo de segurança não é apropriado neste caso.  
  - **C/D:** Configurações incompletas de ACLs podem impedir a conectividade correta.  

### Question #219
O aplicativo de uma empresa está enfrentando problemas de desempenho. O aplicativo é stateful e precisa concluir tarefas em memória em instâncias Amazon EC2. A empresa usou o AWS CloudFormation para implantar a infraestrutura e utilizou a família de instâncias M5 do EC2. À medida que o tráfego aumentou, o desempenho do aplicativo diminuiu. Os usuários estão relatando atrasos ao tentar acessar o aplicativo.  
Qual solução resolverá esses problemas da maneira MAIS eficiente operacionalmente?  
A. Substituir as instâncias EC2 por instâncias T3 que operam em um grupo de Auto Scaling. Fazer as alterações usando o Console de Gerenciamento da AWS.  
B. Modificar os modelos do CloudFormation para executar as instâncias EC2 em um grupo de Auto Scaling. Aumentar manualmente a capacidade desejada e a capacidade máxima do grupo de Auto Scaling quando necessário.  
C. Modificar os modelos do CloudFormation. Substituir as instâncias EC2 por instâncias R5. Usar as métricas de memória integradas do CloudWatch para rastrear o desempenho do aplicativo para planejamento de capacidade futuro.  
D. Modificar os modelos do CloudFormation. Substituir as instâncias EC2 por instâncias R5. Implantar o agente do Amazon CloudWatch nas instâncias EC2 para gerar métricas de latência personalizadas para planejamento de capacidade futuro.

**Resposta correta:**  
**C.** Modificar os modelos do CloudFormation. Substituir as instâncias EC2 por instâncias R5. Usar as métricas de memória integradas do CloudWatch para rastrear o desempenho do aplicativo para planejamento de capacidade futuro.

**Justificativa:**  
- **Por que essa opção?**  
  - As instâncias R5 são otimizadas para cargas de trabalho com uso intensivo de memória, o que é adequado para aplicações stateful com tarefas em memória. Usar métricas integradas do CloudWatch reduz a sobrecarga operacional para monitoramento e planejamento futuro.

- **Por que as outras opções não são adequadas?**  
  - **A:** As instâncias T3 não têm recursos adequados para cargas intensivas de memória e não resolveriam os problemas de desempenho.  
  - **B:** Ajustar manualmente a capacidade do Auto Scaling não é eficiente operacionalmente e não aborda o problema de recursos insuficientes.  
  - **D:** Usar o agente do CloudWatch gera dados adicionais, mas não é necessário para resolver o problema principal de recursos insuficientes.

---

### Question #220
Um arquiteto de soluções está projetando uma nova API usando Amazon API Gateway para receber solicitações de usuários. O volume de solicitações é altamente variável; várias horas podem passar sem receber uma única solicitação. O processamento de dados será realizado de forma assíncrona, mas deve ser concluído em poucos segundos após uma solicitação ser feita.  
Qual serviço de computação o arquiteto de soluções deve configurar para a API para atender aos requisitos com o menor custo?  
A. Um trabalho do AWS Glue  
B. Uma função AWS Lambda  
C. Um serviço conteinerizado hospedado no Amazon Elastic Kubernetes Service (Amazon EKS)  
D. Um serviço conteinerizado hospedado no Amazon ECS com Amazon EC2  

**Resposta correta:**  
**B.** Uma função AWS Lambda  

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Lambda é a solução mais adequada para casos de uso com volume variável e processamento assíncrono. Ele escala automaticamente para atender à demanda e possui cobrança baseada no uso, sendo ideal para cenários de baixa frequência de solicitações.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Glue é projetado para tarefas de ETL e não é adequado para processamento em tempo quase real.  
  - **C:** Serviços conteinerizados no EKS são mais caros e envolvem maior sobrecarga operacional para configurar e manter.  
  - **D:** O ECS com EC2 exige o gerenciamento das instâncias subjacentes, o que aumenta os custos operacionais e não é eficiente para cargas variáveis.  


### Question #221
Uma empresa executa um aplicativo em um grupo de instâncias Amazon Linux EC2. Por razões de conformidade, a empresa deve reter todos os arquivos de log do aplicativo por 7 anos. Os arquivos de log serão analisados por uma ferramenta de relatórios que deve ser capaz de acessar todos os arquivos simultaneamente.  
Qual solução de armazenamento atende a esses requisitos da maneira MAIS econômica?  
A. Amazon Elastic Block Store (Amazon EBS)  
B. Amazon Elastic File System (Amazon EFS)  
C. Armazenamento de instância do Amazon EC2  
D. Amazon S3  

**Resposta correta:**  
**D.** Amazon S3  

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon S3 é a solução de armazenamento mais econômica e escalável para retenção de longo prazo de dados. Ele permite acesso simultâneo por várias ferramentas, atende aos requisitos de conformidade e é altamente durável e disponível.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O EBS é mais caro e não é adequado para armazenar dados de longo prazo ou para acessos simultâneos.  
  - **B:** O EFS é otimizado para sistemas de arquivos compartilhados, mas seu custo é significativamente maior do que o do S3 para armazenamento de logs a longo prazo.  
  - **C:** O armazenamento de instância EC2 é volátil e não persiste após o término da instância, tornando-o inadequado para retenção de dados.  

### Question #222
Uma empresa contratou um fornecedor externo para realizar trabalhos na conta AWS da empresa. O fornecedor usa uma ferramenta automatizada que está hospedada em uma conta AWS pertencente ao fornecedor. O fornecedor não possui acesso IAM à conta AWS da empresa.  
Como um arquiteto de soluções deve conceder esse acesso ao fornecedor?  
A. Criar uma função IAM na conta da empresa para delegar acesso à função IAM do fornecedor. Anexar as políticas IAM apropriadas à função para as permissões necessárias ao fornecedor.  
B. Criar um usuário IAM na conta da empresa com uma senha que atenda aos requisitos de complexidade. Anexar as políticas IAM apropriadas ao usuário para as permissões necessárias ao fornecedor.  
C. Criar um grupo IAM na conta da empresa. Adicionar o usuário IAM da ferramenta da conta do fornecedor ao grupo. Anexar as políticas IAM apropriadas ao grupo para as permissões necessárias ao fornecedor.  
D. Criar um novo provedor de identidade, escolhendo “Conta AWS” como o tipo de provedor no console do IAM. Fornecer o ID da conta AWS do fornecedor e o nome de usuário. Anexar as políticas IAM apropriadas ao novo provedor para as permissões necessárias ao fornecedor.

**Resposta correta:**  
**A.** Criar uma função IAM na conta da empresa para delegar acesso à função IAM do fornecedor. Anexar as políticas IAM apropriadas à função para as permissões necessárias ao fornecedor.

**Justificativa:**  
- **Por que essa opção?**  
  - Criar uma função IAM com confiança delegada permite que a conta do fornecedor assuma a função temporariamente para realizar o trabalho. Esse método é seguro, segue as melhores práticas e evita a necessidade de criar usuários permanentes.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar um usuário IAM diretamente na conta da empresa não segue as melhores práticas de segurança e aumenta o risco de gerenciamento de credenciais.  
  - **C:** Não é possível adicionar usuários IAM de uma conta externa diretamente a um grupo IAM na conta da empresa.  
  - **D:** Criar um provedor de identidade para outro AWS Account ID é desnecessário e não corresponde ao caso de uso descrito.  

### Question #223

**Texto original:**  
Uma empresa implantou um aplicativo Java Spring Boot como um pod que é executado no Amazon Elastic Kubernetes Service (Amazon EKS) em sub-redes privadas. O aplicativo precisa gravar dados em uma tabela Amazon DynamoDB. Um arquiteto de soluções deve garantir que o aplicativo possa interagir com a tabela DynamoDB sem expor o tráfego à internet.  
Quais combinações de etapas o arquiteto de soluções deve realizar para alcançar esse objetivo? (Escolha duas.)  
A. Anexar uma função IAM com privilégios suficientes ao pod do EKS.  
B. Anexar um usuário IAM com privilégios suficientes ao pod do EKS.  
C. Permitir conectividade de saída para a tabela DynamoDB por meio das ACLs de rede das sub-redes privadas.  
D. Criar um endpoint de VPC para o DynamoDB.  
E. Incorporar as chaves de acesso no código Java Spring Boot.

**Respostas corretas:**  
**A.** Anexar uma função IAM com privilégios suficientes ao pod do EKS.  
**D.** Criar um endpoint de VPC para o DynamoDB.

**Justificativa:**  
- **Por que essas opções?**  
  - **A:** Usar uma função IAM com permissões suficientes e configurada para ser assumida pelo pod do EKS é uma prática recomendada para garantir segurança e evitar o uso de credenciais permanentes.  
  - **D:** Um endpoint de VPC para o DynamoDB permite que o tráfego entre o aplicativo no EKS e o DynamoDB seja roteado internamente, sem expor os dados à internet.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Anexar um usuário IAM diretamente ao pod não segue as práticas recomendadas de segurança e gerenciamento de identidades.  
  - **C:** Configurar ACLs de rede ajuda, mas por si só não garante que o tráfego não passe pela internet.  
  - **E:** Incorporar as chaves de acesso no código Java é uma prática insegura que pode levar à exposição de credenciais.  

### Question #224
Uma empresa recentemente migrou seu aplicativo web para a AWS, hospedando-o em instâncias Amazon EC2 em uma única região da AWS. A empresa deseja redesenhar a arquitetura de seu aplicativo para ser altamente disponível e tolerante a falhas. O tráfego deve alcançar todas as instâncias EC2 em execução de forma aleatória.  
Quais combinações de etapas a empresa deve realizar para atender a esses requisitos? (Escolha duas.)  
A. Criar uma política de roteamento de failover no Amazon Route 53.  
B. Criar uma política de roteamento ponderado no Amazon Route 53.  
C. Criar uma política de roteamento de resposta multivalorada no Amazon Route 53.  
D. Lançar três instâncias EC2: duas instâncias em uma zona de disponibilidade e uma instância em outra zona de disponibilidade.  
E. Lançar quatro instâncias EC2: duas instâncias em uma zona de disponibilidade e duas instâncias em outra zona de disponibilidade.

**Respostas corretas:**  
**C.** Criar uma política de roteamento de resposta multivalorada no Amazon Route 53.  
**E.** Lançar quatro instâncias EC2: duas instâncias em uma zona de disponibilidade e duas instâncias em outra zona de disponibilidade.

**Justificativa:**  
- **Por que essas opções?**  
  - **C:** A política de roteamento de resposta multivalorada no Amazon Route 53 distribui o tráfego de forma aleatória entre todas as instâncias EC2 em execução, atendendo ao requisito de balanceamento de carga.  
  - **E:** Distribuir instâncias EC2 em duas zonas de disponibilidade aumenta a disponibilidade e a tolerância a falhas, garantindo que o aplicativo continue funcionando mesmo em caso de falha de uma zona de disponibilidade.  

- **Por que as outras opções não são adequadas?**  
  - **A:** A política de roteamento de failover é usada para direcionar o tráfego para um único recurso primário e não suporta balanceamento aleatório de carga.  
  - **B:** A política de roteamento ponderado direciona o tráfego com base em pesos definidos, o que não atende ao requisito de tráfego aleatório.  
  - **D:** Usar apenas três instâncias em uma configuração assimétrica não otimiza a disponibilidade nem a tolerância a falhas de forma adequada.  


### Question #225
Uma empresa de mídia coleta e analisa dados de atividade de usuários localmente. A empresa deseja migrar essa capacidade para a AWS. O repositório de dados de atividade dos usuários continuará a crescer e atingirá petabytes de tamanho. A empresa precisa criar uma solução de ingestão de dados altamente disponível que facilite análises sob demanda de dados existentes e novos com SQL.  
Qual solução atenderá a esses requisitos com a MENOR sobrecarga operacional?  
A. Enviar os dados de atividade para um stream de dados do Amazon Kinesis. Configurar o stream para entregar os dados a um bucket Amazon S3.  
B. Enviar os dados de atividade para um stream de entrega do Amazon Kinesis Data Firehose. Configurar o stream para entregar os dados a um cluster Amazon Redshift.  
C. Colocar os dados de atividade em um bucket Amazon S3. Configurar o Amazon S3 para executar uma função AWS Lambda nos dados à medida que chegam ao bucket S3.  
D. Criar um serviço de ingestão em instâncias Amazon EC2 distribuídas em várias zonas de disponibilidade. Configurar o serviço para encaminhar os dados para um banco de dados Amazon RDS Multi-AZ.

**Resposta correta:**  
**A.** Enviar os dados de atividade para um stream de dados do Amazon Kinesis. Configurar o stream para entregar os dados a um bucket Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  - Usar o Kinesis Data Streams para ingestão de dados e armazená-los no Amazon S3 fornece uma solução escalável e de baixo custo. O S3 pode armazenar grandes volumes de dados (petabytes) de maneira eficiente. Para consultas SQL sob demanda, serviços como Amazon Athena podem ser usados diretamente no S3, eliminando a necessidade de um data warehouse caro.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Redshift é uma solução de data warehouse e envolve maior sobrecarga operacional, além de custos mais altos para ingestão de dados em grande escala contínua.  
  - **C:** Configurar o Lambda para processar dados diretamente do S3 não é ideal para petabytes de dados, pois pode gerar problemas de escalabilidade e custos adicionais.  
  - **D:** Gerenciar um serviço de ingestão em instâncias EC2 distribui a carga manualmente e requer mais esforço operacional, além de não ser ideal para tamanhos de dados em petabytes.  

### Question #226
Uma empresa coleta dados de milhares de dispositivos remotos usando um aplicativo de serviços web RESTful que é executado em uma instância Amazon EC2. A instância EC2 recebe os dados brutos, transforma os dados brutos e armazena todos os dados em um bucket Amazon S3. O número de dispositivos remotos aumentará para milhões em breve. A empresa precisa de uma solução altamente escalável que minimize a sobrecarga operacional.  
Quais combinações de etapas o arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)  
A. Usar o AWS Glue para processar os dados brutos no Amazon S3.  
B. Usar o Amazon Route 53 para rotear o tráfego para diferentes instâncias EC2.  
C. Adicionar mais instâncias EC2 para acomodar o aumento na quantidade de dados recebidos.  
D. Enviar os dados brutos para o Amazon Simple Queue Service (Amazon SQS). Usar instâncias EC2 para processar os dados.  
E. Usar o Amazon API Gateway para enviar os dados brutos para um stream de dados do Amazon Kinesis. Configurar o Amazon Kinesis Data Firehose para usar o stream de dados como fonte e entregar os dados ao Amazon S3.

**Respostas corretas:**  
**D.** Enviar os dados brutos para o Amazon Simple Queue Service (Amazon SQS). Usar instâncias EC2 para processar os dados.  
**E.** Usar o Amazon API Gateway para enviar os dados brutos para um stream de dados do Amazon Kinesis. Configurar o Amazon Kinesis Data Firehose para usar o stream de dados como fonte e entregar os dados ao Amazon S3.

**Justificativa:**  
- **Por que essas opções?**  
  - **D:** O Amazon SQS desacopla a ingestão de dados do processamento, garantindo escalabilidade para lidar com milhões de dispositivos e reduzindo a carga imediata nas instâncias EC2.  
  - **E:** O uso do API Gateway e do Amazon Kinesis permite ingestão altamente escalável e processamento eficiente. O Kinesis Data Firehose facilita a entrega de dados diretamente ao Amazon S3, reduzindo a sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Glue é útil para tarefas de ETL, mas não resolve o problema de escalabilidade para ingestão de dados em tempo real.  
  - **B:** O Amazon Route 53 não é projetado para balancear carga em tempo real para cenários como esse.  
  - **C:** Adicionar mais instâncias EC2 aumenta a complexidade operacional e não é uma solução escalável para lidar com milhões de dispositivos.  

### Question #227
Uma empresa precisa reter seus logs do AWS CloudTrail por 3 anos. A empresa está aplicando o CloudTrail em um conjunto de contas AWS usando o AWS Organizations a partir da conta principal. O bucket S3 de destino do CloudTrail está configurado com o S3 Versioning habilitado. Uma política de ciclo de vida do S3 está em vigor para excluir objetos atuais após 3 anos.  
Após o quarto ano de uso do bucket S3, as métricas do bucket S3 mostram que o número de objetos continua a aumentar. No entanto, o número de novos logs do CloudTrail entregues ao bucket S3 permanece consistente.  
Qual solução excluirá objetos com mais de 3 anos da maneira MAIS econômica?  
A. Configurar o trail centralizado do CloudTrail da organização para expirar objetos após 3 anos.  
B. Configurar a política de ciclo de vida do S3 para excluir versões anteriores, bem como versões atuais.  
C. Criar uma função AWS Lambda para enumerar e excluir objetos do Amazon S3 com mais de 3 anos.  
D. Configurar a conta principal como proprietária de todos os objetos entregues ao bucket S3.

**Resposta correta:**  
**B.** Configurar a política de ciclo de vida do S3 para excluir versões anteriores, bem como versões atuais.

**Justificativa:**  
- **Por que essa opção?**  
  - O S3 Versioning mantém todas as versões de objetos, incluindo as versões anteriores. A política de ciclo de vida atual está excluindo apenas as versões atuais. Ajustar a política para incluir a exclusão de versões anteriores resolverá o problema de acúmulo de objetos de maneira automática e econômica.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O CloudTrail não tem uma configuração para expirar objetos diretamente. O gerenciamento de retenção é feito no nível do bucket S3.  
  - **C:** Usar uma função AWS Lambda para gerenciar objetos é uma solução mais complexa e custosa em comparação com uma política de ciclo de vida do S3.  
  - **D:** Configurar a conta principal como proprietária dos objetos não afeta a retenção ou exclusão de versões de objetos.  


### Question #228
Uma empresa possui uma API que recebe dados em tempo real de uma frota de dispositivos de monitoramento. A API armazena esses dados em uma instância Amazon RDS para análise posterior. A quantidade de dados que os dispositivos de monitoramento enviam para a API é flutuante. Durante períodos de tráfego intenso, a API frequentemente retorna erros de timeout.  
Após uma inspeção dos logs, a empresa determinou que o banco de dados não é capaz de processar o volume de tráfego de gravação vindo da API. Um arquiteto de soluções deve minimizar o número de conexões ao banco de dados e garantir que os dados não sejam perdidos durante períodos de tráfego intenso.  
Qual solução atenderá a esses requisitos?  
A. Aumentar o tamanho da instância do banco de dados para um tipo de instância que tenha mais memória disponível.  
B. Modificar a instância do banco de dados para ser uma instância Multi-AZ. Configurar o aplicativo para gravar em todas as instâncias ativas do RDS.  
C. Modificar a API para gravar os dados recebidos em uma fila do Amazon Simple Queue Service (Amazon SQS). Usar uma função AWS Lambda invocada pelo Amazon SQS para gravar os dados da fila no banco de dados.  
D. Modificar a API para gravar os dados recebidos em um tópico do Amazon Simple Notification Service (Amazon SNS). Usar uma função AWS Lambda invocada pelo Amazon SNS para gravar os dados do tópico no banco de dados.

**Resposta correta:**  
**C.** Modificar a API para gravar os dados recebidos em uma fila do Amazon Simple Queue Service (Amazon SQS). Usar uma função AWS Lambda invocada pelo Amazon SQS para gravar os dados da fila no banco de dados.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon SQS atua como um buffer para gerenciar tráfego flutuante, desacoplando o recebimento dos dados do processamento no banco de dados. Isso reduz a pressão sobre o RDS durante períodos de tráfego intenso, garantindo que os dados não sejam perdidos. A função Lambda processa os dados da fila de forma escalável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Aumentar o tamanho da instância pode mitigar o problema temporariamente, mas não resolve a escalabilidade em períodos de alta demanda.  
  - **B:** Multi-AZ melhora a disponibilidade, mas não aumenta a capacidade de processamento de gravações.  
  - **D:** O SNS é projetado para notificação e publicação-assinatura, não para buffering de dados para processamento.  

### Question #229
Uma empresa gerencia suas próprias instâncias Amazon EC2 que executam bancos de dados MySQL. A empresa está gerenciando manualmente a replicação e o escalonamento à medida que a demanda aumenta ou diminui. A empresa precisa de uma nova solução que simplifique o processo de adicionar ou remover capacidade computacional no tier de banco de dados conforme necessário. A solução também deve oferecer desempenho, escalabilidade e durabilidade aprimorados com o mínimo de esforço operacional.  
Qual solução atende a esses requisitos?  
A. Migrar os bancos de dados para Amazon Aurora Serverless para Aurora MySQL.  
B. Migrar os bancos de dados para Amazon Aurora Serverless para Aurora PostgreSQL.  
C. Combinar os bancos de dados em um único banco de dados MySQL maior. Executar o banco de dados maior em instâncias EC2 maiores.  
D. Criar um grupo de Auto Scaling do EC2 para o tier de banco de dados. Migrar os bancos de dados existentes para o novo ambiente.

**Resposta correta:**  
**A.** Migrar os bancos de dados para Amazon Aurora Serverless para Aurora MySQL.

**Justificativa:**  
- **Por que essa opção?**  
  - O Amazon Aurora Serverless para Aurora MySQL é uma solução de banco de dados totalmente gerenciada que permite escalabilidade automática com base na demanda, reduzindo a necessidade de operações manuais. Ele oferece alta performance, durabilidade, e simplifica o gerenciamento em comparação com instâncias EC2 autogerenciadas.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Aurora Serverless para PostgreSQL não é relevante, pois a empresa já utiliza MySQL e a migração para PostgreSQL exigiria maior esforço sem atender diretamente aos requisitos.  
  - **C:** Combinar bancos de dados em um único MySQL maior não resolve os problemas de escalabilidade automática e aumenta os riscos de pontos únicos de falha.  
  - **D:** Criar um grupo de Auto Scaling para bancos de dados em EC2 aumenta a complexidade operacional e não oferece os benefícios de escalabilidade e durabilidade automática do Aurora Serverless.  


### Question #230
Uma empresa está preocupada que duas instâncias NAT em uso não sejam mais capazes de suportar o tráfego necessário para o aplicativo da empresa. Um arquiteto de soluções deseja implementar uma solução altamente disponível, tolerante a falhas e escalável automaticamente.  
O que o arquiteto de soluções deve recomendar?  
A. Remover as duas instâncias NAT e substituí-las por dois gateways NAT na mesma zona de disponibilidade.  
B. Usar grupos de Auto Scaling com balanceadores de carga de rede para as instâncias NAT em diferentes zonas de disponibilidade.  
C. Remover as duas instâncias NAT e substituí-las por dois gateways NAT em diferentes zonas de disponibilidade.  
D. Substituir as duas instâncias NAT por instâncias Spot em diferentes zonas de disponibilidade e implantar um balanceador de carga de rede.

**Resposta correta:**  
**C.** Remover as duas instâncias NAT e substituí-las por dois gateways NAT em diferentes zonas de disponibilidade.

**Justificativa:**  
- **Por que essa opção?**  
  - Os NAT gateways são serviços gerenciados pela AWS que oferecem alta disponibilidade e escalabilidade automática. Distribuir os NAT gateways em diferentes zonas de disponibilidade garante tolerância a falhas, proporcionando maior confiabilidade e disponibilidade em comparação com instâncias NAT gerenciadas manualmente.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Implementar dois NAT gateways na mesma zona de disponibilidade não oferece tolerância a falhas entre zonas.  
  - **B:** Usar Auto Scaling com balanceadores de carga para instâncias NAT adiciona complexidade operacional e não é tão eficiente quanto os NAT gateways gerenciados.  
  - **D:** Instâncias Spot não são adequadas para NAT devido à sua natureza temporária e à possibilidade de serem interrompidas.  


### Question #231 
Um aplicativo é executado em uma instância Amazon EC2 que possui um Elastic IP address na VPC A. O aplicativo precisa acessar um banco de dados na VPC B. Ambas as VPCs estão na mesma conta AWS.  
Qual solução fornecerá o acesso necessário de forma MAIS segura?  
A. Criar um grupo de segurança para a instância do banco de dados que permita todo o tráfego do endereço IP público do servidor de aplicativos na VPC A.  
B. Configurar uma conexão de emparelhamento de VPC entre a VPC A e a VPC B.  
C. Tornar a instância do banco de dados acessível publicamente. Atribuir um endereço IP público à instância do banco de dados.  
D. Lançar uma instância EC2 com um Elastic IP address na VPC B. Usar a nova instância EC2 como proxy para todas as solicitações.

**Resposta correta:**  
**B.** Configurar uma conexão de emparelhamento de VPC entre a VPC A e a VPC B.

**Justificativa:**  
- **Por que essa opção?**  
  - O VPC Peering é a solução mais segura e eficiente para permitir a comunicação privada entre VPCs na mesma conta ou entre contas. Ele evita a exposição pública dos recursos e permite o acesso direto entre as VPCs usando endereços IP privados.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Permitir tráfego do endereço IP público expõe os dados a um caminho de rede não seguro.  
  - **C:** Tornar o banco de dados publicamente acessível apresenta sérios riscos de segurança desnecessários.  
  - **D:** Usar uma instância EC2 como proxy adiciona complexidade desnecessária e não é tão seguro quanto o VPC Peering.  


### Question #232
Uma empresa opera ambientes de demonstração para seus clientes em instâncias Amazon EC2. Cada ambiente está isolado em sua própria VPC. A equipe de operações da empresa precisa ser notificada quando o acesso RDP ou SSH a um ambiente for estabelecido.  
Qual solução atenderá a esse requisito?  
A. Configurar o Amazon CloudWatch Application Insights para criar AWS Systems Manager OpsItems quando o acesso RDP ou SSH for detectado.  
B. Configurar as instâncias EC2 com um perfil de instância IAM que tenha uma função IAM com a política AmazonSSMManagedInstanceCore anexada.  
C. Publicar os logs de fluxo da VPC no Amazon CloudWatch Logs. Criar os filtros de métricas necessários. Criar um alarme de métrica do Amazon CloudWatch com uma ação de notificação para quando o alarme estiver no estado ALARM.  
D. Configurar uma regra do Amazon EventBridge para escutar eventos do tipo EC2 Instance State-change Notification. Configurar um tópico do Amazon Simple Notification Service (Amazon SNS) como um destino. Inscrever a equipe de operações no tópico.

**Resposta correta:**  
**C.** Publicar os logs de fluxo da VPC no Amazon CloudWatch Logs. Criar os filtros de métricas necessários. Criar um alarme de métrica do Amazon CloudWatch com uma ação de notificação para quando o alarme estiver no estado ALARM.

**Justificativa:**  
- **Por que essa opção?**  
  - Os logs de fluxo da VPC permitem capturar tentativas de acesso RDP ou SSH. Criar filtros de métrica no CloudWatch Logs permite identificar esses eventos e configurar um alarme para notificar a equipe de operações quando o acesso for detectado. Essa solução é eficiente e diretamente focada no monitoramento de conexões de rede.

- **Por que as outras opções não são adequadas?**  
  - **A:** O CloudWatch Application Insights não é projetado para monitorar diretamente conexões RDP ou SSH.  
  - **B:** Configurar a política AmazonSSMManagedInstanceCore habilita o Systems Manager, mas não atende diretamente ao requisito de notificar sobre conexões RDP ou SSH.  
  - **D:** As notificações de mudança de estado do EC2 monitoram alterações no estado da instância (como iniciar ou parar), mas não capturam conexões RDP ou SSH.  


### Question #233
Um arquiteto de soluções criou uma nova conta AWS e deve proteger o acesso do usuário root da conta AWS.  
Quais combinações de ações realizarão essa tarefa? (Escolha duas.)  
A. Garantir que o usuário root use uma senha forte.  
B. Habilitar a autenticação multifator para o usuário root.  
C. Armazenar as chaves de acesso do usuário root em um bucket Amazon S3 criptografado.  
D. Adicionar o usuário root a um grupo contendo permissões administrativas.  
E. Aplicar as permissões necessárias ao usuário root com um documento de política inline.

**Respostas corretas:**  
**A.** Garantir que o usuário root use uma senha forte.  
**B.** Habilitar a autenticação multifator para o usuário root.

**Justificativa:**  
- **Por que essas opções?**  
  - **A:** Garantir que o usuário root use uma senha forte é uma prática recomendada para proteger a conta contra acessos não autorizados.  
  - **B:** Habilitar a autenticação multifator (MFA) adiciona uma camada extra de segurança ao acesso root, protegendo a conta contra comprometimentos, mesmo que a senha seja comprometida.

- **Por que as outras opções não são adequadas?**  
  - **C:** Armazenar as chaves de acesso do usuário root é uma prática não recomendada, já que o uso de chaves de acesso do root deve ser evitado.  
  - **D:** O usuário root não pode ser adicionado a grupos IAM, pois ele possui permissões irrestritas inerentes.  
  - **E:** Não é necessário aplicar políticas ao usuário root, já que ele já possui todas as permissões inerentemente.  

### Question #234
Uma empresa está desenvolvendo um novo aplicativo web de gerenciamento de relacionamento com clientes. O aplicativo usará várias instâncias Amazon EC2 com volumes Amazon Elastic Block Store (Amazon EBS) por trás de um Application Load Balancer (ALB). O aplicativo também usará um banco de dados Amazon Aurora. Todos os dados do aplicativo devem ser criptografados em repouso e em trânsito.  
Qual solução atenderá a esses requisitos?  
A. Usar certificados do AWS Key Management Service (AWS KMS) no ALB para criptografar dados em trânsito. Usar o AWS Certificate Manager (ACM) para criptografar os volumes EBS e o armazenamento do banco de dados Aurora em repouso.  
B. Usar a conta root da AWS para fazer login no Console de Gerenciamento da AWS. Fazer upload dos certificados de criptografia da empresa. Enquanto estiver na conta root, selecionar a opção para ativar a criptografia para todos os dados em repouso e em trânsito na conta.  
C. Usar o AWS Key Management Service (AWS KMS) para criptografar os volumes EBS e o armazenamento do banco de dados Aurora em repouso. Anexar um certificado do AWS Certificate Manager (ACM) ao ALB para criptografar dados em trânsito.  
D. Usar o BitLocker para criptografar todos os dados em repouso. Importar as chaves de certificado TLS da empresa para o AWS Key Management Service (AWS KMS). Anexar as chaves do KMS ao ALB para criptografar dados em trânsito.

**Resposta correta:**  
**C.** Usar o AWS Key Management Service (AWS KMS) para criptografar os volumes EBS e o armazenamento do banco de dados Aurora em repouso. Anexar um certificado do AWS Certificate Manager (ACM) ao ALB para criptografar dados em trânsito.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS KMS é a solução recomendada para gerenciar chaves de criptografia e proteger dados em repouso, como volumes EBS e armazenamento Aurora. O ACM fornece certificados SSL/TLS gerenciados para criptografar dados em trânsito através do ALB. Essa combinação atende aos requisitos de segurança para criptografia de dados em repouso e em trânsito.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS KMS não é usado para gerenciar certificados em trânsito; isso é responsabilidade do ACM.  
  - **B:** Não existe uma configuração global para criptografar automaticamente todos os dados em uma conta AWS. Usar a conta root é uma prática insegura.  
  - **D:** BitLocker não é uma solução nativa da AWS e não se aplica ao ambiente AWS. Importar chaves TLS para o KMS não é necessário, pois o ACM já gerencia essa funcionalidade.  


### Question #235
Uma empresa está migrando seu banco de dados Oracle on-premises para o Amazon Aurora PostgreSQL. O banco de dados possui várias aplicações que gravam nas mesmas tabelas. As aplicações precisam ser migradas uma a uma, com um mês de intervalo entre cada migração. A gerência expressou preocupação de que o banco de dados tenha um alto número de leituras e gravações. Os dados devem ser mantidos em sincronia entre os dois bancos de dados durante a migração.  
O que o arquiteto de soluções deve recomendar?  
A. Usar o AWS DataSync para a migração inicial. Usar o AWS Database Migration Service (AWS DMS) para criar uma tarefa de replicação com captura de dados alterados (CDC) e um mapeamento de tabelas para selecionar todas as tabelas.  
B. Usar o AWS DataSync para a migração inicial. Usar o AWS Database Migration Service (AWS DMS) para criar uma tarefa de carga completa mais captura de dados alterados (CDC) e um mapeamento de tabelas para selecionar todas as tabelas.  
C. Usar a AWS Schema Conversion Tool com o AWS Database Migration Service (AWS DMS) utilizando uma instância de replicação otimizada para memória. Criar uma tarefa de carga completa mais captura de dados alterados (CDC) e um mapeamento de tabelas para selecionar todas as tabelas.  
D. Usar a AWS Schema Conversion Tool com o AWS Database Migration Service (AWS DMS) utilizando uma instância de replicação otimizada para computação. Criar uma tarefa de carga completa mais captura de dados alterados (CDC) e um mapeamento de tabelas para selecionar as maiores tabelas.

**Resposta correta:**  
**C.** Usar a AWS Schema Conversion Tool com o AWS Database Migration Service (AWS DMS) utilizando uma instância de replicação otimizada para memória. Criar uma tarefa de carga completa mais captura de dados alterados (CDC) e um mapeamento de tabelas para selecionar todas as tabelas.

**Justificativa:**  
- **Por que essa opção?**  
  - A AWS Schema Conversion Tool ajuda a converter o esquema de Oracle para PostgreSQL, permitindo compatibilidade no Aurora PostgreSQL. Usar o AWS DMS com uma tarefa de carga completa mais CDC permite sincronizar os dados entre os bancos de dados durante a migração, garantindo consistência enquanto as aplicações são migradas uma a uma. Uma instância otimizada para memória é adequada para cargas de trabalho intensivas com alto número de leituras e gravações.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS DataSync não é projetado para replicação contínua ou sincronização com CDC; ele é mais adequado para transferência de dados em massa única.  
  - **B:** O DataSync é desnecessário neste caso, pois o AWS DMS já pode lidar com a carga inicial e a replicação contínua.  
  - **D:** Focar apenas nas maiores tabelas não garante que todas as tabelas estejam sincronizadas, o que pode causar inconsistências de dados.  


### Question #236
Uma empresa possui um aplicativo de três camadas para compartilhamento de imagens. O aplicativo utiliza uma instância Amazon EC2 para a camada de front-end, outra instância EC2 para a camada de aplicativo e uma terceira instância EC2 para um banco de dados MySQL. Um arquiteto de soluções deve projetar uma solução escalável e altamente disponível que exija o menor número de alterações no aplicativo.  
Qual solução atende a esses requisitos?  
A. Usar o Amazon S3 para hospedar a camada de front-end. Usar funções AWS Lambda para a camada de aplicativo. Migrar o banco de dados para uma tabela do Amazon DynamoDB. Usar o Amazon S3 para armazenar e servir as imagens dos usuários.  
B. Usar ambientes AWS Elastic Beanstalk balanceados em Multi-AZ para as camadas de front-end e de aplicativo. Migrar o banco de dados para uma instância Amazon RDS com múltiplas réplicas de leitura para servir as imagens dos usuários.  
C. Usar o Amazon S3 para hospedar a camada de front-end. Usar um conjunto de instâncias EC2 em um grupo de Auto Scaling para a camada de aplicativo. Migrar o banco de dados para um tipo de instância otimizado para memória para armazenar e servir as imagens dos usuários.  
D. Usar ambientes AWS Elastic Beanstalk balanceados em Multi-AZ para as camadas de front-end e de aplicativo. Migrar o banco de dados para uma instância Amazon RDS Multi-AZ. Usar o Amazon S3 para armazenar e servir as imagens dos usuários.

**Resposta correta:**  
**D.** Usar ambientes AWS Elastic Beanstalk balanceados em Multi-AZ para as camadas de front-end e de aplicativo. Migrar o banco de dados para uma instância Amazon RDS Multi-AZ. Usar o Amazon S3 para armazenar e servir as imagens dos usuários.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Elastic Beanstalk facilita a implantação e escalabilidade das camadas de front-end e aplicativo, oferecendo alta disponibilidade com balanceamento Multi-AZ. Migrar o banco de dados para uma instância RDS Multi-AZ melhora a disponibilidade e resiliência sem a necessidade de grandes alterações no aplicativo. Usar o S3 para armazenar imagens é econômico e escalável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Migrar para AWS Lambda e DynamoDB exige mudanças significativas na arquitetura do aplicativo, o que não atende ao requisito de menor alteração.  
  - **B:** Usar múltiplas réplicas de leitura do RDS para armazenar imagens não é eficiente para grandes volumes de dados estáticos; o S3 é mais adequado para isso.  
  - **C:** Usar instâncias otimizadas para memória não resolve problemas de escalabilidade e alta disponibilidade da camada de banco de dados.  


### Question #237
Um aplicativo executado em uma instância Amazon EC2 na VPC-A precisa acessar arquivos em outra instância EC2 na VPC-B. Ambas as VPCs estão em contas AWS separadas. O administrador de rede precisa projetar uma solução para configurar o acesso seguro à instância EC2 na VPC-B a partir da VPC-A. A conectividade não deve ter um único ponto de falha ou problemas de largura de banda.  
Qual solução atenderá a esses requisitos?  
A. Configurar uma conexão de emparelhamento de VPC entre a VPC-A e a VPC-B.  
B. Configurar endpoints de gateway VPC para a instância EC2 executada na VPC-B.  
C. Anexar um gateway privado virtual à VPC-B e configurar o roteamento da VPC-A.  
D. Criar uma interface virtual privada (VIF) para a instância EC2 executada na VPC-B e adicionar rotas apropriadas da VPC-A.

**Resposta correta:**  
**A.** Configurar uma conexão de emparelhamento de VPC entre a VPC-A e a VPC-B.

**Justificativa:**  
- **Por que essa opção?**  
  - O VPC Peering permite a comunicação segura entre duas VPCs, mesmo que estejam em contas diferentes. Ele é totalmente gerenciado pela AWS, não tem um único ponto de falha e suporta largura de banda alta entre as VPCs. É uma solução eficiente e segura para conectar instâncias EC2 em diferentes VPCs.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Endpoints de gateway VPC são usados para acessar serviços AWS, como S3 e DynamoDB, e não para comunicação direta entre instâncias EC2.  
  - **C:** Anexar um gateway privado virtual requer configuração de uma VPN ou Direct Connect, que não é necessário neste caso e adiciona complexidade desnecessária.  
  - **D:** Criar uma interface virtual privada (VIF) é apropriado para conectividade Direct Connect, mas não é adequado para comunicação entre VPCs.  


### Question #238
Uma empresa deseja experimentar contas AWS individuais para sua equipe de engenheiros. A empresa quer ser notificada assim que o uso de instâncias Amazon EC2 em um determinado mês exceder um limite específico para cada conta.  
O que um arquiteto de soluções deve fazer para atender a esse requisito de forma MAIS econômica?  
A. Usar o Cost Explorer para criar um relatório diário de custos por serviço. Filtrar o relatório por instâncias EC2. Configurar o Cost Explorer para enviar uma notificação do Amazon Simple Email Service (Amazon SES) quando um limite for excedido.  
B. Usar o Cost Explorer para criar um relatório mensal de custos por serviço. Filtrar o relatório por instâncias EC2. Configurar o Cost Explorer para enviar uma notificação do Amazon Simple Email Service (Amazon SES) quando um limite for excedido.  
C. Usar o AWS Budgets para criar um orçamento de custos para cada conta. Definir o período como mensal. Configurar o escopo para instâncias EC2. Definir um limite de alerta para o orçamento. Configurar um tópico do Amazon Simple Notification Service (Amazon SNS) para receber uma notificação quando um limite for excedido.  
D. Usar os Relatórios de Custo e Uso da AWS para criar um relatório com granularidade horária. Integrar os dados do relatório ao Amazon Athena. Usar o Amazon EventBridge para agendar uma consulta no Athena. Configurar um tópico do Amazon Simple Notification Service (Amazon SNS) para receber uma notificação quando um limite for excedido.

**Resposta correta:**  
**C.** Usar o AWS Budgets para criar um orçamento de custos para cada conta. Definir o período como mensal. Configurar o escopo para instâncias EC2. Definir um limite de alerta para o orçamento. Configurar um tópico do Amazon Simple Notification Service (Amazon SNS) para receber uma notificação quando um limite for excedido.

**Justificativa:**  
- **Por que essa opção?**  
  - O AWS Budgets permite definir orçamentos e limites de custo de maneira granular para diferentes serviços, como instâncias EC2. Ele notifica automaticamente os administradores por meio do Amazon SNS quando um limite é excedido, fornecendo um método econômico e fácil de configurar para monitorar custos.  

- **Por que as outras opções não são adequadas?**  
  - **A/B:** O Cost Explorer não suporta notificações automáticas diretamente; ele é usado para análise manual de custos.  
  - **D:** Os Relatórios de Custo e Uso com integração ao Athena e EventBridge adicionam complexidade e custos desnecessários para este caso de uso simples.  


### Question #239
Um arquiteto de soluções precisa projetar um novo microsserviço para o aplicativo de uma empresa. Os clientes devem ser capazes de chamar um endpoint HTTPS para acessar o microsserviço. O microsserviço também deve usar AWS Identity and Access Management (IAM) para autenticar chamadas. O arquiteto de soluções escreverá a lógica para este microsserviço usando uma única função AWS Lambda escrita em Go 1.x.  
Qual solução implantará a função da maneira MAIS eficiente operacionalmente?  
A. Criar uma API REST no Amazon API Gateway. Configurar o método para usar a função Lambda. Habilitar autenticação IAM na API.  
B. Criar uma URL da função Lambda para a função. Especificar AWS_IAM como o tipo de autenticação.  
C. Criar uma distribuição Amazon CloudFront. Implantar a função no Lambda@Edge. Integrar a lógica de autenticação IAM na função Lambda@Edge.  
D. Criar uma distribuição Amazon CloudFront. Implantar a função no CloudFront Functions. Especificar AWS_IAM como o tipo de autenticação.

**Resposta correta:**  
**B.** Criar uma URL da função Lambda para a função. Especificar AWS_IAM como o tipo de autenticação.

**Justificativa:**  
- **Por que essa opção?**  
  - Criar uma URL da função Lambda permite que os clientes chamem diretamente o endpoint HTTPS gerado pela URL, reduzindo a complexidade e os custos operacionais. Especificar o tipo de autenticação como AWS_IAM garante que a autenticação seja feita de forma segura usando permissões IAM, atendendo aos requisitos de segurança.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o API Gateway adiciona complexidade operacional e custo desnecessário quando uma URL da função Lambda é suficiente para esse caso de uso.  
  - **C:** O Lambda@Edge é projetado para processamento no nível da borda, o que é desnecessário para um microsserviço que não requer distribuição global.  
  - **D:** O CloudFront Functions é mais adequado para manipulações simples de solicitações e não suporta a execução de lógica complexa como a necessária para o microsserviço.  


### Question #240
Uma empresa migrou anteriormente sua solução de data warehouse para a AWS. A empresa também possui uma conexão AWS Direct Connect. Os usuários do escritório corporativo consultam o data warehouse usando uma ferramenta de visualização. O tamanho médio de uma consulta retornada pelo data warehouse é de 50 MB, e cada página da web enviada pela ferramenta de visualização tem aproximadamente 500 KB. Os conjuntos de resultados retornados pelo data warehouse não são armazenados em cache.  
Qual solução fornece o menor custo de saída de transferência de dados para a empresa?  
A. Hospedar a ferramenta de visualização no local e consultar o data warehouse diretamente pela internet.  
B. Hospedar a ferramenta de visualização na mesma região da AWS que o data warehouse. Acessá-la pela internet.  
C. Hospedar a ferramenta de visualização no local e consultar o data warehouse diretamente por uma conexão Direct Connect em um local na mesma região da AWS.  
D. Hospedar a ferramenta de visualização na mesma região da AWS que o data warehouse e acessá-la por uma conexão Direct Connect em um local na mesma região.

**Resposta correta:**  
**D.** Hospedar a ferramenta de visualização na mesma região da AWS que o data warehouse e acessá-la por uma conexão Direct Connect em um local na mesma região.

**Justificativa:**  
- **Por que essa opção?**  
  - Hospedar a ferramenta de visualização na mesma região que o data warehouse elimina a maior parte dos custos de saída de dados. Usar uma conexão Direct Connect para acessar os dados garante alta velocidade e reduz os custos de saída em comparação com a internet pública.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Consultar o data warehouse pela internet incorre em custos de saída de dados mais altos, pois os resultados das consultas são grandes (50 MB).  
  - **B:** Mesmo hospedando a ferramenta na mesma região da AWS, acessar os dados pela internet pública ainda implica custos de transferência de saída.  
  - **C:** Consultar o data warehouse por Direct Connect de um local no local adiciona custos de saída de dados do AWS Direct Connect, o que pode ser mais caro do que acessar diretamente dentro da mesma região.  

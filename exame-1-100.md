### Questão 1
Uma empresa coleta dados de temperatura, umidade e pressão atmosférica em cidades de vários continentes. O volume médio de dados coletados diariamente de cada local é de 500 GB. Cada local tem uma conexão de Internet de alta velocidade.
A empresa deseja agregar os dados de todos esses locais globais o mais rápido possível em um único bucket do Amazon S3. A solução deve minimizar a complexidade operacional.
Qual solução atende a esses requisitos?

A. Ative o S3 Transfer Acceleration no bucket de destino do S3. Use uploads multipart para carregar os dados do local diretamente no bucket de destino do S3.

B. Carregue os dados de cada local em um bucket do S3 na região mais próxima. Use a replicação entre regiões do S3 para copiar os objetos para o bucket de destino. Em seguida, remova os dados do bucket de origem.

C. Agende tarefas diárias de dispositivos AWS Snowball Edge Storage Optimized para transferir dados de cada local para a região mais próxima. Use a replicação entre regiões do S3 para copiar os objetos para o bucket de destino.

D. Carregue os dados de cada local em uma instância do Amazon EC2 na região mais próxima. Armazene os dados em um volume do Amazon Elastic Block Store (Amazon EBS). Em intervalos regulares, tire um snapshot do EBS e copie-o para a região que contém o bucket de destino do S3.

<details>

<summary>Resposta</summary>


**Resposta correta:**  
**A.** Ative o S3 Transfer Acceleration no bucket de destino do S3. Use uploads em várias partes para carregar diretamente os dados do local no bucket de destino do S3.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Transfer Acceleration permite transferências globais mais rápidas para buckets do Amazon S3 ao alavancar a rede de borda da AWS. Ele reduz a latência e acelera o envio de dados, especialmente útil para o volume diário alto (500 GB). O upload em várias partes melhora a eficiência da transferência de arquivos grandes.

- **Por que as outras opções não são adequadas?**  
  - **B:** Embora Cross-Region Replication agregue os dados, ele adiciona complexidade operacional ao exigir buckets regionais intermediários e não é a solução mais rápida para transferência direta.  
  - **C:** O AWS Snowball é eficiente para grandes volumes offline, mas aqui o requisito é rapidez com conectividade de alta velocidade.  
  - **D:** Usar instâncias EC2 e snapshots de EBS é desnecessariamente complexo para um problema resolvível com recursos do S3.

</details>

---

### Questão 2
Uma empresa precisa da capacidade de analisar os arquivos de log de seu aplicativo proprietário. Os logs são armazenados no formato JSON em um bucket do Amazon S3. As consultas serão simples e executadas sob demanda. Um arquiteto de soluções precisa realizar a análise com mínimas alterações na arquitetura existente.
O que o arquiteto de soluções deve fazer para atender a esses requisitos com o menor esforço operacional?

A. Use o Amazon Redshift para carregar todo o conteúdo em um único local e executar as consultas SQL conforme necessário.

B. Use o Amazon CloudWatch Logs para armazenar os logs. Execute as consultas SQL conforme necessário a partir do console do Amazon CloudWatch.

C. Use o Amazon Athena diretamente com o Amazon S3 para executar as consultas conforme necessário.

D. Use o AWS Glue para catalogar os logs. Use um cluster transitório do Apache Spark no Amazon EMR para executar as consultas SQL conforme necessário.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use Amazon Athena diretamente com o Amazon S3 para executar as consultas conforme necessário.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon Athena permite consultas SQL sob demanda diretamente nos dados armazenados no S3, sem necessidade de infraestrutura adicional, minimizando a sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Redshift é excessivo para consultas simples e adiciona complexidade desnecessária.  
  - **B:** O Amazon CloudWatch Logs não suporta diretamente consultas SQL nos dados do S3.  
  - **D:** O AWS Glue com EMR é uma solução mais complexa e cara para o caso apresentado.  
</details>

---


### Questão 3
Uma empresa usa o AWS Organizations para gerenciar várias contas da AWS para diferentes departamentos. A conta de gerenciamento tem um bucket do Amazon S3 que contém relatórios de projetos. A empresa deseja limitar o acesso a esse bucket do S3 apenas aos usuários de contas dentro da organização no AWS Organizations.
Qual solução atende a esses requisitos com o menor esforço operacional?

A. Adicione a chave de condição global aws:PrincipalOrgID com uma referência ao ID da organização na política do bucket do S3.

B. Crie uma unidade organizacional (OU) para cada departamento. Adicione a chave de condição global aws:PrincipalOrgPaths à política do bucket do S3.

C. Use o AWS CloudTrail para monitorar os eventos CreateAccount, InviteAccountToOrganization, LeaveOrganization e RemoveAccountFromOrganization. Atualize a política do bucket do S3 conforme necessário.

D. Etiquete cada usuário que precisa de acesso ao bucket do S3. Adicione a chave de condição global aws:PrincipalTag à política do bucket do S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Adicione a chave global `aws:PrincipalOrgID` com referência ao ID da organização na política do bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  A chave `aws:PrincipalOrgID` limita o acesso ao bucket apenas para usuários dentro da organização no AWS Organizations, com baixa sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** `aws:PrincipalOrgPaths` exige uma estrutura complexa de OUs desnecessária.  
  - **C:** Monitorar eventos com CloudTrail é uma abordagem reativa, não preventiva.  
  - **D:** Usar tags de usuários adiciona mais complexidade para gerenciar acessos.  


</details>

---

### Questão 4
Um aplicativo executado em uma instância do Amazon EC2 em uma VPC processa logs armazenados em um bucket do Amazon S3. A instância do EC2 precisa acessar o bucket do S3 sem conectividade com a Internet.
Qual solução fornecerá conectividade de rede privada ao Amazon S3?

A. Crie um endpoint de gateway da VPC para o bucket do S3.

B. Transmita os logs para o Amazon CloudWatch Logs. Exporte os logs para o bucket do S3.

C. Crie um perfil de instância no Amazon EC2 para permitir o acesso ao S3.

D. Crie uma API Gateway do Amazon com um link privado para acessar o endpoint do S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Crie um endpoint VPC Gateway para o bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway permite conectividade privada com o S3 sem a necessidade de acesso à Internet, reduzindo custos e melhorando a segurança.  

- **Por que as outras opções não são adequadas?**  
  - **B:** CloudWatch Logs não substitui o acesso privado ao S3.  
  - **C:** Um perfil de instância fornece permissões, mas não conectividade privada.  
  - **D:** API Gateway com PrivateLink é excessivo e mais caro.  


</details>

---

### Questão 5
Uma empresa está hospedando um aplicativo web na AWS usando uma única instância do Amazon EC2 que armazena documentos enviados por usuários em um volume do Amazon EBS. Para melhor escalabilidade e disponibilidade, a empresa duplicou a arquitetura e criou uma segunda instância do EC2 e um volume do EBS em outra zona de disponibilidade, colocando ambos atrás de um Application Load Balancer. Após concluir essa alteração, os usuários relataram que, cada vez que atualizavam o site, podiam ver um subconjunto de seus documentos ou outro, mas nunca todos os documentos ao mesmo tempo.
O que um arquiteto de soluções deve propor para garantir que os usuários vejam todos os seus documentos de uma só vez?

A. Copie os dados para que ambos os volumes do EBS contenham todos os documentos.

B. Configure o Application Load Balancer para direcionar o usuário ao servidor com os documentos.

C. Copie os dados de ambos os volumes do EBS para o Amazon EFS. Modifique o aplicativo para salvar novos documentos no Amazon EFS.

D. Configure o Application Load Balancer para enviar a solicitação para ambos os servidores. Retorne cada documento do servidor correto.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Copie os dados de ambos os volumes EBS para o Amazon EFS. Modifique a aplicação para salvar novos documentos no Amazon EFS.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon EFS oferece armazenamento compartilhado, consistente e acessível por múltiplas instâncias, garantindo que todos os documentos fiquem disponíveis.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Copiar manualmente os dados não resolve o problema de consistência em tempo real.  
  - **B:** Configurar o ALB para direcionar solicitações não resolve a inconsistência de dados.  
  - **D:** Direcionar solicitações para servidores específicos aumenta a complexidade e não consolida os documentos.  


</details>

---

### Questão 6
Uma empresa usa o NFS para armazenar grandes arquivos de vídeo em armazenamento anexado à rede (NAS) no local. Cada arquivo de vídeo varia em tamanho de 1 MB a 500 GB. O armazenamento total é de 70 TB e não está mais crescendo. A empresa decide migrar os arquivos de vídeo para o Amazon S3. A empresa deve migrar os arquivos de vídeo o mais rápido possível enquanto usa o menor consumo possível de largura de banda de rede.
Qual solução atenderá a esses requisitos?

A. Crie um bucket do S3. Crie uma função IAM com permissões para gravar no bucket do S3. Use a AWS CLI para copiar todos os arquivos localmente para o bucket do S3.

B. Crie uma tarefa AWS Snowball Edge. Receba um dispositivo Snowball Edge no local. Use o cliente Snowball Edge para transferir dados para o dispositivo. Retorne o dispositivo para que a AWS possa importar os dados para o Amazon S3.

C. Implemente um S3 File Gateway no local. Crie um endpoint de serviço público para conectar-se ao S3 File Gateway. Crie um bucket do S3. Crie um novo compartilhamento de arquivos NFS no S3 File Gateway. Direcione o novo compartilhamento de arquivos para o bucket do S3. Transfira os dados do compartilhamento de arquivos NFS existente para o S3 File Gateway.

D. Configure uma conexão AWS Direct Connect entre a rede local e a AWS. Implante um S3 File Gateway no local. Crie uma interface virtual pública (VIF) para conectar-se ao S3 File Gateway. Crie um bucket do S3. Crie um novo compartilhamento de arquivos NFS no S3 File Gateway. Direcione o novo compartilhamento de arquivos para o bucket do S3. Transfira os dados do compartilhamento de arquivos NFS existente para o S3 File Gateway.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Crie um trabalho AWS Snowball Edge. Receba um dispositivo Snowball Edge no local e use o cliente para transferir os dados para o dispositivo.

**Justificativa:**  
- **Por que essa opção?**  
  O Snowball Edge é ideal para transferências rápidas de grandes volumes de dados com largura de banda limitada, minimizando o uso de rede.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Copiar dados via CLI consome muita largura de banda.  
  - **C:** S3 File Gateway não é ideal para transferências massivas.  
  - **D:** Direct Connect exige mais tempo para configuração e custos contínuos.  

</details>

---

### Questão 7
Uma empresa possui um aplicativo que ingere mensagens recebidas. Dezenas de outros aplicativos e microsserviços então consomem rapidamente essas mensagens. O número de mensagens varia drasticamente e, às vezes, aumenta repentinamente para 100.000 por segundo. A empresa deseja desacoplar a solução e aumentar a escalabilidade.
Qual solução atende a esses requisitos?

A. Persistir as mensagens no Amazon Kinesis Data Analytics. Configurar os aplicativos consumidores para ler e processar as mensagens.

B. Implantar o aplicativo de ingestão em instâncias Amazon EC2 em um grupo de Auto Scaling para escalar o número de instâncias EC2 com base em métricas de CPU.

C. Gravar as mensagens no Amazon Kinesis Data Streams com um único shard. Usar uma função AWS Lambda para pré-processar as mensagens e armazená-las no Amazon DynamoDB. Configurar os aplicativos consumidores para ler do DynamoDB e processar as mensagens.

D. Publicar as mensagens em um tópico do Amazon Simple Notification Service (Amazon SNS) com várias assinaturas do Amazon Simple Queue Service (Amazon SQS). Configurar os aplicativos 

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Publique as mensagens em um tópico do Amazon SNS com várias assinaturas do Amazon SQS. Configure os consumidores para processar as mensagens das filas.

**Justificativa:**  
- **Por que essa opção?**  
  Essa solução desacopla o processamento, aumenta a escalabilidade e permite o consumo de mensagens por múltiplos consumidores sem dependência direta.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Kinesis Data Analytics não é projetado para gerenciar picos de ingestão massiva.  
  - **B:** Escalar instâncias EC2 manualmente é menos eficiente e mais custoso.  
  - **C:** Um único shard no Kinesis limita o throughput.  


</details>

---

### Questão 8
Uma empresa está migrando um aplicativo distribuído para a AWS. O aplicativo atende a cargas de trabalho variáveis. A plataforma legada consiste em um servidor principal que coordena trabalhos entre vários nós de computação. A empresa deseja modernizar o aplicativo com uma solução que maximize a resiliência e a escalabilidade.
Como um arquiteto de soluções deve projetar a arquitetura para atender a esses requisitos?

A. Configurar uma fila do Amazon Simple Queue Service (Amazon SQS) como destino para os trabalhos. Implementar os nós de computação com instâncias Amazon EC2 gerenciadas em um grupo de Auto Scaling. Configurar o Auto Scaling do EC2 para usar escalonamento programado.

B. Configurar uma fila do Amazon Simple Queue Service (Amazon SQS) como destino para os trabalhos. Implementar os nós de computação com instâncias Amazon EC2 gerenciadas em um grupo de Auto Scaling. Configurar o Auto Scaling do EC2 com base no tamanho da fila.

C. Implementar o servidor principal e os nós de computação com instâncias Amazon EC2 gerenciadas em um grupo de Auto Scaling. Configurar o AWS CloudTrail como destino para os trabalhos. Configurar o Auto Scaling do EC2 com base na carga do servidor principal.

D. Implementar o servidor principal e os nós de computação com instâncias Amazon EC2 gerenciadas em um grupo de Auto Scaling. Configurar o Amazon EventBridge (Amazon CloudWatch Events) como destino para os trabalhos. Configurar o Auto Scaling do EC2 com base na carga dos nós de computação.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Configure uma fila Amazon SQS como destino para os jobs. Implemente os nós de computação em uma Auto Scaling group de EC2.

**Justificativa:**  
- **Por que essa opção?**  
  O uso de filas SQS desacopla o processamento dos jobs e permite que a escala dos nós EC2 seja baseada no tamanho da fila, maximizando a resiliência e escalabilidade.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O agendamento fixo de escala não responde a mudanças de carga.  
  - **C:** CloudTrail não é adequado como destino de jobs.  
  - **D:** EventBridge é mais indicado para eventos, não para filas de processamento massivo.  


</details>

---

### Questão 9
Uma empresa está operando um servidor de arquivos SMB em seu data center. O servidor armazena grandes arquivos que são frequentemente acessados nos primeiros dias após sua criação. Após 7 dias, os arquivos raramente são acessados.
O volume total de dados está aumentando e está próximo à capacidade total de armazenamento da empresa. Um arquiteto de soluções deve aumentar o espaço de armazenamento disponível da empresa sem perder o acesso de baixa latência aos arquivos acessados recentemente. O arquiteto de soluções também deve fornecer um gerenciamento do ciclo de vida dos arquivos para evitar problemas futuros de armazenamento.
Qual solução atenderá a esses requisitos?

A. Usar o AWS DataSync para copiar dados com mais de 7 dias do servidor de arquivos SMB para a AWS.

B. Criar um Amazon S3 File Gateway para estender o espaço de armazenamento da empresa. Criar uma política de ciclo de vida do S3 para fazer a transição dos dados para o S3 Glacier Deep Archive após 7 dias.

C. Criar um sistema de arquivos Amazon FSx for Windows File Server para estender o espaço de armazenamento da empresa.

D. Instalar um utilitário em cada computador de usuário para acessar o Amazon S3. Criar uma política de ciclo de vida do S3 para fazer a transição dos dados para o S3 Glacier Flexible Retrieval após 7 dias.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Crie um Amazon S3 File Gateway para expandir o espaço de armazenamento. Configure uma política de ciclo de vida no S3 para mover os dados para o S3 Glacier Deep Archive após 7 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 File Gateway permite acesso de baixa latência para arquivos recentes e armazenamento econômico para arquivos antigos no S3 Glacier Deep Archive.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O DataSync é útil para migração de dados, mas não suporta acesso contínuo e eficiente.  
  - **C:** FSx oferece alta disponibilidade, mas com maior custo em comparação ao S3.  
  - **D:** Um utilitário direto não é suficiente para gerenciar o ciclo de vida dos arquivos.  


</details>

---

### Questão 10
Uma empresa está criando um aplicativo web de comércio eletrônico na AWS. O aplicativo envia informações sobre novos pedidos para uma API REST do Amazon API Gateway para processamento. A empresa deseja garantir que os pedidos sejam processados na ordem em que são recebidos.
Qual solução atenderá a esses requisitos?

A. Usar uma integração do API Gateway para publicar uma mensagem em um tópico do Amazon Simple Notification Service (Amazon SNS) quando o aplicativo receber um pedido. Inscrever uma função AWS Lambda no tópico para realizar o processamento.

B. Usar uma integração do API Gateway para enviar uma mensagem para uma fila FIFO do Amazon Simple Queue Service (Amazon SQS) quando o aplicativo receber um pedido. Configurar a fila FIFO do SQS para invocar uma função AWS Lambda para processamento.

C. Usar um autorizador do API Gateway para bloquear quaisquer solicitações enquanto o aplicativo processa um pedido.

D. Usar uma integração do API Gateway para enviar uma mensagem para uma fila padrão do Amazon Simple Queue Service (Amazon SQS) quando o aplicativo receber um pedido. Configurar a fila padrão do SQS para invocar uma função AWS Lambda para processamento.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use uma integração com o API Gateway para enviar mensagens para uma fila FIFO do Amazon SQS ao receber pedidos.

**Justificativa:**  
- **Por que essa opção?**  
  Uma fila FIFO do SQS garante a ordenação das mensagens, o que é essencial para processar os pedidos na sequência em que foram recebidos.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O SNS não garante a ordenação das mensagens.  
  - **C:** Bloquear requisições durante o processamento adiciona latência desnecessária.  
  - **D:** Uma fila SQS padrão não oferece garantia de ordenação.  


</details>

---

### Questão 11
Uma empresa tem um aplicativo que é executado em instâncias Amazon EC2 e utiliza um banco de dados Amazon Aurora. As instâncias EC2 conectam-se ao banco de dados utilizando nomes de usuários e senhas armazenados localmente em um arquivo. A empresa deseja minimizar o esforço operacional relacionado ao gerenciamento de credenciais.
O que um arquiteto de soluções deve fazer para alcançar esse objetivo?

A. Usar o AWS Secrets Manager. Ativar a rotação automática.

B. Usar o AWS Systems Manager Parameter Store. Ativar a rotação automática.

C. Criar um bucket Amazon S3 para armazenar objetos criptografados com uma chave de criptografia do AWS Key Management Service (AWS KMS). Migrar o arquivo de credenciais para o bucket S3. Apontar o aplicativo para o bucket S3.

D. Criar um volume criptografado Amazon Elastic Block Store (Amazon EBS) para cada instância EC2. Anexar o novo volume EBS a cada instância EC2. Migrar o arquivo de credenciais para o novo volume EBS. Apontar o aplicativo para o novo volume EBS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Use o AWS Secrets Manager. Ative a rotação automática.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager simplifica o gerenciamento de credenciais, incluindo a rotação automática, reduzindo a sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Parameter Store não inclui rotação automática de credenciais.  
  - **C:** Usar o S3 para armazenamento é menos seguro e complexo para integração.  
  - **D:** Volumes EBS não gerenciam credenciais automaticamente.  


</details>

---

### Questão 12
Uma empresa global hospeda seu aplicativo web em instâncias Amazon EC2 atrás de um Application Load Balancer (ALB). O aplicativo web possui dados estáticos e dinâmicos. A empresa armazena seus dados estáticos em um bucket do Amazon S3. A empresa deseja melhorar o desempenho e reduzir a latência para os dados estáticos e dinâmicos. A empresa utiliza seu próprio nome de domínio registrado no Amazon Route 53.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Criar uma distribuição Amazon CloudFront que tenha o bucket S3 e o ALB como origens. Configurar o Route 53 para rotear o tráfego para a distribuição CloudFront.

B. Criar uma distribuição Amazon CloudFront que tenha o ALB como origem. Criar um acelerador padrão do AWS Global Accelerator que tenha o bucket S3 como endpoint. Configurar o Route 53 para rotear o tráfego para a distribuição CloudFront.

C. Criar uma distribuição Amazon CloudFront que tenha o bucket S3 como origem. Criar um acelerador padrão do AWS Global Accelerator que tenha o ALB e a distribuição CloudFront como endpoints. Criar um nome de domínio personalizado que aponte para o nome DNS do acelerador. Usar o nome de domínio personalizado como um endpoint para o aplicativo web.

D. Criar uma distribuição Amazon CloudFront que tenha o ALB como origem. Criar um acelerador padrão do AWS Global Accelerator que tenha o bucket S3 como endpoint. Criar dois nomes de domínio. Apontar um nome de domínio para o nome DNS do CloudFront para conteúdo dinâmico. Apontar o outro nome de domínio para o nome DNS do acelerador para conteúdo estático. Usar os nomes de domínio como endpoints para o aplicativo web.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Crie uma distribuição Amazon CloudFront com o bucket S3 e o ALB como origens. Configure o Route 53 para rotear o tráfego para a distribuição CloudFront.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront melhora o desempenho global e reduz a latência para conteúdo estático e dinâmico ao usar pontos de presença distribuídos.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Global Accelerator não é necessário quando o CloudFront já gerencia desempenho.  
  - **C:** Configurar múltiplos endpoints adiciona complexidade desnecessária.  
  - **D:** Dividir origens dinâmicas e estáticas não garante latência otimizada.  


</details>

---

### Questão 13
Uma empresa realiza manutenção mensal em sua infraestrutura AWS. Durante essas atividades de manutenção, a empresa precisa rodar as credenciais de seus bancos de dados Amazon RDS para MySQL em várias Regiões da AWS.
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?

A. Armazenar as credenciais como segredos no AWS Secrets Manager. Usar a replicação de segredos multi-Região para as Regiões necessárias. Configurar o Secrets Manager para rodar os segredos em um cronograma.

B. Armazenar as credenciais como segredos no AWS Systems Manager criando um parâmetro de string segura. Usar a replicação de segredos multi-Região para as Regiões necessárias. Configurar o Systems Manager para rodar os segredos em um cronograma.

C. Armazenar as credenciais em um bucket Amazon S3 com criptografia do lado do servidor (SSE) ativada. Usar o Amazon EventBridge (Amazon CloudWatch Events) para invocar uma função AWS Lambda para rodar as credenciais.

D. Criptografar as credenciais como segredos usando chaves gerenciadas pelo cliente multi-Região do AWS Key Management Service (AWS KMS). Armazenar os segredos em uma tabela global do Amazon DynamoDB. Usar uma função AWS Lambda para recuperar os segredos do DynamoDB e usar a API do RDS para rodar os segredos.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Armazene as credenciais como segredos no AWS Secrets Manager. Use replicação multi-região e configure a rotação automática.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager simplifica a rotação e replicação de segredos em múltiplas regiões com mínima sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O Parameter Store não possui suporte direto para rotação automática de segredos em várias regiões.  
  - **C:** Usar S3 com eventos EventBridge adiciona complexidade desnecessária.  
  - **D:** DynamoDB e Lambda introduzem mais componentes sem vantagens significativas.  


</details>

---

### Questão 14
Uma empresa executa um aplicativo de comércio eletrônico em instâncias Amazon EC2 atrás de um Application Load Balancer. As instâncias operam em um grupo de Auto Scaling do Amazon EC2 em várias Zonas de Disponibilidade. O grupo de Auto Scaling escala com base nas métricas de utilização de CPU. O aplicativo de comércio eletrônico armazena os dados de transação em um banco de dados MySQL 8.0 hospedado em uma instância EC2 grande.
O desempenho do banco de dados degrada rapidamente à medida que a carga do aplicativo aumenta. O aplicativo lida com mais solicitações de leitura do que transações de gravação. A empresa deseja uma solução que escale automaticamente o banco de dados para atender à demanda de cargas de trabalho de leitura imprevisíveis enquanto mantém alta disponibilidade.
Qual solução atenderá a esses requisitos?

A. Usar o Amazon Redshift com um único nó para funcionalidades de líder e computação.

B. Usar o Amazon RDS com uma implantação de Zona Única (Single-AZ). Configurar o Amazon RDS para adicionar instâncias de leitura em uma Zona de Disponibilidade diferente.

C. Usar o Amazon Aurora com uma implantação Multi-AZ. Configurar o Aurora Auto Scaling com Réplicas Aurora.

D. Usar o Amazon ElastiCache para Memcached com instâncias Spot do EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use Amazon Aurora com uma implantação Multi-AZ. Configure Auto Scaling com réplicas Aurora.

**Justificativa:**  
- **Por que essa opção?**  
  Aurora Multi-AZ oferece alta disponibilidade e escalabilidade automática, ideal para cargas de leitura imprevisíveis.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Redshift não é projetado para cargas OLTP.  
  - **B:** Uma implantação Single-AZ não garante alta disponibilidade.  
  - **D:** ElastiCache não substitui o banco de dados relacional.  


</details>

---

### Questão 15
Uma empresa recentemente migrou para a AWS e deseja implementar uma solução para proteger o tráfego que entra e sai da VPC de produção. A empresa tinha um servidor de inspeção em seu data center on-premises que realizava operações específicas, como inspeção e filtragem de tráfego. A empresa deseja ter as mesmas funcionalidades na AWS.
Qual solução atenderá a esses requisitos?

A. Usar o Amazon GuardDuty para inspeção e filtragem de tráfego na VPC de produção.

B. Usar o Traffic Mirroring para espelhar o tráfego da VPC de produção para inspeção e filtragem de tráfego.

C. Usar o AWS Network Firewall para criar as regras necessárias para inspeção e filtragem de tráfego na VPC de produção.

D. Usar o AWS Firewall Manager para criar as regras necessárias para inspeção e filtragem de tráfego na VPC de produção.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use o AWS Network Firewall para criar as regras necessárias para inspeção e filtragem de tráfego.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Network Firewall é um serviço gerenciado que oferece inspeção e filtragem centralizada de tráfego.  

- **Por que as outras opções não são adequadas?**  
  - **A:** GuardDuty apenas detecta ameaças, mas não filtra tráfego.  
  - **B:** Traffic Mirroring não implementa inspeção ativa.  
  - **D:** Firewall Manager gerencia políticas, mas depende de outros serviços para inspeção.  


</details>

---

### Questão 16
Uma empresa hospeda um data lake na AWS. O data lake consiste em dados no Amazon S3 e no Amazon RDS para PostgreSQL. A empresa precisa de uma solução de relatórios que forneça visualização de dados e inclua todas as fontes de dados no data lake. Somente a equipe de gestão da empresa deve ter acesso total a todas as visualizações. O restante da empresa deve ter apenas acesso limitado.
Qual solução atenderá a esses requisitos?

A. Criar uma análise no Amazon QuickSight. Conectar todas as fontes de dados e criar novos conjuntos de dados. Publicar dashboards para visualizar os dados. Compartilhar os dashboards com as funções (IAM roles) apropriadas.

B. Criar uma análise no Amazon QuickSight. Conectar todas as fontes de dados e criar novos conjuntos de dados. Publicar dashboards para visualizar os dados. Compartilhar os dashboards com os usuários e grupos apropriados.

C. Criar uma tabela e um crawler no AWS Glue para os dados no Amazon S3. Criar um trabalho de ETL no AWS Glue para produzir relatórios. Publicar os relatórios no Amazon S3. Usar políticas de bucket S3 para limitar o acesso aos relatórios.

D. Criar uma tabela e um crawler no AWS Glue para os dados no Amazon S3. Usar o Amazon Athena Federated Query para acessar dados no Amazon RDS para PostgreSQL. Gerar relatórios usando o Amazon Athena. Publicar os relatórios no Amazon S3. Usar políticas de bucket S3 para limitar o acesso aos relatórios.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Crie uma análise no Amazon QuickSight. Conecte todas as fontes de dados e compartilhe os dashboards com os papéis apropriados do IAM.

**Justificativa:**  
- **Por que essa opção?**  
  O QuickSight permite conectar várias fontes, criar visualizações e compartilhar acessos com controle granular.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A opção é redundante, pois sugere usuários e grupos ao invés de papéis IAM.  
  - **C:** Relatórios ETL no S3 não atendem ao requisito de visualização.  
  - **D:** Athena sozinho não gerencia visualizações e acesso restrito.  


</details>

---

### Questão 17
Uma empresa está implementando um novo aplicativo de negócios. O aplicativo é executado em duas instâncias Amazon EC2 e utiliza um bucket do Amazon S3 para armazenamento de documentos. Um arquiteto de soluções precisa garantir que as instâncias EC2 possam acessar o bucket S3.
O que o arquiteto de soluções deve fazer para atender a esse requisito?

A. Criar uma função IAM (IAM role) que concede acesso ao bucket S3. Anexar a função às instâncias EC2.

B. Criar uma política IAM (IAM policy) que concede acesso ao bucket S3. Anexar a política às instâncias EC2.

C. Criar um grupo IAM (IAM group) que concede acesso ao bucket S3. Anexar o grupo às instâncias EC2.

D. Criar um usuário IAM (IAM user) que concede acesso ao bucket S3. Anexar a conta de usuário às instâncias EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Crie uma role IAM que conceda acesso ao bucket S3 e anexe às instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  Roles IAM são a maneira mais segura e eficiente de conceder permissões temporárias para instâncias EC2.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Políticas IAM não podem ser diretamente anexadas a instâncias.  
  - **C:** Grupos IAM não são aplicáveis a instâncias EC2.  
  - **D:** Usuários IAM são menos seguros e não recomendados para esse caso.  


</details>

---

### Questão 18
A equipe de desenvolvimento de aplicativos está projetando um microsserviço que converterá imagens grandes em imagens menores e comprimidas. Quando um usuário carrega uma imagem por meio da interface web, o microsserviço deve armazenar a imagem em um bucket do Amazon S3, processá-la e comprimi-la com uma função AWS Lambda e armazenar a imagem comprimida em um bucket S3 diferente.
Um arquiteto de soluções precisa projetar uma solução que use componentes duráveis e sem estado para processar automaticamente as imagens.
Quais combinações de ações atenderão a esses requisitos? (Escolha duas.)

A. Criar uma fila do Amazon Simple Queue Service (Amazon SQS). Configurar o bucket S3 para enviar uma notificação para a fila SQS quando uma imagem for carregada no bucket S3.

B. Configurar a função Lambda para usar a fila do Amazon Simple Queue Service (Amazon SQS) como a origem de invocação. Quando a mensagem SQS for processada com sucesso, excluir a mensagem da fila.

C. Configurar a função Lambda para monitorar o bucket S3 em busca de novos carregamentos. Quando uma imagem carregada for detectada, escrever o nome do arquivo em um arquivo de texto na memória e usar o arquivo de texto para acompanhar as imagens processadas.

D. Iniciar uma instância Amazon EC2 para monitorar uma fila do Amazon Simple Queue Service (Amazon SQS). Quando itens forem adicionados à fila, registrar o nome do arquivo em um arquivo de texto na instância EC2 e invocar a função Lambda.

E. Configurar um evento do Amazon EventBridge (Amazon CloudWatch Events) para monitorar o bucket S3. Quando uma imagem for carregada, enviar um alerta para um tópico do Amazon Simple Notification Service (Amazon SNS) com o endereço de email do proprietário do aplicativo para processamento adicional.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A e B.** Crie uma fila Amazon SQS. Configure a função Lambda para usar a fila como fonte de invocação.

**Justificativa:**  
- **Por que essa opção?**  
  A fila SQS desacopla o processamento e a Lambda garante a execução automática com monitoramento integrado.  

- **Por que as outras opções não são adequadas?**  
  - **C:** Monitorar uploads diretamente é menos eficiente do que usar filas.  
  - **D:** Usar EC2 para monitorar filas é desnecessário com Lambda.  
  - **E:** Notificações do SNS não automatizam o processamento.  


</details>

---

### Questão 19
Uma empresa possui um aplicativo web de três camadas implantado na AWS. Os servidores web estão implantados em uma sub-rede pública em uma VPC. Os servidores de aplicação e os servidores de banco de dados estão em sub-redes privadas na mesma VPC. A empresa implantou um appliance de firewall virtual de terceiros do AWS Marketplace em uma VPC de inspeção. O appliance está configurado com uma interface IP que pode aceitar pacotes IP.
Um arquiteto de soluções precisa integrar o aplicativo web ao appliance para inspecionar todo o tráfego do aplicativo antes que ele chegue ao servidor web.
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?

A. Criar um Network Load Balancer na sub-rede pública da VPC do aplicativo para rotear o tráfego para o appliance para inspeção de pacotes.

B. Criar um Application Load Balancer na sub-rede pública da VPC do aplicativo para rotear o tráfego para o appliance para inspeção de pacotes.

C. Implantar um transit gateway na VPC de inspeção. Configurar tabelas de rotas para rotear os pacotes recebidos por meio do transit gateway.

D. Implantar um Gateway Load Balancer na VPC de inspeção. Criar um endpoint do Gateway Load Balancer para receber os pacotes recebidos e encaminhá-los para o appliance.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Implemente um Gateway Load Balancer na VPC de inspeção para rotear os pacotes ao appliance.

**Justificativa:**  
- **Por que essa opção?**  
  O Gateway Load Balancer simplifica o roteamento e inspeção de tráfego com alta disponibilidade.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** NLB e ALB não oferecem integração direta para inspeção.  
  - **C:** Transit Gateway é desnecessário para este fluxo específico.  


</details>

---

### Questão 20
Uma empresa deseja melhorar sua capacidade de clonar grandes quantidades de dados de produção em um ambiente de teste na mesma região da AWS. Os dados estão armazenados em instâncias Amazon EC2 em volumes do Amazon Elastic Block Store (Amazon EBS). As modificações nos dados clonados não devem afetar o ambiente de produção. O software que acessa esses dados requer desempenho de I/O consistentemente alto.
Um arquiteto de soluções precisa minimizar o tempo necessário para clonar os dados de produção no ambiente de teste.
Qual solução atenderá a esses requisitos?

A. Tirar snapshots EBS dos volumes EBS de produção. Restaurar os snapshots em volumes de armazenamento de instâncias EC2 no ambiente de teste.

B. Configurar os volumes EBS de produção para usar o recurso EBS Multi-Attach. Tirar snapshots EBS dos volumes EBS de produção. Anexar os volumes EBS de produção às instâncias EC2 no ambiente de teste.

C. Tirar snapshots EBS dos volumes EBS de produção. Criar e inicializar novos volumes EBS. Anexar os novos volumes EBS às instâncias EC2 no ambiente de teste antes de restaurar os volumes dos snapshots EBS de produção.

D. Tirar snapshots EBS dos volumes EBS de produção. Ativar o recurso de restauração rápida de snapshots EBS (EBS fast snapshot restore) nos snapshots EBS. Restaurar os snapshots em novos volumes EBS. Anexar os novos volumes EBS às instâncias EC2 no ambiente de teste.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Ative o recurso de restauração rápida de snapshots no EBS e restaure os snapshots em novos volumes.

**Justificativa:**  
- **Por que essa opção?**  
  A restauração rápida reduz significativamente o tempo necessário para disponibilizar os volumes clonados.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Restaurar sem o recurso de rápida restauração aumenta o tempo de indisponibilidade.  
  - **B:** Multi-Attach é inadequado para separar ambientes de teste e produção.  


</details>

---

### Questão 21
Uma empresa de comércio eletrônico deseja lançar um site "uma oferta por dia" na AWS. Cada dia apresentará exatamente um produto em oferta por um período de 24 horas. A empresa deseja ser capaz de lidar com milhões de solicitações por hora com latência em milissegundos durante os horários de pico.
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?

A. Usar o Amazon S3 para hospedar todo o site em diferentes buckets S3. Adicionar distribuições do Amazon CloudFront. Configurar os buckets S3 como origens para as distribuições. Armazenar os dados dos pedidos no Amazon S3.

B. Implantar todo o site em instâncias Amazon EC2 que operam em grupos de Auto Scaling em várias Zonas de Disponibilidade. Adicionar um Application Load Balancer (ALB) para distribuir o tráfego do site. Adicionar outro ALB para as APIs de backend. Armazenar os dados no Amazon RDS for MySQL.

C. Migrar todo o aplicativo para execução em contêineres. Hospedar os contêineres no Amazon Elastic Kubernetes Service (Amazon EKS). Usar o Kubernetes Cluster Autoscaler para aumentar e diminuir o número de pods para processar picos de tráfego. Armazenar os dados no Amazon RDS for MySQL.

D. Usar um bucket do Amazon S3 para hospedar o conteúdo estático do site. Implantar uma distribuição do Amazon CloudFront. Configurar o bucket S3 como a origem. Usar o Amazon API Gateway e funções AWS Lambda para as APIs de backend. Armazenar os dados no Amazon DynamoDB.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Use um bucket Amazon S3 para hospedar o conteúdo estático, Amazon CloudFront para distribuição e API Gateway com AWS Lambda para backend.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 e o CloudFront são altamente escaláveis e de baixa latência para conteúdo estático, enquanto API Gateway e Lambda gerenciam APIs de backend sem a necessidade de infraestrutura.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar apenas S3 não gerencia a lógica de backend.  
  - **B:** Instâncias EC2 e ALB têm maior complexidade e custos.  
  - **C:** Containers em EKS introduzem mais sobrecarga operacional.  


</details>

---

### Questão 22
Um arquiteto de soluções está usando o Amazon S3 para projetar a arquitetura de armazenamento de um novo aplicativo de mídia digital. Os arquivos de mídia devem ser resilientes à perda de uma Zona de Disponibilidade. Alguns arquivos são acessados com frequência, enquanto outros são raramente acessados em um padrão imprevisível. O arquiteto de soluções deve minimizar os custos de armazenamento e recuperação dos arquivos de mídia.
Qual opção de armazenamento atende a esses requisitos?

A. S3 Standard

B. S3 Intelligent-Tiering

C. S3 Standard-Infrequent Access (S3 Standard-IA)

D. S3 One Zone-Infrequent Access (S3 One Zone-IA)

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** S3 Intelligent-Tiering.

**Justificativa:**  
- **Por que essa opção?**  
  O Intelligent-Tiering ajusta automaticamente os níveis de armazenamento com base nos padrões de acesso, reduzindo custos para dados raramente acessados sem comprometer a resiliência.  

- **Por que as outras opções não são adequadas?**  
  - **A:** S3 Standard é mais caro para dados raramente acessados.  
  - **C:** S3 Standard-IA não ajusta dinamicamente os níveis de armazenamento.  
  - **D:** S3 One Zone-IA não oferece resiliência para múltiplas zonas.  


</details>

---

### Questão 23
Uma empresa está armazenando arquivos de backup usando o armazenamento Amazon S3 Standard. Os arquivos são acessados frequentemente por 1 mês, mas não são acessados após esse período. A empresa deve manter os arquivos indefinidamente.
Qual solução de armazenamento atenderá a esses requisitos de forma mais econômica?

A. Configurar o S3 Intelligent-Tiering para migrar automaticamente os objetos.

B. Criar uma configuração de ciclo de vida (Lifecycle) no S3 para fazer a transição dos objetos do S3 Standard para o S3 Glacier Deep Archive após 1 mês.

C. Criar uma configuração de ciclo de vida (Lifecycle) no S3 para fazer a transição dos objetos do S3 Standard para o S3 Standard-Infrequent Access (S3 Standard-IA) após 1 mês.

D. Criar uma configuração de ciclo de vida (Lifecycle) no S3 para fazer a transição dos objetos do S3 Standard para o S3 One Zone-Infrequent Access (S3 One Zone-IA) após 1 mês.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Configure uma política de ciclo de vida no S3 para mover objetos para o S3 Glacier Deep Archive após 1 mês.

**Justificativa:**  
- **Por que essa opção?**  
  S3 Glacier Deep Archive é a opção mais econômica para armazenamento de longo prazo, ideal para dados raramente acessados após 1 mês.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Intelligent-Tiering não é tão econômico quanto Glacier para dados arquivados.  
  - **C e D:** Standard-IA e One Zone-IA têm custos mais altos para armazenamento de longo prazo.  


</details>

---

### Questão 24
Uma empresa observou um aumento nos custos do Amazon EC2 em sua fatura mais recente. A equipe de faturamento notou escalonamento vertical indesejado nos tipos de instâncias para algumas instâncias EC2. Um arquiteto de soluções precisa criar um gráfico comparando os custos do EC2 dos últimos 2 meses e realizar uma análise detalhada para identificar a causa raiz do escalonamento vertical.
Como o arquiteto de soluções deve gerar essas informações com o MENOR esforço operacional?

A. Usar o AWS Budgets para criar um relatório de orçamento e comparar os custos do EC2 com base nos tipos de instância.

B. Usar o recurso de filtragem granular do Cost Explorer para realizar uma análise detalhada dos custos do EC2 com base nos tipos de instância.

C. Usar os gráficos do painel AWS Billing and Cost Management para comparar os custos do EC2 com base nos tipos de instância nos últimos 2 meses.

D. Usar o AWS Cost and Usage Reports para criar um relatório e enviá-lo para um bucket do Amazon S3. Usar o Amazon QuickSight com o S3 como origem para gerar um gráfico interativo com base nos tipos de instância.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use o recurso de filtragem granular do Cost Explorer para analisar os custos do EC2 com base nos tipos de instância.

**Justificativa:**  
- **Por que essa opção?**  
  O Cost Explorer fornece análises detalhadas e insights sobre custos com filtros baseados em instâncias.  

- **Por que as outras opções não são adequadas?**  
  - **A:** AWS Budgets não fornece visualizações detalhadas de custos.  
  - **C:** O dashboard de Billing é limitado para análises detalhadas.  
  - **D:** Usar QuickSight adiciona complexidade desnecessária.  


</details>

---

### Questão 25
Uma empresa está projetando um aplicativo que usa uma função AWS Lambda para receber informações por meio do Amazon API Gateway e armazená-las em um banco de dados Amazon Aurora PostgreSQL. Durante a etapa de prova de conceito, a empresa precisou aumentar significativamente as cotas do Lambda para lidar com os altos volumes de dados que precisam ser carregados no banco de dados. Um arquiteto de soluções deve recomendar um novo design para melhorar a escalabilidade e minimizar o esforço de configuração.
Qual solução atenderá a esses requisitos?

A. Refatorar o código da função Lambda para código Apache Tomcat que será executado em instâncias Amazon EC2. Conectar-se ao banco de dados usando drivers nativos Java Database Connectivity (JDBC).

B. Alterar a plataforma de Aurora para Amazon DynamoDB. Provisionar um cluster do DynamoDB Accelerator (DAX). Usar o cliente SDK do DAX para direcionar as chamadas de API existentes do DynamoDB para o cluster DAX.

C. Configurar duas funções Lambda. Configurar uma função para receber as informações e outra para carregar as informações no banco de dados. Integrar as funções Lambda usando o Amazon Simple Notification Service (Amazon SNS).

D. Configurar duas funções Lambda. Configurar uma função para receber as informações e outra para carregar as informações no banco de dados. Integrar as funções Lambda usando uma fila do Amazon Simple Queue Service (Amazon SQS).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Configure duas funções Lambda: uma para receber dados e outra para carregá-los no banco de dados. Integre-as com uma fila Amazon SQS.

**Justificativa:**  
- **Por que essa opção?**  
  Separar as funções Lambda reduz gargalos e integrações com SQS garantem processamento escalável e confiável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** EC2 introduz complexidade e custos elevados.  
  - **B:** DynamoDB não é mencionado como requisito no caso.  
  - **C:** SNS não gerencia filas para processamento ordenado.  


</details>

---

### Questão 26
Uma empresa precisa revisar sua implantação na AWS para garantir que seus buckets do Amazon S3 não tenham alterações de configuração não autorizadas.
O que um arquiteto de soluções deve fazer para alcançar esse objetivo?

A. Ativar o AWS Config com as regras apropriadas.

B. Ativar o AWS Trusted Advisor com as verificações apropriadas.

C. Ativar o Amazon Inspector com o modelo de avaliação apropriado.

D. Ativar o Amazon S3 Server Access Logging. Configurar o Amazon EventBridge (Amazon CloudWatch Events).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Ative o AWS Config com as regras apropriadas.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config rastreia alterações em configurações de recursos e oferece alertas de conformidade.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Trusted Advisor não monitora configurações de buckets.  
  - **C:** Amazon Inspector é usado para vulnerabilidades, não configuração de buckets.  
  - **D:** Logs de acesso não previnem mudanças, apenas registram eventos.  


</details>

---

### Questão 27
Uma empresa está lançando um novo aplicativo e exibirá métricas do aplicativo em um painel do Amazon CloudWatch. O gerente de produto da empresa precisa acessar esse painel periodicamente. O gerente de produto não possui uma conta da AWS. Um arquiteto de soluções deve fornecer acesso ao painel seguindo o princípio de privilégio mínimo.
Qual solução atenderá a esses requisitos?

A. Compartilhar o painel a partir do console do CloudWatch. Inserir o endereço de e-mail do gerente de produto e concluir as etapas de compartilhamento. Fornecer um link compartilhável para o painel ao gerente de produto.

B. Criar um usuário IAM especificamente para o gerente de produto. Anexar a política gerenciada AWS CloudWatchReadOnlyAccess ao usuário. Compartilhar as novas credenciais de login com o gerente de produto. Compartilhar a URL do navegador do painel correto com o gerente de produto.

C. Criar um usuário IAM para os funcionários da empresa. Anexar a política gerenciada AWS ViewOnlyAccess ao usuário IAM. Compartilhar as novas credenciais de login com o gerente de produto. Pedir ao gerente de produto para navegar até o console do CloudWatch e localizar o painel pelo nome na seção Dashboards.

D. Implantar um servidor bastion em uma sub-rede pública. Quando o gerente de produto precisar acessar o painel, iniciar o servidor e compartilhar as credenciais RDP. No servidor bastion, garantir que o navegador esteja configurado para abrir a URL do painel com credenciais AWS em cache que tenham permissões apropriadas para visualizar o painel.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Compartilhe o dashboard a partir do console do CloudWatch e forneça um link compartilhável.

**Justificativa:**  
- **Por que essa opção?**  
  O compartilhamento direto do dashboard é a abordagem mais simples e segura, seguindo o princípio do menor privilégio.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar usuários IAM adiciona complexidade e supera o escopo necessário.  
  - **C:** O acesso ViewOnlyAccess permite mais permissões do que o necessário.  
  - **D:** Usar um bastion server é excessivamente complexo.  


</details>

---

### Questão 28
Uma empresa está migrando aplicativos para a AWS. Os aplicativos estão implantados em diferentes contas. A empresa gerencia as contas centralmente usando o AWS Organizations. A equipe de segurança da empresa precisa de uma solução de Single Sign-On (SSO) para todas as contas da empresa. A empresa deve continuar gerenciando os usuários e grupos no Microsoft Active Directory autogerenciado local.
Qual solução atenderá a esses requisitos?

A. Ativar o AWS Single Sign-On (AWS SSO) no console do AWS SSO. Criar uma confiança unidirecional de floresta (forest trust) ou confiança de domínio (domain trust) para conectar o Microsoft Active Directory autogerenciado da empresa ao AWS SSO usando o AWS Directory Service para Microsoft Active Directory.

B. Ativar o AWS Single Sign-On (AWS SSO) no console do AWS SSO. Criar uma confiança bidirecional de floresta (forest trust) para conectar o Microsoft Active Directory autogerenciado da empresa ao AWS SSO usando o AWS Directory Service para Microsoft Active Directory.

C. Usar o AWS Directory Service. Criar uma relação de confiança bidirecional com o Microsoft Active Directory autogerenciado da empresa.

D. Implantar um provedor de identidade (IdP) local. Ativar o AWS Single Sign-On (AWS SSO) no console do AWS SSO.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Ative o AWS SSO e conecte-se ao Active Directory local usando AWS Directory Service.

**Justificativa:**  
- **Por que essa opção?**  
  Essa solução integra o SSO ao Active Directory local sem necessidade de gerenciar infraestrutura adicional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Two-way trust adiciona complexidade desnecessária.  
  - **C:** AWS Directory Service sozinho não oferece SSO para múltiplas contas.  
  - **D:** Usar um IdP local é menos eficiente e requer mais configuração.  


</details>

---

### Questão 29
Uma empresa fornece um serviço de Voz sobre IP (VoIP) que usa conexões UDP. O serviço consiste em instâncias Amazon EC2 que operam em um grupo de Auto Scaling. A empresa tem implantações em várias regiões da AWS.
A empresa precisa rotear os usuários para a região com a menor latência e também requer failover automatizado entre as regiões.
Qual solução atenderá a esses requisitos?

A. Implantar um Network Load Balancer (NLB) e um grupo de destino associado. Associar o grupo de destino ao grupo de Auto Scaling. Usar o NLB como um endpoint do AWS Global Accelerator em cada região.

B. Implantar um Application Load Balancer (ALB) e um grupo de destino associado. Associar o grupo de destino ao grupo de Auto Scaling. Usar o ALB como um endpoint do AWS Global Accelerator em cada região.

C. Implantar um Network Load Balancer (NLB) e um grupo de destino associado. Associar o grupo de destino ao grupo de Auto Scaling. Criar um registro de latência do Amazon Route 53 que aponta para aliases de cada NLB. Criar uma distribuição do Amazon CloudFront que usa o registro de latência como uma origem.

D. Implantar um Application Load Balancer (ALB) e um grupo de destino associado. Associar o grupo de destino ao grupo de Auto Scaling. Criar um registro ponderado do Amazon Route 53 que aponta para aliases de cada ALB. Implantar uma distribuição do Amazon CloudFront que usa o registro ponderado como uma origem.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Use um Network Load Balancer (NLB) associado ao AWS Global Accelerator em cada região.

**Justificativa:**  
- **Por que essa opção?**  
  O NLB fornece suporte para UDP, enquanto o Global Accelerator roteia tráfego com baixa latência e failover automático.  

- **Por que as outras opções não são adequadas?**  
  - **B:** ALB não suporta tráfego UDP.  
  - **C:** Route 53 sozinho não fornece failover automático eficiente.  
  - **D:** ALB com Route 53 não é otimizado para UDP.  


</details>

---

### Questão 30
A equipe de desenvolvimento executa testes mensais que consomem muitos recursos em sua instância de banco de dados Amazon RDS for MySQL de uso geral, com o Performance Insights ativado. Os testes duram 48 horas por mês e são o único processo que utiliza o banco de dados. A equipe deseja reduzir o custo de execução dos testes sem reduzir os atributos de computação e memória da instância do banco de dados.
Qual solução atende a esses requisitos de forma mais econômica?

A. Parar a instância do banco de dados quando os testes forem concluídos. Reiniciar a instância do banco de dados quando necessário.

B. Usar uma política de Auto Scaling com a instância do banco de dados para escalá-la automaticamente quando os testes forem concluídos.

C. Criar um snapshot quando os testes forem concluídos. Encerrar a instância do banco de dados e restaurar o snapshot quando necessário.

D. Modificar a instância do banco de dados para uma instância de baixa capacidade quando os testes forem concluídos. Modificar novamente a instância do banco de dados quando necessário.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie um snapshot após os testes e restaure o banco de dados somente quando necessário.

**Justificativa:**  
- **Por que essa opção?**  
  Restaurar snapshots economiza custos ao evitar execução contínua do banco de dados quando não está em uso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Parar o banco é menos eficiente do que restaurar snapshots.  
  - **B:** Auto Scaling não aplica-se diretamente ao RDS.  
  - **D:** Alterar a capacidade manualmente adiciona complexidade.  


</details>

---

### Questão 31
Uma empresa que hospeda seu aplicativo web na AWS deseja garantir que todas as instâncias Amazon EC2, instâncias Amazon RDS e clusters Amazon Redshift sejam configurados com tags. A empresa deseja minimizar o esforço para configurar e operar essa verificação.
O que um arquiteto de soluções deve fazer para alcançar isso?

A. Usar regras do AWS Config para definir e detectar recursos que não estão devidamente etiquetados.

B. Usar o Cost Explorer para exibir recursos que não estão devidamente etiquetados. Etiquetar esses recursos manualmente.

C. Escrever chamadas de API para verificar todos os recursos quanto à alocação adequada de tags. Executar periodicamente o código em uma instância EC2.

D. Escrever chamadas de API para verificar todos os recursos quanto à alocação adequada de tags. Agendar uma função AWS Lambda por meio do Amazon CloudWatch para executar periodicamente o código.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Use regras do AWS Config para definir e detectar recursos que não estão devidamente etiquetados.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config oferece monitoramento contínuo e conformidade automatizada, facilitando a identificação de recursos sem tags.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Cost Explorer apenas exibe os recursos, sem capacidade de correção.  
  - **C e D:** Criar APIs personalizadas adiciona complexidade operacional desnecessária.  


</details>

---

### Questão 32
A equipe de desenvolvimento precisa hospedar um site que será acessado por outras equipes. O conteúdo do site consiste em HTML, CSS, JavaScript no lado do cliente e imagens.
Qual método é o mais econômico para hospedar o site?

A. Containerizar o site e hospedá-lo no AWS Fargate.

B. Criar um bucket do Amazon S3 e hospedar o site nele.

C. Implantar um servidor web em uma instância Amazon EC2 para hospedar o site.

D. Configurar um Application Load Balancer com um destino AWS Lambda que use o framework Express.js.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Crie um bucket Amazon S3 e hospede o site nele.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 é a opção mais econômica para hospedar conteúdo estático com baixa sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Fargate é projetado para microsserviços, não para sites estáticos.  
  - **C:** Usar EC2 é mais caro e desnecessário para este caso.  
  - **D:** ALB e Lambda introduzem complexidade sem benefícios adicionais.  


</details>

---

### Questão 33
Uma empresa executa um aplicativo web de marketplace online na AWS. O aplicativo atende centenas de milhares de usuários durante os horários de pico. A empresa precisa de uma solução escalável e quase em tempo real para compartilhar os detalhes de milhões de transações financeiras com vários outros aplicativos internos. As transações também precisam ser processadas para remover dados sensíveis antes de serem armazenadas em um banco de dados de documentos para recuperação de baixa latência.
O que um arquiteto de soluções deve recomendar para atender a esses requisitos?

A. Armazenar os dados das transações no Amazon DynamoDB. Configurar uma regra no DynamoDB para remover os dados sensíveis de cada transação ao gravar. Usar o DynamoDB Streams para compartilhar os dados das transações com outros aplicativos.

B. Transmitir os dados das transações para o Amazon Kinesis Data Firehose para armazenar os dados no Amazon DynamoDB e no Amazon S3. Usar a integração do AWS Lambda com o Kinesis Data Firehose para remover dados sensíveis. Outros aplicativos podem consumir os dados armazenados no Amazon S3.

C. Transmitir os dados das transações para o Amazon Kinesis Data Streams. Usar a integração do AWS Lambda para remover os dados sensíveis de cada transação e, em seguida, armazenar os dados das transações no Amazon DynamoDB. Outros aplicativos podem consumir os dados das transações diretamente do fluxo de dados do Kinesis.

D. Armazenar os dados das transações em lotes no Amazon S3 como arquivos. Usar o AWS Lambda para processar cada arquivo e remover os dados sensíveis antes de atualizar os arquivos no Amazon S3. A função Lambda então armazena os dados no Amazon DynamoDB. Outros aplicativos podem consumir os arquivos de transações armazenados no Amazon S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Transmita os dados das transações para o Amazon Kinesis Data Streams e use AWS Lambda para remover dados sensíveis.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis gerencia grandes volumes de dados em tempo real, enquanto o Lambda processa e armazena os dados no DynamoDB.  

- **Por que as outras opções não são adequadas?**  
  - **A e D:** Processar em DynamoDB ou S3 diretamente não é ideal para grandes volumes em tempo real.  
  - **B:** Kinesis Firehose não oferece processamento detalhado como o Lambda.  


</details>

---

### Questão 34
Uma empresa hospeda seus aplicativos de múltiplas camadas na AWS. Por motivos de conformidade, governança, auditoria e segurança, a empresa deve rastrear alterações de configuração em seus recursos AWS e registrar um histórico de chamadas de API feitas a esses recursos.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Usar o AWS CloudTrail para rastrear alterações de configuração e o AWS Config para registrar chamadas de API.

B. Usar o AWS Config para rastrear alterações de configuração e o AWS CloudTrail para registrar chamadas de API.

C. Usar o AWS Config para rastrear alterações de configuração e o Amazon CloudWatch para registrar chamadas de API.

D. Usar o AWS CloudTrail para rastrear alterações de configuração e o Amazon CloudWatch para registrar chamadas de API.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use AWS Config para rastrear mudanças de configuração e AWS CloudTrail para registrar chamadas de API.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Config e CloudTrail são projetados para fornecer histórico detalhado de mudanças e chamadas de API, atendendo requisitos de conformidade.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Misturam serviços que não são adequados para todas as necessidades.  
  - **D:** CloudWatch não é usado para rastrear mudanças de configuração.  


</details>

---

### Questão 35
Uma empresa está se preparando para lançar um aplicativo web voltado para o público na AWS Cloud. A arquitetura consiste em instâncias Amazon EC2 dentro de uma VPC atrás de um Elastic Load Balancer (ELB). Um serviço de terceiros é usado para o DNS. O arquiteto de soluções da empresa deve recomendar uma solução para detectar e proteger contra ataques DDoS em larga escala.
Qual solução atende a esses requisitos?

A. Ativar o Amazon GuardDuty na conta.

B. Ativar o Amazon Inspector nas instâncias EC2.

C. Ativar o AWS Shield e atribuir o Amazon Route 53 a ele.

D. Ativar o AWS Shield Advanced e atribuir o ELB a ele.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Ative o AWS Shield Advanced e associe-o ao ELB.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Shield Advanced oferece proteção DDoS avançada e relatórios detalhados para recursos como ELB.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** GuardDuty e Inspector detectam, mas não mitigam ataques DDoS.  
  - **C:** Shield padrão não inclui suporte avançado ou resposta a incidentes.  


</details>

---

### Questão 36
Uma empresa está desenvolvendo um aplicativo na AWS Cloud. O aplicativo armazenará dados em buckets do Amazon S3 em duas regiões da AWS. A empresa deve usar uma chave gerenciada pelo cliente do AWS Key Management Service (AWS KMS) para criptografar todos os dados armazenados nos buckets do S3. Os dados em ambos os buckets do S3 devem ser criptografados e descriptografados com a mesma chave KMS. Os dados e a chave devem estar armazenados em cada uma das duas regiões.
Qual solução atenderá a esses requisitos com o menor esforço operacional?

A. Criar um bucket S3 em cada região. Configurar os buckets S3 para usar criptografia do lado do servidor com chaves de criptografia gerenciadas pelo Amazon S3 (SSE-S3). Configurar a replicação entre os buckets S3.

B. Criar uma chave KMS gerenciada pelo cliente e multi-regional. Criar um bucket S3 em cada região. Configurar a replicação entre os buckets S3. Configurar o aplicativo para usar a chave KMS com criptografia do lado do cliente.

C. Criar uma chave KMS gerenciada pelo cliente e um bucket S3 em cada região. Configurar os buckets S3 para usar criptografia do lado do servidor com chaves de criptografia gerenciadas pelo Amazon S3 (SSE-S3). Configurar a replicação entre os buckets S3.

D. Criar uma chave KMS gerenciada pelo cliente e um bucket S3 em cada região. Configurar os buckets S3 para usar criptografia do lado do servidor com chaves KMS (SSE-KMS). Configurar a replicação entre os buckets S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Crie uma chave KMS multi-região gerenciada. Configure replicação entre os buckets S3.

**Justificativa:**  
- **Por que essa opção?**  
  Chaves KMS multi-região permitem criptografia e descriptografia consistentes em várias regiões com mínima sobrecarga operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Usar SSE-S3 não atende ao requisito de chaves KMS consistentes.  
  - **D:** Chaves gerenciadas por região não oferecem interoperabilidade.  


</details>

---

### Questão 37
Uma empresa lançou recentemente uma variedade de novas cargas de trabalho em instâncias Amazon EC2 em sua conta AWS. A empresa precisa criar uma estratégia para acessar e administrar as instâncias remotamente e de forma segura. A solução deve implementar um processo repetível que funcione com serviços nativos da AWS e siga o AWS Well-Architected Framework.
Qual solução atenderá a esses requisitos com o menor esforço operacional?

A. Usar o console serial do EC2 para acessar diretamente a interface de terminal de cada instância para administração.

B. Anexar a função IAM apropriada a cada instância existente e nova. Usar o AWS Systems Manager Session Manager para estabelecer uma sessão SSH remota.

C. Criar um par de chaves SSH administrativas. Carregar a chave pública em cada instância EC2. Implantar um host bastion em uma sub-rede pública para fornecer um túnel para a administração de cada instância.

D. Estabelecer uma conexão VPN Site-to-Site da AWS. Instruir os administradores a usarem suas máquinas locais on-premises para se conectarem diretamente às instâncias usando chaves SSH por meio do túnel VPN.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Anexe a role IAM apropriada às instâncias e use o AWS Systems Manager Session Manager.

**Justificativa:**  
- **Por que essa opção?**  
  O Session Manager elimina a necessidade de chaves SSH e simplifica o acesso remoto com segurança integrada.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O console serial não suporta conectividade remota comum.  
  - **C:** Bastion hosts introduzem complexidade e riscos adicionais.  
  - **D:** VPNs não são necessárias com o Session Manager.  


</details>

---

### Questão 38
Uma empresa lançou recentemente uma variedade de novas cargas de trabalho em instâncias Amazon EC2 em sua conta AWS. A empresa precisa criar uma estratégia para acessar e administrar as instâncias remotamente e de forma segura. A solução deve implementar um processo repetível que funcione com serviços nativos da AWS e siga o AWS Well-Architected Framework.
Qual solução atenderá a esses requisitos com o **menor esforço operacional**?

**A.** Usar o console serial do EC2 para acessar diretamente a interface de terminal de cada instância para administração.  

**B.** Anexar a função IAM apropriada a cada instância existente e nova. Usar o AWS Systems Manager Session Manager para estabelecer uma sessão SSH remota.  

**C.** Criar um par de chaves SSH administrativas. Carregar a chave pública em cada instância EC2. Implantar um host bastion em uma sub-rede pública para fornecer um túnel para a administração de cada instância.  

**D.** Estabelecer uma conexão VPN Site-to-Site da AWS. Instruir os administradores a usarem suas máquinas locais on-premises para se conectarem diretamente às instâncias usando chaves SSH por meio do túnel VPN.  

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Anexar a função IAM apropriada a cada instância existente e nova. Usar o AWS Systems Manager Session Manager para estabelecer uma sessão SSH remota.

**Justificativa:**  
- **Por que essa opção?**  
  Configuração simples e suporte a acessos seguros em escala. 


</details>

---

### Questão 39
Uma empresa mantém um repositório pesquisável de itens em seu site. Os dados são armazenados em uma tabela de banco de dados Amazon RDS for MySQL que contém mais de 10 milhões de linhas. O banco de dados possui 2 TB de armazenamento SSD de propósito geral (General Purpose SSD). Há milhões de atualizações nesses dados todos os dias por meio do site da empresa.
A empresa percebeu que algumas operações de inserção estão levando 10 segundos ou mais. Foi determinado que o desempenho do armazenamento do banco de dados é o problema.
Qual solução resolve esse problema de desempenho?

**A.** Alterar o tipo de armazenamento para Provisioned IOPS SSD.  

**B.** Alterar a instância de banco de dados para uma classe de instância otimizada para memória.  

**C.** Alterar a instância de banco de dados para uma classe de instância de desempenho burstável.  

**D.** Habilitar réplicas de leitura Multi-AZ RDS com replicação assíncrona nativa do MySQL.  

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Altere o tipo de armazenamento para Provisioned IOPS SSD.

**Justificativa:**  
- **Por que essa opção?**  
  O Provisioned IOPS SSD oferece maior desempenho de leitura/escrita, resolvendo gargalos de I/O em cenários com alta carga.  

- **Por que as outras opções não são adequadas?**  
  - **B e C:** Alterar a classe da instância não resolve problemas de armazenamento.  
  - **D:** Réplicas de leitura não impactam a performance de gravações.  


</details>

---

### Questão 40
Uma empresa possui milhares de dispositivos de borda que, juntos, geram 1 TB de alertas de status por dia. Cada alerta tem aproximadamente 2 KB de tamanho. Um arquiteto de soluções precisa implementar uma solução para ingerir e armazenar os alertas para análise futura.
A empresa deseja uma solução altamente disponível. No entanto, a empresa precisa minimizar os custos e não quer gerenciar infraestrutura adicional. Além disso, a empresa quer manter 14 dias de dados disponíveis para análise imediata e arquivar dados mais antigos que 14 dias.
Qual é a solução mais eficiente operacionalmente que atende a esses requisitos?

A. Criar um stream de entrega do Amazon Kinesis Data Firehose para ingerir os alertas. Configurar o stream do Kinesis Data Firehose para entregar os alertas a um bucket do Amazon S3. Configurar uma política de ciclo de vida (S3 Lifecycle) para transferir os dados para o Amazon S3 Glacier após 14 dias.

B. Lançar instâncias Amazon EC2 em duas Zonas de Disponibilidade e colocá-las atrás de um Elastic Load Balancer para ingerir os alertas. Criar um script nas instâncias EC2 que armazene os alertas em um bucket do Amazon S3. Configurar uma política de ciclo de vida (S3 Lifecycle) para transferir os dados para o Amazon S3 Glacier após 14 dias.

C. Criar um stream de entrega do Amazon Kinesis Data Firehose para ingerir os alertas. Configurar o stream do Kinesis Data Firehose para entregar os alertas a um cluster do Amazon OpenSearch Service (Amazon Elasticsearch Service). Configurar o cluster do Amazon OpenSearch Service para criar snapshots manuais diariamente e excluir dados do cluster com mais de 14 dias.

D. Criar uma fila padrão do Amazon Simple Queue Service (Amazon SQS) para ingerir os alertas e configurar o período de retenção de mensagens para 14 dias. Configurar consumidores para consultar a fila SQS, verificar a idade da mensagem e analisar os dados conforme necessário. Se a mensagem tiver 14 dias, o consumidor deve copiar a mensagem para um bucket do Amazon S3 e excluí-la da fila SQS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Crie um Kinesis Data Firehose para ingerir os alertas. Configure o Firehose para entregá-los a um bucket S3 e aplique políticas de ciclo de vida para arquivar os dados no Glacier após 14 dias.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis Firehose oferece ingestão contínua e entrega direta ao S3, enquanto as políticas de ciclo de vida automatizam a retenção e arquivamento.  

- **Por que as outras opções não são adequadas?**  
  - **B:** EC2 com script adiciona mais complexidade e custos.  
  - **C:** OpenSearch Service tem custos maiores para dados de longo prazo.  
  - **D:** O SQS não é ideal para ingestão massiva e arquivamento.  


</details>

---

### Questão 41
O aplicativo de uma empresa integra-se com várias fontes de software como serviço (SaaS) para coleta de dados. A empresa utiliza instâncias Amazon EC2 para receber os dados e enviá-los para um bucket do Amazon S3 para análise. A mesma instância EC2 que recebe e envia os dados também envia uma notificação ao usuário quando o upload é concluído. A empresa percebeu um desempenho lento no aplicativo e deseja melhorar o desempenho o máximo possível.
Qual solução atenderá a esses requisitos com o **menor esforço operacional**?

**A.** Criar um grupo de Auto Scaling para que as instâncias EC2 possam escalar horizontalmente. Configurar uma notificação de evento no S3 para enviar eventos para um tópico do Amazon Simple Notification Service (Amazon SNS) quando o upload para o bucket S3 for concluído.  

**B.** Criar um fluxo do Amazon AppFlow para transferir dados entre cada fonte SaaS e o bucket S3. Configurar uma notificação de evento no S3 para enviar eventos para um tópico do Amazon Simple Notification Service (Amazon SNS) quando o upload para o bucket S3 for concluído.  

**C.** Criar uma regra do Amazon EventBridge (Amazon CloudWatch Events) para cada fonte SaaS enviar os dados de saída. Configurar o bucket S3 como o destino da regra. Criar uma segunda regra no EventBridge (CloudWatch Events) para enviar eventos quando o upload para o bucket S3 for concluído. Configurar um tópico do Amazon Simple Notification Service (Amazon SNS) como o destino da segunda regra.  

**D.** Criar um contêiner Docker para substituir uma instância EC2. Hospedar o aplicativo contêinerizado no Amazon Elastic Container Service (Amazon ECS). Configurar o Amazon CloudWatch Container Insights para enviar eventos para um tópico do Amazon Simple Notification Service (Amazon SNS) quando o upload para o bucket S3 for concluído.  

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use Amazon AppFlow para transferir dados entre fontes SaaS e o bucket S3. Configure notificações S3 para enviar eventos ao SNS após o upload.

**Justificativa:**  
- **Por que essa opção?**  
  O AppFlow reduz a sobrecarga operacional ao automatizar transferências de dados entre SaaS e S3, enquanto o SNS simplifica notificações.  

- **Por que as outras opções não são adequadas?**  
  - **A:** EC2 com Auto Scaling adiciona complexidade sem melhorar significativamente o desempenho.  
  - **C e D:** EventBridge e ECS não são tão eficientes para este caso.  


</details>

---

### Questão 42
Uma empresa executa um aplicativo de processamento de imagens altamente disponível em instâncias Amazon EC2 dentro de uma única VPC. As instâncias EC2 operam em várias sub-redes distribuídas por múltiplas Zonas de Disponibilidade (AZs). As instâncias EC2 não se comunicam entre si. No entanto, elas fazem download de imagens do Amazon S3 e enviam as imagens para o Amazon S3 por meio de um único NAT gateway. A empresa está preocupada com os custos de transferência de dados regionais.
Qual é a forma mais econômica de evitar os custos de transferência de dados regionais?

A. Lançar um NAT gateway em cada Zona de Disponibilidade.

B. Substituir o NAT gateway por uma instância NAT.

C. Implantar um endpoint de gateway VPC para o Amazon S3.

D. Provisionar um host dedicado EC2 (EC2 Dedicated Host) para executar as instâncias EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Implemente um endpoint VPC Gateway para o S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway permite acesso ao S3 sem taxas de transferência regionais e com maior segurança.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Lançar múltiplos NAT Gateways aumenta os custos.  
  - **B:** NAT Instance não oferece a mesma escalabilidade de um endpoint.  
  - **D:** EC2 Dedicated Host não resolve problemas de transferência de dados.  


</details>

---

### Questão 43
Uma empresa possui um aplicativo local (on-premises) que gera uma grande quantidade de dados sensíveis ao tempo, que são enviados para o Amazon S3 como backup. O aplicativo cresceu e os usuários estão reclamando de limitações na largura de banda da internet. Um arquiteto de soluções precisa projetar uma solução de longo prazo que permita backups rápidos para o Amazon S3, com impacto mínimo na conectividade da internet para os usuários internos.
Qual solução atende a esses requisitos?

A. Estabelecer conexões AWS VPN e direcionar todo o tráfego por meio de um endpoint de gateway VPC.

B. Estabelecer uma nova conexão AWS Direct Connect e direcionar o tráfego de backup por essa nova conexão.

C. Solicitar dispositivos AWS Snowball diariamente, carregar os dados nesses dispositivos e enviá-los de volta para a AWS todos os dias.

D. Submeter um ticket de suporte pelo console de gerenciamento da AWS, solicitando a remoção dos limites de serviço do S3 na conta.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Estabeleça uma conexão AWS Direct Connect e direcione o tráfego de backup por esta conexão.

**Justificativa:**  
- **Por que essa opção?**  
  O Direct Connect oferece conectividade dedicada e de baixa latência, minimizando impacto na rede local.  

- **Por que as outras opções não são adequadas?**  
  - **A:** AWS VPN não oferece o mesmo desempenho de largura de banda que o Direct Connect.  
  - **C:** Snowball não é adequado para backups contínuos.  
  - **D:** Pedir remoção de limites de serviço não resolve problemas de conectividade.  


</details>

---

### Questão 44
Uma empresa possui um bucket do Amazon S3 que contém dados críticos. A empresa precisa proteger esses dados contra exclusão acidental.
Quais combinações de etapas um arquiteto de soluções deve realizar para atender a esses requisitos? (Escolha duas.)

A. Ativar o versionamento no bucket S3.

B. Ativar o MFA Delete no bucket S3.

C. Criar uma política de bucket no S3.

D. Ativar a criptografia padrão no bucket S3.

E. Criar uma política de ciclo de vida (lifecycle policy) para os objetos no bucket S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A e B.** Ative o versionamento no bucket S3 e habilite a exclusão MFA.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento mantém versões antigas dos objetos e o MFA Delete adiciona uma camada de proteção contra exclusões não autorizadas.  

- **Por que as outras opções não são adequadas?**  
  - **C:** Políticas de bucket não impedem completamente exclusões acidentais.  
  - **D e E:** Criptografia e políticas de ciclo de vida não evitam exclusões.  


</details>

---

### Questão 45
Uma empresa possui um fluxo de ingestão de dados que consiste em:

    Um tópico do Amazon Simple Notification Service (Amazon SNS) para notificações sobre novas entregas de dados.
    Uma função AWS Lambda para processar os dados e registrar os metadados.

A empresa observou que o fluxo de ingestão falha ocasionalmente devido a problemas de conectividade de rede. Quando ocorre uma falha, a função Lambda não processa os dados correspondentes, a menos que a empresa reinicie manualmente o trabalho.
Quais combinações de ações um arquiteto de soluções deve realizar para garantir que a função Lambda processe todos os dados no futuro? (Escolha duas.)

A. Implantar a função Lambda em várias Zonas de Disponibilidade.

B. Criar uma fila do Amazon Simple Queue Service (Amazon SQS) e inscrevê-la no tópico SNS.

C. Aumentar a CPU e a memória alocadas para a função Lambda.

D. Aumentar a capacidade provisionada para a função Lambda.

E. Modificar a função Lambda para ler de uma fila do Amazon Simple Queue Service (Amazon SQS).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B e E.** Subcreva um SQS à SNS e modifique a função Lambda para ler da fila SQS.

**Justificativa:**  
- **Por que essa opção?**  
  O SQS desacopla o fluxo e garante que dados sejam armazenados até serem processados com sucesso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Múltiplas zonas de disponibilidade não resolvem problemas de conectividade.  
  - **C e D:** Ajustar CPU/memória ou throughput não resolve falhas transitórias de rede.  


</details>

---

### Questão 46
Uma empresa possui um aplicativo que fornece serviços de marketing para lojas. Os serviços são baseados em compras anteriores feitas por clientes das lojas. As lojas carregam os dados de transações para a empresa por meio de SFTP, e os dados são processados e analisados para gerar novas ofertas de marketing. Alguns dos arquivos podem ter mais de 200 GB de tamanho.
Recentemente, a empresa descobriu que algumas lojas carregaram arquivos que contêm informações pessoalmente identificáveis (PII) que não deveriam ter sido incluídas. A empresa deseja que os administradores sejam alertados caso PII seja compartilhada novamente. Além disso, a empresa quer automatizar a remediação. 
O que um arquiteto de soluções deve fazer para atender a esses requisitos com o MENOR esforço de desenvolvimento?

A. Use um bucket do Amazon S3 como ponto de transferência seguro. Use o Amazon Inspector para verificar os objetos no bucket. Se os objetos contiverem PII, acione uma política do S3 Lifecycle para remover os objetos que contenham PII.

B. Use um bucket do Amazon S3 como ponto de transferência seguro. Use o Amazon Macie para verificar os objetos no bucket. Se os objetos contiverem PII, use o Amazon Simple Notification Service (Amazon SNS) para acionar uma notificação para os administradores removerem os objetos que contenham PII.

C. Implemente algoritmos de verificação personalizados em uma função AWS Lambda. Acione a função quando os objetos forem carregados no bucket. Se os objetos contiverem PII, use o Amazon Simple Notification Service (Amazon SNS) para acionar uma notificação para os administradores removerem os objetos que contenham PII.

D. Implemente algoritmos de verificação personalizados em uma função AWS Lambda. Acione a função quando os objetos forem carregados no bucket. Se os objetos contiverem PII, use o Amazon Simple Email Service (Amazon SES) para acionar uma notificação para os administradores e acionar uma política do S3 Lifecycle para remover os objetos que contenham PII.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use um bucket S3 como ponto de transferência e Amazon Macie para identificar PII.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon Macie é projetado para detectar PII automaticamente com baixa necessidade de desenvolvimento adicional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Inspector não suporta diretamente detecção de PII em dados S3.  
  - **C e D:** Algoritmos personalizados adicionam desenvolvimento desnecessário.  


</details>

---

### Questão 47
Uma empresa precisa de capacidade garantida do Amazon EC2 em três Zonas de Disponibilidade específicas em uma região específica da AWS para um evento que durará 1 semana.
O que a empresa deve fazer para garantir a capacidade do EC2?

A. Comprar Reserved Instances que especifiquem a região necessária.

B. Criar uma On-Demand Capacity Reservation que especifique a região necessária.

C. Comprar Reserved Instances que especifiquem a região e as três Zonas de Disponibilidade necessárias.

D. Criar uma On-Demand Capacity Reservation que especifique a região e as três Zonas de Disponibilidade necessárias.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Crie uma reserva de capacidade sob demanda que especifica a região e as três zonas de disponibilidade.

**Justificativa:**  
- **Por que essa opção?**  
  Reservas de capacidade sob demanda garantem capacidade nas zonas selecionadas sem necessidade de instâncias reservadas.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Instâncias reservadas não garantem capacidade específica por zona. Não é apropriado para eventos de curta duração.
  - **B:** Reservar capacidade sem zonas definidas não atende ao requisito.   


</details>

---

### Questão 48
O site de uma empresa usa o armazenamento de instâncias do Amazon EC2 para seu catálogo de itens. A empresa deseja garantir que o catálogo seja altamente disponível e armazenado em um local durável.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Mover o catálogo para o Amazon ElastiCache for Redis.

B. Implantar uma instância EC2 maior com um armazenamento de instância maior.

C. Mover o catálogo do armazenamento de instância para o Amazon S3 Glacier Deep Archive.

D. Mover o catálogo para um sistema de arquivos Amazon Elastic File System (Amazon EFS).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Mova o catálogo para um sistema de arquivos Amazon EFS.

**Justificativa:**  
- **Por que essa opção?**  
  O EFS oferece armazenamento altamente disponível e durável, acessível por múltiplas instâncias EC2.  

- **Por que as outras opções não são adequadas?**  
  - **A:** ElastiCache não é ideal para armazenamento de longo prazo.  
  - **B:** Aumentar a capacidade da instância não resolve durabilidade.  
  - **C:** S3 Glacier é para arquivamento, não para acesso frequente.  


</details>

---

### Questão 49
Uma empresa armazena arquivos de transcrições de chamadas mensalmente. Os usuários acessam os arquivos de forma aleatória dentro de 1 ano após a chamada, mas acessam os arquivos com pouca frequência depois de 1 ano. A empresa deseja otimizar sua solução, permitindo que os usuários consultem e recuperem arquivos com menos de 1 ano o mais rápido possível. Um atraso na recuperação de arquivos mais antigos é aceitável.
Qual solução atenderá a esses requisitos de forma mais custo-efetiva?

A. Armazenar arquivos individuais com tags no Amazon S3 Glacier Instant Retrieval. Consultar as tags para recuperar os arquivos do S3 Glacier Instant Retrieval.

B. Armazenar arquivos individuais no Amazon S3 Intelligent-Tiering. Usar políticas do S3 Lifecycle para mover os arquivos para o S3 Glacier Flexible Retrieval após 1 ano. Consultar e recuperar os arquivos no Amazon S3 usando o Amazon Athena. Consultar e recuperar os arquivos no S3 Glacier usando o S3 Glacier Select.

C. Armazenar arquivos individuais com tags no armazenamento Amazon S3 Standard. Armazenar metadados de busca de cada arquivo no Amazon S3 Standard. Usar políticas do S3 Lifecycle para mover os arquivos para o S3 Glacier Instant Retrieval após 1 ano. Consultar e recuperar os arquivos pesquisando os metadados no Amazon S3.

D. Armazenar arquivos individuais no armazenamento Amazon S3 Standard. Usar políticas do S3 Lifecycle para mover os arquivos para o S3 Glacier Deep Archive após 1 ano. Armazenar os metadados de busca no Amazon RDS. Consultar os arquivos no Amazon RDS. Recuperar os arquivos do S3 Glacier Deep Archive.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use S3 Intelligent-Tiering com políticas de ciclo de vida para mover os arquivos para Glacier após 1 ano.

**Justificativa:**  
- **Por que essa opção?**  
  Intelligent-Tiering reduz custos para dados raramente acessados, enquanto Glacier é ideal para arquivamento de longo prazo.  

- **Por que as outras opções não são adequadas?**  
A: S3 Glacier Instant Retrieval oferece acesso rápido, mas é mais caro do que outras classes para arquivos que são acessados com pouca frequência após 1 ano.

C: Usar Amazon S3 Standard para armazenar metadados e S3 Glacier Instant Retrieval para arquivos antigos não é tão custo-efetivo quanto S3 Intelligent-Tiering combinado com S3 Glacier Flexible Retrieval.

D: S3 Glacier Deep Archive é mais barato, mas é projetado para arquivamento a longo prazo. Atrasos significativos na recuperação não são ideais para casos onde os dados ainda podem ser acessados eventualmente.


</details>

---

### Questão 50
Uma empresa tem uma carga de trabalho em produção que roda em 1.000 instâncias Amazon EC2 Linux. Essa carga de trabalho é alimentada por software de terceiros. A empresa precisa aplicar patches no software de terceiros em todas as instâncias EC2 o mais rápido possível para remediar uma vulnerabilidade de segurança crítica.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Criar uma função AWS Lambda para aplicar o patch em todas as instâncias EC2.

B. Configurar o AWS Systems Manager Patch Manager para aplicar o patch em todas as instâncias EC2.

C. Agendar uma janela de manutenção no AWS Systems Manager para aplicar o patch em todas as instâncias EC2.

D. Usar o AWS Systems Manager Run Command para executar um comando personalizado que aplica o patch em todas as instâncias EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Usar o AWS Systems Manager Run Command para executar um comando personalizado que aplica o patch em todas as instâncias EC2.

**Justificativa:**  
- **Por que essa opção?**  
  Permite que você execute comandos personalizados em várias instâncias EC2 simultaneamente sem a necessidade de criar scripts ou agendar processos. Isso é ideal para aplicar patches rapidamente em casos de vulnerabilidades críticas.

- **Por que as outras opções não são adequadas?**  
A: Embora o AWS Lambda possa ser usado para executar automações, ele não é a ferramenta ideal para gerenciar tarefas em grande escala diretamente nas instâncias EC2. Além disso, o processo seria mais complicado de implementar e gerenciar.

B: O AWS Systems Manager Patch Manager é projetado para aplicar patches do sistema operacional e não para software de terceiros. Não atenderia ao requisito de corrigir o software específico.

C: Agendar uma janela de manutenção é útil para operações planejadas, mas introduz atrasos desnecessários em uma situação que requer resposta imediata. 

</details>

---

### Questão 51
A empresa está desenvolvendo um aplicativo que fornece estatísticas de envio de pedidos por meio de uma API REST. A empresa deseja extrair as estatísticas de envio, organizar os dados em um formato HTML de fácil leitura e enviar o relatório para vários endereços de e-mail ao mesmo tempo, todas as manhãs.
Quais passos combinados um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas)

A. Configurar o aplicativo para enviar os dados para o Amazon Kinesis Data Firehose.

B. Usar o Amazon Simple Email Service (Amazon SES) para formatar os dados e enviar o relatório por e-mail.

C. Criar um evento agendado no Amazon EventBridge (Amazon CloudWatch Events) que acione um trabalho AWS Glue para consultar os dados da API do aplicativo.

D. Criar um evento agendado no Amazon EventBridge (Amazon CloudWatch Events) que acione uma função AWS Lambda para consultar os dados da API do aplicativo.

E. Armazenar os dados do aplicativo no Amazon S3. Criar um tópico do Amazon Simple Notification Service (Amazon SNS) como destino de evento do S3 para enviar 
o relatório por e-mail.

<details>

<summary>Resposta</summary>

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


</details>

---

### Questão 52
A empresa deseja migrar seu aplicativo local para a AWS. O aplicativo produz arquivos de saída que variam de dezenas de gigabytes a centenas de terabytes. Os dados do aplicativo devem ser armazenados em uma estrutura de sistema de arquivos padrão. A empresa quer uma solução que escale automaticamente, seja altamente disponível e exija o mínimo de sobrecarga operacional.
Qual solução atenderá a esses requisitos?

A. Migrar o aplicativo para rodar como contêineres no Amazon Elastic Container Service (Amazon ECS). Usar o Amazon S3 para armazenamento.

B. Migrar o aplicativo para rodar como contêineres no Amazon Elastic Kubernetes Service (Amazon EKS). Usar o Amazon Elastic Block Store (Amazon EBS) para armazenamento.

C. Migrar o aplicativo para instâncias Amazon EC2 em um grupo de Auto Scaling Multi-AZ. Usar o Amazon Elastic File System (Amazon EFS) para armazenamento.

D. Migrar o aplicativo para instâncias Amazon EC2 em um grupo de Auto Scaling Multi-AZ. Usar o Amazon Elastic Block Store (Amazon EBS) para armazenamento.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Migrar o aplicativo para instâncias Amazon EC2 em um grupo de Auto Scaling Multi-AZ. Usar o Amazon Elastic File System (Amazon EFS) para armazenamento.

**Justificativa:**  
- **Por que essa opção?**  
  O EFS é ideal para casos em que os dados precisam ser armazenados em uma estrutura de sistema de arquivos padrão. Ele é altamente disponível, escalável automaticamente, suporta Multi-AZ e requer o mínimo de sobrecarga operacional. 

- **Por que as outras opções não são adequadas?**  
- **A:**  O Amazon S3 não oferece uma estrutura de sistema de arquivos padrão. Embora seja escalável e durável, ele não atende ao requisito específico de um sistema de arquivos padrão.
- **B:**  O Amazon EBS não é compartilhado entre instâncias por padrão e não suporta Multi-AZ sem configuração adicional, o que limita a escalabilidade e a alta disponibilidade.
- **D:**  O Amazon EBS é adequado para armazenamento de bloco de alta performance, mas não para um sistema de arquivos distribuído e escalável. Ele requer gerenciamento manual para compartilhar dados entre instâncias e não escala automaticamente.

</details>

---

### Questão 53
Uma empresa precisa armazenar seus registros contábeis no Amazon S3. Os registros devem estar acessíveis imediatamente por 1 ano e, em seguida, devem ser arquivados por mais 9 anos. Ninguém na empresa, incluindo usuários administrativos e o usuário root, pode excluir os registros durante todo o período de 10 anos. Os registros devem ser armazenados com a máxima resiliência.
Qual solução atenderá a esses requisitos?

A. Armazenar os registros no S3 Glacier durante todo o período de 10 anos. Usar uma política de controle de acesso para negar a exclusão dos registros por um período de 10 anos.

B. Armazenar os registros usando o S3 Intelligent-Tiering. Usar uma política do IAM para negar a exclusão dos registros. Após 10 anos, alterar a política do IAM para permitir a exclusão.

C. Usar uma política de ciclo de vida do S3 (S3 Lifecycle) para transicionar os registros do S3 Standard para o S3 Glacier Deep Archive após 1 ano. Usar o S3 Object Lock no modo de conformidade (compliance mode) por um período de 10 anos.

D. Usar uma política de ciclo de vida do S3 (S3 Lifecycle) para transicionar os registros do S3 Standard para o S3 One Zone-Infrequent Access (S3 One Zone-IA) após 1 ano. Usar o S3 Object Lock no modo de governança (governance mode) por um período de 10 anos.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use uma política de ciclo de vida do S3 para transferir os registros do S3 Standard para o S3 Glacier Deep Archive após 1 ano. Use S3 Object Lock em modo de conformidade por um período de 10 anos.

**Justificativa:**  
- **Por que essa opção?**  
  A combinação de S3 Object Lock e o ciclo de vida fornece retenção e segurança necessárias durante os 10 anos, com transição automática para armazenamento mais econômico.  

- **Por que as outras opções não são adequadas?**  
  - **A:** S3 Glacier sozinho não garante acessibilidade imediata no primeiro ano.  
  - **B:** S3 Intelligent-Tiering não é necessário e não bloqueia a exclusão.  
  - **D:** S3 One Zone-IA não atende aos requisitos de resiliência.  Não oferece alta durabilidade, pois armazena dados em apenas uma zona de disponibilidade (AZ). 


</details>

---

### Questão 54
Uma empresa executa várias cargas de trabalho Windows na AWS. Os funcionários da empresa utilizam compartilhamentos de arquivos Windows hospedados em duas instâncias Amazon EC2. Os compartilhamentos de arquivos sincronizam dados entre si e mantêm cópias duplicadas. A empresa deseja uma solução de armazenamento altamente disponível e durável que preserve a forma como os usuários acessam os arquivos atualmente.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Migrar todos os dados para o Amazon S3. Configurar a autenticação IAM para que os usuários acessem os arquivos.

B. Configurar um Amazon S3 File Gateway. Montar o S3 File Gateway nas instâncias EC2 existentes.

C. Expandir o ambiente de compartilhamento de arquivos para o Amazon FSx for Windows File Server com uma configuração Multi-AZ. Migrar todos os dados para o FSx for Windows File Server.

D. Expandir o ambiente de compartilhamento de arquivos para o Amazon Elastic File System (Amazon EFS) com uma configuração Multi-AZ. Migrar todos os dados para o Amazon EFS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Expanda o ambiente de compartilhamento de arquivos para o Amazon FSx para Windows File Server com uma configuração Multi-AZ. Migre todos os dados para o FSx.

**Justificativa:**  
- **Por que essa opção?**  
  O FSx para Windows File Server foi projetado especificamente para suportar cargas de trabalho Windows que utilizam compartilhamentos de arquivos, oferecendo compatibilidade nativa com o protocolo SMB (Server Message Block), que é como os usuários acessam os arquivos atualmente.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O S3 não suporta diretamente compartilhamentos de arquivos no Windows.  
  - **B:** S3 File Gateway adiciona latência e não é adequado para acesso de arquivos nativo no Windows.  
  - **D:** O EFS não é compatível com protocolos de arquivos do Windows.  


</details>

---

### Questão 55
Um arquiteto de soluções está desenvolvendo uma arquitetura de VPC que inclui múltiplas sub-redes. A arquitetura hospedará aplicativos que utilizam instâncias Amazon EC2 e instâncias Amazon RDS DB. A arquitetura consiste em seis sub-redes em duas Zonas de Disponibilidade. Cada Zona de Disponibilidade inclui uma sub-rede pública, uma sub-rede privada e uma sub-rede dedicada para bancos de dados. Apenas as instâncias EC2 que operam nas sub-redes privadas podem acessar os bancos de dados RDS.
Qual solução atenderá a esses requisitos?

A. Criar uma nova tabela de rotas que exclua a rota para os blocos CIDR das sub-redes públicas. Associar a tabela de rotas às sub-redes de banco de dados.

B. Criar um grupo de segurança que negue o tráfego de entrada do grupo de segurança atribuído às instâncias nas sub-redes públicas. Anexar o grupo de segurança às instâncias do banco de dados.

C. Criar um grupo de segurança que permita tráfego de entrada do grupo de segurança atribuído às instâncias nas sub-redes privadas. Anexar o grupo de segurança às instâncias do banco de dados.

D. Criar uma nova conexão de emparelhamento entre as sub-redes públicas e as sub-redes privadas. Criar uma conexão de emparelhamento diferente entre as sub-redes privadas e as sub-redes de banco de dados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie um grupo de segurança que permita tráfego de entrada do grupo de segurança atribuído às instâncias nas sub-redes privadas. Anexe o grupo de segurança às instâncias de banco de dados.

**Justificativa:**  
- **Por que essa opção?**  
 * Grupos de segurança são usados para gerenciar o tráfego de entrada e saída nas instâncias Amazon RDS.
 * Para permitir que apenas instâncias EC2 nas sub-redes privadas acessem os bancos de dados, o grupo de segurança das instâncias do banco de dados deve 
permitir tráfego apenas do grupo de segurança associado às instâncias EC2 nas sub-redes privadas.

- **Por que as outras opções não são adequadas?**  
  - **A:** Alterar tabelas de rota não é suficiente para limitar o tráfego por sub-rede.  
  - **B:** Bloquear tráfego das sub-redes públicas pode impactar funcionalidades legítimas.  
  - **D:** Conexões de emparelhamento não são necessárias nesse caso.  


</details>

---

### Questão 56
Uma empresa registrou seu domínio no Amazon Route 53. A empresa utiliza o Amazon API Gateway na região ca-central-1 como interface pública para suas APIs de microsserviços no backend. Serviços de terceiros consomem essas APIs de forma segura. A empresa quer projetar a URL do API Gateway usando o domínio da empresa e o certificado correspondente para que os serviços de terceiros possam utilizar HTTPS.
Qual solução atenderá a esses requisitos?

A. Criar variáveis de estágio no API Gateway com Name="Endpoint-URL" e Value="Company Domain Name" para substituir a URL padrão. Importar o certificado público associado ao domínio da empresa no AWS Certificate Manager (ACM).

B. Criar registros DNS no Route 53 com o domínio da empresa. Apontar o registro alias para o endpoint de estágio do API Gateway Regional. Importar o certificado público associado ao domínio da empresa no AWS Certificate Manager (ACM) na região us-east-1.

C. Criar um endpoint Regional do API Gateway. Associar o endpoint do API Gateway ao domínio da empresa. Importar o certificado público associado ao domínio da empresa no AWS Certificate Manager (ACM) na mesma região. Anexar o certificado ao endpoint do API Gateway. Configurar o Route 53 para rotear o tráfego para o endpoint do API Gateway.

D. Criar um endpoint Regional do API Gateway. Associar o endpoint do API Gateway ao domínio da empresa. Importar o certificado público associado ao domínio da empresa no AWS Certificate Manager (ACM) na região us-east-1. Anexar o certificado às APIs do API Gateway. Criar registros DNS no Route 53 com o domínio da empresa. Apontar um registro A para o domínio da empresa.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie um endpoint Regional no API Gateway. Associe-o ao domínio da empresa. Importe o certificado público associado ao domínio no AWS Certificate Manager (ACM) na mesma região e configure o Route 53 para rotear o tráfego.

**Justificativa:**  
- **Por que essa opção?**  
* Regional API Gateway Endpoint:
    Para associar uma URL personalizada ao endpoint do API Gateway, é necessário criar um endpoint regional e vincular um nome de domínio personalizado ao API Gateway.

* AWS Certificate Manager (ACM):
    O certificado público associado ao domínio da empresa deve ser importado para o ACM na mesma região onde o API Gateway está configurado (ca-central-1). Isso é necessário para que o certificado seja utilizado pelo endpoint.

* Amazon Route 53:
    Configurar o Amazon Route 53 para rotear o tráfego para o endpoint do API Gateway é essencial para que o domínio da empresa aponte corretamente para o serviço.

- **Por que as outras opções não são adequadas?**  
  - **A e B:** Não atendem ao requisito de configuração na mesma região do API Gateway.  
  - **D:** Usar ACM na região us-east-1 é desnecessário neste caso.  


</details>

---

### Questão 57
Uma empresa está operando um site popular de mídia social. O site permite que os usuários façam upload de imagens para compartilhar com outros usuários. A empresa deseja garantir que as imagens não contenham conteúdo impróprio. A solução deve minimizar o esforço de desenvolvimento.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Usar o Amazon Comprehend para detectar conteúdo impróprio. Utilizar revisão humana para previsões com baixa confiança.

B. Usar o Amazon Rekognition para detectar conteúdo impróprio. Utilizar revisão humana para previsões com baixa confiança.

C. Usar o Amazon SageMaker para detectar conteúdo impróprio. Usar ground truth para rotular previsões com baixa confiança.

D. Usar o AWS Fargate para implantar um modelo de aprendizado de máquina personalizado para detectar conteúdo impróprio. Usar ground truth para rotular previsões com baixa confiança.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use o Amazon Rekognition para detectar conteúdo impróprio. Use revisão humana para previsões com baixa confiança.

**Justificativa:**  
- **Por que essa opção?**  
  O Rekognition é otimizado para análise de imagens e pode identificar conteúdo impróprio de maneira automática e eficaz.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon Comprehend é voltado para análise de texto, não imagens.  
  - **C e D:** Usar SageMaker ou modelos personalizados adiciona complexidade desnecessária.  


</details>

---

### Questão 58
Uma empresa deseja executar suas aplicações críticas em contêineres para atender aos requisitos de escalabilidade e disponibilidade. A empresa prefere focar na manutenção das aplicações críticas e não quer ser responsável pelo provisionamento e gerenciamento da infraestrutura subjacente que executa a carga de trabalho em contêineres.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Usar instâncias Amazon EC2 e instalar Docker nas instâncias.

B. Usar Amazon Elastic Container Service (Amazon ECS) em nós de trabalho Amazon EC2.

C. Usar Amazon Elastic Container Service (Amazon ECS) no AWS Fargate.

D. Usar instâncias Amazon EC2 com uma Amazon Machine Image (AMI) otimizada para o Amazon Elastic Container Service (Amazon ECS).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use o Amazon ECS no AWS Fargate.

**Justificativa:**  
- **Por que essa opção?**  
  O Fargate elimina a necessidade de gerenciar a infraestrutura subjacente, permitindo foco apenas nas aplicações.  

- **Por que as outras opções não são adequadas?**  
  - **A e D:** EC2 requer gerenciamento da infraestrutura.  
  - **B:** ECS com EC2 worker nodes ainda exige manutenção da infraestrutura.  


</details>

---

### Questão 59
Uma empresa hospeda mais de 300 sites e aplicativos globais. A empresa precisa de uma plataforma para analisar mais de 30 TB de dados de clickstream diariamente.
O que um arquiteto de soluções deve fazer para transmitir e processar os dados de clickstream?

A. Projetar um AWS Data Pipeline para arquivar os dados em um bucket Amazon S3 e executar um cluster Amazon EMR com os dados para gerar análises.

B. Criar um grupo de Auto Scaling de instâncias Amazon EC2 para processar os dados e enviá-los para um data lake no Amazon S3 para o Amazon Redshift usar para análise.

C. Armazenar os dados no Amazon CloudFront como cache. Armazenar os dados em um bucket Amazon S3. Quando um objeto for adicionado ao bucket S3, executar uma função AWS Lambda para processar os dados para análise.

D. Coletar os dados com Amazon Kinesis Data Streams. Usar Amazon Kinesis Data Firehose para transmitir os dados para um data lake no Amazon S3. Carregar os dados no Amazon Redshift para análise.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Colete os dados do Amazon Kinesis Data Streams. Use o Amazon Kinesis Data Firehose para transmitir os dados para um data lake no Amazon S3. Carregue os dados no Amazon Redshift para análise.

**Justificativa:**  
- **Por que essa opção?**  
  O Kinesis Data Streams e Firehose são projetados para lidar com grandes volumes de dados em tempo real, e o Redshift é ideal para análise massiva de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Data Pipeline é mais complexo e menos eficiente para ingestão em tempo real.  
  - **B:** EC2 é menos escalável e mais caro para lidar com grandes volumes de dados.  
  - **C:** CloudFront não é adequado para análise de dados clickstream.  


</details>

---

### Questão 60
Uma empresa tem um site hospedado na AWS. O site está atrás de um Application Load Balancer (ALB) configurado para lidar com HTTP e HTTPS separadamente. A empresa deseja que todas as solicitações ao site usem HTTPS.
O que um arquiteto de soluções deve fazer para atender a esse requisito?

A. Atualizar a ACL de rede do ALB para aceitar apenas tráfego HTTPS.

B. Criar uma regra que substitua o HTTP na URL por HTTPS.

C. Criar uma regra de ouvinte no ALB para redirecionar o tráfego HTTP para HTTPS.

D. Substituir o ALB por um Network Load Balancer configurado para usar Server Name Indication (SNI).

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie uma regra de listener no ALB para redirecionar o tráfego HTTP para HTTPS.

**Justificativa:**  
- **Por que essa opção?**  
  Configurar uma regra de redirecionamento no listener é simples, eficaz e elimina a necessidade de configurações adicionais.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Configurar a ACL da rede não realiza redirecionamento.  
  - **B:** Substituir HTTP por HTTPS na URL requer alterações adicionais no lado do cliente.  
  - **D:** Um Network Load Balancer não é necessário para este caso.  


</details>

---

### Questão 61
Uma empresa está desenvolvendo uma aplicação web de dois níveis na AWS. Os desenvolvedores da empresa implantaram a aplicação em uma instância Amazon EC2 que se conecta diretamente a um banco de dados Amazon RDS no backend. A empresa não deve incluir as credenciais do banco de dados no código da aplicação. Além disso, a empresa deve implementar uma solução para rotacionar automaticamente as credenciais do banco de dados regularmente.
Qual solução atenderá a esses requisitos com o menor esforço operacional?

A. Armazenar as credenciais do banco de dados nos metadados da instância. Usar regras do Amazon EventBridge (Amazon CloudWatch Events) para executar uma função AWS Lambda programada que atualiza as credenciais do RDS e dos metadados da instância ao mesmo tempo.

B. Armazenar as credenciais do banco de dados em um arquivo de configuração em um bucket Amazon S3 criptografado. Usar regras do Amazon EventBridge (Amazon CloudWatch Events) para executar uma função AWS Lambda programada que atualiza as credenciais do RDS e do arquivo de configuração ao mesmo tempo. Usar a versionamento do S3 para garantir a capacidade de retornar a valores anteriores.

C. Armazenar as credenciais do banco de dados como um segredo no AWS Secrets Manager. Ativar a rotação automática para o segredo. Anexar a permissão necessária à função da instância EC2 para conceder acesso ao segredo.

D. Armazenar as credenciais do banco de dados como parâmetros criptografados no AWS Systems Manager Parameter Store. Ativar a rotação automática para os parâmetros criptografados. Anexar a permissão necessária à função da instância EC2 para conceder acesso aos parâmetros criptografados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Armazene as credenciais do banco como um segredo no AWS Secrets Manager. Ative a rotação automática para o segredo. Anexe a permissão necessária ao role da instância EC2 para acessar o segredo.

**Justificativa:**  
- **Por que essa opção?**  
  O Secrets Manager oferece rotação automática e gerenciamento seguro de credenciais com integração nativa ao EC2.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Armazenar credenciais nos metadados da instância não é seguro.  
  - **B:** Armazenar credenciais em arquivos de configuração no S3 adiciona complexidade e reduz a segurança.  
  - **D:** O Parameter Store não possui rotação automática nativa como o Secrets Manager.  


</details>

---

### Questão 62
Uma empresa está implantando um novo aplicativo web público na AWS. O aplicativo será executado atrás de um Application Load Balancer (ALB). O aplicativo precisa ser criptografado na borda com um certificado SSL/TLS emitido por uma autoridade certificadora (CA) externa. O certificado deve ser rotacionado todos os anos antes de expirar.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Usar o AWS Certificate Manager (ACM) para emitir um certificado SSL/TLS. Aplicar o certificado ao ALB. Usar o recurso de renovação gerenciada para rotacionar automaticamente o certificado.

B. Usar o AWS Certificate Manager (ACM) para emitir um certificado SSL/TLS. Importar o material da chave do certificado. Aplicar o certificado ao ALB. Usar o recurso de renovação gerenciada para rotacionar automaticamente o certificado.

C. Usar o AWS Certificate Manager (ACM) Private Certificate Authority para emitir um certificado SSL/TLS da CA raiz. Aplicar o certificado ao ALB. Usar o recurso de renovação gerenciada para rotacionar automaticamente o certificado.

D. Usar o AWS Certificate Manager (ACM) para importar um certificado SSL/TLS. Aplicar o certificado ao ALB. Usar o Amazon EventBridge (Amazon CloudWatch Events) para enviar uma notificação quando o certificado estiver próximo de expirar. Rotacionar o certificado manualmente.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Use o AWS Certificate Manager (ACM) para importar um certificado SSL/TLS. Aplique o certificado ao ALB. Use o Amazon EventBridge (Amazon CloudWatch Events) para enviar notificações quando o certificado estiver próximo do vencimento. Faça a rotação do certificado manualmente.

**Justificativa:**  
- **Por que essa opção?**  
  Importar certificados externos no ACM é necessário para atender ao requisito de usar um CA externo, e o EventBridge permite notificações automatizadas para gerenciar a rotação.  

- **Por que as outras opções não são adequadas?**  
  - **A:**  O ACM não pode emitir certificados SSL/TLS de uma autoridade certificadora externa.
  - **B:**  Não há suporte para importar material de chave para certificados gerados pelo ACM. Além disso, a renovação gerenciada não funciona para certificados importados.
  - **C:** O ACM Private Certificate Authority é usado para criar CAs privadas internas. Ele não atende ao requisito de utilizar uma autoridade certificadora externa.

</details>

---

### Questão 63
Uma empresa executa sua infraestrutura na AWS e tem uma base registrada de 700.000 usuários para seu aplicativo de gerenciamento de documentos. A empresa pretende criar um produto que converte grandes arquivos .pdf para o formato de imagem .jpg. Os arquivos .pdf têm, em média, 5 MB de tamanho. A empresa precisa armazenar os arquivos originais e os arquivos convertidos. Um arquiteto de soluções deve projetar uma solução escalável para atender à demanda que crescerá rapidamente ao longo do tempo.
Qual solução atende a esses requisitos da forma mais econômica?

A. Salvar os arquivos .pdf no Amazon S3. Configurar um evento PUT do S3 para invocar uma função AWS Lambda para converter os arquivos para o formato .jpg e armazená-los de volta no Amazon S3.

B. Salvar os arquivos .pdf no Amazon DynamoDB. Usar o recurso Streams do DynamoDB para invocar uma função AWS Lambda para converter os arquivos para o formato .jpg e armazená-los de volta no DynamoDB.

C. Fazer o upload dos arquivos .pdf para uma aplicação AWS Elastic Beanstalk que inclui instâncias Amazon EC2, armazenamento Amazon Elastic Block Store (Amazon EBS) e um grupo Auto Scaling. Usar um programa nas instâncias EC2 para converter os arquivos para o formato .jpg. Salvar os arquivos .pdf e .jpg no armazenamento EBS.

D. Fazer o upload dos arquivos .pdf para uma aplicação AWS Elastic Beanstalk que inclui instâncias Amazon EC2, armazenamento Amazon Elastic File System (Amazon EFS) e um grupo Auto Scaling. Usar um programa nas instâncias EC2 para converter os arquivos para o formato .jpg. Salvar os arquivos .pdf e .jpg no armazenamento EBS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Salve os arquivos PDF no Amazon S3. Configure um evento PUT no S3 para invocar uma função AWS Lambda que converte os arquivos para o formato JPG e os armazena novamente no S3.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 e o Lambda são escaláveis e econômicos, permitindo ingestão automática e processamento de arquivos sem infraestrutura adicional.  

- **Por que as outras opções não são adequadas?**  
  - **B:** DynamoDB Streams não é projetado para processar arquivos grandes como PDFs.  
  - **C e D:** Elastic Beanstalk e EC2 aumentam a complexidade e o custo operacional.  


</details>

---

### Questão 64
Uma empresa possui mais de 5 TB de dados de arquivos em servidores de arquivos Windows que operam no local (on-premises). Usuários e aplicativos interagem com os dados diariamente. A empresa está migrando suas cargas de trabalho Windows para a AWS. À medida que continua esse processo, a empresa precisa de acesso ao armazenamento de arquivos na AWS e no local com latência mínima. A solução deve minimizar a sobrecarga operacional e não exigir mudanças significativas nos padrões existentes de acesso aos arquivos. A empresa usa uma conexão VPN Site-to-Site da AWS para conectividade com a AWS.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Implantar e configurar o Amazon FSx for Windows File Server na AWS. Mover os dados de arquivos locais para o FSx for Windows File Server. Reconfigurar as cargas de trabalho para usar o FSx for Windows File Server na AWS.

B. Implantar e configurar um Amazon S3 File Gateway no local. Mover os dados de arquivos locais para o S3 File Gateway. Reconfigurar as cargas de trabalho locais e na nuvem para usar o S3 File Gateway.

C. Implantar e configurar um Amazon S3 File Gateway no local. Mover os dados de arquivos locais para o Amazon S3. Reconfigurar as cargas de trabalho para usar diretamente o Amazon S3 ou o S3 File Gateway, dependendo da localização de cada carga de trabalho.

D. Implantar e configurar o Amazon FSx for Windows File Server na AWS. Implantar e configurar um Amazon FSx File Gateway no local. Mover os dados de arquivos locais para o FSx File Gateway. Configurar as cargas de trabalho na nuvem para usar o FSx for Windows File Server na AWS. Configurar as cargas de trabalho locais para usar o FSx File Gateway.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Implante e configure Amazon FSx for Windows File Server na AWS. Implante e configure um Amazon FSx File Gateway no local. Mova os dados locais para o FSx File Gateway.

**Justificativa:**  
- **Por que essa opção?**  
  O FSx for Windows File Server oferece um sistema de arquivos totalmente gerenciado e compatível com Windows. O FSx File Gateway garante acesso contínuo e com baixa latência para os usuários locais.  

- **Por que as outras opções não são adequadas?**  
  - **A e C:** Apenas o FSx ou o S3 File Gateway não atendem ao requisito de baixa latência para acessos locais e na nuvem.  
  - **B:** O S3 File Gateway sozinho não é compatível com os padrões de compartilhamento de arquivos do Windows.  


</details>

---

### Questão 65
Um hospital implantou recentemente uma API RESTful com o Amazon API Gateway e o AWS Lambda. O hospital usa o API Gateway e o Lambda para fazer upload de relatórios nos formatos PDF e JPEG. O hospital precisa modificar o código do Lambda para identificar informações protegidas de saúde (PHI, Protected Health Information) nos relatórios.
Qual solução atenderá a esses requisitos com a menor sobrecarga operacional?

A. Usar bibliotecas Python existentes para extrair o texto dos relatórios e identificar as PHI a partir do texto extraído.

B. Usar o Amazon Textract para extrair o texto dos relatórios. Usar o Amazon SageMaker para identificar as PHI a partir do texto extraído.

C. Usar o Amazon Textract para extrair o texto dos relatórios. Usar o Amazon Comprehend Medical para identificar as PHI a partir do texto extraído.

D. Usar o Amazon Rekognition para extrair o texto dos relatórios. Usar o Amazon Comprehend Medical para identificar as PHI a partir do texto extraído.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use Amazon Textract para extrair texto dos relatórios. Use Amazon Comprehend Medical para identificar PHI no texto extraído.

**Justificativa:**  
- **Por que essa opção?**  
  O Textract automatiza a extração de texto de PDFs e imagens, enquanto o Comprehend Medical é otimizado para detectar informações de saúde protegidas, minimizando o esforço operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Bibliotecas Python exigem mais desenvolvimento e manutenção manual.  
  - **B e D:** SageMaker e Rekognition adicionam complexidade desnecessária para o caso específico de PHI.  


</details>

---

### Questão 66
Uma empresa possui um aplicativo que gera um grande número de arquivos, cada um com aproximadamente 5 MB. Os arquivos são armazenados no Amazon S3. A política da empresa exige que os arquivos sejam armazenados por 4 anos antes de serem excluídos. A acessibilidade imediata é sempre necessária, pois os arquivos contêm dados críticos de negócios que não são fáceis de reproduzir. Os arquivos são acessados frequentemente nos primeiros 30 dias após a criação, mas raramente são acessados após esses 30 dias.
Qual solução de armazenamento é a mais econômica?

A. Criar uma política de ciclo de vida do S3 para mover arquivos do S3 Standard para o S3 Glacier 30 dias após a criação do objeto. Excluir os arquivos 4 anos após a criação.

B. Criar uma política de ciclo de vida do S3 para mover arquivos do S3 Standard para o S3 One Zone-Infrequent Access (S3 One Zone-IA) 30 dias após a criação do objeto. Excluir os arquivos 4 anos após a criação.

C. Criar uma política de ciclo de vida do S3 para mover arquivos do S3 Standard para o S3 Standard-Infrequent Access (S3 Standard-IA) 30 dias após a criação do objeto. Excluir os arquivos 4 anos após a criação.

D. Criar uma política de ciclo de vida do S3 para mover arquivos do S3 Standard para o S3 Standard-Infrequent Access (S3 Standard-IA) 30 dias após a criação do objeto. Mover os arquivos para o S3 Glacier 4 anos após a criação do objeto.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie uma política de ciclo de vida para mover arquivos do S3 Standard para S3 Standard-Infrequent Access (S3 Standard-IA) após 30 dias. Exclua os arquivos após 4 anos.

**Justificativa:**  
- **Por que essa opção?**  
  O S3 Standard-IA oferece armazenamento mais barato para dados acessados raramente, mantendo acessibilidade imediata.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Glacier não é adequado para acessos frequentes nos primeiros 30 dias.  
  - **B:** One Zone-IA compromete a resiliência.  
  - **D:** Mover para Glacier depois de 4 anos adiciona complexidade desnecessária.  


</details>

---

### Questão 67
Uma empresa hospeda um aplicativo em várias instâncias Amazon EC2. O aplicativo processa mensagens de uma fila Amazon SQS, escreve em uma tabela do Amazon RDS e exclui a mensagem da fila. Ocasionalmente, são encontrados registros duplicados na tabela RDS. A fila SQS não contém mensagens duplicadas.
O que um arquiteto de soluções deve fazer para garantir que as mensagens sejam processadas apenas uma vez?

A. Usar a chamada da API CreateQueue para criar uma nova fila.

B. Usar a chamada da API AddPermission para adicionar as permissões apropriadas.

C. Usar a chamada da API ReceiveMessage para definir um tempo de espera apropriado.

D. Usar a chamada da API ChangeMessageVisibility para aumentar o visibility timeout.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Use a chamada ChangeMessageVisibility API para aumentar o timeout de visibilidade.

**Justificativa:**  
- **Por que essa opção?**  
  Um timeout de visibilidade maior garante que mensagens em processamento não sejam entregues novamente antes de serem excluídas.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Criar uma nova fila não resolve o problema.  
  - **B:** Adicionar permissões não impacta duplicidade de mensagens.  
  - **C:** Ajustar o tempo de espera na API ReceiveMessage não evita o problema de timeout.  O ReceiveMessage com um tempo de espera (wait time) adequado é útil para diminuir chamadas desnecessárias à API, mas não afeta o comportamento do visibility timeout.


</details>

---

### Questão 68
Um arquiteto de soluções está projetando uma nova arquitetura híbrida para estender a infraestrutura local (on-premises) de uma empresa para a AWS. A empresa requer uma conexão altamente disponível com baixa latência consistente para uma região da AWS. A empresa deseja minimizar custos e está disposta a aceitar tráfego mais lento caso a conexão principal falhe.
O que o arquiteto de soluções deve fazer para atender a esses requisitos?

A. Provisionar uma conexão AWS Direct Connect para uma região. Provisionar uma conexão VPN como backup caso a conexão principal Direct Connect falhe.

B. Provisionar uma conexão de túnel VPN para uma região para conectividade privada. Provisionar um segundo túnel VPN para conectividade privada e como backup caso a conexão VPN principal falhe.

C. Provisionar uma conexão AWS Direct Connect para uma região. Provisionar uma segunda conexão Direct Connect para a mesma região como backup caso a conexão principal Direct Connect falhe.

D. Provisionar uma conexão AWS Direct Connect para uma região. Usar o atributo de failover do Direct Connect no AWS CLI para criar automaticamente uma conexão de backup caso a conexão principal Direct Connect falhe.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Configure uma conexão AWS Direct Connect para a região. Configure uma conexão VPN como backup.

**Justificativa:**  
- **Por que essa opção?**  
  O Direct Connect oferece latência consistente, e a VPN serve como uma solução de backup mais barata.  

- **Por que as outras opções não são adequadas?**  
  - **B:** VPNs não oferecem a mesma consistência de latência que o Direct Connect.  
  - **C:** Usar duas conexões Direct Connect aumenta os custos desnecessariamente.  
  - **D:** O atributo failover não cria automaticamente uma conexão de backup.  


</details>

---

### Questão 69
Uma empresa está executando um aplicativo web crítico para os negócios em instâncias Amazon EC2 atrás de um Application Load Balancer (ALB). As instâncias EC2 estão em um grupo de Auto Scaling. O aplicativo utiliza um banco de dados Amazon Aurora PostgreSQL implantado em uma única Zona de Disponibilidade (AZ). A empresa deseja que o aplicativo seja altamente disponível, com mínimo tempo de inatividade e mínima perda de dados.
Qual solução atenderá a esses requisitos com o menor esforço operacional?

A. Colocar as instâncias EC2 em diferentes regiões da AWS. Usar verificações de integridade do Amazon Route 53 para redirecionar o tráfego. Usar a replicação entre regiões do Aurora PostgreSQL.

B. Configurar o grupo de Auto Scaling para usar várias Zonas de Disponibilidade. Configurar o banco de dados como Multi-AZ. Configurar uma instância Amazon RDS Proxy para o banco de dados.

C. Configurar o grupo de Auto Scaling para usar uma única Zona de Disponibilidade. Gerar snapshots do banco de dados a cada hora. Recuperar o banco de dados a partir dos snapshots em caso de falha.

D. Configurar o grupo de Auto Scaling para usar várias regiões da AWS. Escrever os dados do aplicativo no Amazon S3. Usar notificações de eventos do S3 para acionar uma função AWS Lambda para gravar os dados no banco de dados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Configure o Auto Scaling Group para usar múltiplas zonas de disponibilidade. Configure o banco de dados como Multi-AZ. Configure uma instância Amazon RDS Proxy para o banco de dados.

**Justificativa:**  
- **Por que essa opção?**  
  * Configurar instâncias em múltiplas zonas e usar Multi-AZ no Aurora PostgreSQL garante alta disponibilidade e resiliência. O RDS Proxy melhora o gerenciamento de conexões e minimiza o impacto de falhas.  
  * O Amazon RDS Proxy melhora a escalabilidade e a disponibilidade ao gerenciar conexões entre o aplicativo e o banco de dados Aurora. Ele reduz o impacto de picos de tráfego e melhora a resiliência.

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar múltiplas regiões e replicação cross-region aumenta complexidade e latência.  
  - **C:** Backups por snapshots não garantem alta disponibilidade ou recuperação rápida.  
  - **D:** Usar múltiplas regiões para dados críticos adiciona desafios de sincronização e latência.  


</details>

---

### Questão 70
O aplicativo HTTP de uma empresa está atrás de um Network Load Balancer (NLB). O grupo de destino do NLB está configurado para usar um grupo de Auto Scaling do Amazon EC2 com várias instâncias EC2 que executam o serviço web.
A empresa percebeu que o NLB não está detectando erros HTTP do aplicativo. Esses erros exigem reinicializações manuais das instâncias EC2 que executam o serviço web. A empresa precisa melhorar a disponibilidade do aplicativo sem escrever scripts ou código personalizados.
O que um arquiteto de soluções deve fazer para atender a esses requisitos?

A. Ativar verificações de integridade HTTP no NLB, fornecendo a URL do aplicativo da empresa.

B. Adicionar um cron job às instâncias EC2 para verificar os logs locais do aplicativo a cada minuto. Se erros HTTP forem detectados, o aplicativo será reiniciado.

C. Substituir o NLB por um Application Load Balancer (ALB). Ativar verificações de integridade HTTP fornecendo a URL do aplicativo da empresa. Configurar uma ação de Auto Scaling para substituir instâncias não saudáveis.

D. Criar um alarme do Amazon CloudWatch que monitore a métrica UnhealthyHostCount para o NLB. Configurar uma ação de Auto Scaling para substituir instâncias não saudáveis quando o alarme estiver no estado ALARM.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Substitua o NLB por um Application Load Balancer. Habilite verificações de integridade HTTP fornecendo o URL da aplicação. Configure uma ação de Auto Scaling para substituir instâncias não saudáveis.

**Justificativa:**  
- **Por que essa opção?**  
  Um Application Load Balancer (ALB) é mais adequado para aplicações HTTP/HTTPS e suporta verificações de integridade baseadas em URL.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O NLB não oferece suporte a verificações de integridade baseadas em HTTP.  
  - **B:** Adicionar um cron job aumenta a complexidade sem resolver o problema da detecção automática.  
  - **D:** Alarmes do CloudWatch monitoram, mas não substituem o NLB inadequado para HTTP.  


</details>

---

### Questão 71
Uma empresa opera um aplicativo de compras que usa o Amazon DynamoDB para armazenar informações de clientes. Em caso de corrupção de dados, um arquiteto de soluções precisa projetar uma solução que atenda a um RPO (Recovery Point Objective) de 15 minutos e um RTO (Recovery Time Objective) de 1 hora.
O que o arquiteto de soluções deve recomendar para atender a esses requisitos?

A. Configurar tabelas globais do DynamoDB. Para recuperação de RPO, apontar o aplicativo para uma região da AWS diferente.

B. Configurar a recuperação no tempo (point-in-time recovery) do DynamoDB. Para recuperação de RPO, restaurar para o ponto no tempo desejado.

C. Exportar os dados do DynamoDB para o Amazon S3 Glacier diariamente. Para recuperação de RPO, importar os dados do S3 Glacier para o DynamoDB.

D. Agendar snapshots do Amazon Elastic Block Store (Amazon EBS) para a tabela do DynamoDB a cada 15 minutos. Para recuperação de RPO, restaurar a tabela do DynamoDB usando o snapshot do EBS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Configure a recuperação point-in-time (PITR) do DynamoDB. Para recuperação, restaure para o ponto desejado no tempo.

**Justificativa:**  
- **Por que essa opção?**  
  O PITR do DynamoDB fornece restauração granular em até 35 dias, permitindo recuperação rápida e precisa dentro do RPO/RTO.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Global tables não são projetadas para recuperação de dados corrompidos.  
  - **C:** Exportar para Glacier não atende ao RTO de 1 hora devido ao tempo de recuperação.  
  - **D:** Snapshots do EBS não são uma funcionalidade nativa do DynamoDB.  


</details>

---

### Questão 72
Uma empresa opera um aplicativo de processamento de fotos que precisa frequentemente fazer upload e download de imagens de buckets do Amazon S3 localizados na mesma região da AWS. Um arquiteto de soluções percebeu um aumento nos custos de transferência de dados e precisa implementar uma solução para reduzir esses custos.
Como o arquiteto de soluções pode atender a esse requisito?

A. Implantar o Amazon API Gateway em uma sub-rede pública e ajustar a tabela de rotas para rotear as chamadas ao S3 através dele.

B. Implantar um gateway NAT em uma sub-rede pública e anexar uma política de endpoint que permita acesso aos buckets S3.

C. Implantar o aplicativo em uma sub-rede pública e permitir que ele roteie por meio de um internet gateway para acessar os buckets S3.

D. Implantar um endpoint de gateway S3 para a VPC e anexar uma política de endpoint que permita acesso aos buckets S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Implemente um endpoint de gateway S3 VPC na VPC e anexe uma política de endpoint que permita acesso aos buckets S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint de gateway para S3 permite que instâncias na VPC acessem o S3 sem usar a internet pública, eliminando custos adicionais de transferência de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A e B:** O uso de NAT ou API Gateway adiciona complexidade e custos desnecessários.  
  - **C:** Encaminhar pelo internet gateway não resolve os custos de transferência dentro da mesma região.  


</details>

---

### Questão 73
Uma empresa lançou recentemente instâncias de aplicação baseadas em Linux no Amazon EC2 em uma sub-rede privada e uma instância de bastion host baseada em Linux no Amazon EC2 em uma sub-rede pública de uma VPC. Um arquiteto de soluções precisa conectar-se da rede local (on-premises), através da conexão de internet da empresa, ao bastion host e, em seguida, aos servidores de aplicação. O arquiteto de soluções deve garantir que os grupos de segurança de todas as instâncias EC2 permitam esse acesso.
Quais combinações de etapas o arquiteto de soluções deve realizar para atender a esses requisitos? (Escolha duas.)

A. Substituir o grupo de segurança atual do bastion host por um que permita apenas acesso de entrada a partir das instâncias de aplicação.

B. Substituir o grupo de segurança atual do bastion host por um que permita apenas acesso de entrada a partir do intervalo de IP interno da empresa.

C. Substituir o grupo de segurança atual do bastion host por um que permita apenas acesso de entrada a partir do intervalo de IP externo da empresa.

D. Substituir o grupo de segurança atual das instâncias de aplicação por um que permita acesso SSH de entrada somente a partir do endereço IP privado do bastion host.

E. Substituir o grupo de segurança atual das instâncias de aplicação por um que permita acesso SSH de entrada somente a partir do endereço IP público do bastion host.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C, D.** Substitua o grupo de segurança do bastion host para permitir acesso apenas do IP interno da empresa. Configure o grupo de segurança das instâncias de aplicação para permitir acesso SSH apenas do IP privado do bastion host.

**Justificativa:**  
- **Por que essas opções?**  
 * Opção C: Permitir acesso de entrada ao bastion host apenas do intervalo de IP externo da empresa atende ao requisito de restringir o acesso ao bastion host.
 * Opção D: Configurar o grupo de segurança das instâncias de aplicação para permitir acesso SSH apenas do endereço IP privado do bastion host é a abordagem correta.  

- **Por que as outras opções não são adequadas?**  
 **A**  Restringir o acesso ao bastion host apenas às instâncias de aplicação é desnecessário. O bastion host precisa permitir acesso da rede externa para que o administrador se conecte.
 **B**  Permitir acesso ao bastion host a partir do intervalo de IP interno da empresa não funcionaria porque a conexão é feita através da internet pública.
 **E:**  Permitir acesso às instâncias de aplicação a partir do endereço IP público do bastion host é inseguro e não reflete as práticas recomendadas para sub-redes privadas.


</details>

---

### Questão 74
Um arquiteto de soluções está projetando uma aplicação web de dois níveis. A aplicação consiste em um nível web voltado para o público, hospedado em instâncias Amazon EC2 em sub-redes públicas. O nível de banco de dados consiste em um Microsoft SQL Server executado no Amazon EC2 em uma sub-rede privada. A segurança é uma alta prioridade para a empresa.
Como os grupos de segurança devem ser configurados nesta situação? (Escolha duas.)

A. Configurar o grupo de segurança para o nível web para permitir tráfego de entrada na porta 443 a partir de 0.0.0.0/0.

B. Configurar o grupo de segurança para o nível web para permitir tráfego de saída na porta 443 para 0.0.0.0/0.

C. Configurar o grupo de segurança para o nível de banco de dados para permitir tráfego de entrada na porta 1433 a partir do grupo de segurança do nível web.

D. Configurar o grupo de segurança para o nível de banco de dados para permitir tráfego de saída nas portas 443 e 1433 para o grupo de segurança do nível web.

E. Configurar o grupo de segurança para o nível de banco de dados para permitir tráfego de entrada nas portas 443 e 1433 a partir do grupo de segurança do nível web.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A, C.** Configure o grupo de segurança da camada web para permitir tráfego de entrada na porta 443 de 0.0.0.0/0. Configure o grupo de segurança da camada de banco de dados para permitir tráfego de entrada na porta 1433 do grupo de segurança da camada web.

**Justificativa:**  
- **Por que essas opções?**  
  Garantem acesso seguro ao front-end público e tráfego controlado para o banco de dados.  

- **Por que as outras opções não são adequadas?**  
  - **B, D, E:** Configurações de saída não atendem ao requisito principal de tráfego controlado entre as camadas.  


</details>

---

### Questão 75
Uma empresa deseja migrar um aplicativo de múltiplos níveis de sua infraestrutura local para a AWS Cloud para melhorar o desempenho do aplicativo. O aplicativo consiste em camadas de aplicação que se comunicam entre si por meio de serviços RESTful. Transações são perdidas quando uma camada fica sobrecarregada. Um arquiteto de soluções deve projetar uma solução que resolva esses problemas e modernize o aplicativo.
Qual solução atende a esses requisitos e é a mais eficiente operacionalmente?

A. Usar o Amazon API Gateway para direcionar transações para funções AWS Lambda como camada de aplicação. Usar o Amazon Simple Queue Service (Amazon SQS) como camada de comunicação entre os serviços de aplicação.

B. Usar métricas do Amazon CloudWatch para analisar o histórico de desempenho do aplicativo e determinar a utilização máxima dos servidores durante as falhas de desempenho. Aumentar o tamanho das instâncias Amazon EC2 do servidor de aplicação para atender aos requisitos de pico.

C. Usar o Amazon Simple Notification Service (Amazon SNS) para gerenciar a comunicação entre servidores de aplicação executados no Amazon EC2 em um grupo de Auto Scaling. Usar o Amazon CloudWatch para monitorar o comprimento da fila SNS e escalar para cima e para baixo conforme necessário.

D. Usar o Amazon Simple Queue Service (Amazon SQS) para gerenciar a comunicação entre servidores de aplicação executados no Amazon EC2 em um grupo de Auto Scaling. Usar o Amazon CloudWatch para monitorar o comprimento da fila SQS e escalar quando falhas de comunicação forem detectadas.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Use o Amazon API Gateway para direcionar transações para funções AWS Lambda como camada de aplicação. Use o SQS como camada de comunicação entre os serviços de aplicação.

**Justificativa:**  
- **Por que essa opção?**  
  Moderniza a arquitetura, reduz custos operacionais e melhora a escalabilidade com um design serverless.  

- **Por que as outras opções não são adequadas?**  
  - **B, C, D:** Soluções baseadas em EC2 ou SNS adicionam complexidade e não otimizam a eficiência operacional.  


</details>

---

### Questão 76
Uma empresa recebe 10 TB de dados de instrumentação todos os dias de várias máquinas localizadas em uma única fábrica. Os dados consistem em arquivos JSON armazenados em uma rede de armazenamento (SAN) em um data center local situado dentro da fábrica. A empresa deseja enviar esses dados para o Amazon S3, onde poderão ser acessados por vários sistemas adicionais que fornecem análises críticas em tempo quase real. Uma transferência segura é importante porque os dados são considerados sensíveis.
Qual solução oferece a transferência de dados MAIS confiável?

A. AWS DataSync via internet pública

B. AWS DataSync via AWS Direct Connect

C. AWS Database Migration Service (AWS DMS) via internet pública

D. AWS Database Migration Service (AWS DMS) via AWS Direct Connect

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use o AWS DataSync sobre AWS Direct Connect.

**Justificativa:**  
- **Por que essa opção?**  
  O DataSync é confiável e eficiente para transferências em grande escala, enquanto o Direct Connect garante segurança e baixa latência.  

- **Por que as outras opções não são adequadas?**  
  - **A, C, D:** Usar a internet pública ou DMS não oferece o nível de segurança e desempenho exigido para esse volume de dados.  


</details>

---

### Questão 77
Uma empresa precisa configurar uma arquitetura de ingestão de dados em tempo real para sua aplicação. A empresa precisa de uma API, um processo que transforme os dados enquanto eles são transmitidos, e uma solução de armazenamento para os dados.
Qual solução atenderá a esses requisitos com o MENOR esforço operacional?

A. Implantar uma instância Amazon EC2 para hospedar uma API que envie dados para um stream de dados do Amazon Kinesis. Criar um stream de entrega do Amazon Kinesis Data Firehose que use o stream de dados do Kinesis como fonte de dados. Usar funções AWS Lambda para transformar os dados. Usar o stream de entrega do Kinesis Data Firehose para enviar os dados ao Amazon S3.

B. Implantar uma instância Amazon EC2 para hospedar uma API que envie dados para o AWS Glue. Desativar a verificação de fonte/destino na instância EC2. Usar o AWS Glue para transformar os dados e enviá-los ao Amazon S3.

C. Configurar uma API do Amazon API Gateway para enviar dados para um stream de dados do Amazon Kinesis. Criar um stream de entrega do Amazon Kinesis Data Firehose que use o stream de dados do Kinesis como fonte de dados. Usar funções AWS Lambda para transformar os dados. Usar o stream de entrega do Kinesis Data Firehose para enviar os dados ao Amazon S3.

D. Configurar uma API do Amazon API Gateway para enviar dados para o AWS Glue. Usar funções AWS Lambda para transformar os dados. Usar o AWS Glue para enviar os dados ao Amazon S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Configure uma API no Amazon API Gateway para enviar dados para um fluxo de dados do Amazon Kinesis. Crie um fluxo de entrega do Amazon Kinesis Data Firehose que use o fluxo de dados do Kinesis como fonte de dados. Use funções AWS Lambda para transformar os dados. Use o Kinesis Data Firehose para enviar os dados para o Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  A combinação de Kinesis, Firehose e Lambda permite ingestão, transformação e armazenamento em tempo real, com o menor overhead operacional.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar EC2 aumenta o custo e a complexidade em relação à solução serverless.  
  - **B:** O AWS Glue é mais adequado para ETL em grande escala, mas não é ideal para transformações em tempo real.  
  - **D:** A solução de Lambda com Glue adiciona complexidade sem necessidade de integração com Firehose.  


</details>

---

### Questão 78
Uma empresa precisa manter dados de transações de usuários em uma tabela do Amazon DynamoDB. A empresa deve reter os dados por 7 anos.
Qual é a solução mais eficiente em termos operacionais que atende a esses requisitos?

A. Use o recurso de recuperação pontual do DynamoDB (point-in-time recovery) para fazer backups contínuos da tabela.

B. Use o AWS Backup para criar agendamentos de backup e políticas de retenção para a tabela.

C. Crie um backup sob demanda da tabela usando o console do DynamoDB. Armazene o backup em um bucket do Amazon S3. Configure uma política de ciclo de vida no bucket do S3.

D. Crie uma regra do Amazon EventBridge (Amazon CloudWatch Events) para invocar uma função AWS Lambda. Configure a função Lambda para fazer o backup da tabela e armazená-lo em um bucket do Amazon S3. Configure uma política de ciclo de vida no bucket do S3.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use o AWS Backup para criar agendamentos de backup e políticas de retenção para a tabela.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Backup oferece uma solução centralizada e de baixo overhead para gerenciar backups e políticas de retenção de dados.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O DynamoDB point-in-time recovery (PITR) não é uma solução de backup de longo prazo.  
  - **C:** Armazenar backups em S3 não é automatizado e adiciona complexidade.  
  - **D:** Usar Lambda para backups manualmente exigiria mais configuração e não é tão eficiente quanto o AWS Backup.  


</details>

---

### Questão 79
Uma empresa está planejando usar uma tabela do Amazon DynamoDB para armazenamento de dados. A empresa está preocupada com a otimização de custos. A tabela não será usada na maioria das manhãs. À noite, o tráfego de leitura e gravação será frequentemente imprevisível. Quando ocorrerem picos de tráfego, eles acontecerão muito rapidamente.
O que um arquiteto de soluções deve recomendar?

A. Criar uma tabela DynamoDB no modo de capacidade sob demanda (on-demand).

B. Criar uma tabela DynamoDB com um índice secundário global (global secondary index).

C. Criar uma tabela DynamoDB com capacidade provisionada e auto scaling.

D. Criar uma tabela DynamoDB no modo de capacidade provisionada, configurando-a como uma tabela global.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Criar uma tabela DynamoDB no modo de capacidade sob demanda (on-demand).

**Justificativa:**  
- **Por que essa opção?**  
* O modo on-demand ajusta automaticamente a capacidade de leitura e gravação com base na demanda atual, eliminando a necessidade de gerenciamento manual de capacidade.
* Ideal para casos em que o tráfego é imprevisível e pode ter picos rápidos.
* Custos são otimizados porque você paga apenas pelo que usa, sem necessidade de provisionar capacidade antecipadamente.
* Conclusão: A melhor escolha para cenários com tráfego imprevisível e picos rápidos.

- **Por que as outras opções não são adequadas?**  
  - **B:** Criar um índice global secundário não resolve o problema de otimização de capacidade.  
  - **C:** Funciona, mas não é a solução mais eficiente para este caso.
  - **D:** Global tables não são necessárias para este cenário, já que não há exigência de múltiplas regiões.  


</details>

---

### Questão 80
Uma empresa recentemente assinou um contrato com um parceiro AWS Managed Service Provider (MSP) para ajudar em uma iniciativa de migração de aplicativos. Um arquiteto de soluções precisa compartilhar uma Amazon Machine Image (AMI) de uma conta AWS existente com a conta AWS do parceiro MSP. A AMI é baseada em volumes do Amazon Elastic Block Store (EBS) e utiliza uma chave gerenciada pelo cliente no AWS Key Management Service (KMS) para criptografar os snapshots dos volumes EBS.
Qual é a maneira MAIS segura de o arquiteto de soluções compartilhar a AMI com a conta AWS do parceiro MSP?

A. Torne a AMI e os snapshots criptografados publicamente disponíveis. Modifique a política da chave para permitir que a conta AWS do parceiro MSP use a chave.

B. Modifique a propriedade launchPermission da AMI. Compartilhe a AMI apenas com a conta AWS do parceiro MSP. Modifique a política da chave para permitir que a conta AWS do parceiro MSP use a chave.

C. Modifique a propriedade launchPermission da AMI. Compartilhe a AMI apenas com a conta AWS do parceiro MSP. Modifique a política da chave para confiar em uma nova chave KMS de propriedade do parceiro MSP para criptografia.

D. Exporte a AMI da conta de origem para um bucket Amazon S3 na conta AWS do parceiro MSP. Criptografe o bucket S3 com uma nova chave KMS de propriedade do parceiro MSP. Copie e inicie a AMI na conta AWS do parceiro MSP.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Modifique a propriedade launchPermission da AMI. Compartilhe a AMI apenas com a conta AWS do parceiro MSP. Modifique a política da chave para confiar em uma nova chave KMS de propriedade do parceiro MSP para criptografia.

**Justificativa:**  
- **Por que essa opção?**  
  Modificar as permissões de lançamento e as políticas da chave KMS permite compartilhar a AMI de maneira segura, sem torná-la pública.  

- **Por que as outras opções não são adequadas?**  
  - **B:** Permitir que a conta do parceiro use a chave original (gerenciada pelo cliente) mantém dependências entre as contas e não transfere o controle total para o parceiro MSP.
  - **C:** Usar uma chave do MSP comprometeria o controle sobre a criptografia.  
  - **D:** Exportar a AMI para S3 não é a abordagem mais eficiente para compartilhar uma AMI.  


</details>

---

### Questão 81
Um arquiteto de soluções está projetando a arquitetura em nuvem para um novo aplicativo que será implantado na AWS. O processo deve ser executado em paralelo enquanto adiciona e remove nós do aplicativo conforme necessário, com base no número de trabalhos a serem processados. O aplicativo de processamento é sem estado (stateless). O arquiteto de soluções deve garantir que o aplicativo seja fracamente acoplado e que os itens de trabalho sejam armazenados de forma durável.
Qual design o arquiteto de soluções deve usar?

A. Crie um tópico do Amazon SNS para enviar os trabalhos que precisam ser processados. Crie uma Amazon Machine Image (AMI) que contenha o aplicativo de processamento. Crie uma configuração de inicialização usando a AMI. Crie um grupo de Auto Scaling usando a configuração de inicialização. Defina a política de escalabilidade do grupo de Auto Scaling para adicionar e remover nós com base no uso de CPU.

B. Crie uma fila do Amazon SQS para armazenar os trabalhos que precisam ser processados. Crie uma Amazon Machine Image (AMI) que contenha o aplicativo de processamento. Crie uma configuração de inicialização usando a AMI. Crie um grupo de Auto Scaling usando a configuração de inicialização. Defina a política de escalabilidade do grupo de Auto Scaling para adicionar e remover nós com base no uso da rede.

C. Crie uma fila do Amazon SQS para armazenar os trabalhos que precisam ser processados. Crie uma Amazon Machine Image (AMI) que contenha o aplicativo de processamento. Crie um modelo de inicialização usando a AMI. Crie um grupo de Auto Scaling usando o modelo de inicialização. Defina a política de escalabilidade do grupo de Auto Scaling para adicionar e remover nós com base no número de itens na fila do SQS.

D. Crie um tópico do Amazon SNS para enviar os trabalhos que precisam ser processados. Crie uma Amazon Machine Image (AMI) que contenha o aplicativo de processamento. Crie um modelo de inicialização usando a AMI. Crie um grupo de Auto Scaling usando o modelo de inicialização. Defina a política de escalabilidade do grupo de Auto Scaling para adicionar e remover nós com base no número de mensagens publicadas no tópico SNS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie uma fila SQS para armazenar os trabalhos a serem processados. Crie uma Amazon Machine Image (AMI) que consista na aplicação de processamento. Crie um modelo de lançamento que use a AMI. Crie um Auto Scaling group usando o modelo de lançamento. Defina a política de escalabilidade do Auto Scaling para adicionar e remover nós com base no número de itens na fila SQS.

**Justificativa:**  
- **Por que essa opção?**  
  Usar uma fila SQS desacopla os componentes, e a política de escalabilidade baseada no número de itens na fila permite um ajuste dinâmico da capacidade da aplicação.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O SNS não é adequado para filas duráveis como o SQS.  
  - **B:** Usar o tráfego de rede como base para escalabilidade não é eficaz para garantir que os trabalhos sejam processados.  
  - **D:** Usar o SNS e a política de escalabilidade baseada no número de mensagens não é tão eficaz quanto o SQS.  


</details>

---

### Questão 82
Uma empresa hospeda suas aplicações web na AWS Cloud. A empresa configura Elastic Load Balancers para usar certificados importados no AWS Certificate Manager (ACM). A equipe de segurança da empresa deve ser notificada 30 dias antes da expiração de cada certificado.
O que um arquiteto de soluções deve recomendar para atender a esse requisito?

A. Adicionar uma regra no ACM para publicar uma mensagem personalizada em um tópico do Amazon Simple Notification Service (Amazon SNS) todos os dias, começando 30 dias antes da expiração de qualquer certificado.

B. Criar uma regra do AWS Config que verifique certificados que irão expirar em até 30 dias. Configurar o Amazon EventBridge (Amazon CloudWatch Events) para invocar um alerta personalizado por meio do Amazon SNS quando o AWS Config relatar um recurso não conforme.

C. Usar o AWS Trusted Advisor para verificar certificados que irão expirar em até 30 dias. Criar um alarme do Amazon CloudWatch baseado em métricas do Trusted Advisor para mudanças de status. Configurar o alarme para enviar um alerta personalizado por meio do Amazon SNS.

D. Criar uma regra do Amazon EventBridge (Amazon CloudWatch Events) para detectar certificados que irão expirar em até 30 dias. Configurar a regra para invocar uma função AWS Lambda. Configurar a função Lambda para enviar um alerta personalizado por meio do Amazon SNS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Crie uma regra do Amazon EventBridge (Amazon CloudWatch Events) para detectar qualquer certificado que vá expirar dentro de 30 dias. Configure a regra para invocar uma função AWS Lambda. Configure a função Lambda para enviar um alerta personalizado por meio do Amazon Simple Notification Service (Amazon SNS).

**Justificativa:**  
- **Por que essa opção?**  
  Usar o EventBridge com a função Lambda fornece uma maneira escalável e automatizada de monitorar a expiração de certificados e enviar alertas.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O ACM não tem suporte nativo para criar regras personalizadas ou enviar notificações diretamente para o SNS. Isso não é tecnicamente viável. 
  - **B:** Embora o AWS Config possa detectar recursos não conformes, ele não é ideal para monitorar eventos de expiração de certificados no ACM. A configuração seria complexa e menos eficiente. 
  - **C:** O Trusted Advisor não monitora diretamente a expiração de certificados no ACM. Criar um alarme do CloudWatch baseado no Trusted Advisor também não atende ao requisito.


</details>

---

### Questão 83
O site dinâmico de uma empresa está hospedado em servidores locais nos Estados Unidos. A empresa está lançando seu produto na Europa e deseja otimizar os tempos de carregamento do site para os novos usuários europeus. O backend do site deve permanecer nos Estados Unidos. O produto será lançado em alguns dias, e uma solução imediata é necessária.
O que o arquiteto de soluções deve recomendar?

A. Lançar uma instância Amazon EC2 na região us-east-1 e migrar o site para ela.

B. Mover o site para o Amazon S3. Usar replicação entre regiões (Cross-Region Replication).

C. Usar o Amazon CloudFront com uma origem personalizada apontando para os servidores locais.

D. Usar uma política de roteamento geoproximidade do Amazon Route 53 apontando para os servidores locais.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Use o Amazon CloudFront com uma origem personalizada apontando para os servidores locais.

**Justificativa:**  
- **Por que essa opção?**  
  O CloudFront melhora significativamente os tempos de carregamento para usuários globais ao armazenar em cache o conteúdo estático em locais próximos aos usuários.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Mover a aplicação para outra região não é uma solução rápida.  
  - **B:**  O Amazon S3 é ideal para hospedar sites estáticos, mas o site descrito na questão é dinâmico, o que torna o S3 inadequado para este caso. Além disso, configurar replicação entre regiões não seria imediato.
  - **D:** Uma política de geoproximidade apenas direciona os usuários para o endpoint mais próximo, mas os servidores ainda estariam localizados nos EUA, sem redução da latência. Além disso, o Route 53 não oferece caching ou aceleração de conteúdo.  


</details>

---

### Questão 84
Uma empresa deseja reduzir o custo de sua arquitetura web de três camadas existente. Os servidores web, de aplicação e de banco de dados estão sendo executados em instâncias Amazon EC2 para os ambientes de desenvolvimento, teste e produção. As instâncias EC2 apresentam uma utilização média de 30% de CPU durante horários de pico e 10% de CPU durante horários fora de pico.
As instâncias de produção EC2 funcionam 24 horas por dia. As instâncias EC2 de desenvolvimento e teste funcionam pelo menos 8 horas por dia. A empresa planeja implementar automação para desligar as instâncias de desenvolvimento e teste quando não estiverem em uso.
Qual solução de compra de instâncias EC2 atenderá aos requisitos da empresa da maneira mais econômica?

A. Usar Spot Instances para as instâncias de produção EC2. Usar Reserved Instances para as instâncias de desenvolvimento e teste EC2.

B. Usar Reserved Instances para as instâncias de produção EC2. Usar On-Demand Instances para as instâncias de desenvolvimento e teste EC2.

C. Usar Spot blocks para as instâncias de produção EC2. Usar Reserved Instances para as instâncias de desenvolvimento e teste EC2.

D. Usar On-Demand Instances para as instâncias de produção EC2. Usar Spot blocks para as instâncias de desenvolvimento e teste EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Use Reserved Instances para as instâncias EC2 de produção. Use instâncias sob demanda para os ambientes de desenvolvimento e teste.

**Justificativa:**  
- **Por que essa opção?**  
  Reserved Instances oferecem um desconto significativo para instâncias de produção que estão sempre em uso. Instâncias sob demanda são mais flexíveis e adequadas para ambientes de desenvolvimento e teste.  
  As Reserved Instances são adequadas para cargas de trabalho previsíveis e que funcionam 24 horas por dia, como o ambiente de produção.

- **Por que as outras opções não são adequadas?**  
  - **A** As Spot Instances são apropriadas para cargas de trabalho tolerantes a interrupções, mas as instâncias de produção precisam de alta disponibilidade e confiabilidade.
  - **C**  Spot blocks podem ser usados para tarefas de longa duração, mas ainda assim têm uma janela limitada e podem ser encerrados. Isso não atende ao requisito de alta disponibilidade para produção.
  - **D** Usar On-Demand Instances para produção é mais caro do que Reserved Instances, já que a produção funciona 24/7.


</details>

---

### Questão 85
Uma empresa possui um aplicativo web de produção no qual os usuários enviam documentos por meio de uma interface web ou de um aplicativo móvel. De acordo com uma nova exigência regulatória, documentos novos não podem ser modificados ou excluídos após serem armazenados.
O que um arquiteto de soluções deve fazer para atender a esse requisito?

A. Armazenar os documentos enviados em um bucket do Amazon S3 com o S3 Versioning e o S3 Object Lock habilitados.

B. Armazenar os documentos enviados em um bucket do Amazon S3. Configurar uma política de ciclo de vida (S3 Lifecycle) para arquivar os documentos periodicamente.

C. Armazenar os documentos enviados em um bucket do Amazon S3 com o S3 Versioning habilitado. Configurar uma ACL para restringir todo o acesso como somente leitura.

D. Armazenar os documentos enviados em um volume do Amazon Elastic File System (Amazon EFS). Acessar os dados montando o volume no modo somente leitura.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Armazene os documentos carregados em um bucket Amazon S3 com versionamento e S3 Object Lock habilitado.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento do S3 e o Object Lock garantem que os documentos não possam ser modificados ou excluídos após o armazenamento, atendendo às exigências regulatórias.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A política de ciclo de vida do S3 não garante que os documentos não possam ser excluídos ou modificados.  
  - **C:** As ACLs de somente leitura restringem o acesso, mas não impedem a modificação ou exclusão de objetos no bucket. Além disso, o Versioning por si só não garante imutabilidade.
  - **D:** O EFS é um sistema de arquivos, mas não oferece as funcionalidades necessárias para impedir alterações ou exclusões.  


</details>

---

### Questão 86
Uma empresa possui vários servidores web que precisam acessar com frequência uma instância de banco de dados Amazon RDS MySQL Multi-AZ. A empresa deseja um método seguro para que os servidores web se conectem ao banco de dados, atendendo ao requisito de segurança de rotacionar as credenciais de usuário frequentemente.
Qual solução atende a esses requisitos?

A. Armazenar as credenciais do banco de dados no AWS Secrets Manager. Conceder as permissões necessárias do IAM para permitir que os servidores web acessem o AWS Secrets Manager.

B. Armazenar as credenciais do banco de dados no AWS Systems Manager OpsCenter. Conceder as permissões necessárias do IAM para permitir que os servidores web acessem o OpsCenter.

C. Armazenar as credenciais do banco de dados em um bucket seguro do Amazon S3. Conceder as permissões necessárias do IAM para permitir que os servidores web recuperem as credenciais e acessem o banco de dados.

D. Armazenar as credenciais do banco de dados em arquivos criptografados com o AWS Key Management Service (AWS KMS) no sistema de arquivos dos servidores web. Os servidores web devem ser capazes de descriptografar os arquivos e acessar o banco de dados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Armazene as credenciais do banco de dados no AWS Secrets Manager. Conceda as permissões IAM necessárias para permitir que os servidores web acessem o AWS Secrets Manager.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS Secrets Manager permite gerenciar e rotacionar credenciais automaticamente, atendendo aos requisitos de segurança e flexibilidade.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O OpsCenter não é uma solução projetada para gerenciar credenciais. É usado para operações de gerenciamento e análise de incidentes.
  - **C:** Usar um bucket S3 não é uma prática recomendada para armazenar credenciais de banco de dados, pois pode comprometer a segurança.  
  - **D:** Armazenar credenciais criptografadas localmente nas instâncias pode ser inseguro e difícil de gerenciar em escala.  


</details>

---

### Questão 87
Uma empresa hospeda um aplicativo em funções AWS Lambda que são acionadas por uma API do Amazon API Gateway. As funções Lambda salvam dados de clientes em um banco de dados Amazon Aurora MySQL. Sempre que a empresa atualiza o banco de dados, as funções Lambda falham ao estabelecer conexões com o banco até que a atualização seja concluída. Como resultado, os dados dos clientes não são registrados para alguns eventos.
Um arquiteto de soluções precisa projetar uma solução que armazene os dados dos clientes criados durante as atualizações do banco de dados.
Qual solução atenderá a esses requisitos?

A. Provisionar um proxy do Amazon RDS para ficar entre as funções Lambda e o banco de dados. Configurar as funções Lambda para se conectar ao proxy do RDS.

B. Aumentar o tempo de execução das funções Lambda para o máximo. Criar um mecanismo de nova tentativa no código que armazene os dados dos clientes no banco de dados.

C. Persistir os dados dos clientes no armazenamento local da Lambda. Configurar novas funções Lambda para analisar o armazenamento local e salvar os dados dos clientes no banco de dados.

D. Armazenar os dados dos clientes em uma fila FIFO do Amazon Simple Queue Service (Amazon SQS). Criar uma nova função Lambda que consulte a fila e armazene os dados dos clientes no banco de dados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Provisione um proxy Amazon RDS para ficar entre as funções Lambda e o banco de dados. Configure as funções Lambda para se conectarem ao proxy RDS.

**Justificativa:**  
- **Por que essa opção?**  
  * Amazon SQS FIFO: Uma fila FIFO garante que os eventos sejam processados em ordem e sem duplicação. Isso é ideal para registrar dados enquanto o banco de dados está indisponível.
  * Decoupling: Armazenar dados em uma fila desacopla as funções Lambda do banco de dados, permitindo que os eventos sejam processados posteriormente, quando o banco estiver disponível.
  * Alta disponibilidade: O SQS armazena os dados com alta durabilidade, garantindo que nenhuma informação seja perdida durante a atualização do banco de dados.

- **Por que as outras opções não são adequadas?**  
  - **A:** O RDS Proxy melhora a eficiência de conexões e gerenciamento, mas não resolve o problema de indisponibilidade do banco de dados durante as atualizações.
  - **B:** Prolongar o tempo de execução não garante que o banco estará disponível antes do tempo limite.
  - **C:** O armazenamento local em funções Lambda é temporário e não é compartilhado entre invocações. 

</details>

---

### Questão 88
Uma empresa de pesquisa coletou dados por vários anos de áreas nos Estados Unidos. A empresa armazena os dados em um bucket do Amazon S3 com 3 TB de tamanho e em crescimento. A empresa começou a compartilhar os dados com uma empresa de marketing europeia que possui buckets S3. A empresa deseja garantir que os custos de transferência de dados permaneçam o mais baixos possível.
Qual solução atenderá a esses requisitos?

A. Configurar o recurso Requester Pays no bucket S3 da empresa.

B. Configurar a replicação entre regiões (S3 Cross-Region Replication) do bucket S3 da empresa para um dos buckets S3 da empresa de marketing.

C. Configurar acesso entre contas para a empresa de marketing para que ela tenha acesso ao bucket S3 da empresa.

D. Configurar o bucket S3 da empresa para usar S3 Intelligent-Tiering. Sincronizar o bucket S3 com um dos buckets S3 da empresa de marketing.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Configure o recurso Requester Pays no bucket S3 da empresa.

**Justificativa:**  
- **Por que essa opção?**  
  A configuração de Requester Pays permite que os custos de transferência de dados sejam arcados pela empresa de marketing, reduzindo os custos para a empresa.  

- **Por que as outras opções não são adequadas?**  
  - **B:** A replicação cross-region resulta em custos adicionais de armazenamento e transferência.  
  - **C:** O acesso cross-account não resolve diretamente os custos de transferência de dados.  
  - **D:** O uso do S3 Intelligent-Tiering não reduz custos de transferência de dados entre contas e regiões.  


</details>

---

### Questão 89
Uma empresa utiliza o Amazon S3 para armazenar documentos de auditoria confidenciais. O bucket S3 usa políticas de bucket para restringir o acesso aos documentos para os usuários IAM da equipe de auditoria, seguindo o princípio do menor privilégio. Os gerentes da empresa estão preocupados com a exclusão acidental de documentos no bucket S3 e desejam uma solução mais segura.
O que um arquiteto de soluções deve fazer para proteger os documentos de auditoria?

A. Habilitar os recursos de versionamento e MFA Delete no bucket S3.

B. Habilitar a autenticação multifator (MFA) nas credenciais de usuário IAM de cada conta de usuário da equipe de auditoria.

C. Adicionar uma política de ciclo de vida do S3 às contas de usuário IAM da equipe de auditoria para negar a ação s3:DeleteObject durante as datas de auditoria.

D. Usar o AWS Key Management Service (AWS KMS) para criptografar o bucket S3 e restringir as contas de usuário IAM da equipe de auditoria de acessar a chave KMS.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**A.** Habilite as funcionalidades de versionamento e MFA Delete no bucket S3.

**Justificativa:**  
- **Por que essa opção?**  
  O versionamento e o MFA Delete protegem contra a exclusão acidental de objetos no S3, exigindo autenticação multifatorial para exclusão de versões.  

- **Por que as outras opções não são adequadas?**  
  - **B:** O MFA em credenciais IAM não impede a exclusão acidental de documentos.  
  - **C:** A política de Lifecycle não impede exclusões acidentais.  
  - **D:** O KMS não impede a exclusão de objetos no S3.  


</details>

---

### Questão 90
Uma empresa está usando um banco de dados SQL para armazenar dados de filmes que são publicamente acessíveis. O banco de dados é executado em uma instância Amazon RDS Single-AZ. Um script executa consultas em intervalos aleatórios durante o dia para registrar o número de novos filmes adicionados ao banco de dados. O script deve relatar um total final durante o horário comercial.
A equipe de desenvolvimento da empresa percebe que o desempenho do banco de dados é inadequado para tarefas de desenvolvimento enquanto o script está em execução. Um arquiteto de soluções deve recomendar uma solução para resolver esse problema.
Qual solução atenderá a esse requisito com o MENOR esforço operacional?

A. Modificar a instância do banco de dados para ser uma implantação Multi-AZ.

B. Criar uma réplica de leitura do banco de dados. Configurar o script para consultar apenas a réplica de leitura.

C. Instruir a equipe de desenvolvimento a exportar manualmente as entradas no banco de dados no final de cada dia.

D. Usar o Amazon ElastiCache para armazenar em cache as consultas comuns que o script executa no banco de dados.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Crie uma réplica de leitura do banco de dados. Configure o script para consultar apenas a réplica de leitura.

**Justificativa:**  
- **Por que essa opção?**  
  A réplica de leitura permite que o script faça consultas sem afetar a performance do banco de dados principal.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Modificar para Multi-AZ não resolve o problema de sobrecarga de leitura.  
  - **C:** Exportar manualmente é uma solução menos eficiente e mais trabalhosa.  
  - **D:** O ElastiCache não é necessário para consultas simples e frequentes em um banco de dados SQL.  


</details>

---

### Questão 91
Uma empresa possui aplicações que executam em instâncias Amazon EC2 em uma VPC. Uma dessas aplicações precisa chamar a API do Amazon S3 para armazenar e ler objetos. De acordo com os regulamentos de segurança da empresa, nenhum tráfego das aplicações pode viajar pela internet.
Qual solução atenderá a esses requisitos?

A. Configurar um endpoint de gateway do S3.

B. Criar um bucket S3 em uma sub-rede privada.

C. Criar um bucket S3 na mesma região da AWS que as instâncias EC2.

D. Configurar um NAT gateway na mesma sub-rede que as instâncias EC2.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
* **A.*** Configurar um endpoint de gateway do S3.

**Justificativa:**  
- **Por que essa opção?**  
  Um endpoint VPC Gateway para o S3 permite que o tráfego entre as instâncias EC2 e o S3 ocorra dentro da VPC, sem necessidade de tráfego pela internet, atendendo às exigências de segurança.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar um internet gateway permitiria tráfego pela internet, o que viola as regulamentações de segurança.  
  - **C:** Usar um NAT Gateway também envolve tráfego pela internet, o que não é permitido.  
  - **D:** Um VPC Peering não resolveria o problema de acessar o S3 de forma segura dentro da mesma VPC.  


</details>

---

### Questão 92
Uma empresa está armazenando informações sensíveis de usuários em um bucket Amazon S3. A empresa deseja fornecer acesso seguro a esse bucket a partir do nível de aplicação que está sendo executado em instâncias Amazon EC2 dentro de uma VPC.
Quais combinações de etapas um arquiteto de soluções deve adotar para alcançar esse objetivo? (Escolha duas.)

A. Configurar um endpoint de gateway da VPC para o Amazon S3 dentro da VPC.

B. Criar uma política de bucket para tornar os objetos no bucket S3 públicos.

C. Criar uma política de bucket que limite o acesso apenas ao nível de aplicação executado na VPC.

D. Criar um usuário IAM com uma política de acesso ao S3 e copiar as credenciais IAM para a instância EC2.

E. Criar uma instância NAT e configurar as instâncias EC2 para usarem a instância NAT para acessar o bucket S3.

<details>

<summary>Resposta</summary>

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


</details>

---

### Questão 93
Uma empresa executa uma aplicação on-premises alimentada por um banco de dados MySQL. A empresa está migrando a aplicação para a AWS para aumentar a elasticidade e a disponibilidade.
A arquitetura atual apresenta alta atividade de leitura no banco de dados durante períodos normais de operação. A cada 4 horas, a equipe de desenvolvimento realiza uma exportação completa do banco de dados de produção para preencher um banco de dados no ambiente de staging. Durante esse período, os usuários experimentam latência inaceitável na aplicação. A equipe de desenvolvimento também não consegue usar o ambiente de staging até que o procedimento seja concluído.
Um arquiteto de soluções deve recomendar uma arquitetura substituta que resolva o problema de latência da aplicação. A nova arquitetura também deve permitir que a equipe de desenvolvimento continue usando o ambiente de staging sem atrasos.
Qual solução atende a esses requisitos?

A. Use o Amazon Aurora MySQL com réplicas Multi-AZ Aurora para produção. Preencha o banco de dados de staging implementando um processo de backup e restauração que use o utilitário mysqldump.

B. Use o Amazon Aurora MySQL com réplicas Multi-AZ Aurora para produção. Use clonagem de banco de dados para criar o banco de dados de staging sob demanda.

C. Use o Amazon RDS para MySQL com uma implantação Multi-AZ e réplicas de leitura para produção. Use a instância standby como o banco de dados de staging.

D. Use o Amazon RDS para MySQL com uma implantação Multi-AZ e réplicas de leitura para produção. Preencha o banco de dados de staging implementando um processo de backup e restauração que use o utilitário mysqldump.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
  **B.** Use o Amazon Aurora MySQL com réplicas Multi-AZ Aurora para produção. Use clonagem de banco de dados para criar o banco de dados de staging sob demanda.

**Justificativa:**  
- **Por que essa opção?**  
  A Aurora MySQL com réplicas Multi-AZ proporciona alta disponibilidade e pode ser escalada para lidar com tráfego de leitura. A clonagem de banco de dados permite que o banco de dados de teste seja criado rapidamente, sem afetar o banco de dados de produção.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o mysqldump para backup e restauração pode causar latência devido à interrupção de produção durante o processo.  
  - **C:** Usar instâncias standby para o ambiente de teste pode resultar em um processo de configuração mais complexo e menos eficiente.  
  - **D:** A replicação com mysqldump não resolve o problema de latência de maneira eficiente.  


</details>

---

### Questão 94
Uma empresa está projetando uma aplicação onde os usuários enviam pequenos arquivos para o Amazon S3. Após o upload, cada arquivo precisa de um processamento simples único para transformar os dados e salvá-los no formato JSON para análises futuras.
Cada arquivo deve ser processado o mais rápido possível após o upload. A demanda será variável. Em alguns dias, os usuários enviarão um grande número de arquivos; em outros dias, poucos ou nenhum arquivo será enviado.
Qual solução atende a esses requisitos com o MENOR esforço operacional?

A. Configure o Amazon EMR para ler arquivos de texto do Amazon S3. Execute scripts de processamento para transformar os dados. Armazene o arquivo JSON resultante em um cluster Amazon Aurora.

B. Configure o Amazon S3 para enviar uma notificação de evento para uma fila do Amazon Simple Queue Service (Amazon SQS). Use instâncias Amazon EC2 para ler da fila e processar os dados. Armazene o arquivo JSON resultante no Amazon DynamoDB.

C. Configure o Amazon S3 para enviar uma notificação de evento para uma fila do Amazon Simple Queue Service (Amazon SQS). Use uma função AWS Lambda para ler da fila e processar os dados. Armazene o arquivo JSON resultante no Amazon DynamoDB.

D. Configure o Amazon EventBridge (Amazon CloudWatch Events) para enviar um evento para o Amazon Kinesis Data Streams quando um novo arquivo for carregado. Use uma função AWS Lambda para consumir o evento do stream e processar os dados. Armazene o arquivo JSON resultante em um cluster Amazon Aurora.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Configure o Amazon S3 para enviar uma notificação de evento para uma fila Amazon Simple Queue Service (Amazon SQS). Use uma função AWS Lambda para ler da fila e processar os dados. Armazene o arquivo JSON resultante no Amazon DynamoDB.

**Justificativa:**  
- **Por que essa opção?**  
  Usar o SQS com Lambda permite o processamento assíncrono dos arquivos sem sobrecarga adicional, e o DynamoDB fornece armazenamento de dados escalável.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon EMR introduz complexidade operacional desnecessária para um processamento simples de arquivos.  
  - **B:** Usar EC2 não é escalável nem ideal para processar arquivos individualmente com alta variabilidade de demanda.  
  - **D:** O Kinesis Data Streams não é necessário para esse tipo de processamento, e a Lambda com SQS é uma solução mais simples.


</details>

---

### Questão 95
Uma aplicação permite que usuários na sede de uma empresa acessem dados de produtos. Os dados de produtos são armazenados em uma instância de banco de dados Amazon RDS MySQL. A equipe de operações identificou uma lentidão de desempenho na aplicação e deseja separar o tráfego de leitura do tráfego de gravação. Um arquiteto de soluções precisa otimizar rapidamente o desempenho da aplicação.
O que o arquiteto de soluções deve recomendar?

A. Alterar o banco de dados existente para uma implantação Multi-AZ. Atender às solicitações de leitura a partir da zona de disponibilidade primária.

B. Alterar o banco de dados existente para uma implantação Multi-AZ. Atender às solicitações de leitura a partir da zona de disponibilidade secundária.

C. Criar réplicas de leitura para o banco de dados. Configurar as réplicas de leitura com metade dos recursos de computação e armazenamento do banco de dados de origem.

D. Criar réplicas de leitura para o banco de dados. Configurar as réplicas de leitura com os mesmos recursos de computação e armazenamento do banco de dados de origem.

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Crie réplicas de leitura para o banco de dados. Configure as réplicas de leitura com os mesmos recursos de computação e armazenamento da instância de origem.

**Justificativa:**  
- **Por que essa opção?**  
  Criar réplicas de leitura distribui o tráfego de leitura e melhora o desempenho sem afetar o tráfego de escrita.  

- **Por que as outras opções não são adequadas?**  
  - **A** O Multi-AZ melhora a disponibilidade, mas não é projetado para separar tráfego de leitura e gravação. A zona primária já está sobrecarregada, e essa abordagem não melhora o desempenho.
  - **B** Em uma implantação Multi-AZ, a instância secundária é apenas para failover e não pode ser usada para leituras ativas.
  - **C:** Configurar réplicas de leitura com menos recursos pode criar gargalos durante períodos de alta demanda, resultando em um desempenho insatisfatório.


</details>

---

### Questão 96
Um administrador do Amazon EC2 criou a seguinte política associada a um grupo IAM contendo vários usuários:  
Qual é o efeito dessa política?

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Os usuários podem terminar uma instância EC2 na região us-east-1 quando o IP de origem do usuário for 10.100.100.254.

**Justificativa:**  
- **Por que essa opção?**  
  A política específica permite que instâncias EC2 sejam terminadas, mas com a restrição de que o IP de origem seja 10.100.100.254 na região us-east-1.  

- **Por que as outras opções não são adequadas?**  
  - **A:** A política não permite que instâncias sejam terminadas em regiões diferentes de us-east-1.  
  - **B:** A política não permite a terminação de instâncias com o IP 10.100.100.1.  
  - **D:** A política não bloqueia a terminação de instâncias com o IP 10.100.100.254.


</details>

---

### Questão 97
Uma empresa tem uma grande implantação do Microsoft SharePoint em servidores locais, que requer armazenamento compartilhado de arquivos Windows. A empresa deseja migrar essa carga de trabalho para a AWS e está considerando várias opções de armazenamento. A solução de armazenamento deve ser altamente disponível e integrada ao Active Directory para controle de acesso.  
Qual solução atenderá a esses requisitos?

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Crie um sistema de arquivos Amazon FSx for Windows File Server na AWS e defina o domínio Active Directory para autenticação.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon FSx for Windows File Server é totalmente gerenciado, altamente disponível e integrado com o Active Directory, atendendo aos requisitos de armazenamento e controle de acesso.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O Amazon EFS não oferece suporte para compartilhamento de arquivos do Windows.  
  - **B:** O Storage Gateway não é ideal para integrar com Active Directory.  
  - **C:** O S3 não oferece suporte nativo para arquivos compartilhados com o Windows.


</details>

---

### Questão 98
Uma empresa de processamento de imagens tem uma aplicação web que os usuários utilizam para carregar imagens. A aplicação carrega as imagens em um bucket Amazon S3. A empresa configurou notificações de eventos S3 para publicar os eventos de criação de objetos em uma fila padrão do Amazon SQS. A fila SQS serve como fonte de eventos para uma função AWS Lambda que processa as imagens e envia os resultados aos usuários por email.  
Os usuários relatam que estão recebendo várias mensagens de email para cada imagem carregada. Um arquiteto de soluções determina que as mensagens SQS estão invocando a função Lambda mais de uma vez, resultando em mensagens duplicadas.  
O que o arquiteto de soluções deve fazer para resolver esse problema com o MENOR overhead operacional?

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**B.** Mude a fila SQS padrão para uma fila SQS FIFO. Use o ID de deduplicação da mensagem para descartar mensagens duplicadas.

**Justificativa:**  
- **Por que essa opção?**  
  As filas FIFO do SQS permitem a deduplicação automática de mensagens com base no ID, resolvendo o problema de múltiplas invocações da função Lambda.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Long polling ajuda na eficiência, mas não resolve a duplicação de mensagens.  
  - **C:** Aumentar o timeout de visibilidade não resolve a duplicação.  
  - **D:** A exclusão imediata das mensagens não elimina a duplicação e pode afetar o processamento de falhas.


Posso continuar com mais questões ou fornecer mais detalhes?
</details>

---

### Questão 99
Uma empresa está implementando uma solução de armazenamento compartilhado para uma aplicação de jogos que está hospedada em um data center local. A empresa precisa da capacidade de usar clientes Lustre para acessar dados. A solução deve ser totalmente gerenciada.  
Qual solução atende a esses requisitos?

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**D.** Crie um sistema de arquivos Amazon FSx for Lustre. Anexe o sistema de arquivos ao servidor de origem. Conecte o servidor de aplicação ao sistema de arquivos.

**Justificativa:**  
- **Por que essa opção?**  
  O Amazon FSx for Lustre é totalmente gerenciado e oferece suporte nativo para Lustre, tornando a solução ideal para esse tipo de carga de trabalho de jogos.  

- **Por que as outras opções não são adequadas?**  
  - **A:** O AWS Storage Gateway não oferece suporte a clientes Lustre.  
  - **B:** Usar uma instância EC2 não seria totalmente gerenciado e introduziria complexidade adicional.  
  - **C:** O Amazon EFS não suporta o Lustre como um protocolo de acesso.  


</details>

---

### Questão 100
A aplicação conteinerizada de uma empresa está sendo executada em uma instância Amazon EC2. A aplicação precisa baixar certificados de segurança antes que possa se comunicar com outros aplicativos de negócios. A empresa deseja uma solução altamente segura para criptografar e descriptografar os certificados em tempo real. A solução também precisa armazenar dados em armazenamento altamente disponível após a criptografia.  
Qual solução atenderá a esses requisitos com o MENOR overhead operacional?

<details>

<summary>Resposta</summary>

**Resposta correta:**  
**C.** Crie uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). Permita que a função EC2 use a chave KMS para operações de criptografia. Armazene os dados criptografados no Amazon S3.

**Justificativa:**  
- **Por que essa opção?**  
  O AWS KMS oferece uma solução segura e gerenciada para criptografar e descriptografar dados em tempo real. O S3 fornece armazenamento altamente disponível.  

- **Por que as outras opções não são adequadas?**  
  - **A:** Usar o AWS Secrets Manager manualmente para atualizar os certificados não é tão eficiente quanto usar o KMS.  
  - **B:** A Lambda não é necessária para criptografar e descriptografar dados em tempo real em um caso simples como este.  
  - **D:** Usar o Amazon EBS para armazenar os dados criptografados não oferece o mesmo nível de disponibilidade e simplicidade que o S3.  

</details>

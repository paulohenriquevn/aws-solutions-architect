# Pergunta 
**Uma empresa precisa executar um aplicativo crítico na AWS. A empresa precisa usar Amazon EC2 para o banco de dados do aplicativo. O banco de dados deve ser altamente disponível e deve failover automaticamente se ocorrer um evento disruptivo. Qual solução atenderá a esses requisitos?**

- Inicie duas instâncias EC2, cada uma em uma zona de disponibilidade diferente na mesma região AWS. Instale o banco de dados em ambas as instâncias EC2. Configure as instâncias EC2 como um cluster. Configure a replicação do banco de dados.


# Pergunta 
**Uma empresa executa um aplicativo web global em instâncias Amazon EC2 por trás de um Application Load Balancer. O aplicativo armazena dados no Amazon Aurora. A empresa precisa criar uma solução de recuperação de desastres e pode tolerar até 30 minutos de inatividade e possível perda de dados. A solução não precisa lidar com a carga quando a infraestrutura principal está saudável. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

- Implante o aplicativo com os elementos de infraestrutura necessários no lugar. Use Amazon Route 53 para configurar failover ativo-passivo. Crie uma réplica Aurora em uma segunda região AWS.


# Pergunta
**Uma empresa recentemente migrou seu aplicativo web para a AWS realocando o aplicativo em instâncias Amazon EC2 em uma única região AWS. A empresa deseja redesenhar a arquitetura do aplicativo para ser altamente disponível e tolerante a falhas. O tráfego deve alcançar todas as instâncias EC2 em execução aleatoriamente. Qual combinação de etapas a empresa deve tomar para atender a esses requisitos? (Escolha duas.)**

 - Crie uma política de roteamento de resposta múltipla no Amazon Route 53.

 - Inicie quatro instâncias EC2: duas instâncias em uma zona de disponibilidade e duas instâncias em outra zona de disponibilidade. 

 # Pergunta
 **Uma empresa oferece um serviço de entrega de alimentos que está crescendo rapidamente. Devido ao crescimento, o sistema de processamento de pedidos da empresa está enfrentando problemas de escalabilidade durante as horas de pico de tráfego. A arquitetura atual inclui o seguinte: • Um grupo de instâncias Amazon EC2 que são executadas em um grupo de Auto Scaling do Amazon EC2 para coletar pedidos do aplicativo • Outro grupo de instâncias EC2 que são executadas em um grupo de Auto Scaling do Amazon EC2 para atender os pedidos. O processo de coleta de pedidos ocorre rapidamente, mas o processo de atendimento dos pedidos pode demorar mais. Os dados não devem ser perdidos devido a um evento de escalabilidade. Um arquiteto de soluções deve garantir que o processo de coleta de pedidos e o processo de atendimento de pedidos possam escalar adequadamente durante as horas de pico de tráfego. A solução deve otimizar a utilização dos recursos da AWS da empresa. Qual solução atende a esses requisitos?**

- Provisione duas filas Amazon Simple Queue Service (Amazon SQS): uma para coleta de pedidos e outra para atendimento de pedidos. Configure as instâncias EC2 para fazer polling de suas respectivas filas. Crie uma métrica com base em um cálculo de backlog por instância. Escale os grupos de Auto Scaling com base nessa métrica.

# Pergunta
**Uma empresa hospeda seu aplicativo na AWS. A empresa usa o Amazon Cognito para gerenciar usuários. Quando os usuários fazem login no aplicativo, o aplicativo busca os dados necessários do Amazon DynamoDB usando uma API REST hospedada no Amazon API Gateway. A empresa deseja uma solução gerenciada pela AWS que controle o acesso à API REST para reduzir os esforços de desenvolvimento. Qual solução atenderá a esses requisitos com a menor sobrecarga operacional?**

- Configure um autorizador de pool de usuários Amazon Cognito no API Gateway para permitir que o Amazon Cognito valide cada solicitação.

# Pergunta
**Uma empresa tem uma conta AWS usada para engenharia de software. A conta AWS tem acesso ao data center on-premises da empresa através de um par de conexões AWS Direct Connect. Todo o tráfego não-VPC é roteado para o gateway privado virtual. Uma equipe de desenvolvimento criou recentemente uma função AWS Lambda através do console. A equipe de desenvolvimento precisa permitir que a função acesse um banco de dados que roda em uma subnet privada no data center da empresa. Qual solução atenderá a esses requisitos**

- Configure a função Lambda para ser executada na VPC com o grupo de segurança apropriado.

# Pergunta
**Uma empresa deseja gerenciar Imagens de Máquinas da Amazon (AMIs). Atualmente, a empresa copia AMIs para a mesma Região AWS onde as AMIs foram criadas. A empresa precisa projetar um aplicativo que capture chamadas de API da AWS e envie alertas sempre que a operação CreateImage da Amazon EC2 for chamada dentro da conta da empresa. Qual solução atenderá a esses requisitos com a menor sobrecarga operacional?**

- Crie uma regra Amazon EventBridge (Amazon CloudWatch Events) para a chamada API CreateImage. Configure o alvo como um tópico Amazon Simple Notification Service (Amazon SNS) para enviar um alerta quando uma chamada API CreateImage for detectada.

# Pergunta
**Uma empresa contratou um fornecedor externo para realizar trabalhos na conta AWS da empresa. O fornecedor usa uma ferramenta automatizada que está hospedada em uma conta AWS que o fornecedor possui. O fornecedor não tem acesso IAM à conta AWS da empresa. Como um arquiteto de soluções deve conceder esse acesso ao fornecedor?**

- Crie uma função IAM na conta da empresa para delegar acesso à função IAM do fornecedor. Anexe as políticas IAM apropriadas à função para as permissões que o fornecedor requer.

# Pergunta
**Um servidor web de uma empresa está sendo executado em uma instância Amazon EC2 em uma subnet pública com um endereço IP elástico. O grupo de segurança padrão está atribuído à instância EC2. O ACL de rede padrão foi modificado para bloquear todo o tráfego. Um arquiteto de soluções precisa tornar o servidor web acessível de qualquer lugar na porta 443. Qual combinação de etapas realizará essa tarefa? (Escolha duas.)**

- Crie um grupo de segurança com uma regra para permitir TCP na porta 443 da origem 0.0.0.0/0.

- Atualize o ACL de rede para permitir a entrada na porta TCP 443 da origem 0.0.0.0/0 e saída na porta TCP 32768-65535 para o destino 0.0.0.0/0.

# Pergunta
**Uma empresa precisa armazenar documentos de contrato. Um contrato dura 5 anos. Durante o período de 5 anos, a empresa deve garantir que os documentos não possam ser sobrescritos ou excluídos. A empresa precisa criptografar os documentos em repouso e girar as chaves de criptografia automaticamente a cada ano. Qual combinação de etapas um arquiteto de soluções deve tomar para atender a esses requisitos com a menor sobrecarga operacional? (Escolha duas.)**

- Use criptografia do lado do servidor com chaves gerenciadas pelo AWS Key Management Service (AWS KMS). Configure a rotação de chaves.
- Armazene os documentos no Amazon S3. Use S3 Object Lock no modo de conformidade.

# Pergunta
**Uma empresa coleta dados de milhares de dispositivos remotos usando um aplicativo de serviços web RESTful que é executado em uma instância Amazon EC2. A instância EC2 recebe os dados brutos, transforma os dados brutos e armazena todos os dados em um bucket Amazon S3. O número de dispositivos remotos aumentará para milhões em breve. A empresa precisa de uma solução altamente escalável que minimize a sobrecarga operacional. Qual combinação de etapas um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Use o Amazon API Gateway para enviar os dados brutos para um stream de dados Amazon Kinesis. Configure o Amazon Kinesis Data Firehose para usar o stream de dados como uma fonte para entregar os dados ao Amazon S3.
- Use AWS Glue para processar os dados brutos no Amazon S3.

# Pergunta
**Uma empresa implantou um aplicativo Java Spring Boot como um pod que é executado no Amazon Elastic Kubernetes Service (Amazon EKS) em subnets privadas. O aplicativo precisa gravar dados em uma tabela Amazon DynamoDB. Um arquiteto de soluções deve garantir que o aplicativo possa interagir com a tabela DynamoDB sem expor o tráfego à internet. Qual combinação de etapas o arquiteto de soluções deve tomar para realizar essa tarefa? (Escolha duas.)**

- Anexe uma função IAM que tenha privilégios suficientes ao pod EKS.
- Crie um endpoint VPC para o DynamoDB.

# Pergunta
**Uma empresa quer experimentar contas AWS individuais para sua equipe de engenharia. A empresa quer ser notificada assim que o uso de instâncias Amazon EC2 em um determinado mês exceder um limite específico para cada conta. O que um arquiteto de soluções deve fazer para atender a esse requisito da maneira mais econômica?**

- Use AWS Budgets para criar um orçamento de custo para cada conta. Defina o período como mensal. Defina o escopo para instâncias EC2. Defina um limite de alerta para o orçamento. Configure um tópico Amazon Simple Notification Service (Amazon SNS) para receber uma notificação quando um limite for excedido.

# Pergunta
**Uma empresa possui um aplicativo de três camadas para compartilhamento de imagens. O aplicativo usa uma instância Amazon EC2 para a camada front-end, outra instância EC2 para a camada de aplicativo e uma terceira instância EC2 para um banco de dados MySQL. Um arquiteto de soluções deve projetar uma solução escalável e altamente disponível que exija a menor quantidade de alterações no aplicativo. Qual solução atende a esses requisitos?**

- Use ambientes AWS Elastic Beanstalk Multi-AZ balanceados por carga para a camada front-end e a camada de aplicativo. Mova o banco de dados para uma instância DB Amazon RDS Multi-AZ. Use Amazon S3 para armazenar e servir as imagens dos usuários.

# Pergunta
**Um hospital quer criar cópias digitais de sua grande coleção de registros escritos históricos. O hospital continuará a adicionar centenas de novos documentos todos os dias. A equipe de dados do hospital escaneará os documentos e fará o upload dos documentos para a nuvem AWS. Um arquiteto de soluções deve implementar uma solução para analisar os documentos, extrair as informações médicas e armazenar os documentos para que um aplicativo possa executar consultas SQL nos dados. A solução deve maximizar a escalabilidade e a eficiência operacional. Qual combinação de etapas o arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Escreva as informações do documento em um bucket Amazon S3. Use Amazon Athena para consultar os dados.
- Crie uma função AWS Lambda que seja executada quando novos documentos forem carregados. Use o Amazon Textract para converter os documentos em texto bruto. Use o Amazon Comprehend Medical para detectar e extrair informações médicas relevantes do texto.

# Pergunta
**Uma empresa precisa reter seus logs do AWS CloudTrail por 3 anos. A empresa está aplicando o CloudTrail em um conjunto de contas da AWS usando o AWS Organizations a partir da conta principal. O bucket de destino do CloudTrail no S3 está configurado com Versionamento S3 habilitado. Uma política de ciclo de vida do S3 está em vigor para excluir objetos atuais após 3 anos. Após o quarto ano de uso do bucket S3, as métricas do bucket S3 mostram que o número de objetos continuou a aumentar. No entanto, o número de novos logs do CloudTrail que são entregues ao bucket S3 permaneceu consistente. Qual solução excluirá objetos que tenham mais de 3 anos da maneira mais econômica?**

- Configure a política de ciclo de vida do S3 para excluir versões anteriores, bem como versões atuais.

# Pergunta
**Uma empresa quer migrar seu banco de dados MySQL de on-premises para a AWS. Recentemente, a empresa sofreu uma interrupção do banco de dados que impactou significativamente os negócios. Para garantir que isso não aconteça novamente, a empresa quer uma solução de banco de dados confiável na AWS que minimize a perda de dados e armazene cada transação em pelo menos dois nós. Qual solução atende a esses requisitos?**

- Crie uma instância Amazon RDS MySQL com funcionalidade Multi-AZ habilitada para replicar os dados de forma síncrona.

# Pergunta
**Uma empresa está desenvolvendo um aplicativo de comércio eletrônico que consistirá de um front end balanceado por carga, um aplicativo baseado em contêiner e um banco de dados relacional. Um arquiteto de soluções precisa criar uma solução altamente disponível que opere com o mínimo de intervenção manual possível. Quais soluções atendem a esses requisitos? (Escolha duas.)**

- Crie uma instância Amazon RDS DB no modo Multi-AZ.
- Crie uma instância Amazon RDS DB no modo Multi-AZ.

# Pergunta
**Uma empresa está preocupada que duas instâncias NAT em uso não serão mais capazes de suportar o tráfego necessário para o aplicativo da empresa. Um arquiteto de soluções deseja implementar uma solução que seja altamente disponível, tolerante a falhas e escalável automaticamente. O que o arquiteto de soluções deve recomendar?**

- Remova as duas instâncias NAT e substitua-as por dois gateways NAT em diferentes zonas de disponibilidade.

# Pergunta
**Uma empresa executa ambientes de demonstração para seus clientes em instâncias Amazon EC2. Cada ambiente é isolado em sua própria VPC. A equipe de operações da empresa precisa ser notificada quando o acesso RDP ou SSH a um ambiente for estabelecido.**

- Publique logs de fluxo VPC no Amazon CloudWatch Logs. Crie os filtros de métricas necessários. Crie um alarme de métrica do Amazon CloudWatch com uma ação de notificação para quando o alarme estiver no estado ALARM.

# Pergunta
**Uma empresa está migrando seu banco de dados Oracle on-premises para Amazon Aurora PostgreSQL. O banco de dados possui vários aplicativos que gravam nas mesmas tabelas. Os aplicativos precisam ser migrados um a um com um mês de intervalo entre cada migração. A gestão expressou preocupações de que o banco de dados possui um alto número de leituras e gravações. Os dados devem ser mantidos em sincronia entre ambos os bancos de dados durante a migração. O que um arquiteto de soluções deve recomendar?**

- Use a AWS Schema Conversion Tool com AWS Database Migration Service (AWS DMS) usando uma instância de replicação otimizada para memória. Crie uma tarefa de replicação de carga completa mais captura de dados de alteração (CDC) e um mapeamento de tabela para selecionar todas as tabelas.

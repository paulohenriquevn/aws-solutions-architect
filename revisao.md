**Uma empresa sofreu uma violação que afetou vários aplicativos em seu data center local. O invasor aproveitou vulnerabilidades nos aplicativos personalizados que estavam rodando nos servidores. A empresa está agora migrando seus aplicativos para serem executados em instâncias do Amazon EC2. A empresa deseja implementar uma solução que ativamente escaneie vulnerabilidades nas instâncias EC2 e envie um relatório detalhando as descobertas. Qual solução atenderá a esses requisitos?**

- Implantar o AWS Shield para escanear as instâncias EC2 em busca de vulnerabilidades. Criar uma função AWS Lambda para registrar qualquer achado no AWS CloudTrail.


O AWS Global Accelerator é um serviço da Amazon Web Services (AWS) que melhora o desempenho de aplicações para usuários locais e globais

**Uma empresa recentemente migrou todo o seu ambiente de TI para a Nuvem AWS. A empresa descobre que os usuários estão provisionando instâncias Amazon EC2 superdimensionadas e modificando regras de grupos de segurança sem usar o processo de controle de mudanças adequado. Um arquiteto de soluções deve elaborar uma estratégia para rastrear e auditar essas mudanças de inventário e configuração. Quais ações o arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Habilitar o AWS CloudTrail e usá-lo para auditoria.
- Ative o AWS Config e crie regras para fins de auditoria e conformidade.

**Uma empresa armazena dados confidenciais em um banco de dados Amazon Aurora PostgreSQL na região ap-southeast-3. O banco de dados está criptografado com uma chave gerenciada pelo cliente no AWS Key Management Service (AWS KMS). A empresa foi recentemente adquirida e deve compartilhar com segurança um backup do banco de dados com a conta AWS da empresa adquirente na região ap-southeast-3. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

-  Crie um snapshot do banco de dados. Adicione a conta AWS da empresa adquirente à política da chave KMS. Compartilhe o snapshot com a conta AWS da empresa adquirente.

**Uma empresa está hospedando um aplicativo web a partir de um bucket do Amazon S3. O aplicativo usa o Amazon Cognito como um provedor de identidade para autenticar os usuários e retornar um JSON Web Token (JWT) que fornece acesso a recursos protegidos armazenados em outro bucket do S3. Após a implantação do aplicativo, os usuários relatam erros e não conseguem acessar o conteúdo protegido. Um arquiteto de soluções deve resolver esse problema fornecendo permissões adequadas para que os usuários possam acessar o conteúdo protegido. Qual solução atende a esses requisitos?**

- Atualize o pool do Amazon Cognito para usar mapeamentos de atributos personalizados dentro do pool de identidades e conceda aos usuários as permissões adequadas para acessar o conteúdo protegido.


**Uma empresa deseja criar um aplicativo móvel que permita aos usuários transmitir vídeos em câmera lenta em seus dispositivos móveis. Atualmente, o aplicativo captura clipes de vídeo e os carrega no formato bruto para um bucket do Amazon S3. O aplicativo recupera esses clipes de vídeo diretamente do bucket do S3. No entanto, os vídeos são grandes em seu formato bruto. Os usuários estão enfrentando problemas de buffering e reprodução em dispositivos móveis. A empresa deseja implementar soluções para maximizar o desempenho e a escalabilidade do aplicativo, minimizando a sobrecarga operacional. Qual combinação de soluções atenderá a esses requisitos? (Escolha duas.)**

- Use o Amazon Elastic Transcoder para converter os arquivos de vídeo em formatos mais apropriados.

**Uma empresa possui várias contas AWS que usam faturamento consolidado. A empresa executa várias instâncias de banco de dados Amazon RDS for Oracle On-Demand de alto desempenho ativamente por 90 dias. A equipe financeira da empresa tem acesso ao AWS Trusted Advisor na conta de faturamento consolidado e em todas as outras contas AWS. A equipe financeira precisa usar a conta AWS apropriada para acessar as recomendações do Trusted Advisor para RDS. A equipe financeira deve revisar a verificação do Trusted Advisor apropriada para reduzir os custos do RDS. Qual combinação de etapas a equipe financeira deve seguir para atender a esses requisitos? (Escolha duas.)**

 - Use as recomendações do Trusted Advisor da conta de faturamento consolidado para ver todas as verificações de instâncias RDS ao mesmo tempo.

  - Revise a verificação do Trusted Advisor para instâncias de banco de dados ociosas do Amazon RDS.

**Uma empresa coleta dados de um grande número de participantes que usam dispositivos vestíveis. A empresa armazena os dados em uma tabela Amazon DynamoDB e usa aplicativos para analisar os dados. A carga de trabalho dos dados é constante e previsível. A empresa quer manter-se dentro ou abaixo do seu orçamento previsto para o DynamoDB. Qual solução atenderá a esses requisitos da maneira mais econômica?**

- Use o modo provisionado. Especifique as unidades de capacidade de leitura (RCUs) e as unidades de capacidade de gravação (WCUs).

**Uma empresa tem um aplicativo que é executado em várias instâncias Amazon EC2. Cada instância EC2 possui vários volumes de dados Amazon Elastic Block Store (Amazon EBS) anexados a ela. A configuração da instância EC2 e os dados do aplicativo precisam ser copiados diariamente. O aplicativo também precisa ser recuperável em uma Região AWS diferente. Qual solução atenderá a esses requisitos da maneira mais eficiente operacionalmente?**

- Crie um plano de backup usando o AWS Backup para realizar backups noturnos. Copie os backups para outra Região. Adicione as instâncias EC2 do aplicativo como recursos.

**Uma empresa deve migrar 20 TB de dados de um data center para a Nuvem AWS em 30 dias. A largura de banda da rede da empresa é limitada a 15 Mbps e não pode exceder 70% de utilização. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

- Usar o AWS Snowball.

**Um laboratório de pesquisa precisa processar aproximadamente 8 TB de dados. O laboratório requer latências de sub-milisegundo e uma taxa de transferência mínima de 6 GBps para o subsistema de armazenamento. Centenas de instâncias Amazon EC2 que executam Amazon Linux distribuirão e processarão os dados. Qual solução atenderá aos requisitos de desempenho?**

- Criar um bucket Amazon S3 para armazenar os dados brutos. Criar um sistema de arquivos Amazon FSx for Lustre que usa armazenamento SSD persistente. Selecionar a opção para importar dados de e exportar dados para o Amazon S3. Montar o sistema de arquivos nas instâncias EC2.


**Uma empresa de mídia usa o Amazon CloudFront para seu conteúdo de vídeo de streaming disponível publicamente. A empresa deseja proteger o conteúdo de vídeo hospedado no Amazon S3 controlando quem tem acesso. Alguns dos usuários da empresa estão usando um cliente HTTP personalizado que não suporta cookies. Alguns dos usuários da empresa não podem alterar as URLs hardcoded que estão usando para acessar. Quais serviços ou métodos atenderão a esses requisitos com o menor impacto para os usuários? (Escolha dois.)**

- URLs assinados
- Cookies assinados


**Uma empresa está construindo uma solução que irá relatar eventos do Amazon EC2 Auto Scaling em todos os aplicativos em uma conta AWS. A empresa precisa usar uma solução serverless para armazenar os dados de status do Auto Scaling do EC2 no Amazon S3. A empresa então usará os dados no S3 para fornecer atualizações quase em tempo real em um painel de controle. A solução não deve afetar a velocidade dos lançamentos de instâncias EC2. Como a empresa deve mover os dados para o Amazon S3 para atender a esses requisitos?**

- Usar um script de bootstrap durante o lançamento de uma instância EC2 para instalar o Amazon Kinesis Agent. Configurar o Kinesis Agent para coletar os dados de status do EC2 Auto Scaling e enviar os dados para o Amazon Kinesis Data Firehose. Armazenar os dados no Amazon S3.


**Um laboratório de pesquisa médica produz dados relacionados a um novo estudo. O laboratório deseja disponibilizar os dados com latência mínima para clínicas em todo o país para suas aplicações baseadas em arquivos on-premises. Os arquivos de dados estão armazenados em um bucket do Amazon S3 que possui permissões de leitura para cada clínica. O que um arquiteto de soluções deve recomendar para atender a esses requisitos?**

- Implantar um AWS Storage Gateway file gateway como uma máquina virtual (VM) no local em cada clínica

**Uma empresa executa um aplicativo interno baseado em navegador. O aplicativo é executado em instâncias Amazon EC2 atrás de um Application Load Balancer. As instâncias são executadas em um grupo de Auto Scaling do Amazon EC2 em várias Zonas de Disponibilidade. O grupo de Auto Scaling escala até 20 instâncias durante o horário de trabalho, mas escala para 2 instâncias durante a noite. Os funcionários estão reclamando que o aplicativo é muito lento quando o dia começa, embora funcione bem no meio da manhã. Como a escalabilidade deve ser alterada para resolver as reclamações dos funcionários e manter os custos no mínimo?**

- Implementar uma ação de escalonamento de etapas acionada em um limite inferior de CPU e diminuir o período de cooldown.

**Uma empresa está usando uma conta centralizada da AWS para armazenar dados de log em vários buckets do Amazon S3. Um arquiteto de soluções precisa garantir que os dados sejam criptografados em repouso antes de serem carregados nos buckets do S3. Os dados também devem ser criptografados em trânsito. Qual solução atende a esses requisitos?**

- Usar criptografia no lado do cliente para criptografar os dados que estão sendo enviados para os buckets S3.

**Uma empresa de comércio eletrônico em rápido crescimento está executando suas cargas de trabalho em uma única Região da AWS. Um arquiteto de soluções deve criar uma estratégia de recuperação de desastres (DR) que inclua uma Região da AWS diferente. A empresa deseja que seu banco de dados esteja atualizado na Região DR com a menor latência possível. A infraestrutura restante na Região DR precisa operar em capacidade reduzida e deve ser capaz de escalar se necessário. Qual solução atenderá a esses requisitos com o menor tempo de recuperação (RTO)?**

- Usar um banco de dados global Amazon Aurora com uma implantação de standby aquecido.

**Uma empresa oferece um serviço online para postar conteúdo de vídeo e transcodificá-lo para uso em qualquer plataforma móvel. A arquitetura do aplicativo usa Amazon Elastic File System (Amazon EFS) Standard para coletar e armazenar os vídeos para que várias instâncias Amazon EC2 Linux possam acessar o conteúdo do vídeo para processamento. À medida que a popularidade do serviço cresceu ao longo do tempo, os custos de armazenamento se tornaram muito caros. Qual solução de armazenamento é mais econômica?**

- Usar o Amazon S3 para armazenar o conteúdo de vídeo. Mover os arquivos temporariamente para um volume Amazon Elastic Block Store (Amazon EBS) anexado ao servidor para processamento.


**Usar o Amazon S3 para armazenar o conteúdo de vídeo. Mover os arquivos temporariamente para um volume Amazon Elastic Block Store (Amazon EBS) anexado ao servidor para processamento.**

- Criar um sistema de arquivos Amazon Elastic File System (Amazon EFS). Montar o sistema de arquivos EFS em todos os servidores web.

**Uma empresa tem um aplicativo web baseado em Java e PHP. A empresa planeja mover o aplicativo de on-premises para a AWS. A empresa precisa da capacidade de testar novos recursos do site com frequência. A empresa também precisa de uma solução altamente disponível e gerenciada que requeira o mínimo de sobrecarga operacional. Qual solução atenderá a esses requisitos?**

- Implante o aplicativo web em um ambiente AWS Elastic Beanstalk. Use troca de URL para alternar entre vários ambientes Elastic Beanstalk para teste de funcionalidades.

**Uma empresa recentemente migrou seu aplicativo web para a AWS realocando o aplicativo em instâncias Amazon EC2 em uma única região AWS. A empresa deseja redesenhar a arquitetura do aplicativo para ser altamente disponível e tolerante a falhas. O tráfego deve alcançar todas as instâncias EC2 em execução aleatoriamente. Qual combinação de etapas a empresa deve tomar para atender a esses requisitos? (Escolha duas.)**

- Inicie quatro instâncias EC2: duas instâncias em uma zona de disponibilidade e duas instâncias em outra zona de disponibilidade.
- Crie uma política de roteamento de resposta múltipla no Amazon Route 53.

**Um servidor web de uma empresa está sendo executado em uma instância Amazon EC2 em uma subnet pública com um endereço IP elástico. O grupo de segurança padrão está atribuído à instância EC2. O ACL de rede padrão foi modificado para bloquear todo o tráfego. Um arquiteto de soluções precisa tornar o servidor web acessível de qualquer lugar na porta 443. Qual combinação de etapas realizará essa tarefa? (Escolha duas.)**

- Crie um grupo de segurança com uma regra para permitir TCP na porta 443 da ORIGEM 0.0.0.0/0.
- Atualize o ACL de rede para permitir a entrada na porta TCP 443 da ORIGEM 0.0.0.0/0 e saída na porta TCP 32768-65535 para o destino 0.0.0.0/0.

**Uma empresa está executando um aplicativo em lote em instâncias Amazon EC2. O aplicativo consiste em um back-end com vários bancos de dados Amazon RDS. O aplicativo está causando um grande número de leituras nos bancos de dados. Um arquiteto de soluções deve reduzir o número de leituras no banco de dados enquanto garante alta disponibilidade. O que o arquiteto de soluções deve fazer para atender a esse requisito?**

- Use Amazon ElastiCache for Redis.


# SIMULADO 4
---

**Uma empresa recentemente começou a usar o Amazon Aurora como o repositório de dados para seu aplicativo de comércio eletrônico global. Quando grandes relatórios são executados, os desenvolvedores relatam que o aplicativo de comércio eletrônico está tendo um desempenho ruim. Após revisar as métricas no Amazon CloudWatch, um arquiteto de soluções descobre que as métricas ReadIOPS e CPUUtilization estão disparando quando os relatórios mensais são executados. Qual é a solução mais econômica?**

- Migre o relatório mensal para um Aurora Replica.

**Uma empresa está migrando um aplicativo de servidores on-premises para instâncias Amazon EC2. Como parte dos requisitos de design de migração, um arquiteto de soluções deve implementar alarmes de métrica de infraestrutura. A empresa não precisa agir se a utilização da CPU aumentar para mais de 50% por um curto período de tempo. No entanto, se a utilização da CPU aumentar para mais de 50% e os IOPS de leitura no disco estiverem altos ao mesmo tempo, a empresa precisa agir o mais rápido possível. O arquiteto de soluções também deve reduzir falsos alarmes. O que o arquiteto de soluções deve fazer para atender a esses requisitos?**

- Crie alarmes compostos do Amazon CloudWatch sempre que possível.

**Uma empresa está migrando seu banco de dados PostgreSQL on-premises para o Amazon Aurora PostgreSQL. O banco de dados on-premises deve permanecer online e acessível durante a migração. O banco de dados Aurora deve permanecer sincronizado com o banco de dados on-premises. Qual combinação de ações um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas)**

- Crie uma tarefa de replicação contínua.
- Crie um servidor de replicação do AWS Database Migration Service (AWS DMS).

**O aplicativo web de uma empresa está sendo executado em instâncias Amazon EC2 por trás de um Application Load Balancer. A empresa recentemente mudou sua política, que agora exige que o aplicativo seja acessado apenas de um país específico. Qual configuração atenderá a esse requisito?**

- Configure o AWS WAF no Application Load Balancer em uma VPC.

**Um arquiteto de soluções está criando uma nova distribuição Amazon CloudFront para um aplicativo. Algumas das informações enviadas pelos usuários são confidenciais. O aplicativo usa HTTPS, mas precisa de outra camada de segurança. As informações confidenciais devem ser protegidas em toda a pilha do aplicativo, e o acesso às informações deve ser restrito a certos aplicativos. Qual ação o arquiteto de soluções deve tomar?**

- Configure um perfil de criptografia de nível de campo do CloudFront.

**IncorretoUma empresa de entretenimento está usando o Amazon DynamoDB para armazenar metadados de mídia. O aplicativo é intensivo em leitura e está apresentando atrasos. A empresa não tem equipe para lidar com sobrecarga operacional adicional e precisa melhorar a eficiência de desempenho do DynamoDB sem reconfigurar o aplicativo. O que um arquiteto de soluções deve recomendar para atender a esse requisito?**

- Use o Amazon DynamoDB Accelerator (DAX).

**Uma empresa executa cargas de trabalho na AWS. A empresa precisa se conectar a um serviço de um provedor externo. O serviço é hospedado na VPC do provedor. De acordo com a equipe de segurança da empresa, a conectividade deve ser privada e deve ser restrita ao serviço de destino. A conexão deve ser iniciada apenas a partir da VPC da empresa. Qual solução atenderá a esses requisitos?**

- Peça ao provedor para criar um endpoint de VPC para o serviço de destino. Use o AWS PrivateLink para se conectar ao serviço de destino.


**Um arquiteto de soluções está otimizando um site para um próximo evento musical. Vídeos das apresentações serão transmitidos em tempo real e depois estarão disponíveis sob demanda. Espera-se que o evento atraia um público online global. Qual serviço melhorará o desempenho tanto do streaming em tempo real quanto do streaming sob demanda**

- AWS Global Accelerator.

**Uma empresa produz dados em lote que vêm de diferentes bancos de dados. A empresa também produz dados de stream ao vivo de sensores de rede e APIs de aplicativos. A empresa precisa consolidar todos os dados em um único lugar para análises de negócios. A empresa precisa processar os dados recebidos e depois armazenar os dados em diferentes buckets Amazon S3. As equipes executarão consultas únicas e importarão os dados para uma ferramenta de inteligência de negócios para mostrar indicadores chave de desempenho (KPIs). Qual combinação de etapas atenderá a esses requisitos com a menor sobrecarga operacional? (Escolha duas.)**

-  Use modelos no AWS Lake Formation para identificar os dados que podem ser ingeridos em um data lake. Use o AWS Glue para rastrear a fonte, extrair os dados e carregar os dados no Amazon S3 no formato Apache Parquet.

- Use o Amazon Athena para consultas únicas. Use o Amazon QuickSight para criar dashboards para KPIs.

**Um arquiteto de soluções precisa ajudar uma empresa a otimizar o custo de execução de um aplicativo na AWS. O aplicativo usará instâncias Amazon EC2, AWS Fargate e AWS Lambda para computação dentro da arquitetura. As instâncias EC2 executarão a camada de ingestão de dados do aplicativo. O uso do EC2 será esporádico e imprevisível. As cargas de trabalho que são executadas nas instâncias EC2 podem ser interrompidas a qualquer momento. A interface do aplicativo será executada no Fargate, e o Lambda servirá a camada de API. A utilização da interface e a utilização da camada de API serão previsíveis ao longo do próximo ano. Qual combinação de opções de compra fornecerá a solução mais econômica para hospedar este aplicativo? (Escolha duas.)**

- Compre um Compute Savings Plan de 1 ano para a camada front-end e API.
- Use Spot Instances para a camada de ingestão de dados.

**Uma empresa está projetando uma plataforma de comunicações em nuvem que é acionada por APIs. O aplicativo é hospedado em instâncias Amazon EC2 por trás de um Network Load Balancer (NLB). A empresa usa Amazon API Gateway para fornecer aos usuários externos acesso ao aplicativo através de APIs. A empresa quer proteger a plataforma contra exploits web como injeção de SQL e também quer detectar e mitigar grandes ataques DDoS sofisticados. Qual combinação de soluções fornece a maior proteção? (Escolha duas.)**

- Use o AWS Shield Advanced com o NLB.
- Use o AWS WAF para proteger o Amazon API Gateway.

**Uma empresa precisa salvar os resultados de um ensaio médico em um repositório Amazon S3. O repositório deve permitir que alguns cientistas adicionem novos arquivos e deve restringir todos os outros usuários ao acesso somente leitura. Nenhum usuário pode ter a capacidade de modificar ou excluir qualquer arquivo no repositório. A empresa deve manter cada arquivo no repositório por um mínimo de 1 ano após sua data de criação. Qual solução atenderá a esses requisitos?**

- Use o S3 Object Lock no modo de conformidade com um período de retenção de 365 dias.

**Uma empresa de jogos está projetando uma arquitetura altamente disponível. O aplicativo é executado em um kernel Linux modificado e suporta apenas tráfego baseado em UDP. A empresa precisa que a camada de front-end forneça a melhor experiência possível para o usuário. Essa camada deve ter baixa latência, rotear o tráfego para a localização de borda mais próxima e fornecer endereços IP estáticos para entrada nos endpoints do aplicativo. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

- Configure o AWS Global Accelerator para encaminhar solicitações para um Network Load Balancer. Use instâncias Amazon EC2 para o aplicativo em um grupo de Auto Scaling do EC2.

# SIMULADO 5 

**Uma empresa quer migrar um data center on-premises para a AWS. O data center hospeda um servidor SFTP que armazena seus dados em um sistema de arquivos baseado em NFS. O servidor possui 200 GB de dados que precisam ser transferidos. O servidor deve ser hospedado em uma instância Amazon EC2 que usa um sistema de arquivos Amazon Elastic File System (Amazon EFS). Qual combinação de etapas um arquiteto de soluções deve seguir para automatizar essa tarefa? (Escolha duas.)**

- Lance a instância EC2 na mesma zona de disponibilidade que o sistema de arquivos EFS.
- Instale um agente AWS DataSync no data center on-premises.

**Uma empresa usa um popular sistema de gerenciamento de conteúdo (CMS) para seu site corporativo. No entanto, o patching e a manutenção necessários são onerosos. A empresa está redesenhando seu site e deseja uma nova solução. O site será atualizado quatro vezes por ano e não precisa ter nenhum conteúdo dinâmico disponível. A solução deve fornecer alta escalabilidade e segurança aprimorada. Qual combinação de mudanças atenderá a esses requisitos com o MENOR esforço operacional? (Escolha duas.)**

- Crie o novo site e um bucket Amazon S3. Implemente o site no bucket S3 com o hosting de site estático habilitado.
- Configure o Amazon CloudFront na frente do site para usar a funcionalidade HTTPS.

**Uma empresa armazena seus logs de aplicativos em um grupo de logs do Amazon CloudWatch Logs. Uma nova política exige que a empresa armazene todos os logs de aplicativos no Amazon OpenSearch Service (Amazon Elasticsearch Service) em quase tempo real. Qual solução atenderá a esse requisito com o MENOR esforço operacional?**

- Configure uma assinatura de logs do CloudWatch para transmitir os logs para o Amazon OpenSearch Service (Amazon Elasticsearch Service).

**Uma empresa de pesquisa reuniu dados por vários anos de áreas nos Estados Unidos. A empresa hospeda os dados em um bucket Amazon S3 que tem 3 TB de tamanho e está crescendo. A empresa começou a compartilhar os dados com uma empresa de marketing europeia que possui buckets S3. A empresa quer garantir que seus custos de transferência de dados permaneçam os mais baixos possíveis. Qual solução atenderá a esses requisitos?**

- Configure o recurso Requester Pays no bucket S3 da empresa.

**Uma empresa global está usando o Amazon API Gateway para projetar APIs REST para seus usuários do clube de fidelidade na região us-east-1 e na região ap-southeast-2. Um arquiteto de soluções deve projetar uma solução para proteger essas APIs REST gerenciadas pelo API Gateway em várias contas contra ataques de injeção de SQL e scripts entre sites. Qual solução atenderá a esses requisitos com o menor esforço administrativo?**

- Configure o AWS Firewall Manager em ambas as regiões. Configure centralmente as regras do AWS WAF.

**Uma empresa implementou uma solução de DNS autogerenciada em três instâncias Amazon EC2 atrás de um Network Load Balancer (NLB) na região us-west-2. A maioria dos usuários da empresa está localizada nos Estados Unidos e na Europa. A empresa deseja melhorar o desempenho e a disponibilidade da solução. A empresa lança e configura três instâncias EC2 na região eu-west-1 e adiciona as instâncias EC2 como destinos para um novo NLB. Qual solução a empresa pode usar para rotear o tráfego para todas as instâncias EC2?**

- Crie um acelerador padrão no AWS Global Accelerator. Crie grupos de endpoints em us-west-2 e eu-west-1. Adicione os dois NLBs como endpoints para os grupos de endpoints.

**Uma empresa executa um aplicativo de compras que usa o Amazon DynamoDB para armazenar informações dos clientes. Em caso de corrupção de dados, um arquiteto de soluções precisa projetar uma solução que atenda a um objetivo de ponto de recuperação (RPO) de 15 minutos e um objetivo de tempo de recuperação (RTO) de 1 hora. O que o arquiteto de soluções deve recomendar para atender a esses requisitos?**

- Configure a recuperação point-in-time do DynamoDB. Para recuperação de RPO, restaure para o ponto no tempo desejado.

**Uma empresa de compartilhamento de bicicletas está desenvolvendo uma arquitetura em várias camadas para rastrear a localização de suas bicicletas durante as horas de operação de pico. A empresa deseja usar esses pontos de dados em sua plataforma de análise existente. Um arquiteto de soluções deve determinar a opção de várias camadas mais viável para suportar essa arquitetura. Os pontos de dados devem ser acessíveis a partir da API REST. Qual ação atende a esses requisitos para armazenar e recuperar dados de localização?**

- Use o Amazon API Gateway com o AWS Lambda.

**Uma empresa recebe 10 TB de dados de instrumentação todos os dias de várias máquinas localizadas em uma única fábrica. Os dados consistem em arquivos JSON armazenados em uma rede de armazenamento (SAN) em um data center local localizado dentro da fábrica. A empresa quer enviar esses dados para o Amazon S3, onde eles podem ser acessados por vários sistemas adicionais que fornecem análises críticas quase em tempo real. Uma transferência segura é importante porque os dados são considerados sensíveis. Qual solução oferece a transferência de dados mais confiável?**

- AWS DataSync sobre AWS Direct Connect

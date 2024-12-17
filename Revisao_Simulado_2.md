# Pergunta 1
**Uma empresa anunciou recentemente o lançamento de seu site de varejo para um público global. O site roda em várias instâncias Amazon EC2 atrás de um Elastic Load Balancer. As instâncias rodam em um grupo de Auto Scaling em várias zonas de disponibilidade. A empresa quer fornecer aos seus clientes diferentes versões de conteúdo com base nos dispositivos que os clientes usam para acessar o site. Qual combinação de ações um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Configurar o Amazon CloudFront para armazenar em cache várias versões do conteúdo.
- Configurar uma função Lambda@Edge para enviar objetos específicos para usuários com base no cabeçalho User-Agent.

---

# Pergunta 2
**Uma equipe de desenvolvimento lançou um novo aplicativo hospedado em instâncias Amazon EC2 dentro de uma VPC de desenvolvimento. Um arquiteto de soluções precisa criar uma nova VPC na mesma conta. A nova VPC será pareada com a VPC de desenvolvimento. O bloco CIDR da VPC de desenvolvimento é 192.168.0.0/24. O arquiteto de soluções precisa criar um bloco CIDR para a nova VPC. O bloco CIDR deve ser válido para uma conexão de emparelhamento VPC com a VPC de desenvolvimento. Qual é o menor bloco CIDR que atende a esses requisitos?**

- 10.0.1.0/24

---

# Pergunta 3
**Uma empresa está preparando uma nova plataforma de dados que irá ingerir dados de streaming em tempo real de várias fontes. A empresa precisa transformar os dados antes de gravar os dados no Amazon S3. A empresa precisa da capacidade de usar SQL para consultar os dados transformados. Quais soluções atenderão a esses requisitos? (Escolha dois.)**

- Usar o Amazon Kinesis Data Streams para transmitir os dados. Usar o Amazon Kinesis Data Analytics para transformar os dados. Usar o Amazon Kinesis Data Firehose para gravar os dados no Amazon S3. Usar o Amazon Athena para consultar os dados transformados do Amazon S3.
- Usar o Amazon Managed Streaming for Apache Kafka (Amazon MSK) para transmitir os dados. Usar o AWS Glue para transformar os dados e gravá-los no Amazon S3. Usar o Amazon Athena para consultar os dados transformados do Amazon S3.

---

# Pergunta 4
**Um laboratório de pesquisa precisa processar aproximadamente 8 TB de dados. O laboratório requer latências de sub-milisegundo e uma taxa de transferência mínima de 6 GBps para o subsistema de armazenamento. Centenas de instâncias Amazon EC2 que executam Amazon Linux distribuirão e processarão os dados. Qual solução atenderá aos requisitos de desempenho?**

- Criar um bucket Amazon S3 para armazenar os dados brutos. Criar um sistema de arquivos Amazon FSx for Lustre que usa armazenamento SSD persistente. Selecionar a opção para importar dados de e exportar dados para o Amazon S3. Montar o sistema de arquivos nas instâncias EC2.

---

# Pergunta 5
**Uma empresa de mídia usa o Amazon CloudFront para seu conteúdo de vídeo de streaming disponível publicamente. A empresa deseja proteger o conteúdo de vídeo hospedado no Amazon S3 controlando quem tem acesso. Alguns dos usuários da empresa estão usando um cliente HTTP personalizado que não suporta cookies. Alguns dos usuários da empresa não podem alterar as URLs hardcoded que estão usando para acessar. Quais serviços ou métodos atenderão a esses requisitos com o menor impacto para os usuários? (Escolha dois.)**

- Cookies assinados
- URLs assinados

---

# Pergunta 6
**Uma empresa hospeda um aplicativo web em várias instâncias Amazon EC2. As instâncias EC2 estão em um grupo de Auto Scaling que escala em resposta à demanda dos usuários. A empresa deseja otimizar as economias de custos sem assumir um compromisso de longo prazo. Qual opção de compra de instância EC2 um arquiteto de soluções deve recomendar para atender a esses requisitos?**

- Uma mistura de instâncias On-Demand e Spot

---

# Pergunta 7
**Uma empresa precisa migrar um aplicativo legado de um data center local para a Nuvem AWS devido a restrições de capacidade de hardware. O aplicativo funciona 24 horas por dia, 7 dias por semana. O armazenamento do banco de dados do aplicativo continua a crescer ao longo do tempo. O que um arquiteto de soluções deve fazer para atender a esses requisitos da maneira mais econômica?**

- Migrar a camada de aplicação para instâncias reservadas do Amazon EC2. Migrar a camada de armazenamento.

---

# Pergunta 8
**Um arquiteto de soluções precisa projetar um aplicativo altamente disponível composto por camadas web, de aplicação e de banco de dados. A entrega de conteúdo HTTPS deve estar o mais próxima possível da borda, com o menor tempo de entrega. Qual solução atende a esses requisitos e é a mais segura?**

- Configurar um Application Load Balancer (ALB) público com várias instâncias Amazon EC2 redundantes em sub-redes privadas. Configurar o Amazon CloudFront para entregar conteúdo HTTPS usando o ALB público como origem.

---

# Pergunta 9
**Um laboratório de pesquisa médica produz dados relacionados a um novo estudo. O laboratório deseja disponibilizar os dados com latência mínima para clínicas em todo o país para suas aplicações baseadas em arquivos on-premises. Os arquivos de dados estão armazenados em um bucket do Amazon S3 que possui permissões de leitura para cada clínica. O que um arquiteto de soluções deve recomendar para atender a esses requisitos?**

- Implantar um AWS Storage Gateway file gateway como uma máquina virtual (VM) no local em cada clínica.

---

# Pergunta 10
**Uma empresa está revisando uma migração recente de um aplicativo de três camadas para uma VPC. A equipe de segurança descobre que o princípio do menor privilégio não está sendo aplicado às regras de entrada e saída dos grupos de segurança do Amazon EC2 entre as camadas do aplicativo. O que um arquiteto de soluções deve fazer para corrigir esse problema?**

- Criar regras de grupo de segurança usando o ID do grupo de segurança como origem ou destino.

# Pergunta 11
**Uma empresa executa um aplicativo interno baseado em navegador. O aplicativo é executado em instâncias Amazon EC2 atrás de um Application Load Balancer. As instâncias são executadas em um grupo de Auto Scaling do Amazon EC2 em várias Zonas de Disponibilidade. O grupo de Auto Scaling escala até 20 instâncias durante o horário de trabalho, mas escala para 2 instâncias durante a noite. Os funcionários estão reclamando que o aplicativo é muito lento quando o dia começa, embora funcione bem no meio da manhã. Como a escalabilidade deve ser alterada para resolver as reclamações dos funcionários e manter os custos no mínimo?**

- Implementar uma ação de rastreamento de alvo acionada em um limite inferior de CPU e diminuir o período de cooldown.

---
# Pergunta 12
**Uma empresa está executando um aplicativo de negócios crítico em instâncias Amazon EC2 atrás de um Application Load Balancer. As instâncias EC2 são executadas em um grupo de Auto Scaling e acessam uma instância Amazon RDS. O design não passou por uma revisão operacional porque as instâncias EC2 e a instância RDS estão todas localizadas em uma única Zona de Disponibilidade. Um arquiteto de soluções deve atualizar o design para usar uma segunda Zona de Disponibilidade. Qual solução tornará o aplicativo altamente disponível?**

- Provisionar uma sub-rede em cada Zona de Disponibilidade. Configurar o grupo de Auto Scaling para distribuir as instâncias EC2 entre ambas as Zonas de Disponibilidade. Configurar a instância do DB para implantação Multi-AZ.

---

# Pergunta 13
**Um arquiteto de soluções precisa projetar um sistema para armazenar arquivos de casos de clientes. Os arquivos são ativos principais da empresa e são importantes. O número de arquivos crescerá com o tempo. Os arquivos devem ser acessíveis simultaneamente a partir de vários servidores de aplicação que rodam em instâncias Amazon EC2. A solução deve ter redundância embutida. Qual solução atende a esses requisitos?**

- Amazon Elastic File System (Amazon EFS)

---

# Pergunta 14
**Uma empresa deseja migrar um aplicativo baseado em Windows do local para a Nuvem AWS. O aplicativo possui três camadas: uma camada de aplicativo, uma camada de negócios e uma camada de banco de dados com Microsoft SQL Server. A empresa deseja usar recursos específicos do SQL Server, como backups nativos e Data Quality Services. A empresa também precisa compartilhar arquivos para processamento entre as camadas. Como um arquiteto de soluções deve projetar a arquitetura para atender a esses requisitos?**

- Hospedar todas as três camadas em instâncias Amazon EC2. Usar Amazon FSx for Windows File Server para compartilhamento de arquivos entre as camadas.

---

# Pergunta 15
**Uma empresa está implementando novas políticas de retenção de dados para todos os bancos de dados que rodam em instâncias Amazon RDS DB. A empresa deve reter backups diários por um período mínimo de 2 anos. Os backups devem ser consistentes e restauráveis. Qual solução um arquiteto de soluções deve recomendar para atender a esses requisitos?**

- Criar um cofre de backup no AWS Backup para reter backups do RDS. Criar um novo plano de backup com uma programação diária e um período de expiração de 2 anos após a criação. Atribuir as instâncias do RDS ao plano de backup.

---

# Pergunta 16
**Uma empresa planeja usar o Amazon ElastiCache para seu aplicativo web de várias camadas. Um arquiteto de soluções cria uma VPC Cache para o cluster ElastiCache e uma VPC App para as instâncias Amazon EC2 do aplicativo. Ambas as VPCs estão na região us-east-1. O arquiteto de soluções deve implementar uma solução para fornecer às instâncias EC2 do aplicativo acesso ao cluster ElastiCache. Qual solução atenderá a esses requisitos da maneira mais econômica?**

- Criar uma conexão de emparelhamento entre as VPCs. Adicionar uma entrada na tabela de rotas para a conexão de emparelhamento em ambas as VPCs. Configurar uma regra de entrada para o grupo de segurança do cluster do ElastiCache para permitir a conexão de entrada do grupo de segurança do aplicativo.

---

# Pergunta 17
**Uma empresa deseja criar um aplicativo para armazenar dados de funcionários em uma estrutura hierárquica. A empresa precisa de uma resposta de latência mínima para consultas de alto tráfego aos dados dos funcionários e deve proteger quaisquer dados confidenciais. A empresa também precisa receber mensagens de e-mail mensais se houver qualquer informação financeira presente nos dados dos funcionários. Qual combinação de etapas um arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Usar o Amazon DynamoDB para armazenar os dados dos funcionários em hierarquias. Exportar os dados para o Amazon S3 todos os meses.
- Configurar o Amazon Macie para a conta da AWS. Integrar o Macie com o Amazon EventBridge para enviar notificações mensais através de uma assinatura Amazon Simple Notification Service (Amazon SNS).

---

# Pergunta 18
**Uma empresa executa um aplicativo em instâncias Amazon EC2. A empresa precisa implementar uma solução de recuperação de desastres (DR) para o aplicativo. A solução DR precisa ter um objetivo de tempo de recuperação (RTO) de menos de 4 horas. A solução DR também precisa usar o menor número possível de recursos da AWS durante as operações normais. Qual solução atenderá a esses requisitos da maneira mais eficiente operacionalmente?**

- Criar Amazon Machine Images (AMIs) para fazer backup das instâncias EC2. Copiar as AMIs para uma região secundária da AWS. Automatizar a implantação da infraestrutura na região secundária usando AWS CloudFormation.

---

# Pergunta 19
**Uma empresa está implementando uma solução de armazenamento compartilhado para um aplicativo de mídia que está hospedado na AWS Cloud. A empresa precisa da capacidade de usar clientes SMB para acessar os dados. A solução deve ser totalmente gerenciada. Qual solução da AWS atende a esses requisitos?**

- Criar um sistema de arquivos Amazon FSx for Windows File Server. Anexar o sistema de arquivos ao servidor de origem. Conectar o servidor de aplicativos ao sistema de arquivos.

---

# Pergunta 20
**Uma empresa está construindo uma solução que irá relatar eventos do Amazon EC2 Auto Scaling em todos os aplicativos em uma conta AWS. A empresa precisa usar uma solução serverless para armazenar os dados de status do Auto Scaling do EC2 no Amazon S3. A empresa então usará os dados no S3 para fornecer atualizações quase em tempo real em um painel de controle. A solução não deve afetar a velocidade dos lançamentos de instâncias EC2. Como a empresa deve mover os dados para o Amazon S3 para atender a esses requisitos?**

- Usar um script de bootstrap durante o lançamento de uma instância EC2 para instalar o Amazon Kinesis Agent. Configurar o Kinesis Agent para coletar os dados de status do EC2 Auto Scaling e enviar os dados para o Amazon Kinesis Data Firehose. Armazenar os dados no Amazon S3.

---

# Pergunta 21
**Uma empresa oferece um serviço online para postar conteúdo de vídeo e transcodificá-lo para uso em qualquer plataforma móvel. A arquitetura do aplicativo usa Amazon Elastic File System (Amazon EFS) Standard para coletar e armazenar os vídeos para que várias instâncias Amazon EC2 Linux possam acessar o conteúdo do vídeo para processamento. À medida que a popularidade do serviço cresceu ao longo do tempo, os custos de armazenamento se tornaram muito caros. Qual solução de armazenamento é mais econômica?**

- Usar o Amazon EFS para armazenar o conteúdo de vídeo. Após o processamento ser concluído, transferir os arquivos para o Amazon Elastic Block Store (Amazon EBS).

# Pergunta 22
**Uma empresa executa um aplicativo web em instâncias Amazon EC2 em várias zonas de disponibilidade. As instâncias EC2 estão em sub-redes privadas. Um arquiteto de soluções implementa um Application Load Balancer (ALB) voltado para a internet e especifica as instâncias EC2 como o grupo de destino. No entanto, o tráfego da internet não está alcançando as instâncias EC2. Como o arquiteto de soluções deve reconfigurar a arquitetura para resolver esse problema?**

- Criar sub-redes públicas em cada Zona de Disponibilidade. Associar as sub-redes públicas ao ALB. Atualizar as tabelas de rotas para as sub-redes públicas com uma rota para as sub-redes privadas.

---

# Pergunta 23
**Uma empresa tem uma função AWS Lambda que precisa de acesso de leitura a um bucket Amazon S3 que está localizado na mesma conta da AWS. Qual solução atenderá a esses requisitos da maneira mais segura?**

- Aplicar uma função IAM à função Lambda. Aplicar uma política IAM à função para conceder acesso de leitura ao bucket S3.

---

# Pergunta 24
**A equipe de conformidade de uma empresa precisa mover seus compartilhamentos de arquivos para a AWS. Os compartilhamentos rodam em um compartilhamento de arquivos SMB do Windows Server. Um Active Directory autogerenciado on-premises controla o acesso aos arquivos e pastas. A empresa quer usar o Amazon FSx para Windows File Server como parte da solução. A empresa deve garantir que os grupos do Active Directory on-premises restrinjam o acesso aos compartilhamentos de conformidade SMB do FSx para Windows File Server, pastas e arquivos após a mudança para a AWS. A empresa criou um sistema de arquivos FSx para Windows File Server. Qual solução atenderá a esses requisitos?**

- Juntar o sistema de arquivos ao Active Directory para restringir o acesso.

---

# Pergunta 25
**Uma empresa implantou um banco de dados no Amazon RDS para MySQL. Devido ao aumento das transações, a equipe de suporte do banco de dados está relatando leituras lentas contra a instância do DB e recomenda adicionar uma réplica de leitura. Quais ações um arquiteto de soluções deve tomar antes de implementar essa mudança? (Escolha duas.)**

- Habilite backups automáticos na instância de origem, definindo o período de retenção de backup para um valor diferente de 0.
- Permitir que transações de longa duração sejam concluídas na instância de origem do DB.

---

# Pergunta 26
**Uma empresa de comércio eletrônico armazena terabytes de dados de clientes na Nuvem AWS. Os dados contêm informações de identificação pessoal (PII). A empresa deseja usar os dados em três aplicativos. Apenas um dos aplicativos precisa processar as PII. As PII devem ser removidas antes que os outros dois aplicativos processem os dados. Qual solução atenderá a esses requisitos com o menor overhead operacional?**

- Armazenar os dados em um bucket Amazon S3. Processar e transformar os dados usando o S3 Object Lambda antes de retornar os dados para o aplicativo solicitante.

---

# Pergunta 27
**Uma empresa está usando uma conta centralizada da AWS para armazenar dados de log em vários buckets do Amazon S3. Um arquiteto de soluções precisa garantir que os dados sejam criptografados em repouso antes de serem carregados nos buckets do S3. Os dados também devem ser criptografados em trânsito. Qual solução atende a esses requisitos?**

- Usar criptografia no lado do cliente para criptografar os dados que estão sendo enviados para os buckets S3.

---

# Pergunta 28
**Uma empresa hospeda seu aplicativo web na AWS usando sete instâncias Amazon EC2. A empresa exige que os endereços IP de todas as instâncias EC2 saudáveis sejam retornados em resposta às consultas DNS. Qual política deve ser usada para atender a essa exigência?**

- Política de roteamento multivalor.

---

# Pergunta 29
**Uma empresa de jogos tem um aplicativo web que exibe pontuações. O aplicativo roda em instâncias Amazon EC2 atrás de um Application Load Balancer. O aplicativo armazena dados em um banco de dados Amazon RDS para MySQL. Os usuários estão começando a experimentar longos atrasos e interrupções causados pelo desempenho de leitura do banco de dados. A empresa quer melhorar a experiência do usuário enquanto minimiza as mudanças na arquitetura do aplicativo. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

- Usar o Amazon ElastiCache na frente do banco de dados.

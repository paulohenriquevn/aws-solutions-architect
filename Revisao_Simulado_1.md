# Pergunta 1
**Uma empresa possui um aplicativo Java que usa o Amazon Simple Queue Service (Amazon SQS) para analisar mensagens. O aplicativo não consegue analisar mensagens maiores que 256 KB. A empresa deseja implementar uma solução para dar ao aplicativo a capacidade de analisar mensagens de até 50 MB. Qual solução atenderá a esses requisitos com o MENOR número de mudanças no código?**

- Usar a Amazon SQS Extended Client Library para Java para hospedar mensagens maiores que 256 KB no Amazon S3.

# Pergunta 2
**Um hospital precisa armazenar registros de pacientes em um bucket Amazon S3. A equipe de conformidade do hospital deve garantir que todas as informações de saúde protegidas (PHI) sejam criptografadas em trânsito e em repouso. A equipe de conformidade deve gerenciar a chave de criptografia para dados em repouso. Qual solução atenderá a esses requisitos?**

- Use a condição aws:SecureTransport nas políticas de bucket S3 para permitir apenas conexões criptografadas via HTTPS (TLS). Configure a criptografia padrão para cada bucket S3 para usar criptografia no lado do servidor com chaves do AWS KMS (SSE-KMS). Configure a equipe de conformidade para gerenciar as chaves KMS.

# Pergunta 3
**Uma empresa deseja executar um banco de dados na memória para um aplicativo sensível à latência que é executado em instâncias Amazon EC2. O aplicativo processa mais de 100.000 transações por minuto e requer alta taxa de transferência de rede. Um arquiteto de soluções precisa fornecer um design de rede econômico que minimize as taxas de transferência de dados. Qual solução atende a esses requisitos?**

- Lançar todas as instâncias EC2 na mesma Zona de Disponibilidade dentro da mesma Região AWS. Especificar um grupo de colocação com estratégia de cluster ao lançar instâncias EC2.

# Pergunta 4
**Uma empresa usa uma instância Amazon RDS para Microsoft SQL Server Single-AZ de 100 GB na região us-east-1 para armazenar transações de clientes. A empresa precisa de alta disponibilidade e recuperação automática para a instância do banco de dados. A empresa também deve executar relatórios no banco de dados do RDS várias vezes por ano. O processo de relatório faz com que as transações demorem mais do que o usual para serem registradas nas contas dos clientes. A empresa precisa de uma solução que melhore o desempenho do processo de relatório. Qual combinação de etapas atenderá a esses requisitos? (Escolha duas.)**

- Modificar a instância DB de uma instância Single-AZ para uma implantação Multi-AZ.
- Crie uma réplica de leitura da instância DB em uma Zona de Disponibilidade diferente. Direcione todas as solicitações de relatórios para a réplica de leitura.

# Pergunta 5
**Uma empresa de mídia hospeda seu site na AWS. A arquitetura do aplicativo do site inclui uma frota de instâncias Amazon EC2 atrás de um Application Load Balancer (ALB) e um banco de dados hospedado no Amazon Aurora. A equipe de cibersegurança da empresa relata que o aplicativo é vulnerável a injeção de SQL. Como a empresa deve resolver esse problema?**

- Usar AWS WAF na frente do ALB. Associar os ACLs da web apropriados ao AWS WAF.

# Pergunta 6
**O que um arquiteto de soluções deve fazer para garantir que todos os objetos carregados em um bucket do Amazon S3 sejam criptografados?**

- Atualize a política do bucket para negar se o PutObject não tiver o cabeçalho x-amz-server-side-encryption definido.

# Pergunta 7
**Uma empresa quer restringir o acesso ao conteúdo de um de seus principais aplicativos web e proteger o conteúdo usando técnicas de autorização disponíveis na AWS. A empresa quer implementar uma arquitetura serverless e uma solução de autenticação para menos de 100 usuários. A solução precisa integrar-se com o aplicativo web principal e servir conteúdo web globalmente. A solução também deve escalar conforme a base de usuários da empresa cresce, enquanto proporciona a menor latência de login possível. Qual solução atenderá a esses requisitos da maneira mais econômica?**

- Usar Amazon Cognito para autenticação. Usar Lambda@Edge para autorização. Usar Amazon CloudFront para servir o aplicativo web globalmente.


# Pergunta 8
**Uma empresa de processamento de transações tem trabalhos de lote programados que rodam semanalmente em instâncias Amazon EC2. As instâncias do EC2 estão em um grupo de Auto Scaling. O número de transações pode variar, mas a utilização da CPU básica observada em cada execução é de pelo menos 60%. A empresa precisa provisionar a capacidade 30 minutos antes de os trabalhos serem executados. Atualmente, os engenheiros completam essa tarefa modificando manualmente os parâmetros do grupo de Auto Scaling. A empresa não tem recursos para analisar as tendências de capacidade necessárias para as contagens do grupo de Auto Scaling. A empresa precisa de uma maneira automatizada para modificar a capacidade desejada do grupo de Auto Scaling. Qual solução atenderá a esses requisitos com a MENOR sobrecarga operacional?**

- Crie uma política de escalabilidade preditiva para o grupo de Auto Scaling. Configure a política para escalar com base na previsão. Defina a métrica de escalabilidade para utilização da CPU. Defina o valor alvo para a métrica em 60%. Na política, defina as instâncias para pré-lançamento 30 minutos antes dos trabalhos serem executados.

# Pergunta 9
**Uma empresa está migrando um aplicativo antigo para a AWS. O aplicativo executa um trabalho em lote a cada hora e é intensivo em CPU. O trabalho em lote leva em média 15 minutos em um servidor local. O servidor possui 64 vCPUs virtuais (vCPU) e 512 GiB de memória. Qual solução executará o trabalho em lote dentro de 15 minutos com a MENOR sobrecarga operacional?**

- Use o AWS Batch no Amazon EC2.

# Pergunta 10
**Uma empresa possui um aplicativo que está rodando em instâncias Amazon EC2. Um arquiteto de soluções padronizou a empresa em uma determinada família de instâncias e vários tamanhos de instância com base nas necessidades atuais da empresa. A empresa quer maximizar as economias de custo para o aplicativo nos próximos 3 anos. A empresa precisa ser capaz de mudar a família de instâncias e tamanhos nos próximos 6 meses com base na popularidade e uso do aplicativo. Qual solução atenderá a esses requisitos da maneira mais econômica?**

- Compute Savings Plan

# Pergunta 11
**Uma empresa coleta dados de um grande número de participantes que usam dispositivos vestíveis. A empresa armazena os dados em uma tabela Amazon DynamoDB e usa aplicativos para analisar os dados. A carga de trabalho dos dados é constante e previsível. A empresa quer manter-se dentro ou abaixo do seu orçamento previsto para o DynamoDB. Qual solução atenderá a esses requisitos da maneira mais econômica?**

- Use o modo sob demanda. Especifique as unidades de capacidade de leitura (RCUs) e unidades de capacidade de gravação (WCUs) com capacidade reservada.

# Pergunta 12
**Uma empresa está usando uma frota de instâncias Amazon EC2 para ingerir dados de fontes de dados locais. Os dados estão em formato JSON e as taxas de ingestão podem ser de até 1 MB/s. Quando uma instância EC2 é reiniciada, os dados em trânsito são perdidos. A equipe de ciência de dados da empresa deseja consultar os dados ingeridos em tempo quase real. Qual solução fornece consulta de dados em tempo quase real que é escalável com perda mínima de dados?**

- Publicar dados no Amazon Kinesis Data Streams, usar o Kinesis Data Analytics para consultar os dados.

# Pergunta 13
**Uma empresa sofreu uma violação que afetou vários aplicativos em seu data center local. O invasor aproveitou vulnerabilidades nos aplicativos personalizados que estavam rodando nos servidores. A empresa está agora migrando seus aplicativos para serem executados em instâncias do Amazon EC2. A empresa deseja implementar uma solução que ativamente escaneie vulnerabilidades nas instâncias EC2 e envie um relatório detalhando as descobertas. Qual solução atenderá a esses requisitos?**

- Ative o Amazon Inspector. Implemente o agente do Amazon Inspector nas instâncias EC2. Configure uma função AWS Lambda para automatizar a geração e distribuição de relatórios detalhando as descobertas.

# Pergunta 14
**Uma empresa tem um banco de dados MySQL local usado pela equipe de vendas global com padrões de acesso infrequentes. A equipe de vendas exige que o banco de dados tenha tempo de inatividade mínimo. Um administrador de banco de dados deseja migrar este banco de dados para a AWS sem selecionar um tipo de instância específico antecipando mais usuários no futuro. Qual serviço um arquiteto de soluções deve recomendar?**

- Amazon Aurora Serverless for MySQL

# Pergunta 15
**Uma empresa que executa principalmente seus servidores de aplicativos localmente decidiu migrar para a AWS. A empresa deseja minimizar sua necessidade de escalar seu armazenamento de Interface de Sistema de Computador Pequeno na Internet (iSCSI) localmente. A empresa deseja que apenas seus dados acessados recentemente permaneçam armazenados localmente. Qual solução AWS a empresa deve usar para atender a esses requisitos?**

- AWS Storage Gateway Volume Gateway com volumes em cache

# Pergunta 16
**Uma empresa criou recentemente um site de recuperação de desastres em uma Região AWS diferente. A empresa precisa transferir grandes quantidades de dados entre sistemas de arquivos NFS nas duas Regiões periodicamente. Qual solução atenderá a esses requisitos com a MENOR sobrecarga operacional?**

- Usar o AWS DataSync.

# Pergunta 17
**Uma empresa vende conjuntos de dados para clientes que fazem pesquisas em inteligência artificial e aprendizado de máquina (AI/ML). Os conjuntos de dados são arquivos grandes e formatados armazenados em um bucket do Amazon S3 na Região us-east-1. A empresa hospeda um aplicativo web que os clientes usam para comprar acesso a um conjunto de dados específico. O aplicativo web é implantado em várias instâncias Amazon EC2 atrás de um Application Load Balancer. Após a compra, os clientes recebem uma URL assinada do S3 que permite o acesso aos arquivos. Os clientes estão distribuídos pela América do Norte e Europa. A empresa deseja reduzir os custos associados às transferências de dados e manter ou melhorar o desempenho. O que um arquiteto de soluções deve fazer para atender a esses requisitos?**

- Implante uma distribuição Amazon CloudFront com o bucket S3 existente como a origem. Direcione as solicitações dos clientes para o URL do CloudFront. Mude para URLs assinados do CloudFront para controle de acesso.

# Pergunta 18
**Uma empresa possui várias contas AWS que usam faturamento consolidado. A empresa executa várias instâncias de banco de dados Amazon RDS for Oracle On-Demand de alto desempenho ativamente por 90 dias. A equipe financeira da empresa tem acesso ao AWS Trusted Advisor na conta de faturamento consolidado e em todas as outras contas AWS. A equipe financeira precisa usar a conta AWS apropriada para acessar as recomendações do Trusted Advisor para RDS. A equipe financeira deve revisar a verificação do Trusted Advisor apropriada para reduzir os custos do RDS. Qual combinação de etapas a equipe financeira deve seguir para atender a esses requisitos? (Escolha duas.)**

- Revise a verificação do Trusted Advisor para instâncias de banco de dados ociosas do Amazon RDS.
- Use as recomendações do Trusted Advisor da conta de faturamento consolidado para ver todas as verificações de instâncias RDS ao mesmo tempo.

# Pergunta 19
**Uma empresa possui um data lake no Amazon S3 que é gerenciado pelo AWS Lake Formation. A empresa deseja criar uma visualização no Amazon QuickSight unindo os dados no data lake com dados operacionais que estão armazenados em um banco de dados Amazon Aurora MySQL. A empresa deseja impor autorização em nível de coluna para que a equipe de marketing da empresa possa acessar apenas um subconjunto de colunas no banco de dados. Qual solução atenderá a esses requisitos com a MENOR sobrecarga operacional?**

- Use um blueprint do Lake Formation para ingerir os dados do banco de dados no data lake S3. Use o Lake Formation para impor o controle de acesso a nível de coluna para os usuários do QuickSight. Use o Amazon Athena como a fonte de dados no QuickSight.

# Pergunta 20
**Um arquiteto de soluções precisa otimizar os custos de armazenamento. O arquiteto de soluções deve identificar quaisquer buckets do Amazon S3 que não estão mais sendo acessados ou que são raramente acessados. Qual solução alcançará esse objetivo com a MENOR sobrecarga operacional?**

- Analisar os padrões de acesso ao bucket usando o painel S3 Storage Lens para métricas avançadas de atividade.

# Pergunta 21
**Uma empresa recentemente migrou todo o seu ambiente de TI para a Nuvem AWS. A empresa descobre que os usuários estão provisionando instâncias Amazon EC2 superdimensionadas e modificando regras de grupos de segurança sem usar o processo de controle de mudanças adequado. Um arquiteto de soluções deve elaborar uma estratégia para rastrear e auditar essas mudanças de inventário e configuração. Quais ações o arquiteto de soluções deve tomar para atender a esses requisitos? (Escolha duas.)**

- Ative o AWS Config e crie regras para fins de auditoria e conformidade.
- Habilitar o AWS CloudTrail e usá-lo para auditoria.

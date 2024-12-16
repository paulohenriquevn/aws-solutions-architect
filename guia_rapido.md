## Networking e Segurança

### AWS PrivateLink
- **Descrição**: Conecta serviços dentro da AWS sem expor tráfego à Internet pública.
- **Dica**: Use para proteger comunicações entre VPCs e serviços no mesmo tenant.
- **Exemplo**: Acessar endpoints de APIs privadas no AWS Lambda.

### AWS ClassicLink
- **Descrição**: Conecta instâncias no EC2-Classic a VPCs.
- **Dica**: Útil para contas antigas que ainda usam EC2-Classic (não recomendado para novos designs).
- **Exemplo**: Migrar aplicações legadas de EC2-Classic para VPCs.

### AWS WAF
- **Descrição**: Firewall de aplicação web que protege contra ataques como SQL Injection.
- **Dica**: Configure regras customizadas para bloquear padrões de tráfego malicioso.
- **Exemplo**: Proteger APIs hospedadas em API Gateway contra ataques de bots.

### AWS WAF ACL
- **Descrição**: Lista de controle de acesso associada a AWS WAF para gerenciar tráfego.
- **Dica**: Combine ACLs com IP sets para gerenciar acesso de forma dinâmica.
- **Exemplo**: Criar uma ACL para bloquear acessos por IP suspeitos.

### AWS Network Firewall
- **Descrição**: Firewall gerenciado para proteger redes VPC.
- **Dica**: Use em redes complexas com tráfego entre várias VPCs.
- **Exemplo**: Implementar políticas de inspeção profunda de pacotes (DPI).

### AWS VPN CloudHub
- **Descrição**: Conecta vários sites remotos usando VPN em um hub-and-spoke.
- **Dica**: Ideal para conexões híbridas com baixa latência.
- **Exemplo**: Conectar escritórios regionais a uma infraestrutura central na AWS.

### AWS Route 53 e Failover
- **Descrição**: Serviço de DNS gerenciado com suporte a failover.
- **Dica**: Configure registros de failover para alta disponibilidade de aplicações.
- **Exemplo**: Redirecionar tráfego para uma região de backup durante falhas.

### AWS CloudFront
- **Descrição**: Rede de entrega de conteúdo (CDN) para baixa latência e alta performance.
- **Dica**: Use com S3 para distribuir conteúdos estáticos globalmente.
- **Exemplo**: Entregar vídeos de um site para usuários ao redor do mundo.

### AWS Global Accelerator
- **Descrição**: Melhora a performance de tráfego para aplicativos globais.
- **Dica**: Ideal para aplicações que exigem baixa latência em várias regiões.
- **Exemplo**: Reduzir a latência de um aplicativo SaaS global.

---

## Armazenamento e Migração

### Amazon EBS
- **Descrição**: Armazenamento em blocos para EC2 com alta performance.
- **Dica**: Utilize volumes otimizados para IOPS em bancos de dados.
- **Exemplo**: Configurar volumes GP3 para MySQL no EC2.

### Amazon EFS
- **Descrição**: Sistema de arquivos elástico, compartilhado e gerenciado para múltiplas instâncias.
- **Dica**: Use para compartilhar arquivos entre serviços como ECS ou Lambda.
- **Exemplo**: Armazenar arquivos temporários de um aplicativo web em múltiplos servidores.

### AWS S3 Transfer Acceleration
- **Descrição**: Acelera uploads para o S3 usando pontos de presença globais.
- **Dica**: Útil para uploads de regiões distantes da AWS.
- **Exemplo**: Transferir grandes arquivos de mídia de clientes globais para o S3.

### AWS Snowball
- **Descrição**: Dispositivo físico para transferir grandes volumes de dados.
- **Dica**: Use para migrações massivas quando o upload via rede não for viável.
- **Exemplo**: Transferir 100 TB de dados locais para o S3.

### AWS Snowcone
- **Descrição**: Dispositivo portátil para transferir ou processar dados.
- **Dica**: Ideal para locais remotos com conectividade limitada.
- **Exemplo**: Coletar dados de sensores em ambientes industriais.

### AWS DataSync
- **Descrição**: Automatiza transferências rápidas de dados para a AWS.
- **Dica**: Use para sincronizar sistemas de arquivos locais com S3 ou EFS.
- **Exemplo**: Migrar backups diários de um NAS local para o S3.

### AWS Storage Gateway
- **Descrição**: Integra armazenamento local com a nuvem AWS.
- **Dica**: Ideal para backup e arquivamento em S3.
- **Exemplo**: Configurar um gateway para armazenar snapshots locais no S3.

### AWS File Gateway Virtual
- **Descrição**: Serviço do AWS Storage Gateway para arquivos.
- **Dica**: Use para acessar objetos S3 como arquivos NFS.
- **Exemplo**: Compartilhar arquivos armazenados no S3 em um ambiente on-premises.

---

## Big Data e Streaming

### AWS Kinesis Data Stream
- **Descrição**: Processamento de grandes volumes de dados em tempo real.
- **Dica**: Particione os streams para alta escalabilidade.
- **Exemplo**: Coletar logs de aplicações para análise em tempo real.

### AWS Kinesis Data Firehose
- **Descrição**: Carrega streams diretamente em serviços de armazenamento ou analytics.
- **Dica**: Configure transformações em tempo real com AWS Lambda.
- **Exemplo**: Enviar logs de acesso do CloudFront para um bucket S3.

### AWS RedShift
- **Descrição**: Data warehouse gerenciado para análises em grande escala.
- **Dica**: Utilize compressores de coluna para otimizar consultas.
- **Exemplo**: Analisar dados históricos de vendas.

---

## Banco de Dados

### AWS RDS Proxy
- **Descrição**: Proxy gerenciado para bancos de dados RDS.
- **Dica**: Melhora a escalabilidade de conexões para aplicações sem alteração no código.
- **Exemplo**: Reduzir latência em aplicações com alto número de conexões ao MySQL.

### AWS DynamoDB Streams
- **Descrição**: Permite capturar alterações de dados no DynamoDB.
- **Dica**: Use com AWS Lambda para processar eventos em tempo real.
- **Exemplo**: Atualizar índices de busca ao inserir itens no DynamoDB.

### AWS Database Migration Service (DMS)
- **Descrição**: Migra bancos de dados para a AWS com interrupção mínima.
- **Dica**: Combine com schema conversion tool para migrações heterogêneas.
- **Exemplo**: Migrar um banco Oracle on-premise para o Aurora PostgreSQL.

---

## Gerenciamento e Automação

### AWS Trusted Advisor
- **Descrição**: Fornece recomendações para otimizar segurança, custo e performance.
- **Dica**: Verifique regularmente para evitar despesas desnecessárias.
- **Exemplo**: Identificar instâncias EC2 não utilizadas.

### AWS Systems Manager Patch Manager
- **Descrição**: Automatiza o gerenciamento de patches em instâncias.
- **Dica**: Configure janelas de manutenção para aplicar patches em horários específicos.
- **Exemplo**: Manter instâncias EC2 atualizadas com os patches mais recentes.

### AWS AppFlow
- **Descrição**: Serviço de integração de dados com outras aplicações SaaS.
- **Dica**: Use para sincronizar dados entre Salesforce e S3.
- **Exemplo**: Transferir leads do Salesforce para análise em Redshift.

---

# Dicas e Exemplos de Uso - AWS Networking, Armazenamento e Segurança

### Virtual Private Gateway (VPG)
- **Descrição**: Componente do AWS Site-to-Site VPN que conecta redes on-premises a uma VPC.
- **Dica**: Use para configurar VPNs redundantes em conjunto com Direct Connect para maior confiabilidade.
- **Exemplo**: Conectar uma rede corporativa a uma VPC para acesso seguro aos serviços na nuvem.

### Volume Gateway do AWS Storage Gateway
- **Descrição**: Integra armazenamento local com volumes de disco virtual no S3.
- **Dica**: Use como extensão de armazenamento para backups de aplicações locais.
- **Exemplo**: Armazenar snapshots de volumes locais no S3 para recuperação de desastres.

### VPC Endpoint
- **Descrição**: Permite conexões privadas de uma VPC a serviços AWS sem usar a Internet pública.
- **Dica**: Use endpoints privados para acessar S3 ou DynamoDB, evitando tráfego externo.
- **Exemplo**: Configurar um endpoint para acessar buckets S3 em uma VPC com políticas restritas.

### VPN IPSec
- **Descrição**: Protocolo usado para criar conexões seguras entre redes.
- **Dica**: Use como fallback para Direct Connect ou para conexões híbridas temporárias.
- **Exemplo**: Configurar uma VPN IPSec para conectar uma filial remota à AWS.

### Volume Gateway
- **Descrição**: Armazena backups locais no S3, permitindo cache local de dados frequentemente acessados.
- **Dica**: Combine com AWS Backup para maior automação e controle.
- **Exemplo**: Usar o Volume Gateway para replicar volumes de servidores locais para recuperação de dados.

### Virtual Interfaces (VIFs)
- **Descrição**: Interface virtual associada ao AWS Direct Connect.
- **Dica**: Configure VIFs públicas para acessar serviços AWS ou privadas para acessar VPCs.
- **Exemplo**: Configurar uma VIF privada para conectar um ambiente on-premises à VPC.

### S3 URL Pré-assinado
- **Descrição**: URL gerada para acesso temporário a objetos no S3.
- **Dica**: Configure TTLs curtos para maior segurança ao compartilhar dados sensíveis.
- **Exemplo**: Enviar links temporários de download para clientes após uma transação.

### AWS SSE-S3 (Server-Side Encryption)
- **Descrição**: Protocolo de criptografia gerenciado pelo S3.
- **Dica**: Ative a criptografia padrão para todos os novos uploads em buckets S3.
- **Exemplo**: Armazenar relatórios de conformidade criptografados no S3 para atender a regulamentos.

### NFS (Network File System)
- **Descrição**: Sistema de arquivos distribuído para compartilhamento de dados.
- **Dica**: Use com Amazon EFS para compartilhar arquivos entre múltiplas instâncias EC2.
- **Exemplo**: Configurar EFS para armazenar logs de um cluster de servidores.

### Protocolo iSCSI
- **Descrição**: Protocolo de comunicação para acesso a dispositivos de armazenamento remoto.
- **Dica**: Use com Volume Gateway para acessar volumes no S3 como discos locais.
- **Exemplo**: Criar um disco virtual iSCSI em um servidor local para backup contínuo no S3.

### Protocolo iSCSI (VTL)
- **Descrição**: Interface para bibliotecas de fita virtual (Virtual Tape Library).
- **Dica**: Ideal para substituir fitas físicas em backups tradicionais.
- **Exemplo**: Migrar backups de fita física para S3 Glacier via VTL.

### Protocolo NFS
- **Descrição**: Protocolo de compartilhamento de arquivos entre servidores locais e soluções na nuvem.
- **Dica**: Use com AWS Storage Gateway para acessar buckets S3 como sistemas de arquivos locais.
- **Exemplo**: Montar S3 como um volume de leitura/escrita para um sistema de arquivos local.

### Elastic Fabric Adapter (EFA)
- **Descrição**: Interface de rede especializada para aplicações de alta performance (HPC).
- **Dica**: Configure EFAs em clusters de computação para workloads de baixa latência.
- **Exemplo**: Executar simulações científicas em instâncias EC2 com alta conectividade.

### Elastic Network Interface (ENI)
- **Descrição**: Interface de rede virtual atribuída a instâncias EC2.
- **Dica**: Use ENIs secundárias para segmentar o tráfego de rede em instâncias.
- **Exemplo**: Configurar ENIs em uma instância para gerenciar sub-redes distintas.

### Elastic Network Adapter (ENA)
- **Descrição**: Interface de rede de alta performance para instâncias EC2.
- **Dica**: Escolha instâncias EC2 com suporte a ENA para requisitos de alta largura de banda.
- **Exemplo**: Implementar ENA em um ambiente de análise de big data para otimizar a transferência de dados.

# Comparações e Casos de Uso

## CloudFront vs Route 53

### Roteamento de Geoproximidade
- **CloudFront**:
  - **Descrição**: Usa a rede de pontos de presença (POPs) da AWS para entregar conteúdo a usuários no menor tempo possível.
  - **Caso de Uso**: Ideal para distribuição de conteúdo estático/dinâmico, como vídeos ou páginas web, com baixa latência.
  - **Exemplo**: Um site de streaming entrega vídeos de um POP próximo ao usuário.

- **Route 53**:
  - **Descrição**: Direciona usuários ao endpoint mais próximo com base na menor latência percebida.
  - **Caso de Uso**: Gerencia DNS e encaminha tráfego para a região mais próxima (usando políticas de geoproximidade).
  - **Exemplo**: Um usuário da Europa acessa um servidor europeu para um SaaS hospedado em múltiplas regiões.

---

### Roteamento de Geolocalização
- **CloudFront**:
  - **Descrição**: Usa regras baseadas na localização do cliente para aplicar comportamentos específicos (por exemplo, bloquear acessos ou direcionar para diferentes versões de conteúdo).
  - **Caso de Uso**: Oferecer conteúdo personalizado ou filtrar acessos baseados em país.
  - **Exemplo**: Bloquear acesso de usuários fora dos EUA a conteúdo restrito por questões legais.

- **Route 53**:
  - **Descrição**: Direciona tráfego DNS baseado na localização geográfica do cliente.
  - **Caso de Uso**: Redirecionar usuários para servidores regionais ou oferecer diferentes websites baseados na origem do tráfego.
  - **Exemplo**: Usuários na América Latina são redirecionados para um site traduzido em espanhol.

---

## Application Load Balancer (ALB) vs Network Load Balancer (NLB)

### ALB
- **Descrição**: Load balancer de camada 7 (HTTP/HTTPS) que distribui tráfego com base em conteúdo de aplicação.
- **Caso de Uso**: Ideal para aplicações web e APIs que requerem roteamento baseado em URLs, cabeçalhos ou cookies.
- **Exemplo**: Um ALB roteia tráfego `/api` para um grupo de instâncias e `/app` para outro.

### NLB
- **Descrição**: Load balancer de camada 4 (TCP/UDP) para tráfego de baixa latência e alto throughput.
- **Caso de Uso**: Usado para conexões de rede rápidas ou serviços que não dependem de regras complexas, como bancos de dados ou VPNs.
- **Exemplo**: Um NLB gerencia conexões TCP para um servidor de banco de dados de alta performance.

---

## EFS vs EBS

### Amazon EFS (Elastic File System)
- **Descrição**: Sistema de arquivos gerenciado que permite múltiplos acessos simultâneos.
- **Caso de Uso**: Compartilhamento de arquivos entre várias instâncias EC2.
- **Exemplo**: Uma aplicação distribuída precisa acessar arquivos de configuração em um sistema centralizado.

### Amazon EBS (Elastic Block Store)
- **Descrição**: Armazenamento em blocos de alto desempenho associado a uma única instância EC2.
- **Caso de Uso**: Ideal para bancos de dados ou aplicações que necessitam de armazenamento dedicado com baixa latência.
- **Exemplo**: Uma instância EC2 com MySQL utiliza um volume EBS otimizado para IOPS.

---

## Lambda vs Lambda@Edge

### Lambda
- **Descrição**: Serviço de computação serverless que executa código em resposta a eventos (nível regional).
- **Caso de Uso**: Automação de tarefas backend, processamento de dados, APIs sem servidor.
- **Exemplo**: Processar uploads de imagens no S3.

### Lambda@Edge
- **Descrição**: Extensão do Lambda para execução em pontos de presença do CloudFront (nível global).
- **Caso de Uso**: Personalizar ou otimizar respostas a partir do CloudFront, como compressão de dados ou personalização baseada em localização.
- **Exemplo**: Personalizar o conteúdo de uma página com base no cabeçalho de localização do cliente.

# AWS - Tipos de Instâncias, Armazenamento S3 e Volumes EBS

## Tipos de Instâncias EC2

### Instâncias Sob Demanda
- **Descrição**: Pagamento por hora ou segundo, sem compromissos de longo prazo.
- **Dica**: Ideal para workloads imprevisíveis ou testes.
- **Exemplo**: Hospedar um site que precisa de capacidade adicional durante eventos específicos.

### Reservas de Capacidade Sob Demanda
- **Descrição**: Garante capacidade disponível em zonas de disponibilidade específicas.
- **Dica**: Útil para workloads críticas em regiões específicas que requerem alta disponibilidade.
- **Exemplo**: Garantir instâncias EC2 para processamento de dados em horários de pico.

### Instâncias Reservadas Regionais
- **Descrição**: Compromisso de longo prazo para EC2 em troca de descontos significativos.
- **Dica**: Use para aplicações estáveis e previsíveis.
- **Exemplo**: Executar um banco de dados que precisa de recursos constantes por 1-3 anos.

### Savings Plans
- **Descrição**: Modelos de desconto flexíveis que oferecem preços reduzidos para EC2, Lambda ou Fargate.
- **Dica**: Ideal para workloads previsíveis que variam entre tipos de instâncias ou regiões.
- **Exemplo**: Reduzir custos em um ambiente que usa EC2 para desenvolvimento e produção.

---

## Tipos de Armazenamento S3

### S3 Standard
- **Descrição**: Armazenamento para dados de acesso frequente.
- **Dica**: Use para dados críticos que requerem baixa latência e alta durabilidade.
- **Exemplo**: Hospedar imagens e vídeos acessados regularmente por um site.

### S3 One Zone-Infrequent Access (S3 One Zone-IA)
- **Descrição**: Armazenamento de baixo custo para dados raramente acessados em uma única zona.
- **Dica**: Use para backups que podem ser recriados em caso de falha na zona.
- **Exemplo**: Backups de logs para retenção a curto prazo.

### S3 Glacier
- **Descrição**: Armazenamento para arquivamento de longo prazo com custos reduzidos.
- **Dica**: Use para dados que precisam ser acessados esporadicamente.
- **Exemplo**: Arquivos financeiros antigos mantidos para conformidade regulatória.

### S3 Intelligent-Tiering
- **Descrição**: Alterna automaticamente entre camadas de custo com base nos padrões de acesso.
- **Dica**: Ideal para dados com padrões de acesso imprevisíveis.
- **Exemplo**: Armazenar dados de IoT que podem ser acessados irregularmente.

### S3 Standard-Infrequent Access (S3 Standard-IA)
- **Descrição**: Armazenamento para dados raramente acessados, mas com alta disponibilidade.
- **Dica**: Use para dados que precisam de acesso rápido, mas esporádico.
- **Exemplo**: Documentos de referência para uma aplicação corporativa.

---

## Tipos de Volumes EBS

### Amazon EBS General Purpose SSD (gp3/gp2)
- **Descrição**: Volumes SSD de propósito geral com bom equilíbrio entre custo e performance.
- **Dica**: Use gp3 para workloads de IOPS moderada com maior flexibilidade de custo.
- **Exemplo**: Hospedar um banco de dados MySQL em uma instância EC2.

### Amazon EBS Cold HDD (sc1)
- **Descrição**: Volumes de HDD com menor custo para dados acessados raramente.
- **Dica**: Use para grandes volumes de dados que não requerem alta performance.
- **Exemplo**: Armazenar backups de logs ou arquivos de mídia antigos.

---

## Tipos de Instâncias EC2

### T3/T4
- **Descrição**: Instâncias otimizadas para custo com capacidade de burst (explosão temporária de desempenho).
- **Dica**: Use para aplicações que têm cargas variáveis e não demandam alta performance contínua.
- **Exemplo**: Hospedar aplicações de desenvolvimento e servidores web de baixa utilização.

### C7
- **Descrição**: Instâncias otimizadas para computação com processadores de última geração.
- **Dica**: Ideal para aplicações que exigem alto desempenho de CPU, como análises financeiras ou simulações.
- **Exemplo**: Executar processamento de imagem ou análise de dados intensiva.

### R7
- **Descrição**: Instâncias otimizadas para memória, projetadas para workloads que consomem muita RAM.
- **Dica**: Use para bancos de dados em memória e caches.
- **Exemplo**: Hospedar bancos de dados Redis ou Apache Spark para big data.

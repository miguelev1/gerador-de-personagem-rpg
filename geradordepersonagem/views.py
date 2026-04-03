import random
from django.shortcuts import render
from django.http import JsonResponse

# ============================================================
#  DATABASE COMPLETA
# ============================================================

abridores_cheiro = [
    "O personagem exala um odor de",
    "É possível notar um aroma persistente de",
    "O ar ao redor dele carrega um cheiro de",
    "Há uma fragrância sutil de",
    "Um cheiro marcante de",
]

descricoes_cheiro = {
    "Couro":   "couro curtido, suor e o toque rústico de peles tratadas.",
    "Papel":   "pergaminho antigo, mofo e o aroma seco de tinta envelhecida.",
    "Vinho":   "vinho barato, tabaco forte e o azedo de bebidas fermentadas.",
    "Ferro":   "ferro frio, óleo de manutenção e o odor metálico de fricção.",
    "Terra":   "terra fresca, umidade profunda e o cheiro de raízes arrancadas.",
    "Sangue":  "sangue metálico, denso e levemente adocicado pelo tempo.",
    "Ervas":   "ervas amargas, plantas esmagadas e um frescor medicinal.",
    "Enxofre": "enxofre acre, fumaça persistente e um ar que pinica as narinas.",
}

abridores_marcas = [
    "É possível notar, em uma área visível,",
    "Uma marca distinta cruza",
    "Sua pele exibe",
    "Há o rastro de",
    "Nota-se claramente",
]

marcas_pele = {
    "Cicatriz Linear":     "uma linha fina e pálida de tecido endurecido.",
    "Cicatriz de Batalha": "uma marca irregular, profunda e com bordas serrilhadas.",
    "Queimadura":          "uma mancha de pele brilhante, repuxada e de tom avermelhado.",
    "Tatuagem Desbotada":  "pigmentos escuros e falhos, cujas formas se perderam no tempo.",
    "Sinais de Nascença":  "pequenas manchas irregulares e escuras espalhadas de forma única.",
    "Escarificação":       "padrões geométricos em alto-relevo, esculpidos deliberadamente na pele.",
    "Marcas de Castigo":   "linhas paralelas e esbranquiçadas que indicam chicotadas antigas.",
    "Pústulas/Varíola":    "pequenas marcas circulares e cavidades que dão uma textura áspera à pele.",
    "Mancha de Vinho":     "uma grande mancha de nascença arroxeada que cobre uma área extensa.",
}

abridores_voz = [
    "Sua fala é marcada por um tom",
    "O personagem possui uma voz",
    "Ao falar, emite um som",
    "Sua dicção revela um aspecto",
]

database_vozes = {
    "Grave":       "profundo e ressonante, como o eco em uma caverna vazia.",
    "Rouca":       "quebrado e áspero, lembrando o som de pedras se chocando.",
    "Sussurrante": "baixo e sibilante, quase como um segredo constante.",
    "Melódica":    "suave e rítmica, com uma cadência que prende a atenção.",
    "Estridente":  "agudo e cortante, capaz de se sobrepor a outros ruídos.",
    "Monótona":    "frio e desprovido de emoção, sem oscilações de tom.",
    "Autoritária": "firme e projetado, carregando um peso natural de comando.",
    "Tremulante":  "incerto e vacilante, como se estivesse sempre sob pressão.",
    "Aveludada":   "macio e profundo, transmitindo uma calma quase artificial.",
}

detalhes_extras_fala = [
    "acompanhado de pausas longas entre as palavras.",
    "com um sotaque carregado de terras distantes.",
    "interrompido por uma tosse seca e persistente.",
    "que termina cada frase com uma leve interrogação.",
    "carregado de um sarcasmo difícil de ocultar.",
]

expressoes = {
    "Fria/Distante":     "Olhar vago, como se estivesse analisando números em vez de pessoas.",
    "Séria/Solene":      "Um rosto que raramente relaxa, transmitindo responsabilidade ou luto.",
    "Inexpressiva":      "Impossível de ler; os músculos faciais parecem estáticos.",
    "Melancólica":       "Um olhar de quem carrega um peso constante ou uma tristeza antiga.",
    "Arrogante":         "Queixo levemente erguido, olhando os outros de cima para baixo.",
    "Sarcástica/Cínica": "Um leve repuxar no canto da boca, como se tudo fosse uma piada interna.",
    "Ameaçadora/Feroz":  "Sobrancelhas franzidas e olhos cerrados, sempre em estado de alerta.",
    "Desdenhosa":        "Nariz levemente franzido, como se sentisse um cheiro ruim no ambiente.",
    "Amigável/Calorosa": "Rugas suaves nos cantos dos olhos que transmitem sinceridade.",
    "Curiosa/Atenta":    "Olhos bem abertos e cabeça levemente inclinada, demonstrando interesse.",
    "Serena/Tranquila":  "Transmite paz, como se nada pudesse abalar o personagem.",
    "Radiante":          "Um sorriso que parece estar sempre prestes a aparecer.",
}

sexos = ["Masculino"] * 48 + ["Feminino"] * 48 + ["Intersexo"] * 4

origens = [
    "Criado sob o teto de palha de um vilarejo pacato no reino de",
    "Oriundo das ruas movimentadas e becos de uma metrópole em",
    "Sobrevivente das terras ermas e esquecidas nas fronteiras de",
    "Nascido em uma modesta aldeia camponesa nos domínios de",
    "Fruto do caos urbano e da nobreza das grandes cidades de",
]

reinos = [
    ("Aetelgardia",    "Reino agrícola próspero com cidades bem planejadas."),
    ("Aethelos",       "Conhecida por aproveitar energia geotérmica."),
    ("Aurenia",        "Reino rico, conhecido por cidades douradas e irrigação avançada."),
    ("Auralis",        "Forte defensivo contra o frio extremo."),
    ("Azaerlia",       "Sociedade militarizada que protege oásis estratégicos."),
    ("Basaltia",       "Arquitetura feita de pedra vulcânica."),
    ("Boreal de Prata","Clima atípico, com fenômenos luminosos no céu."),
    ("Bravora",        "Principal produtor de alimentos."),
    ("Brazes",         "Clã guerreiro com cultura rígida e expansionista."),
    ("Bruma-Real",     "Envolta em mistério e possíveis propriedades mágicas."),
    ("Brumaris",       "Conhecido por sua constante neblina e navegação furtiva."),
    ("Calitaria",      "Reino de mercadores de areia, domina rotas caravaneiras."),
    ("Centregolia",    "Reino montanhoso, resistente e isolado."),
    ("Cinza Eterna",   "Coberto por cinzas, ambiente hostil e misterioso."),
    ("Ciliatea",       "Florestas frias, densas e biodiversidade única."),
    ("Crysalon",       "Ponto estratégico entre regiões."),
    ("Gravaleinia",    "Região instável, com fenômenos naturais incomuns."),
    ("Gravelyna",      "Florestas frias, densas e selvagem."),
    ("Indralai",       "Forte tradição espiritual ligada à natureza e criaturas da selva."),
    ("Iot",            "Isolado e misterioso, quase inacessível."),
    ("Jinmaer",        "Região rica em recursos naturais e minérios."),
    ("Jinmork",        "Território fronteiriço, constantemente em conflito."),
    ("Kalai",          "Conhecido por suas cavernas e riquezas escondidas."),
    ("Kalindre",       "Civilização subterrânea altamente desenvolvida."),
    ("Karele",         "Grande produtor agrícola, base alimentar."),
    ("Karaere",        "Rival direto de Karele; disputa por terras férteis."),
    ("Kyomir",         "Conhecido por seus cavaleiros e domínio em combate montado."),
    ("Laminia",        "Forte crescimento urbano e expansão territorial."),
    ("Lanionia",       "Extração mineral intensa e cidades próximas a vulcões."),
    ("Magnamia",       "Potência naval dominante e expansionista."),
    ("Malakiel",       "Centro logístico com rotas comerciais organizadas."),
    ("Malandrir",      "Zona de transição climática e cultural."),
    ("Matramia",       "Rival direta, com estratégia focada em comércio e espionagem."),
    ("Materinia",      "Região rica em cristais e minerais raros."),
    ("Mayori",         "Região elevada com importância militar."),
    ("Montrali",       "Centro comercial vibrante, porta de entrada estratégica."),
    ("Musgária",       "Habitantes adaptados ao pântano e baixa luminosidade."),
    ("Naal'tora",      "Domínio de florestas boreais densas."),
    ("Navarion",       "Potência comercial com grande porto."),
    ("Nevoris",        "Reino naval avançado, domina rotas marítimas."),
    ("Osal",           "Região isolada, com tradições antigas preservadas."),
    ("Paraka",         "Porto estratégico, elo com outros continentes."),
    ("Pelagornia",     "Reino insular estratégico no norte."),
    ("Pico de Ferro",  "Centro metalúrgico e produção de armamentos."),
    ("Ruptal",         "Região instável com atividade geológica intensa."),
    ("Sakabe",         "Centro cultural e filosófico."),
    ("Saprovia",       "Vida centrada em lagos e pesca."),
    ("Savahrilia",     "Cultura espiritual ligada ao deserto; templos esculpidos em rochas."),
    ("Seonril",        "Potência dominante com forte tradição militar."),
    ("Sinaal",         "Portal comercial com mistura cultural intensa."),
    ("Siraal",         "Sociedade adaptada ao calor extremo, mestres na sobrevivência."),
    ("Tariel",         "Cultura pacífica, mas altamente estratégica nas alianças."),
    ("Toreo",          "Região industrial e de produção de armas."),
    ("Umbrelis",       "Região sombria com neblinas constantes e fauna perigosa."),
    ("Valerial",       "Potência costeira, exporta recursos raros da floresta."),
    ("Veel'tora",      "Voltado à extração de recursos em florestas frias."),
    ("Vinteralia",     "Cultura resiliente, focada em sobrevivência."),
    ("Vornakai",       "Reino isolado, com cidades escondidas sob copas gigantes."),
    ("Yaguara",        "Cultura tribal com ligação espiritual com animais."),
    ("Zionis",         "Sociedade disciplinada e organizada."),
]

racas_db = {
    "Humano":             {"descricao": "Feições diversificadas e pele que reflete o clima do reino de origem.", "bonus": "+1 em um atributo à escolha", "alturas": ["Baixo", "Médio", "Alto"], "peles": ["Pálido", "Bronzeado", "Oliva", "Retinto"]},
    "Elfo":               {"descricao": "Silhueta esguia, orelhas pontiagudas e movimentos graciosos.", "bonus": "+2 DESTREZA", "alturas": ["Médio", "Alto"], "peles": ["Pálido", "Alvo", "Bronzeado suave", "Azul Pastel", "Verde Pastel"]},
    "Anão":               {"descricao": "Baixo e largo, com ossatura densa e expressão firme.", "bonus": "+2 CONSTITUIÇÃO", "alturas": ["Muito Baixo", "Baixo"], "peles": ["Bronzeado pelo sol", "Cinza-pedra", "Pardo"]},
    "Meio-Orc":           {"descricao": "Porte imponente, mandíbula proeminente e musculatura rígida.", "bonus": "+2 FORÇA", "alturas": ["Alto", "Muito Alto"], "peles": ["Verde musgo", "Cinza-azulado", "Marrom terroso"]},
    "Gnomo":              {"descricao": "Pequena estatura, olhos curiosos e mãos inquietas.", "bonus": "+2 INTELIGÊNCIA", "alturas": ["Muito Baixo"], "peles": ["Pálido rosado", "Bronzeado vivo", "Creme"]},
    "Meio-Elfo":          {"descricao": "Traços equilibrados entre humano e elfo.", "bonus": "+1 CARISMA e +1 DESTREZA", "alturas": ["Médio", "Alto"], "peles": ["Pálido", "Bronzeado claro", "Oliva suave"]},
    "Elfo Sombrio (Drow)":{"descricao": "Pele de tons escuros e aparência inquietante.", "bonus": "+1 DESTREZA e +1 INTELIGÊNCIA", "alturas": ["Médio", "Alto"], "peles": ["Ébano", "Cinza-escuro", "Roxo-azulado profundo"]},
    "Halfling":           {"descricao": "Rostos amigáveis e aparência inofensiva.", "bonus": "+1 DESTREZA e +1 CARISMA", "alturas": ["Muito Baixo"], "peles": ["Bronzeado", "Pardo"]},
    "Draconato":          {"descricao": "Corpo humanoide coberto por escamas e traços dracônicos.", "bonus": "+1 FORÇA e +1 CARISMA", "alturas": ["Alto", "Muito Alto"], "peles": ["Vermelho fosco", "Azul metálico", "Verde escuro", "Dourado envelhecido", "Preto"]},
    "Tiefling":           {"descricao": "Chifres proeminentes, olhos de cores sólidas e traços demoníacos.", "bonus": "+1 CARISMA e +1 INTELIGÊNCIA", "alturas": ["Médio", "Alto"], "peles": ["Vermelho carmesim", "Roxo", "Azul escuro", "Pálido cadavérico"]},
    "Aasimar":            {"descricao": "Aparência angelical, com brilho suave e presença serena.", "bonus": "+1 SABEDORIA e +1 CARISMA", "alturas": ["Médio", "Alto"], "peles": ["Alvo radiante", "Dourado pálido", "Bege impecável"]},
    "Licantropo":         {"descricao": "Mistura de humano com besta na forma híbrida.", "bonus": "+1 FORÇA e +1 CONSTITUIÇÃO", "alturas": ["Alto", "Muito Alto"], "peles": ["Marrom acinzentado", "Preto", "Cinza", "Malhado"]},
    "Feral (Beastfolk)":  {"descricao": "Humanoides com traços animais (felinos, caninos).", "bonus": "+1 DESTREZA e +1 FORÇA", "alturas": ["Baixo", "Médio", "Alto"], "peles": ["Laranja listrado", "Cinza", "Areia", "Malhado"]},
    "Insetoide":          {"descricao": "Exoesqueleto rígido e membros segmentados.", "bonus": "+1 DESTREZA e +1 CONSTITUIÇÃO", "alturas": ["Médio", "Alto"], "peles": ["Preto brilhante", "Verde oliva", "Marrom casca", "Amarelo vespa"]},
    "Autômato":           {"descricao": "Corpo mecânico com engrenagens ou runas.", "bonus": "+1 CONSTITUIÇÃO e +1 INTELIGÊNCIA", "alturas": ["Médio", "Alto", "Muito Alto"], "peles": ["Ferro oxidado", "Bronze polido", "Aço fosco", "Madeira reforçada"]},
    "Musgomita":          {"descricao": "Corpo simbiótico onde o musgo é vivo.", "bonus": "+1 SABEDORIA e +1 CONSTITUIÇÃO", "alturas": ["Baixo", "Médio"], "peles": ["Verde musgo", "Marrom úmido", "Líquen acinzentado"]},
}

classes_db = {
    "Mago":     [("Tecelão","INT + SAB","Manipulação temporal, teletransporte tático e controle de gravidade."),("Evocador Elemental","INT","Dano em área preciso, versatilidade elemental e destruição de barreiras."),("Beligerante Arcano","INT + FOR/DES","Buffs de combate pessoal, armas encantadas e durabilidade mágica."),("Necromante","INT + CON","Invocação de horda, debuffs de definhamento e drenagem de vida."),("Invocador","INT + CAR","Invocação de Pet de Elite, pactos planares e magias de comando."),("Mentalista","INT + DES","Controle mental, invisibilidade/ilusões e alta evasão.")],
    "Ladino":   [("Gatuno","DES","Infiltração urbana, escalada e mobilidade extrema."),("Trapaceiro","DES + CAR","Furtividade, truques, ilusões leves e manipulação social."),("Assassino","DES + INT","Precisão cirúrgica, estudo anatômico e execução em um golpe."),("Duelista","DES + FOR","Esgrima, reflexos rápidos e combate direto ágil.")],
    "Feiticeiro":[("Feiticeiro das Sombras","CAR + DES","Furtividade mágica, manipulação de sombras e dano necrótico."),("Feiticeiro Elemental","CAR + CON","Dano em área massivo, resistência e explosões de curto alcance."),("Linhagem Divina","CAR + SAB","Suporte ofensivo, dano radiante e purificação de aliados.")],
    "Warlock":  [("Pacto do Abismo","CAR + CON","Dano de fogo/trevas, regeneração ao abater e magias de explosão."),("Pacto do Observador","CAR + SAB","Controle mental, percepção apurada e magias de suporte/comando."),("Pacto da Lâmina Maldita","CAR + FOR","Combate corpo a corpo mágico, maldições e dano escalado com CAR."),("Pacto do Tecelão do Caos","CAR + DES","Alta mobilidade, invisibilidade momentânea e ilusão/confusão.")],
    "Clérigo":  [("Taumaturgo de Sacrifício","SAB + CON","Cura por transferência de vida, tanque regenerativo."),("Inquisidor de Vidro","SAB + DES","Alta mobilidade, dano elétrico/sagrado e controle por paralisia."),("Arquiteto do Verbo","SAB + INT","Criação de zonas de bônus (glifos) e anulação de magias."),("Evangelista do Êxtase","SAB + CAR","Buffs de área (Auras), controle emocional e liderança.")],
    "Druida":   [("Guardião Primal","SAB + CON","Tanque puro, alta regeneração de vida e controle de ameaça."),("Predador Alfa","SAB + FOR","Combatente corpo a corpo agressivo e lifesteal."),("Geólogo","SAB + CON","Controle total de terreno e criação de barreiras físicas."),("Enxame","SAB + DES","Dano por tempo, alta evasão e debuffs de velocidade."),("Entrópico","SAB + CAR","Necrose botânica, controle de área com esporos.")],
    "Caçador":  [("Bruxo","DES + CAR","Magias rápidas, resistência a venenos e bônus vs monstros."),("Rastreador","DES + SAB","Companheiro animal, rastreio impecável e bônus em terrenos naturais."),("Especialista Tático","DES + SAB","Dano crítico à distância e controle de área com armadilhas."),("Caçador de Recompensas","DES + CON","Resistência à fadiga e mestre em técnicas de contenção.")],
    "Bárbaro":  [("Berserker","FOR + CON","Ataques extras, resistência massiva e bônus pela vida perdida."),("Guardião Totêmico","FOR + SAB","Buffs baseados em animais e utilidade fora de combate."),("Primal de Sangue","FOR + DES","Alta mobilidade, lifesteal e críticos devastadores."),("Flagelo dos Elementos","FOR + CON","Aura elemental, retaliação mágica e resistência a elementos.")],
    "Guerreiro":[("Guerreiro Arcano","FOR + INT","Combate híbrido, buffs pessoais e dano físico arcano."),("Guardião Inabalável","FOR + CON","Alta durabilidade, controle de área e proteção de aliados."),("Mestre de Armas","FOR + DES + SAB","Versatilidade de arsenal e adaptação ao combate."),("Comandante de Campo","FOR + CAR","Liderança ativa, buffs em equipe e controle tático.")],
    "Lutador":  [("Punho de Ferro","FOR + CON","Dano massivo por golpe e quebra de postura/armadura."),("Artista Marcial","DES + SAB","Alta esquiva, múltiplos ataques rápidos e contra-ataques."),("Subjugador","FOR + DES","Imobilização (grappling) e anulação de oponentes."),("Punho Espiritual","SAB + CON","Dano de energia, ataques de curto/médio alcance e autossuficiência.")],
    "Paladino": [("Juramento da Aniquilação","FOR + INT","Dano explosivo, análise de fraquezas e interrupção de habilidades."),("Juramento do Mártir","FOR + CON","Absorção massiva e fortalecimento através de ferimentos."),("Juramento do Domínio","FOR + CAR","Comandos táticos, buffs e debuffs de controle psicológico."),("Juramento da Claridade","FOR + SAB","Anti-ilusão, revelação de inimigos ocultos e cura de status.")],
    "Artífice": [("Mecanicista","INT + DES","Pets mecânicos, ataques coordenados e visão compartilhada."),("Alquimista Volátil","INT + CON","Poções, dano de estado (Ácido/Gás) e cura química."),("Engenheiro de Guerra","INT + CON","Tanque tecnológico e modificação de equipamentos em tempo real.")],
    "Bardo":    [("Virtuoso do Som","CAR + DES","Dano de som, controle de grupo e alta evasão rítmica."),("Arauto da Vitória","CAR + SAB","Buffs de área, remoção de medo e ações extras para aliados."),("Charlatão de Corte","CAR + INT","Debuffs psicológicos, ilusões e manipulação fora de combate."),("Menestrel das Sombras","CAR + DES","Furtividade sonora, dano necrótico e magias de sono/paralisia.")],
}

arquetipos = [
    "O Guardião Silencioso — Protege algo ou alguém sem buscar reconhecimento.",
    "O Explorador do Desconhecido — Vive para descobrir o que ninguém ousa investigar.",
    "O Justiceiro Solitário — Faz justiça com as próprias mãos, fora da lei.",
    "O Diplomata Frio — Resolve conflitos com palavras, mesmo sem empatia.",
    "O Ferreiro de Destinos — Molda armas ou artefatos com propósito quase sagrado.",
    "O Navegador Errante — Nunca permanece em um lugar; busca sentido na jornada.",
    "O Professor Desiludido — Ensina, mas já perdeu a fé no futuro dos alunos.",
    "O Contrabandista Carismático — Vive à margem, usando charme para sobreviver.",
    "O Caçador de Relíquias — Procura artefatos antigos por obsessão ou dever.",
    "O Soldado Abandonado — Foi deixado para trás por uma causa que já não existe.",
    "O Artista Visionário — Expressa verdades através de sua arte incompreendida.",
    "O Curador de Almas — Ajuda os outros emocionalmente, mesmo estando quebrado.",
    "O Espião Patriota — Serve a uma nação, mesmo quando ela não merece.",
    "O Juiz Errante — Viaja julgando crimes e aplicando sua própria lei.",
    "O Sobrevivente Urbano — Cresceu nas ruas e domina suas regras cruéis.",
    "O Inventor Obcecado — Cria soluções inovadoras, ignorando consequências.",
    "O Herdeiro Indesejado — Carrega um legado que nunca quis.",
    "O Mensageiro Condenado — Transporta informações que podem mudar o mundo.",
    "O Protetor de Monstros — Defende criaturas rejeitadas pela sociedade.",
    "O Cronista do Fim — Registra eventos como se tudo estivesse prestes a acabar.",
]

tracos_sombra = [
    "Desapego Frio — Não cria laços profundos para evitar sofrimento.",
    "Controle Excessivo — Precisa dominar cada situação.",
    "Ressentimento Oculto — Guarda mágoas por longos períodos.",
    "Impulsividade Perigosa — Age antes de pensar nas consequências.",
    "Orgulho Ferido — Não aceita falhas pessoais.",
    "Dependência de Validação — Precisa da aprovação alheia.",
    "Rigidez Moral — Incapaz de aceitar nuances éticas.",
    "Fuga da Realidade — Evita problemas em vez de enfrentá-los.",
    "Frieza Emocional — Dificuldade em demonstrar sentimentos.",
    "Obstinação Cega — Não desiste, mesmo quando deveria.",
    "Desconfiança Instintiva — Sempre espera traição.",
    "Ambição Desmedida — Nunca está satisfeito com o que tem.",
    "Insegurança Disfarçada — Compensa dúvidas com atitudes exageradas.",
    "Necessidade de Superioridade — Precisa se sentir melhor que os outros.",
    "Negação do Passado — Recusa-se a lidar com seus erros.",
    "Apego ao Sofrimento — Acredita que dor é necessária.",
    "Ceticismo Absoluto — Não acredita em nada além do que vê.",
    "Passividade Covarde — Evita agir em momentos críticos.",
    "Competitividade Tóxica — Precisa vencer, custe o que custar.",
    "Isolamento Voluntário — Se afasta mesmo quando precisa de ajuda.",
]

virtudes = [
    "Determinação Firme — Persiste diante de qualquer dificuldade.",
    "Compaixão Genuína — Se importa profundamente com os outros.",
    "Honra Pessoal — Segue um código próprio inquebrável.",
    "Paciência Estratégica — Sabe esperar o momento certo.",
    "Coragem Moral — Faz o certo mesmo sob pressão.",
    "Generosidade Espontânea — Ajuda sem pensar em retorno.",
    "Disciplina Consistente — Mantém foco e rotina mesmo no caos.",
    "Lealdade Seletiva — Protege quem considera digno.",
    "Humildade Consciente — Reconhece suas limitações.",
    "Resiliência Emocional — Se recupera rapidamente de traumas.",
    "Curiosidade Ativa — Busca aprender constantemente.",
    "Empatia Controlada — Entende os outros sem se perder neles.",
    "Pragmatismo Ético — Toma decisões úteis sem perder valores.",
    "Responsabilidade — Assume consequências de seus atos.",
    "Adaptabilidade — Se ajusta a qualquer situação.",
    "Esperança Realista — Acredita no futuro, mas com cautela.",
    "Autocontrole — Domina impulsos e emoções.",
    "Criatividade Funcional — Resolve problemas de forma eficiente.",
    "Senso de Justiça — Busca equilíbrio e equidade.",
    "Proteção Instintiva — Age rapidamente para defender outros.",
]

vicios = [
    "Teimosia — Recusa-se a mudar de opinião.",
    "Procrastinação — Adia decisões importantes.",
    "Apego a Rotina — Resiste a mudanças.",
    "Gosto por Luxo — Busca conforto excessivo.",
    "Impaciência — Se irrita com lentidão.",
    "Necessidade de Aprovação Social — Quer ser aceito por todos.",
    "Excesso de Trabalho — Não sabe parar.",
    "Fuga em Entretenimento — Evita problemas com distrações.",
    "Colecionismo Inútil — Junta coisas sem valor real.",
    "Comparação Constante — Mede seu valor pelos outros.",
    "Dependência de Rotina Ritualística — Precisa de hábitos específicos.",
    "Sarcasmo Excessivo — Usa ironia para tudo.",
    "Aversão a Autoridade — Resiste a qualquer comando.",
    "Apego ao Passado — Vive preso a memórias.",
    "Perfeccionismo Paralisante — Não age até tudo estar perfeito.",
    "Busca por Reconhecimento — Quer ser notado constantemente.",
    "Evitação de Conflito — Prefere não confrontar ninguém.",
    "Consumo Compulsivo — Compra ou usa coisas sem necessidade.",
    "Dependência de Conforto — Evita situações difíceis.",
    "Excesso de Planejamento — Planeja tanto que não age.",
]

# ============================================================
#  SISTEMA DE ATRIBUTOS
# ============================================================

NOMES_ATRIBUTOS = {
    "FOR": "Força", "DES": "Destreza", "CON": "Constituição",
    "INT": "Inteligência", "SAB": "Sabedoria", "CAR": "Carisma",
}
TODOS_ATRIBUTOS = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]


def _sortear_com_total(faixa_min, faixa_max, quantidade, total_alvo):
    total_alvo = max(total_alvo, faixa_min * quantidade)
    total_alvo = min(total_alvo, faixa_max * quantidade)
    if quantidade == 1:
        return [total_alvo]
    excedente    = total_alvo - faixa_min * quantidade
    espaco_total = faixa_max - faixa_min
    cortes = sorted(random.randint(0, excedente) for _ in range(quantidade - 1))
    partes = (
        [cortes[0]]
        + [cortes[i] - cortes[i - 1] for i in range(1, quantidade - 1)]
        + [excedente - cortes[-1]]
    )
    valores = []; sobra = 0
    for p in partes:
        v = faixa_min + min(p + sobra, espaco_total)
        sobra = max(0, (p + sobra) - espaco_total)
        valores.append(v)
    for i in range(len(valores) - 1, -1, -1):
        if sobra <= 0: break
        delta = min(sobra, faixa_max - valores[i])
        valores[i] += delta; sobra -= delta
    random.shuffle(valores)
    return valores


def extrair_primarios(atributos_str):
    primarios = []
    for parte in atributos_str.split("+"):
        token = parte.strip().split("/")[0].strip()
        if token in TODOS_ATRIBUTOS:
            primarios.append(token)
    return primarios


def gerar_atributos(atributos_str):
    TOTAL_PONTOS = 75
    MIN_CON_DES = 10  # Sua regra de garantir sobrevivência

    primarios = extrair_primarios(atributos_str)

    # 1. Definimos quem é o quê
    sec_pool = [a for a in TODOS_ATRIBUTOS if a not in primarios]
    # Se tiver 1 ou 2 primários, escolhemos 2 secundários. Se tiver 3 primários, 1 secundário.
    n_sec = 1 if len(primarios) >= 3 else 2
    secundarios = random.sample(sec_pool, n_sec)
    terciarios = [a for a in sec_pool if a not in secundarios]

    atribs = {a: 0 for a in TODOS_ATRIBUTOS}

    # 2. Definimos faixas rígidas para garantir a hierarquia
    # Primários: 16-20 | Secundários: 12-15 | Terciários: 5-11
    for a in primarios:
        atribs[a] = random.randint(16, 20)

    for a in secundarios:
        atribs[a] = random.randint(12, 15)

    for a in terciarios:
        atribs[a] = random.randint(5, 11)

    # 3. Aplicamos sua regra: CON e DES precisam de no mínimo 10
    for a in ["CON", "DES"]:
        if atribs[a] < MIN_CON_DES:
            atribs[a] = MIN_CON_DES

    # 4. Ajuste fino para bater exatamente 75 pontos sem quebrar a hierarquia
    atual = sum(atribs.values())
    tentativas = 0

    while atual != TOTAL_PONTOS and tentativas < 100:
        tentativas += 1
        diff = 1 if atual < TOTAL_PONTOS else -1

        # Escolhemos um atributo para alterar com base na necessidade
        alvo = random.choice(TODOS_ATRIBUTOS)
        novo_valor = atribs[alvo] + diff

        # Validações de segurança para não estourar os limites de RPG (3 a 20)
        # E para não deixar CON/DES abaixo de 10
        if 3 <= novo_valor <= 20:
            if alvo in ["CON", "DES"] and novo_valor < MIN_CON_DES:
                continue

            # Verificação de Hierarquia:
            # Primário não pode ser menor que Secundário, etc.
            if alvo in primarios and any(novo_valor < atribs[s] for s in secundarios):
                continue
            if alvo in secundarios and any(novo_valor > atribs[p] for p in primarios):
                continue
            if alvo in secundarios and any(novo_valor < atribs[t] for t in terciarios):
                continue

            atribs[alvo] = novo_valor
            atual = sum(atribs.values())

    return atribs, primarios
# ============================================================
#  GERADOR PRINCIPAL
# ============================================================

def gerar_personagem():
    # Raça
    raca_nome = random.choice(list(racas_db.keys()))
    raca      = racas_db[raca_nome]
    altura    = random.choice(raca["alturas"])
    pele      = random.choice(raca["peles"])

    # Sexo
    sexo = random.choice(sexos)

    # Origem
    frase_origem     = random.choice(origens)
    nome_reino, desc_reino = random.choice(reinos)
    origem_texto     = f"{frase_origem} {nome_reino}."

    # Classe
    classe_nome = random.choice(list(classes_db.keys()))
    sub_nome, atributos_str, identidade = random.choice(classes_db[classe_nome])

    # Atributos numéricos
    atribs, primarios = gerar_atributos(atributos_str)
    atributos_lista = [
        {
            "sigla": a,
            "nome":  NOMES_ATRIBUTOS[a],
            "valor": atribs[a],
            "primario": a in primarios,
        }
        for a in TODOS_ATRIBUTOS
    ]

    # Sensorial
    odor      = f"{random.choice(abridores_cheiro)} {random.choice(list(descricoes_cheiro.values()))}"
    base_voz  = random.choice(list(database_vozes.values()))
    voz       = f"{random.choice(abridores_voz)} {base_voz}"
    if random.random() < 0.20:
        voz += f" {random.choice(detalhes_extras_fala)}"
    exp_chave   = random.choice(list(expressoes.keys()))
    expressao   = f"{exp_chave}: {expressoes[exp_chave]}"

    chance = random.random()
    if chance < 0.50:
        marca = "Pele limpa, sem marcas visíveis de distinção."
    elif chance < 0.90:
        marca = f"{random.choice(abridores_marcas)} {random.choice(list(marcas_pele.values()))}"
    else:
        dois  = random.sample(list(marcas_pele.values()), 2)
        a1, a2 = random.choice(abridores_marcas), random.choice(abridores_marcas).lower()
        marca = f"O corpo carrega histórias duplas: {a1} {dois[0]} Além disso, {a2} {dois[1]}"

    # Personalidade
    arquetipo    = random.choice(arquetipos)
    traco_sombra = random.choice(tracos_sombra)
    virtude      = random.choice(virtudes)
    vicio        = random.choice(vicios)

    return {
        # Raça
        "raca_nome":  raca_nome,
        "raca_desc":  raca["descricao"],
        "raca_bonus": raca["bonus"],
        "altura":     altura,
        "pele":       pele,
        # Sexo e origem
        "sexo":          sexo,
        "origem":        origem_texto,
        "reino_nome":    nome_reino,
        "reino_desc":    desc_reino,
        # Classe
        "classe_nome": classe_nome,
        "sub_nome":    sub_nome,
        "atributos_str": atributos_str,
        "identidade":  identidade,
        # Atributos numéricos
        "atributos_lista": atributos_lista,
        "total_atributos": sum(atribs.values()),
        # Sensorial
        "odor":      odor,
        "voz":       voz,
        "expressao": expressao,
        "marca":     marca,
        # Personalidade
        "arquetipo":    arquetipo,
        "traco_sombra": traco_sombra,
        "virtude":      virtude,
        "vicio":        vicio,
    }


# ============================================================
#  VIEWS DJANGO
# ============================================================

def index(request):
    """Página principal — gera um personagem ao carregar."""
    personagem = gerar_personagem()
    return render(request, "geradordepersonagem/index.html", {"personagem": personagem})


def gerar_ajax(request):
    """Endpoint AJAX — retorna novo personagem como JSON."""
    if request.method == "GET":
        return JsonResponse(gerar_personagem())
    return JsonResponse({"erro": "Método não permitido."}, status=405)
